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

# btn_A = 14
# btn_B = 15
# btn_C = 18
# btn_D = 23

# GPIO.setmode(GPIO.BCM)

# GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

url = 'http://localhost:4000/domanda/'

domanda = ""

async def inizio():
	"""
	Quando si accenda la rpi cosa succede?
		- prendo dal file l'ultima domanda usata
		- la mando a Chrome
	"""
	global domanda
	with open("../data/data.txt", "r") as myfile:
		content = myfile.readlines()

	content = [x.strip() for x in content] 

	domanda = content[-1].split(',')[1]
	print("inizio")
	print(domanda)
	driver.get(url + '?testo=' + domanda)
    	


def handle(msg):
	"""
	Telegram Function Bot
	Questioniere
	QuariniBot
	"""
	global domanda

	flavor = telepot.flavor(msg)

	summary = telepot.glance(msg, flavor=flavor)

	domanda = msg['text']

	print(flavor, summary)
	#r = requests.post(url, data = {'testo':domanda})
	print("bot")
	print(domanda)
	driver.get(url + '?testo=' + domanda)


async def leggi_bottoni():
	"""
	Monitora i pulsanti
	"""

	await asyncio.sleep(1)
	s = input('>')
	if s == '1':
		print(":)")
		send_signal(int(s))
	elif s == '2':
		print(":|")
		send_signal(int(s))
	elif s == '3':
		print(":(")
		send_signal(int(s))
	await hello_world()



def send_signal( btn ):
	"""
	Quando un pulstante viene schiacciato accadono alcune cose:
		- Manda messaggio di apertura pagina "GRAZIE"
		- Manda messaggio al database
		- Tutto questo tramite un API
		- nel frattempo fa un backup su un file
	"""
	global domanda

	st = datetime.datetime.utcnow()

	with open("data/data.txt", "a") as myfile:
		myfile.write(str(st) + ',' + domanda + ',' + str(btn))

	payload = {'datetime': str(st), 'btn': str(btn)}
	r = requests.post(url, data=payload)

	if r.status_code == 400:
		print('server down!')

	time.sleep(5)

	r = requests.post(url, data=payload)

	if r.status_code == 400:
		print('server down!')


TOKEN = '349391683:AAFE2_8jNCpJwi4pzAbwNee6t2yIXaFZkNc'

bot = telepot.aio.Bot(TOKEN)
loop = asyncio.get_event_loop()

loop.create_task(inizio())
loop.create_task(leggi_bottoni)
loop.create_task(bot.message_loop(handle))
print('Listening ...')

loop.run_forever()





# while True:

#	if GPIO.input(btn_A) == False:
#		print('Button A Pressed')
#		send_signal(0)

#	elif GPIO.input(btn_B) == False:
#		print('Button B Pressed')
#		send_signal(1)

#	elif GPIO.input(btn_C) == False:
#		print('Button C Pressed')
#		send_signal(2)

#	elif GPIO.input(btn_D) == False:
#		print('Button D Pressed')
#		send_signal(3)



