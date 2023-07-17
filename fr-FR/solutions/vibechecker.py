from time import sleep
from picozero import Button, RGBLED

heureux = Button(13)
colere = Button(14)
triste = Button(15)
led = RGBLED(18, 17, 16)

while True:
    if heureux.is_pressed:
        print('heureux!')
        led.color = (255,255,0)
    elif colere.is_pressed:
        print('COLERE!')
        led.color = (255,0,0)
    elif triste.is_pressed:
        print('triste et bleu...')
        led.color = (0,125,255)
