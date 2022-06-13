from picozero import LED, Speaker, Button, Pot

led = LED(13)
speaker1 = Speaker(5)
speaker2 = Speaker(10)
button1 = Button(18)
button2 = Button(28)
dial = Pot(0)

def tune1():
    speaker1.play(500)  
    print('1 pressed')

def tune2():
    speaker2.play(600) 
    print('2 pressed')

while True:
    led.brightness = dial.percent
    button1.when_pressed = tune1
    button2.when_pressed = tune2
    
    