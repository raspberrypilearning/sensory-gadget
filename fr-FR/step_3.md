## Construire et tester

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Il est maintenant temps de fabriquer ton gadget sensoriel.  
</div>
<div>
![Trois images sur une boîte montrant manger, boire et jouer. L'une des images est rétroéclairée par une LED.](images/communication-tool.PNG){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Ton gadget sensoriel est ta propre conception et peut avoir une **combinaison différente** de composants par rapport à ceux suggérés dans les schémas ci-dessous. 

Si une broche est déjà utilisée, tu devras sélectionner une broche et une masse différentes à utiliser. Assure-toi de **noter** la broche utilisée lorsque tu écris ton code. 
</p>

Tu as acquis des compétences vraiment utiles. Voici un rappel pour t'aider à fabriquer ton gadget sensoriel :

### Connecter tes sorties

[[[sharing-a-ground-pin]]]

--- task ---

### LEDs monochromes

[[[single-led-wiring]]]

[[[multiple-single-led-wiring]]]

[[[sing-led-pins]]]

[[[multiple-single-led-pins]]]

--- collapse ---

---
title: Ajouter une fonction pour allumer une seule LED
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 1-2
---
def excite(): # Ton humeur
    violet.on() # Allumer

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Ajouter des fonctions pour contrôler plusieurs LED individuelles
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 1-2
---
def excite(): # Ta première humeur
    violet.on() # Allumer
    bleu.off() # Éteindre

def worried(): # Your second mood
    violet.off() # Éteindre
    bleu.on() # Allumer

--- /code ---

--- /collapse ---

### LEDs RVB

[[[rgb-wiring]]]

[[[rgb-led-pins]]]

--- collapse ---

---
title: Ajouter des fonctions pour définir la couleur d'une LED RVB
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 1-5
---
def heureux(): # Ta première humeur
    rvb.color = (0, 255, 0) # Ta première couleur

def triste(): # Ta deuxième humeur
    rvb.color = (255, 0, 0) # Ta deuxième couleur

--- /code ---

--- /collapse ---

[[[generic-theory-simple-colours]]]

### Haut-parleurs et buzzers

[[[single-buzzer-wire]]]
[[[stereo-buzzer-wiring]]]
[[[earphones-wiring]]]
[[[single-buzzer-pin]]]
[[[multiple-buzzer-pins]]]

**Informations utiles sur le son**

[[[list-of-notes]]]
[[[note-length]]]
[[[frequency-numbers]]] 
[[[sheet-to-notes]]]

**Exemples de code sonore**

[[[play-single-note]]]
[[[play-a-tune]]]
[[[pico-sound-frequency]]]
[[[whitenoise-drum-beat]]]
[[[notes-in-loop]]]
[[[interrupt-tune]]]

--- /task ---

### Connecter tes entrées

--- task ---

### Bouton

[[[single-button-wiring]]]

[[[multiple-button-wiring]]]

--- collapse ---

---
title: Importer Button
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Button

--- /code ---

--- /collapse ---

[[[single-button-pins]]]
[[[multiple-button-pins]]]

--- collapse ---

---
title: Appeller une fonction différente lorsque chaque bouton est enfoncé
---

Tu peux avoir plusieurs boutons qui appellent chacun une fonction différente lorsqu'ils sont enfoncés.

Assure-toi d'utiliser les noms de fonction de ton projet et n'utilise que le nom de la fonction; ne l'appelle pas en ajoutant des crochets.

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 
line_highlights: 
---

bouton_heureux.when_pressed = heureux
bouton_triste.when_pressed = triste
bouton_colere.when_pressed = colere

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Passer à la fonction suivante lorsqu'un seul bouton est enfoncé
---

Utilise une variable `option` pour garder une trace de l'humeur actuelle afin que tu puisses décider quelle fonction appeler ensuite.

Assure-toi que les noms de fonction correspondent aux fonctions d'ambiance que tu as défini à l'étape précédente.

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 
line_highlights: 
---
option = 0 # Mémoriser l'option actuelle

def choix(): # Appelle la fonction suivante et met à jour l'option
    global option
    if option == 0:
        energique() # Ta première humeur
    elif option == 1:
        calme()      # Ta deuxième humeur
    elif option == 2:
        concentre()   # Ta troisième humeur
    elif option == 3:    
        rvb.off()
    
    # Passer à l'option suivante
    if option == 3:
        option = 0
    else:
        option = option + 1
    
bouton.when_pressed = choix # Appelle la fonction de choix lorsque le bouton est enfoncé

--- /code ---

--- /collapse ---

### Interrupteur

[[[crafted-switch-button-wiring]]]

[[[multiple-crafted-switch-button-wiring]]]

--- collapse ---

---
title: Importer Switch
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Switch

--- /code ---

--- /collapse ---

[[[single-switch-pins]]]
[[[multiple-switches-pins]]]

### Potentiomètre

[[[potentiometer-wiring]]]
[[[potentiometer-pin]]]]

--- collapse ---

---
title: Importer Potentiometer
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Pot

--- /code ---

--- /collapse ---

[[[potentiometer-function-value]]]

--- /task ---

--- task ---

**Test :** Teste tes entrées et sorties pour t'assurer que tout fonctionne comme prévu.

