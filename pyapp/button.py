#import RPi.GPIO as GPIO
import time
import datetime
import requests
import telepot
import sys
import asyncio
import telepot.aio
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

btn_A = 26
btn_B = 13
btn_C = 5

# GPIO.setmode(GPIO.BCM)

# GPIO.setup(btn_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(btn_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(btn_C, GPIO.IN, pull_up_down=GPIO.PUD_UP)

profile=webdriver.FirefoxProfile()
profile.add_extension("./r_kiosk-0.9.0-fx.xpi")
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

def got_input(lettera):
	global loop
	st = datetime.datetime.utcnow()

	ipt = lettera
	print(ipt)

	with open("../data/data.txt", "a") as myfile:
		myfile.write(str(st) + ',' + str(domanda) + ',' + str(ipt))
	
	r = requests.post(url_btn, data = {'istante':str(st), 'domanda':str(domanda), 'voto':str(ipt)})

	if r.json()['status'] == 'ok':
		browser.get(url_btn)
		
		time.sleep(5)
		browser.get(url_qst + '?testo=' + domanda)

	else:
		browser.get(url_err)

	
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


def funA(btn_A):

	got_input('a')

def funB(btn_B):

	got_input('b')

def funC(btn_C):

	got_input('c')


# GPIO.add_event_detect(btn_A, GPIO.RISING, callback=funA, bouncetime=5000)
# GPIO.add_event_detect(btn_B, GPIO.RISING, callback=funB, bouncetime=5000)
# GPIO.add_event_detect(btn_C, GPIO.RISING, callback=funC, bouncetime=5000)

loop.create_task(bot.message_loop(handle))
print('Listening ...')
browser.maximize_window()
browser.get(url_qst + '?testo=' + domanda)
#elem = browser.find_element_by_tag_name('html')
#elem.send_keys(Keys.F11)
loop.run_forever()
