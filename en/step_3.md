## Build and test

Now it's time to make your sensory gadget.

![](images/image.png)

--- task ---

You have built up some really useful skills. Here is a reminder to help you make your sensory gadget: 

### Outputs

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

### Inputs


### Craft your gadget


--- /task ---







--- task ---

**Test:** Show someone else your project and get their feedback. Do you want make any changes to your book? 

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

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
