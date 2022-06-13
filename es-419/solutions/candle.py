from picozero import RGBLED, Switch
from time import sleep
from random import randint

# State which pins the components are placed on the Pico
led = RGBLED(13, 14, 15)
trigger = Switch(18)


def light(): # flickering flame loop
      red = randint(125,255)
      yellow = (red - 125)
      delay = randint(0,100)
      led.color  =(red, yellow, 0)
      sleep(delay/1000)

def dark(): # no flame
   led.off()
   sleep(2) # dark time before reset


while True: # loop to check if switch is closed
    if trigger.is_closed:
        dark()
    else:
        light()