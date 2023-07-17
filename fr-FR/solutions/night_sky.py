from picozero import RGBLED, Button

rvb = RGBLED(1, 2, 3)
bouton = Button(18)
option = 0

def change_option():
    global option
    option += 1
        
    if option == 1:
        rvb.cycle()
    else:
        rvb.off()
        option = 0

bouton.when_pressed = change_option