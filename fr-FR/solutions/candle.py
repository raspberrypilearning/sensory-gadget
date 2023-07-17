from picozero import RGBLED, Switch
from time import sleep
from random import randint

# Indique à quelles broches les composants sont attachés sur le Pico
led = RGBLED(13, 14, 15)
declencher = Switch(18)


def lumiere(): # Boucle de flamme vacillante
      rouge = randint(125,255)
      jaune = (rouge - 125)
      delai = randint(0,100)
      led.color  =(rouge, jaune, 0)
      sleep(delai/1000)

def sombre(): # Pas de flamme
   led.off()
   sleep(2) # Temps sombre avant la réinitialisation


while True: # Boucle pour vérifier si l'interrupteur est fermé
    if declencher.is_closed:
        sombre()
    else:
        lumiere()