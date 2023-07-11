from picozero import LED, Speaker, Button
from time import sleep

eet = LED(13)
drink = LED(8)
speel = LED(5)

luidspreker = Speaker(1)

kies = Button(18)
bevestig = Button(22)

optie = 0 # Sla de huidige optie op

def keuze(): # Roep de volgende functie aan en werk de optie bij
    global optie
    if optie == 0:
        eet.on()
        drink.off()
        speel.off()
    elif optie == 1:
        eet.off()
        drink.on()
        speel.off()    
    elif optie == 2:
        eet.off()
        drink.off()
        speel.on()   
    elif optie == 3:
        eet.off()
        drink.off()
        speel.off()

    if optie == 3:
        optie = 0
    else:
        optie = optie + 1

def geluid_zoemer():
    luidspreker.on()
    sleep(1)
    luidspreker.off()

kies.when_pressed = keuze 
bevestig.when_pressed = geluid_zoemer

