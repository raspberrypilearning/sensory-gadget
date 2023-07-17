from time import sleep
from picozero import Button, RGBLED, Pot, Speaker
from random import randint

led = RGBLED(13,14,15) # Configurer RGBLED
led2 = RGBLED(10,11,12) # Configure d'autres LED RVB - plus il y en a, plus c'est lumineux !

hum = Speaker(5) # Configure un buzzer passif pour les sons de bourdonnement/démarrage/arrêt

puissance = Button(17) # Bouton de configuration pour allumer le sabre

cadran = Pot(0) # Configure le potentiomètre pour changer la couleur de la lame et éteindre

# Éteindre les lumières et faire un son de « mise hors tension »
def eteint():
    for i in range(400): # Boucle de bruit blanc 1 seconde
        tone = randint(4000,6000) # Choisit un nombre aléatoire ente 4000 et 6000
        hum.play(tone, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    for i in range(200): # Boucle de bruit blanc 1 seconde
        tone = randint(2000,4000) # Choisit un nombre aléatoire ente 2000 et 4000
        hum.play(tone, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    for i in range(200): # Boucle de bruit blanc 1 seconde
        tone = randint(1000,3000) # Choisit un nombre aléatoire ente 1000 et 3000
        hum.play(tone, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    for i in range(200): # Boucle de bruit blanc 1 seconde
        tone = randint(50,1000) # Choisit un nombre aléatoire ente 50 et 1000
        hum.play(tone, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    led.color = (0,0,0)
    led2.color = (0,0,0)
    hum.off()


# Faire le son de démarrage du sabre laser et allumer les lumières
def actif():
    for i in range(200): # Boucle de bruit blanc 0.2 seconde
        tone = randint(50,1000) # Choisit un nombre aléatoire ente 50 et 1000
        hum.play(tone, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    for i in range(200): # Boucle de bruit blanc 0.2 seconde
        tone = randint(1000,3000) # Choisit un nombre aléatoire ente 1000 et 3000
        hum.play(tone, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    for i in range(200): # Boucle de bruit blanc 0.2 seconde
        tone = randint(2000,4000) # Choisit un nombre aléatoire ente 2000 et 4000
        hum.play(tone, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    for i in range(400): # Boucle de bruit blanc 0.4 seconde
        tone = randint(3000,5000) # Choisit un nombre aléatoire ente 3000 et 5000
        hum.play(tone, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    while True: # Boucle éternelle vérifiant la lecture du cadran pour définir la couleur et changer le son du bourdonnement
        if dial.value >= 0.8: # Réglage le plus élevé sur le cadran - 5
            led.color = (255,255,255) # Blanc
            led2.color = (255,255,255)
            hum.play(90)
        elif dial.value >= 0.6: # Réglage élevé sur le cadran - 4
            led.color = (255,0,255) # Lame violette
            led2.color = (255,0,255)
            hum.play(80)
        elif dial.value >= 0.4: # Réglage du milieu sur le cadran - 3
            led.color = (0,0,255) # Lame bleue
            led2.color = (0,0,255)
            hum.play(70)
        elif dial.value >= 0.2: # Réglage bas sur le cadran - 2
            led.color = (0,255,0) # Lame verte
            led2.color = (0,255,0)
            hum.play(60)
        elif dial.value >= 0.01: # Réglage le plus bas sur le cadran (au-dessus de 0,01) - 1
            led.color = (255,0,0) # Lame rouge
            led2.color = (255,0,0)
            hum.play(50)
        else: # Si le cadran est complètement tourné vers le bas - 0
            eteint() # Exécuter la fonction 'eteint'
            break # Quitter la boucle
    

puissance.when_pressed = actif