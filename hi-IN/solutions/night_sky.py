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