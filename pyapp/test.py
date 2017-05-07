import RPi.GPIO as GPIO
import keyboard
import time

btn_A = 26
btn_B = 13
btn_C = 5

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(btn_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn_C, GPIO.IN, pull_up_down=GPIO.PUD_UP)

a = False;
b = False;
c = False;

def funA(btn_A):
	print("a\n")

def funB(btn_B):
	print("b\n")

def funC(btn_C):
	print("c\n")

GPIO.add_event_detect(btn_A, GPIO.RISING, callback=funA, bouncetime=5000)
GPIO.add_event_detect(btn_B, GPIO.RISING, callback=funB, bouncetime=5000)
GPIO.add_event_detect(btn_C, GPIO.RISING, callback=funC, bouncetime=5000)

while True:
	time.sleep(10)


