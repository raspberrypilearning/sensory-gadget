## Introduction

Make a fidget toy or sensory gadget. Your gadget will need to meet the **project brief**. 

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A <span style="color: #0faeb0">sensory gadget</span> is something that makes you want to keep interacting with it. A fidget toy is a type of sensory gadget that helps the user relieve stress or improve their concentration. An adaptive gadget can be used by people with physical disabilities for communication. A sensory gadget might stimulate all the senses or just focus on one.
</p>

You will:
+ Use your digital making skills to design and make a gadget for a user
+ Use physical inputs such as buttons and potentiometers to control physical outputs such as LEDs and a buzzer
+ Let others try our your gadget and improve it based on their feedback

--- no-print ---

--- task ---

### Try it

Watch the video below. Which senses are being stimulated? What output occurs when each input is used?

**An assistive gadget**
A user can select an option to let their carer know of their current need. Once they have made a selection, they press another button which alerts their carer.

<video width="640" height="360" controls>
<source src="images/communication-tool.mp4" type="video/mp4">
Your browser does not support WebM video, try FireFox or Chrome
</video>

--- collapse ---
---
title: See inside
---
--- code ---
---
language: python
filename: assistive_gadget.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
from picozero import LED, Speaker, Button
from time import sleep

eat = LED(13)
drink = LED(8)
play = LED(5)

speaker = Speaker(1)

choose = Button(18)
confirm = Button(22)

option = 0 # store the current option

def choice(): # call the next function and update the option
    global option
    if option == 0:
        eat.on()
        drink.off()
        play.off()
    elif option == 1:
        eat.off()
        drink.on()
        play.off()    
    elif option == 2:
        eat.off()
        drink.off()
        play.on()   
    elif option == 3:
        eat.off()
        drink.off()
        play.off()

    if option == 3:
        option = 0
    else:
        option = option + 1

def sound_buzzer():
    speaker.on()
    sleep(1)
    speaker.off()

choose.when_pressed = choice 
confirm.when_pressed = sound_buzzer
--- /code ---

--- /collapse ---

--- /task ---

--- /no-print ---

--- print-only ---

**An assistive gadget**
A user can select an option to let their carer know of their current need. Once they have made a selection, they press another button which alerts their carer.

![desc](images/communication-tool.PNG)

--- /print-only ---

<div style="border-top: 15px solid #f3524f; background-color: whitesmoke; margin-bottom: 20px; padding: 10px;">

### PROJECT BRIEF: Project title
<hr style="border-top: 2px solid black;">

Brief explanation of aims of project. 

Your sensory gadget should:
+ Have multiple different kinds of input
+ Have multiple different outputs
+ Be appealing to the user and robust enough to be used

Your sensory gadget could:
+ Take ergonomics like user comfort into consideration
+ Reset on user input or after a set amount of time 
+ Connect to a specific theme

</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">Ergonomics</span> is a science that seeks to overcome problems and improve how humans can interact with their environment. Improving the ergonomics of a gadget will make it easier to use and more comfortable to interact with. 
</p>

--- no-print ---

### Get inspiration

--- task ---

Think about the sensory gadget that you would like to make as you investigate these example projects:

**The night sky**
Tiny holes have been poked through a piece of black card to make a night sky effect on a ceiling in a dark room. An RGB LED pulses to create a twinkling effect. A button is used to switch the light on and off.

<video width="640" height="360" controls>
<source src="images/the-night-sky.mp4" type="video/mp4">
Your browser does not support WebM video, try FireFox or Chrome
</video>

--- collapse ---
---
title: See inside
---
--- code ---
---
language: python
filename: night_sky.py
line_numbers: true
line_number_start: 
line_highlights: 
---
from picozero import RGBLED, Button

rgb = RGBLED(1, 2, 3)
button = Button(18)
option = 0

def change_option():
    global option
    option += 1
        
    if option == 1:
        rgb.cycle()
    else:
        rgb.off()
        option = 0

button.when_pressed = change_option
--- /code ---

--- /collapse ---

**The buzzy bee**
The bee's wings have kitchen foil on the back of them and when pressed down they connect to another piece of foil on the card - this makes a buzzer play a note. Each wing plays a different sound. A potentiometer controls a blue LED on the bee's tail.

<video width="640" height="360" controls>
<source src="images/buzy-bee.mp4" type="video/mp4">
Your browser does not support WebM video, try FireFox or Chrome
</video>

--- collapse ---
---
title: See inside
---
--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 
line_highlights: 
---

--- /code ---


--- /collapse ---

**Picosaber**
Pressing the button lights the blade of the saber and starts the buzzers making a humming sound. Turning the potentiometer changes the colour of the blade and pitch of the hum. Turning the potentiometer all the way down plays a 'power-down sound' then switches off the lights and buzzers.

<video width="640" height="360" controls>
<source src="images/picosaber.mp4" type="video/mp4">
Your browser does not support WebM video, try FireFox or Chrome
</video>

--- collapse ---
---
title: See inside
---
--- code ---
---
language: python
filename: saber.py
line_numbers: true
line_number_start: 
line_highlights: 
---
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
--- /code ---

--- /collapse ---

**Marc Scotts example**
Add description here...

<video width="640" height="360" controls>
<source src="images/filename" type="video/mp4">
Your browser does not support WebM video, try FireFox or Chrome
</video>


--- /task ---

--- /no-print ---

--- print-only ---

<mark> copy descriptions from above and replace videos with a still image </mark>

**An assistive gadget**
A user can select an option to let their carer know of their current need. Once they have made a selection, they press another button which alerts their carer.
![desc](images/communication-tool.PNG)

**The night sky**
Tiny holes have been poked through a piece of black card to make a starry night effect on a ceiling in a dark room. An RGB LED pulses to create a twinkling effect.
![desc](images/night-sky.PNG)

**The buzzy bee**
The bee's wings have kitchen foil on the back of them and when pressed down they connect to another piece of foil on the card - this makes a buzzer play a note. Each wing plays a different sound. A potentiometer controls a blue LED on the bee's tail.
![desc](images/buzy-bee.png)

**Picosaber**
Pressing the button lights the blade of the saber and starts the buzzers making a humming sound. Turning the potentiometer changes the colour of the blade and pitch of the hum. Turning the potentiometer all the way down plays a 'power-down sound' then switches off the lights and buzzers.
![desc](images/picosaber.png)

**Marc Scotts example**
Description
![](images/image)


--- /print-only ---


