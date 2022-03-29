## Build and test

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Now it's time to make your sensory gadget.  
</div>
<div>
![Three images on a box showing eating, drinking and playing. One of the images is backlit by an LED.](images/communication-tool.PNG){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Your sensory gadget is your own design and may have a **different combination** of components to the ones suggested in the diagrams below. 

If a pin is already in use then you will need to select a different pin and ground to use. Make sure that you **note down** which pin is in use for when you are writing your code. 
</p>

You have built up some really useful skills. Here is a reminder to help you make your sensory gadget: 

### Connect your outputs

[[[sharing-a-ground-pin]]]

--- task ---

### Single colour LEDs

[[[single-led-wiring]]]

[[[multiple-single-led-wiring]]] 

[[[sing-led-pins]]]

[[[multiple-single-led-pins]]]

--- collapse ---

---
title: Add a function to turn on a single LED
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 1-2
---
def excited(): # Your mood
    purple.on() # Turn on

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Add functions to control multiple single LEDs
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 1-2
---
def excited(): # Your first mood
    purple.on() # Turn on
    blue.off() # Turn off

def worried(): # Your second mood
    purple.off() # Turn off
    blue.on() # Turn on

--- /code ---

--- /collapse ---

### RGB LEDs

[[[rgb-wiring]]]

[[[rgb-led-pins]]]

--- collapse ---

---
title: Add functions to set an RGB LED colour
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 1-5
---
def happy(): # Your first mood
    rgb.color = (0, 255, 0) # Your first colour

def sad(): # Your second mood
    rgb.color = (255, 0, 0) # Your second colour

--- /code ---

--- /collapse ---

[[[generic-theory-simple-colours]]]

### Speakers and buzzers

[[[single-buzzer-wire]]]
[[[stereo-buzzer-wiring]]]
[[[earphones-wiring]]]
[[[single-buzzer-pin]]]
[[[multiple-buzzer-pins]]]

**Useful information about sound**

[[[list-of-notes]]]
[[[note-length]]]
[[[frequency-numbers]]] 
[[[sheet-to-notes]]]

**Sound code samples**

[[[play-single-note]]]
[[[play-a-tune]]]
[[[notes-in-loop]]]
[[[pico-sound-frequency]]]
[[[whitenoise-drum-beat]]]
[[[interrupt-tune]]]

--- /task ---

### Connect your inputs

--- task ---

### Button

[[[single-button-wiring]]]

[[[multiple-button-wiring]]]

--- collapse ---

---
title: Import Button
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Button

--- /code ---

--- /collapse ---

[[[single-button-pins]]]
[[[multiple-button-pins]]]

--- collapse ---

---
title: Call a different function when each button is pressed
---

You can have multiple buttons that each call a different function when they are pressed. 

Make sure you use the function names from your project and just use the name of the function, do not call it by adding brackets.

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 
line_highlights: 
---

happy_button.when_pressed = happy
sad_button.when_pressed = sad
angry_button.when_pressed = angry

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Change to the next function when a single button is pressed
---

Use an `option` variable to keep track of the current mood so that you can decide which function to call next. 

Make sure the function names match the mood functions you defined in the previous step.

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 
line_highlights: 
---
option = 0 # store the current option

def choice(): # call the next function and update the option
    global option
    if option == 0:
        energised() # your first mood
    elif option == 1:
        calm()      # your second mood
    elif option == 2:
        focused()   # your third mood
    elif option == 3:    
        rgb.off()
    
    # move to the next option
    if option == 3:
        option = 0
    else:
        option = option + 1
    
button.when_pressed = choice # Call the choice function when the button is pressed

--- /code ---

--- /collapse ---

### Switch

[[[crafted-switch-button-wiring]]]

[[[multiple-crafted-switch-button-wiring]]]

--- collapse ---

---
title: Import Switch
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Switch

--- /code ---

--- /collapse ---

[[[single-switch-pins]]]
[[[multiple-switches-pins]]]

### Potentiometer

[[[potentiometer-wiring]]]
[[[potentiometer-pin]]]

--- collapse ---

---
title: Import Potentiometer
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Pot

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Call a function based on the value of the potentiometer
---

If you are using a potentiometer to control outputs then you will need to divide up the dial into equal sections. 

You can use `dial.percent` to get a value between 0 and 1 from the potentiometer. If you have 5 moods then you can check whether the value is less than 20, 40, 60, 80 or 100. If you have 3 moods then you can check whether the value is less that 33, 66 or 100. 

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 
line_highlights: 
---

while True:
    mood = dial.percent
    print(mood)
    if mood < 20:
        happy()
    elif mood < 40:
        good()
    elif mood < 60:
        okay()
    elif mood < 80:
        unsure()
    else:
        unhappy()
    sleep(0.1) 

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Test:** Test your inputs and outputs to make sure everything works as expected. 

Use the **debug** task at the bottom of this step if you come across any problems.

--- /task ---

### Craft your gadget

--- task ---

[[[mount-components]]]

[[[diffuse-leds]]]

--- collapse ---

---
title: Use tape to hold jumper wires in place
---

Use sticky tape or electrical tape to hold jumper wires in place so that your device stays together. 

You can remove the tape later if you want to reuse the components. 

--- /collapse ---

[[[using-craft-knife]]]

[[[joining-jumper-wires]]] 

[[[drop-switch]]]

[[[pull-switch]]] 

[[[taping-components]]] 

--- /task ---

--- task ---

**Test:** Show someone else your project and get their feedback. Do you want make any changes to your book? 

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

[[[debug-pico-code]]] 
[[[debug-pico-hardware]]]
[[[pico-debug-led]]]

Code runs, but nothing happens:
+ Check that your inputs are connected correctly and that you used the correct pin in your code
+ Check the Thonny Shell for any messages about variables or functions not being defined, you might have forgotten to change the examples to match your code
+ Check your code carefully. You could add `print` statements to help you understand what is happening. 
+ Check that you have called your functions

--- collapse ---

---
title: Call a function 
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 7
---
def happy(): # Your first mood
    rgb.color = (0, 255, 0) # Your first colour

def sad(): # Your second mood
    rgb.color = (255, 0, 0) # Your second colour

happy() 

--- /code ---

--- /collapse ---

--- collapse ---

---
title: My LED doesn't light when I call my function
---

Check that the pins in your code match the pins your LED is connected to.

--- /collapse ---

--- collapse ---

---
title: My RGB LED show the wrong colour
---

Check your code to make sure that your colour values are in the right order. Use the ['RGB Colour guide'](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} to check your code matches the colour you expect.

--- /collapse ---

--- collapse ---
---
title: My sounds are not playing, or not playing as I expected
---

Your code was working before you assembled your sensory gadget. It is unlikely that your code will be broken at this stage. The majority of bugs will be from wiring and components. 

+ Check that your components have been rewired to the correct pins (you should have noted these down earlier, they are displayed at the top of your code)
+ Look for any loose connections and secure with tape
+ Check that you haven't covered any conductive elements of your circuit with sticky tape or glue.

--- /collapse ---

--- collapse ---
---
title: My wires aren't long enough now that they are in my sensory gadget
---

Now that you have crafted your sensory gadget, you might need extra-long wires to attach your component to your Raspberry Pi pins. Look at the instructions above to 'join jumper wires to extend them'.

--- /collapse ---

--- collapse ---
---
title: My wires or components wont stay in place
---

Some connections are stronger than others so you might find that you need to use tape to keep your wires connected to your components or to hold your components in place on your gadget. Look at the instructions above to 'secure wires and components using tape'.

--- /collapse ---

You might find a bug not listed here. Can you figure out how to fix it?

We love hearing about your bugs and how you fixed them. Use the feedback button at the bottom of this page if you found a different bug in your project.

--- /task ---