Utilise la tâche **débogage** au bas de cette étape si tu rencontres des problèmes.

--- /task ---

### Fabrique ton gadget

--- task ---

[[[mount-components]]]

[[[diffuse-leds]]]

--- collapse ---

---
title: Utiliser du ruban adhésif pour maintenir les fils de raccordement en place
---

Utilise du ruban adhésif ou du ruban électrique pour maintenir les fils de liaison en place afin que ton appareil reste solidaire.

Tu peux retirer la bande ultérieurement si tu souhaites réutiliser les composants.

--- /collapse ---

[[[using-craft-knife]]]

[[[joining-jumper-wires]]]

[[[drop-switch]]]

[[[pull-switch]]]

[[[taping-components]]]

--- /task ---

--- task ---

**Test :** Montre ton projet à quelqu'un d'autre pour avoir son avis. Souhaites-tu apporter des modifications à ton gadget ?

--- /task ---

--- task ---

**Débogage :** Il est possible que tu trouves des bogues dans ton projet que tu dois corriger. Voici quelques bogues assez courants.

[[[debug-pico-code]]] 
[[[debug-pico-hardware]]]
[[[pico-debug-led]]]

Le code s'exécute, mais rien ne se passe :
+ Vérifie que tes entrées sont correctement connectées et que tu as utilisé la bonne broche dans ton code.
+ Vérifie le shell Thonny pour tout message concernant des variables ou des fonctions non définies; tu as peut-être oublié de modifier les exemples pour qu'ils correspondent à ton code.
+ Vérifie bien ton code. Tu peux ajouter des instructions `print` pour t'aider à comprendre ce qui se passe.
+ Vérifie que tu as appelé tes fonctions.

--- collapse ---

---
title: Appeler une fonction
---

--- code ---
---
language: python
filename: sensory-gadget.py
line_numbers: false
line_number_start: 1
line_highlights: 7
---
def heureux(): # Ta première humeur
    rvb.color = (0, 255, 0) # Ta première couleur

def triste(): # Ta deuxième humeur
    rvb.color = (255, 0, 0) # Ta deuxième couleur

heureux() 

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Ma LED ne s'allume pas lorsque j'appelle ma fonction
---

Vérifie que les broches de ton code correspondent aux broches auxquelles ta LED est connectée.

--- /collapse ---

--- collapse ---

---
title: Ma LED RVB affiche la mauvaise couleur
---

Vérifie ton code pour t'assurer que tes valeurs de couleur sont dans le bon ordre. Utilise le ['Guide des couleurs RVB'](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} pour vérifier que ton code correspond à la couleur que tu attends.

--- /collapse ---

--- collapse ---
---
title: Mes sons ne sont pas joués, ou ne sont pas joués comme je l'attendais
---

Ton code fonctionnait avant que tu n'aies assemblé ton gadget sensoriel. Il est peu probable que ton code soit cassé à ce stade. La majorité des bogues proviendront du câblage et des composants.

+ Vérifie que tes composants ont été câblés sur les bonnes broches (tu aurais dû les noter plus tôt, elles sont affichées en haut de ton code)
+ Recherche les connexions desserrées et fixe-les avec du ruban adhésif
+ Vérifie que tu n'as recouvert aucun élément conducteur de ton circuit avec du ruban adhésif ou de la colle

--- /collapse ---

--- collapse ---

---
title: La mélodie principale est retardée lorsque j'appuie sur un bouton
---

Lorsque tu utilises un événement tel que `when_pressed` pour exécuter une fonction, cette fonction s'exécutera jusqu'à ce qu'elle soit terminée et empêchera l'exécution d'autres codes.

Si tu souhaites démarrer une mélodie à partir d'un événement, tu peux utiliser `play` avec `wait=False`. La fonction se terminera et la mélodie continuera à jouer sans retarder l'exécution du code dans ton code principal.

--- code ---
---
language: python
line_numbers: true
line_number_start: 
line_highlights: 
---

son = [ [523, 0.1], [None, 0.1], [523, 0.4] ]

def son_ennuyeux():
    haut_parleur.play(sound, wait=False) # Ne pas retarder le code principal
    
bouton.when_pressed = son_ennuyeux

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Mes fils ne sont plus assez longs maintenant qu'ils sont dans mon gadget sensoriel
---

Maintenant que tu as conçu ton gadget sensoriel, tu auras peut-être besoin de fils extra-longs pour attacher ton composant à tes broches Raspberry Pi. Regarde les instructions ci-dessus pour "joindre les fils de connexion pour les étendre".

--- /collapse ---

--- collapse ---
---
title: Mes fils ou mes composants ne tiennent pas en place
---

Certaines connexions sont plus solides que d'autres, tu devras donc peut-être utiliser du ruban adhésif pour maintenir tes fils connectés à tes composants ou pour maintenir tes composants en place sur ton gadget. Consulte les instructions ci-dessus pour "fixer les fils et les composants à l'aide de ruban adhésif".

--- /collapse ---

Tu pourrais trouver un bogue qui n'est pas répertorié ici. Peux-tu trouver comment le résoudre?

Nous aimons avoir des nouvelles de tes bogues et de la façon dont tu les as corrigés. Utilise le bouton de commentaires au bas de cette page si tu as trouvé un bogue différent dans ton projet.

--- /task ---



