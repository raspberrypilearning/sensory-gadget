from time import sleep
from picozero import Button, RGBLED, Pot, Speaker
from random import randint

led = RGBLED(13,14,15) # setup RGBLED
led2 = RGBLED(10,11,12) # setup other RGBLED - the more the brighter!

hum = Speaker(5) # setup passive buzzer for hum/start/stop sounds

power = Button(17) # setup button to turn on saber

dial = Pot(0) # setup Potentiometer to change blade colour and turn off

# Turn off lights and make 'power down' sound
def off():
    for i in range(400): # white noise loop 1 sec
        tone = randint(4000,6000) # pick a random number 1k-5k
        hum.play(tone, 0.001) # play tone for 1/1000th sec
    for i in range(200): # white noise loop 1 sec
        tone = randint(2000,4000) # pick a random number 1k-5k
        hum.play(tone, 0.001) # play tone for 1/1000th sec
    for i in range(200): # white noise loop 1 sec
        tone = randint(1000,3000) # pick a random number 1k-5k
        hum.play(tone, 0.001) # play tone for 1/1000th sec
    for i in range(200): # white noise loop 1 sec
        tone = randint(50,1000) # pick a random number 1k-5k
        hum.play(tone, 0.001) # play tone for 1/1000th sec
    led.color = (0,0,0)
    led2.color = (0,0,0)
    hum.off()


# Make lightsaber start sound then turn on lights
def on():
    for i in range(200): # white noise loop 0.2 sec
        tone = randint(50,1000) # pick a random number 50-1k
        hum.play(tone, 0.001) # play tone for 1/1000th sec
    for i in range(200): # white noise loop 0.2 sec
        tone = randint(1000,3000) # pick a random number 1k-3k
        hum.play(tone, 0.001) # play tone for 1/1000th sec
    for i in range(200): # white noise loop 0.2 sec
        tone = randint(2000,4000) # pick a random number 2k-4k
        hum.play(tone, 0.001) # play tone for 1/1000th sec
    for i in range(400): # white noise loop 0.4 sec
        tone = randint(3000,5000) # pick a random number 3k-5k
        hum.play(tone, 0.001) # play tone for 1/1000th sec
    while True: # forever loop checking the dial reading to set colour and change hum sound
        if dial.value >= 0.8: # highest setting on dial - 5
            led.color = (255,255,255) # white
            led2.color = (255,255,255)
            hum.play(90)
        elif dial.value >= 0.6: # high setting on dial - 4
            led.color = (255,0,255) # purple blade
            led2.color = (255,0,255)
            hum.play(80)
        elif dial.value >= 0.4: # middle setting on dial - 3
            led.color = (0,0,255) # blue blade
            led2.color = (0,0,255)
            hum.play(70)
        elif dial.value >= 0.2: # low setting on dial - 2
            led.color = (0,255,0) # green blade
            led2.color = (0,255,0)
            hum.play(60)
        elif dial.value >= 0.01: # lowest setting on dial (above 0.01) - 1
            led.color = (255,0,0) # red blade
            led2.color = (255,0,0)
            hum.play(50)
        else: # if dial turned all the way down - 0
            off() # run off function
            break # leave the loop
    

power.when_pressed = on