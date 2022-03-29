## Your idea

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Use this step to plan your sensory gadget. You can plan by just thinking; tinkering; drawing or writing; or however you like!  
</div>
<div>
![A drawing of a bee with buzzers and a potentiometer attached.](images/buzy-bee.png){:width="300px"}
</div>
</div>


### Why are you making your sensory gadget?

--- task ---

Think about the purpose of your sensory gadget. 

It could be:
+ For a younger sibling to learn about sights, and sounds
+ A way of relieving tension through pressing buttons and hearing sounds
+ A communication tool to help people express their needs 

--- /task ---

### Who is it for?

--- task ---

Think about who you will make your sensory gadget for (your **audience**). 

It could be for a friend, for a family member, for a school class, for people who share a hobby, for fans of a TV programme or musician, or just for yourself.

--- /task ---

### What features will your gadget have?

--- task ---

Think about how many components your gadget will need. 

[[[pico-limitations]]]

--- /task ---

--- task ---

Think about the types of inputs and outputs you will have.

You gadget could:
+ Have push buttons for inputs
+ Use crafted switches
+ Use a dial input using a potentiometer
+ Play a specific sound
+ Play a tune, or several tunes
+ Use single coloured LEDs
+ Use an RGB LED

--- /task ---

--- task ---

Think about what your sensory gadget will look like.

It could:

+ Be based on a sensory gadget that already exists like a fidget cube or popper
+ Have a theme that is based on your favourite comic, tv show or song
+ Be a crafted enclosure made from an old cardboard box, a fabric material or a plastic container

--- /task ---

### Get started

--- task ---

Gather the components that you will need to make your sensory gadget. You will need inputs, outputs, jumper wires and your Raspberry Pi Pico.

--- /task ---

--- task ---

**Test:** Connect your Raspberry Pi Pico to your computer and check that it works by blinking the on board LED.

Here is some example code for blinking the on board LED:

--- code ---
---
language: python
filename: 
line_numbers: false
line_number_start: 1
line_highlights: 
---
from picozero import pico_led
from time import sleep

pico_led.on()
sleep(1)
pico_led.off()
--- /code ---

--- /task ---

--- task ---

If you have not already prepared your inputs and outputs, and need to remind yourself of how to connect LEDs to resistors and jumper wires, visit our [Introduction to the Pico](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"} guide. 

--- /task ---


