## Ce que tu vas faire

Fabriquer un jouet ou un gadget sensoriel. Ton gadget devra respecter la **fiche de projet**.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Un <span style="color: #0faeb0">gadget sensoriel</span> est quelque chose qui te donne envie de continuer à interagir avec lui. Un jouet fidget est un type de gadget sensoriel qui aide l'utilisateur à soulager le stress ou à améliorer sa concentration. Un gadget adaptatif peut être utilisé par les personnes souffrant d'un handicap physique pour communiquer. Un gadget sensoriel peut stimuler tous les sens ou se concentrer sur un seul.
</p>

Tu vas devoir :
+ Utiliser tes compétences en création numérique pour concevoir et fabriquer un gadget pour un utilisateur
+ Utiliser des entrées physiques telles que des boutons et des potentiomètres pour contrôler des sorties physiques telles que des LEDs et un buzzer
+ Laisser les autres essayer ton gadget et l'améliorer en fonction de leurs commentaires

--- no-print ---

Pour mener à bien ce projet, tu auras besoin de :

**Matériel :**

Tu peux acheter tout le matériel requis pour ce projet et les autres projets de ce parcours à partir de la boutique en ligne [Pimoroni.](https://shop.pimoroni.com/products/pico-intro-kit?variant=39893512945747){:target='_blank'} et la boutique en ligne [Kitronik.](https://kitronik.co.uk/products/5343-raspberry-pi-foundation-pico-pathway-pack){:target='_blank'}

+ Un Raspberry Pi Pico avec des broches soudées dessus
+ Un câble de données USB A vers micro USB
+ Une variété de composants électroniques et de câbles de liaison

**Logiciel:**
+ Thonny : ce projet peut être réalisé à l'aide de l'éditeur Thonny Python, qui peut être installé sur un ordinateur Linux, Windows ou Mac.

[[[thonny-install]]]

[[[change-theme-thonny]]]

+ picozero - tu devras configurer picozero sur ton Raspberry Pi Pico

[[[set-up-picozero]]]

--- task ---

### Découvrir ▶️

Regarde la vidéo ci-dessous. Comment l'outil est-il utilisé pour la communication ? Quelles entrées et sorties ont été utilisées ?

**Un gadget d'assistance** Un utilisateur peut sélectionner une option pour informer son soignant de son besoin actuel. Une fois qu'ils ont fait une sélection, ils appuient sur un autre bouton qui alerte leur soignant.

<video width="640" height="360" controls>
<source src="images/communication-tool.mp4" type="video/mp4">
Ton navigateur ne prend pas en charge la vidéo WebM, essaye FireFox ou Chrome
</video>

--- collapse ---
---
title: Voir à l'intérieur
---
--- code ---
---
language: python
filename: assistive_gadget.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
from picozero import LED, Speaker, Button
from time import sleep

manger = LED(13)
boire = LED(8)
jouer = LED(5)

haut_parleur = Speaker(1)

choisir = Button(18)
confirmer = Button(22)

option = 0 # Mémoriser l'option actuelle

def choix(): # Appelle la fonction suivante et met à jour l'option
    global option
    if option == 0:
        manger.on()
        boire.off()
        jouer.off()
    elif option == 1:
        manger.off()
        boire.on()
        jouer.off()    
    elif option == 2:
        manger.off()
        boire.off()
        jouer.on()   
    elif option == 3:
        manger.off()
        boire.off()
        jouer.off()

    if option == 3:
        option = 0
    else:
        option = option + 1

def son_buzzer():
    haut_parleur.on()
    sleep(1)
    haut_parleur.off()

choisir.when_pressed = choix 
confirmer.when_pressed = son_buzzer
--- /code ---

--- /collapse ---

--- /task ---

--- /no-print ---

--- print-only ---

**Un gadget d'assistance** Un utilisateur peut sélectionner une option pour informer son soignant de son besoin actuel. Une fois qu'ils ont fait une sélection, ils appuient sur un autre bouton qui alerte leur soignant.

![desc](images/communication-tool.PNG)

--- /print-only ---

<div style="border-top: 15px solid #f3524f; background-color: whitesmoke; margin-bottom: 20px; padding: 10px;">

### Résumé du projet : Gadget sensoriel
<hr style="border-top: 2px solid black;">
Fabrique un gadget sensoriel que les gens voudront utiliser.

Ton gadget sensoriel devrait :
+ Avoir plusieurs types d'entrées différents
+ Avoir plusieurs sorties différentes
+ Être attrayant pour l'utilisateur et suffisamment robuste pour être utilisé

Ton gadget sensoriel pourrait :
+ Prendre en considération l'ergonomie comme le confort de l'utilisateur
+ Réinitialiser sur saisie de l'utilisateur ou après un laps de temps défini 
+ Se connecter à un thème spécifique

</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">L'ergonomie</span> est une science qui cherche à surmonter les problèmes et à améliorer la façon dont les humains peuvent interagir avec leur environnement. L'amélioration de l'ergonomie d'un gadget le rendra plus facile à utiliser et plus agréable à manipuler. 
</p>

--- no-print ---

### Trouver des idées 💭

--- task ---

Pense au gadget sensoriel que tu aimerais créer en étudiant ces exemples de projets :

**Le ciel nocturne** De minuscules trous ont été percés dans un morceau de carton noir pour créer un effet de ciel nocturne sur le plafond d'une pièce sombre. Une LED RVB émet des impulsions pour créer un effet scintillant. Un bouton sert à allumer et éteindre la lumière.

<video width="640" height="360" controls>
<source src="images/the-night-sky.mp4" type="video/mp4">
Ton navigateur ne prend pas en charge la vidéo WebM, essaye FireFox ou Chrome
</video>

--- collapse ---
---
title: Voir à l'intérieur
---
--- code ---
---
language: python
filename: night_sky.py
line_numbers: true
line_number_start: 
line_highlights: 
---
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
--- /code ---

--- /collapse ---

**L'abeille bourdonnante** Les ailes de l'abeille ont du papier d'aluminium à l'arrière et lorsqu'elles sont enfoncées, elles se connectent à un autre morceau de papier d'aluminium sur la carte — cela fait jouer une note à un buzzer. Chaque aile joue un son différent. Un potentiomètre contrôle une LED bleue sur la queue de l'abeille.

<video width="640" height="360" controls>
<source src="images/buzy-bee.mp4" type="video/mp4">
Ton navigateur ne prend pas en charge la vidéo WebM, essaye FireFox ou Chrome
</video>

--- collapse ---
---
title: Voir à l'intérieur
---
--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 
line_highlights: 
---
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

--- /code ---


--- /collapse ---

**Picosaber** En appuyant sur le bouton, la lame du sabre s'allume et les buzzers émettent un bourdonnement. Tourner le potentiomètre change la couleur de la lame et la hauteur du bourdonnement. Tourner le potentiomètre à fond produit un « son de mise hors tension », puis éteint les lumières et les buzzers.

<video width="640" height="360" controls>
<source src="images/picosaber.mp4" type="video/mp4">
Ton navigateur ne prend pas en charge la vidéo WebM, essaye FireFox ou Chrome
</video>

--- collapse ---
---
title: Voir à l'intérieur
---
--- code ---
---
language: python
filename: saber.py
line_numbers: true
line_number_start: 
line_highlights: 
---
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
        ton = randint(4000,6000) # Choisit un nombre aléatoire ente 4000 et 6000
        hum.play(ton, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    for i in range(200): # Boucle de bruit blanc 1 seconde
        ton = randint(2000,4000) # Choisit un nombre aléatoire ente 2000 et 4000
        hum.play(ton, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    for i in range(200): # Boucle de bruit blanc 1 seconde
        ton = randint(1000,3000) # Choisit un nombre aléatoire ente 1000 et 3000
        hum.play(ton, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    for i in range(200): # Boucle de bruit blanc 1 seconde
        ton = randint(50,1000) # Choisit un nombre aléatoire ente 50 et 1000
        hum.play(ton, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    led.color = (0,0,0)
    led2.color = (0,0,0)
    hum.off()


# Faire le son de démarrage du sabre laser et allumer les lumières
def actif():
    for i in range(200): # Boucle de bruit blanc 0.2 seconde
        ton = randint(50,1000) # Choisit un nombre aléatoire ente 50 et 1000
        hum.play(ton, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    for i in range(200): # Boucle de bruit blanc 0.2 seconde
        ton = randint(1000,3000) # Choisit un nombre aléatoire ente 1000 et 3000
        hum.play(ton, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    for i in range(200): # Boucle de bruit blanc 0.2 seconde
        ton = randint(2000,4000) # Choisit un nombre aléatoire ente 2000 et 4000
        hum.play(ton, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    for i in range(400): # Boucle de bruit blanc 0.4 seconde
        ton = randint(3000,5000) # Choisit un nombre aléatoire ente 3000 et 5000
        hum.play(ton, 0.001) # Joue la tonalité pendant 1/1000e de seconde
    while True: # Boucle éternelle vérifiant la lecture du cadran pour définir la couleur et changer le son du bourdonnement
        if cadran.value >= 0.8: # Réglage le plus élevé sur le cadran - 5
            led.color = (255,255,255) # Blanc
            led2.color = (255,255,255)
            hum.play(90)
        elif cadran.value >= 0.6: # Réglage élevé sur le cadran - 4
            led.color = (255,0,255) # Lame violette
            led2.color = (255,0,255)
            hum.play(80)
        elif cadran.value >= 0.4: # Réglage du milieu sur le cadran - 3
            led.color = (0,0,255) # Lame bleue
            led2.color = (0,0,255)
            hum.play(70)
        elif cadran.value >= 0.2: # Réglage bas sur le cadran - 2
            led.color = (0,255,0) # Lame verte
            led2.color = (0,255,0)
            hum.play(60)
        elif cadran.value >= 0.01: # Réglage le plus bas sur le cadran (au-dessus de 0,01) - 1
            led.color = (255,0,0) # Lame rouge
            led2.color = (255,0,0)
            hum.play(50)
        else: # Si le cadran est complètement tourné vers le bas - 0
            eteint() # Exécuter la fonction 'eteint'
            break # Quitter la boucle
    

puissance.when_pressed = actif
--- /code ---

--- /collapse ---

**Bougie numérique** La LED RVB est sur une boucle qui ressemble à une flamme vacillante. En soufflant sur la bougie, un contact en feuille d'aluminium touche un autre contact de la bougie et arrête la boucle. Au bout d'un moment, la boucle redémarre.

![Animation montrant Mr C soufflant une bougie numérique.](images/candle.gif)

--- collapse ---
---
title: Voir à l'intérieur
---

--- code ---
---
language: python
filename: candle.py
line_numbers: true
line_number_start: 
line_highlights: 
---
from picozero import RGBLED, Switch
from time import sleep
from random import randint

# Indique à quelles broches les composants sont attachés sur le Pico
led = RGBLED(13, 14, 15)
declencher = Switch(18)


def lumiere(): # Boucle de flamme vacillante
      rouge = randint(125,255) # Principalement rouge
      jaune = (rouge - 125) # Jamais plus que rouge
      delai = randint(0,100)
      led.color = (rouge, jaune, 0)
      sleep(delai/1000)


def sombre(): # Pas de flamme
   led.off()
   sleep(2) # Temps sombre avant la réinitialisation


# Boucle pour vérifier si l'interrupteur est fermé
while True: 
    if declencher.is_closed:
        sombre()
    else:
        lumiere()

--- /code ---

--- /collapse ---

--- /task ---

--- /no-print ---

--- print-only ---

**Un gadget d'assistance** Un utilisateur peut sélectionner une option pour informer son soignant de son besoin actuel. Une fois qu'ils ont fait une sélection, ils appuient sur un autre bouton qui alerte leur soignant.
![desc](images/communication-tool.PNG)

**Le ciel nocturne** De minuscules trous ont été percés dans un morceau de carton noir pour créer un effet de nuit étoilée sur le plafond d'une pièce sombre. Une LED RVB émet des impulsions pour créer un effet scintillant.
![desc](images/night-sky.PNG)

**L'abeille bourdonnante** Les ailes de l'abeille ont du papier d'aluminium à l'arrière et lorsqu'elles sont enfoncées, elles se connectent à un autre morceau de papier d'aluminium sur la carte — cela fait qu'un buzzer joue une note. Chaque aile joue un son différent. Un potentiomètre contrôle une LED bleue sur la queue de l'abeille.
![desc](images/buzy-bee.png)

**Picosaber** En appuyant sur le bouton, la lame du sabre s'allume et les avertisseurs émettent un bourdonnement. Tourner le potentiomètre change la couleur de la lame et la hauteur du bourdonnement. Tourner le potentiomètre à fond produit un « son de mise hors tension », puis éteint les lumières et les buzzers.
![desc](images/picosaber.png)

**Bougie numérique** La LED RVB est sur une boucle qui ressemble à une flamme vacillante. Souffler sur la bougie provoque un contact entre une feuille d'aluminium et un autre contact sur la bougie et stoppe la boucle. Au bout d'un moment, la boucle redémarre.

![desc](images/candle.PNG)

--- /print-only ---


