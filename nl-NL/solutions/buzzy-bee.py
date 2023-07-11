from picozero import LED, Speaker, Button, Pot

led = LED(13)
luidspreker1 = Speaker(5)
luidspreker2 = Speaker(10)
knop1 = Button(18)
knop2 = Button(28)
instelwiel = Pot(0)

def melodie1():
    luidspreker1.play(500)  
    print('1 ingedrukt')

def melodie2():
    luidspreker2.play(600) 
    print('2 ingedrukt')

while True:
    led.brightness = instelwiel.percent
    knop1.when_pressed = melodie1
    knop2.when_pressed = melodie2
    
    