import RPi.GPIO as GPIO
import asyncio
import socket

btn_A = 26
btn_B = 13
btn_C = 5

GPIO.setmode(GPIO.BCM)

GPIO.setup(btn_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn_C, GPIO.IN, pull_up_down=GPIO.PUD_UP)

rsock, wsock = socket.socketpair()

def wrapper():
	
	if GPIO.input(btn_A) == False:
    	print('Button A Pressed')

    elif GPIO.input(btn_B) == False:
    	print('Button B Pressed')

    elif GPIO.input(btn_C) == False:
    	print('Button C Pressed')

	rsock.recv(100)
	callback()

loop = asyncio.get_event_loop()
loop.add_reader(rsock, wrapper)
loop.run_forever()


    
