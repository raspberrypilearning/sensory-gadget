from picozero import LED, Speaker, Button, Pot

led = LED(13)
haut_parleur1 = Speaker(5)
haut_parleur2 = Speaker(10)
bouton1 = Button(18)
bouton2 = Button(28)
cadran = Pot(0)

def melodie1():
    haut_parleur1.play(500)  
    print('1 pressé')

def melodie2():
    haut_parleur2.play(600) 
    print('2 pressé')

while True:
    led.brightness = cadran.percent
    bouton1.when_pressed = melodie1
    bouton2.when_pressed = melodie2
    
    