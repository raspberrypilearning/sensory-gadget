from time import sleep
from picozero import Button, RGBLED

gelukkig = Button(13)
boos = Button(14)
verdrietig = Button(15)
led = RGBLED(18, 17, 16)

while True:
    if gelukkig.is_pressed:
        print('gelukkig!')
        led.color = (255,255,0)
    elif boos.is_pressed:
        print('BOOS!')
        led.color = (255,0,0)
    elif verdrietig.is_pressed:
        print('verdrietig...')
        led.color = (0,125,255)
