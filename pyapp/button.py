#import RPi.GPIO as GPIO
import time
import datetime
import requests
import telepot
import sys
import asyncio
import telepot.aio
import termios
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

profile=webdriver.FirefoxProfile()
profile.add_extension("/Users/paolo/Desktop/r_kiosk-0.9.0-fx.xpi")
profile.set_preference("extensions.r_kiosk.currentVersion", "0.9.0")
	# firefoxOptions = Options()
	# firefoxOptions.add_argument("--kiosk")
#firefoxOptions.add_argument("disable-infobars")
browser = webdriver.Firefox(profile)

loop = asyncio.get_event_loop()

url_qst = 'http://localhost:4000/domanda/'
url_btn = 'http://localhost:4000/risposta/'
url_err = 'http://localhost:4000/errore/'

with open("../data/data.txt", "r") as myfile:
	content = myfile.readlines()
	print(content)
	domanda = content[-1].split(',')[1]

def got_input():
	global loop
	st = datetime.datetime.utcnow()

	ipt = sys.stdin.readline()
	print(ipt)

	with open("../data/data.txt", "a") as myfile:
		myfile.write(str(st) + ',' + str(domanda) + ',' + str(ipt))
	
	r = requests.post(url_btn, data = {'istante':str(st), 'domanda':str(domanda), 'voto':str(ipt)})

	if r.json()['status'] == 'ok':
		browser.get(url_btn)
		loop.remove_reader(sys.stdin)
		time.sleep(5)
		termios.tcflush(sys.stdin, termios.TCIOFLUSH)
		browser.get(url_qst + '?testo=' + domanda)
	else:
		browser.get(url_err)

	termios.tcflush(sys.stdin, termios.TCIOFLUSH)
	loop.add_reader(sys.stdin, got_input)

def handle(msg):
	global domanda

	flavor = telepot.flavor(msg)
	summary = telepot.glance(msg, flavor=flavor)

	print(flavor, summary)
	print(msg['chat']['id'])

	domanda = msg['text']

	browser.get(url_qst + '?testo=' + domanda)


TOKEN = '349391683:AAFE2_8jNCpJwi4pzAbwNee6t2yIXaFZkNc'

bot = telepot.aio.Bot(TOKEN)

loop.add_reader(sys.stdin, got_input)
loop.create_task(bot.message_loop(handle))
print('Listening ...')
browser.maximize_window()
browser.get(url_qst + '?testo=' + domanda)
#elem = browser.find_element_by_tag_name('html')
#elem.send_keys(Keys.F11)
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



