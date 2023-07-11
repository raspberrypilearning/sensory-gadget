from picozero import RGBLED, Button

rgb = RGBLED(1, 2, 3)
knop = Button(18)
optie = 0

def verander_optie():
    global optie
    optie += 1
        
    if optie == 1:
        rgb.cycle()
    else:
        rgb.off()
        optie = 0

knop.when_pressed = verander_optie