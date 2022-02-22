## Build and test

Now it's time to make your sensory gadget.

![](images/image.png)

### Output

--- task ---

You have built up some really useful skills. Here is a reminder to help you make your sensory gadget: 

### Single colour LEDs

[[[single-led-wiring]]]

[[[multiple-single-led-wiring]]] 

--- collapse ---

---
title: Import the single LED 
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import LED

--- /code ---

--- /collapse ---

[[[sing-led-pins]]]

[[[multiple-single-led-pins]]]

--- collapse ---

---
title: Add a function to turn on a single LED
---

--- code ---
---
language: python
filename: mood-check-in.py
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
filename: mood-check-in.py
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

--- collapse ---

---
title: Import the RGB LED
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import RGBLED

--- /code ---

--- /collapse ---

[[[rgb-led-pins]]]

--- collapse ---

---
title: Add functions to set an RGB LED colour
---

--- code ---
---
language: python
filename: mood-check-in.py
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
<mark>Add import statements for a speaker</mark>
[[[single-buzzer-pin]]]
[[[multiple-buzzer-pins]]]
<mark>Add sample code for a speaker</mark>

--- collapse ---

---
title: Call a function 
---

--- code ---
---
language: python
filename: mood-check-in.py
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

--- /task ---

--- task ---

### Inputs

[[[single-button-wiring]]]

[[[multiple-button-wiring]]]

[[[crafted-switch-button-wiring]]]

[[[multiple-crafted-switch-button-wiring]]]

--- collapse ---

---
title: Import Button
---

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Button

--- /code ---

--- /collapse ---

[[[single-button-pins]]]
[[[multiple-button-pins]]]
[[[single-switch-pins]]]
[[[multiple-switches-pins]]]

--- collapse ---

---
title: Call a different function when each button is pressed
---

You can have multiple buttons that each call a different function when they are pressed. 

Make sure you use the function names from your project and just use the name of the function, do not call it by adding brackets.

--- code ---
---
language: python
filename: mood-check-in.py
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
filename: mood-check-in.py
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

[[[potentiometer-wiring]]]
[[[potentiometer-pin]]]

--- collapse ---

---
title: Call a function based on the value of the potentiometer
---

If you are using a potentiometer to control outputs then you will need to divide up the dial into equal sections. 

You can use `dial.percent` to get a value between 0 and 1 from the potentiometer. If you have 5 moods then you can check whether the value is less than 20, 40, 60, 80 or 100. If you have 3 moods then you can check whether the value is less that 33, 66 or 100. 

--- code ---
---
language: python
filename: mood-check-in.py
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

--- collapse ---

---
title: Import Switch
---

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Switch

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Import Potentiometer
---

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Pot

--- /code ---

--- /collapse ---

--- /task ---

### Craft your gadget

--- task ---

--- /task ---

--- task ---

**Test:** Show someone else your project and get their feedback. Do you want make any changes to your book? 

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

[pico-common-code-errors]

Code runs, but nothings happens:
+ Check that your inputs are connected correctly and that you used the correct pin in your code
+ Check the Thonny Shell for any messages about variables or functions not being defined, you might have forgotten to change the examples to match your code
+ Check your code carefully. You could add `print` statements to help you understand what is happening. 

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

You might find a bug not listed here. Can you figure out how to fix it?

We love hearing about your bugs and how you fixed them. Use the feedback button at the bottom of this page if you found a different bug in your project.

--- /task ---


--- save ---
