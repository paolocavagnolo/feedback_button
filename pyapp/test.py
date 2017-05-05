btn_A = 26
btn_B = 5
btn_C = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(btn_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn_C, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:

    if GPIO.input(btn_A) == False:
    	print('Button A Pressed')

    elif GPIO.input(btn_B) == False:
    	print('Button B Pressed')

    elif GPIO.input(btn_C) == False:
    	print('Button C Pressed')
