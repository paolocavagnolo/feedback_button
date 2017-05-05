import os
import sys
import asyncio
import select
import socket
import threading

GPIO_EXPORT = "/sys/class/gpio/export"
GPIO_BASE_PATH = "/sys/class/gpio/gpio%i/%s"

TEST_PIN = 24

OUT = b"out"
IN = b"in"
NONE, RISING, FALLING, BOTH =  b"none", b"rising", b"falling", b"both"


def gpio_function(pin, function):
    return GPIO_BASE_PATH % (pin, function)


def export_pin(pin):
    if not os.path.exists(gpio_function(pin, "value")):
        with open(GPIO_EXPORT, "wb") as outf:
            outf.write(b"%i" % pin)


def direction_pin(pin, direction=None):
    if direction is None:
        with open(gpio_function(pin, "direction"), "r") as inf:
            return inf.read()
    else:
        assert direction in (OUT, IN)
        with open(gpio_function(pin, "direction"), "w") as outf:
            return outf.write(direction)


def value_pin(pin):
    with open(gpio_function(pin, "value"), "r") as inf:
        return int(inf.read())


def detect_edge(loop, pin, edge, callback):
    assert edge in (RISING, FALLING, BOTH)
    with open(gpio_function(pin, "edge"), "wb") as outf:
        outf.write(edge)


    rsock, wsock = socket.socketpair()

    def background():
        with open(gpio_function(pin, "value")) as inf:
            inf.read()
            while True:
                res = select.select([], [], [inf])
                inf.seek(0)
                wsock.send(inf.read().encode("ascii"))


    t = threading.Thread(target=background)
    t.daemon = True
    t.start()

    def wrapper():
        rsock.recv(100)
        callback()

    loop.add_reader(rsock, wrapper)


async def timed_pin(pin, timeout):
    print(pin, "an")
    await asyncio.sleep(timeout)
    print(pin, "aus")


def value_changed():
    print("value_changed", value_pin(TEST_PIN))
    loop = asyncio.get_event_loop()
    loop.create_task(timed_pin("A", 2))
    loop.create_task(timed_pin("B", 3))


def main():
    export_pin(TEST_PIN)
    if direction_pin(TEST_PIN) == OUT:
        direction_pin(TEST_PIN, IN)

    loop = asyncio.get_event_loop()

    detect_edge(loop, TEST_PIN, RISING, value_changed)
    loop.run_until_complete(asyncio.sleep(10.0))
    print("finished!")
    sys.exit()


if __name__ == "__main__":
    main()