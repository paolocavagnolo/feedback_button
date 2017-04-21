#import RPi.GPIO as GPIO
import time
import datetime
import requests
import telepot
import sys
import telepot
import asyncio
import telepot.aio
from selenium import webdriver

browser = webdriver.Firefox()

url = 'http://localhost:4000/domanda/'

def handle(msg):
    flavor = telepot.flavor(msg)

    summary = telepot.glance(msg, flavor=flavor)

    print(flavor, summary)
    r = requests.post(url, data = {'testo':msg['text']})
    browser.get(url + '?testo=' + msg['text'])

TOKEN = '349391683:AAFE2_8jNCpJwi4pzAbwNee6t2yIXaFZkNc'

bot = telepot.aio.Bot(TOKEN)
loop = asyncio.get_event_loop()

loop.create_task(bot.message_loop(handle))
print('Listening ...')

loop.run_forever()

# url_btn = 'http://localhost:4000'
# url_btn = 'http://localhost:4000'

# btn_A = 14
# btn_B = 15
# btn_C = 18
# btn_D = 23

# GPIO.setmode(GPIO.BCM)

# GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# def send_signal( btn ):
# 	st = datetime.datetime.utcnow()
# 	with open("data.txt", "a") as myfile:
#     	myfile.write(str(st) + ',' + str(btn))

#     payload = {'datetime': str(st), 'btn': str(btn)}
#     r = requests.post(url, data=payload)

#     if r.status_code == 400:
#     	print('server down!')

#     time.sleep(5)

#     r = requests.post(url, data=payload)

#     if r.status_code == 400:
#     	print('server down!')



# while True:

#     if GPIO.input(btn_A) == False:
#     	print('Button A Pressed')
#     	send_signal(0)

#     elif GPIO.input(btn_B) == False:
#     	print('Button B Pressed')
#     	send_signal(1)

#     elif GPIO.input(btn_C) == False:
#     	print('Button C Pressed')
#     	send_signal(2)

#     elif GPIO.input(btn_D) == False:
#     	print('Button D Pressed')
#     	send_signal(3)



