from time import sleep
from picozero import Button, RGBLED, Pot, Speaker
from random import randint

led = RGBLED(13,14,15) # Stel RGB-LED in
led2 = RGBLED(10,11,12) # Stel andere RGB-LED's in: Hoe meer, hoe helderder!

zoem = Speaker(5) # Stel de passieve zoemer in voor zoem-/start-/stopgeluiden

kracht = Button(17) # Stel de knop in om de sabel in te schakelen

instelwiel = Pot(0) # Stel de potentiometer in om de kleur van het blad te veranderen en uit te schakelen

# Schakel de lampjes uit en maak een 'power-down'-geluid
def uit():
    for i in range(400): # Witte ruis lus 1 seconde
        toon = randint(4000,6000) # Neem een willekeurig getal tussen 4000 en 6000
        zoem.play(toon, 0.001) # Speel een toon gedurende 1/1000e seconde
    for i in range(200): # Witte ruis lus 1 seconde
        toon = randint(2000,4000) # Neem een willekeurig getal tussen 2000 en 4000
        zoem.play(toon, 0.001) # Speel een toon gedurende 1/1000e seconde
    for i in range(200): # Witte ruis lus 1 seconde
        toon = randint(1000,3000) # Neem een willekeurig getal tussen 1000 en 3000
        zoem.play(toon, 0.001) # Speel een toon gedurende 1/1000e seconde
    for i in range(200): # Witte ruis lus 1 seconde
        toon = randint(50,1000) # Neem een willekeurig getal tussen 50 en 1000
        zoem.play(toon, 0.001) # Speel een toon gedurende 1/1000e seconde
    led.color = (0,0,0)
    led2.color = (0,0,0)
    zoem.off()


# Laat lichtsabel beginnen met geluid en schakel vervolgens de lichten in
def aan():
    for i in range(200): # Witte ruis lus 0.2 seconde
        toon = randint(50,1000) # Neem een willekeurig getal tussen 50 en 1000
        zoem.play(toon, 0.001) # Speel een toon gedurende 1/1000e seconde
    for i in range(200): # Witte ruis lus 0.2 seconde
        toon = randint(1000,3000) # Neem een willekeurig getal tussen 1000 en 3000
        zoem.play(toon, 0.001) # Speel een toon gedurende 1/1000e seconde
    for i in range(200): # Witte ruis lus 0.2 seconde
        toon = randint(2000,4000) # Neem een willekeurig getal tussen 2000 en 4000
        zoem.play(toon, 0.001) # Speel een toon gedurende 1/1000e seconde
    for i in range(400): # Witte ruis lus 0.4 seconde
        toon = randint(3000,5000) # Neem een willekeurig getal tussen 3000 en 5000
        zoem.play(toon, 0.001) # Speel een toon gedurende 1/1000e seconde
    while True: # Herhaal lus die de waarde van het instelwiel checkt om de kleur in te stellen en het zoemgeluid te veranderen
        if instelwiel.value >= 0.8: # Hoogste instelling op het instelwiel - 5
            led.color = (255,255,255) # Wit
            led2.color = (255,255,255)
            zoem.play(90)
        elif instelwiel.value >= 0.6: # Hoge instelling op het instelwiel - 4
            led.color = (255,0,255) # Paars blad
            led2.color = (255,0,255)
            zoem.play(80)
        elif instelwiel.value >= 0.4: # Middelste instelling op het instelwiel - 3
            led.color = (0,0,255) # Blauw blad
            led2.color = (0,0,255)
            zoem.play(70)
        elif instelwiel.value >= 0.2: # Lage instelling op het instelwiel - 2
            led.color = (0,255,0) # Groen blad
            led2.color = (0,255,0)
            zoem.play(60)
        elif instelwiel.value >= 0.01: # Laagste instelling op het instelwiel (boven 0.01) - 1
            led.color = (255,0,0) # Rood mes
            led2.color = (255,0,0)
            zoem.play(50)
        else: # Als de knop helemaal naar beneden is gedraaid - 0
            uit() # Run off-functie
            break # Verlaat de lus
    

kracht.when_pressed = aan