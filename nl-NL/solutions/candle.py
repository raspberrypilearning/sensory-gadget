from picozero import RGBLED, Switch
from time import sleep
from random import randint

# Geef aan op welke pinnen de onderdelen op de Pico zijn bevestigd
led = RGBLED(13, 14, 15)
signaal = Switch(18)


def licht(): # Flakkerende vlamlus
      rood = randint(125,255)
      geel = (rood - 125)
      vertraging = randint(0,100)
      led.color  =(rood, geel, 0)
      sleep(vertraging/1000)

def donker(): # Geen vlam
   led.off()
   sleep(2) # Uitschakelen voor reset


while True: # Lus om te controleren of de schakelaar gesloten is
    if signaal.is_closed:
        donker()
    else:
        licht()