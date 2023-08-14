## Bouwen en testen

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Nu is het tijd om je sensorische gadget te maken.  
</div>
<div>
![drie afbeeldingen op een doos met eten, drinken en spelen. Een van de afbeeldingen wordt verlicht door een LED.](images/communication-tool.PNG){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Je sensorische gadget is je eigen ontwerp en kan een **andere combinatie** van onderdelen hebben dan die in de onderstaande diagrammen worden gesuggereerd. 

Als een pin al in gebruik is, moet je een andere pin en aarde selecteren om te gebruiken. Zorg ervoor dat je **noteert** welke pin in gebruik is voor wanneer je je code schrijft. 
</p>

Je hebt een aantal echt nuttige vaardigheden opgebouwd. Hier is een herinnering om je te helpen je sensorische gadget te maken:

### Verbind je outputs

[[[sharing-a-ground-pin]]]

--- task ---

### LED's met één kleur

[[[single-led-wiring]]]

[[[multiple-single-led-wiring]]]

[[[sing-led-pins]]]

[[[multiple-single-led-pins]]]

--- collapse ---

---
Title: Voeg een functie toe om een enkele LED in te schakelen
---

--- code ---
---
language: python filename: sensory-gadget.py line_numbers: false line_number_start: 1
line_highlights: 1-2
---
def excited(): # Your mood purple.on() # Turn on

--- /code ---

--- /collapse ---

--- collapse ---

---
Title: Voeg functies toe om meerdere afzonderlijke LED's te bedienen
---

--- code ---
---
language: python filename: sensory-gadget.py line_numbers: false line_number_start: 1
line_highlights: 1-2
---
def excited(): # Your first mood purple.on() # Turn on blue.off() # Turn off

def worried(): # Your second mood purple.off() # Turn off blue.on() # Turn on

--- /code ---

--- /collapse ---

### RGB-LED's

[[[rgb-wiring]]]

[[[rgb-led-pins]]]

--- collapse ---

---
Title: Voeg functies toe om een RGB LED-kleur in te stellen
---

--- code ---
---
language: python filename: sensory-gadget.py line_numbers: false line_number_start: 1
line_highlights: 1-5
---
def happy(): # Your first mood rgb.color = (0, 255, 0) # Your first colour

def sad(): # Your second mood rgb.color = (255, 0, 0) # Your second colour

--- /code ---

--- /collapse ---

[[[generic-theory-simple-colours]]]

### Luidsprekers en zoemers

\[[[single-buzzer-wire]]\] \[[[stereo-buzzer-wiring\]]] \[[[earphones-wiring]]\] \[[[single-buzzer-pin\]]] [[[multiple-buzzer-pins]]]

**Nuttige informatie over geluid**

\[[[list-of-notes]]\] \[[[note-length\]]] \[[[frequency-numbers]]\] \[[[sheet-to-notes\]]]

**Voorbeelden van geluidscode**

\[[[play-single-note]]\] \[[[play-a-tune\]]] \[[[pico-sound-frequency]]\] \[[[whitenoise-drum-beat\]]] \[[[notes-in-loop]]\] \[[[interrupt-tune\]]]

--- /task ---

### Sluit je ingangen aan

--- task ---

### Drukknop

[[[single-button-wiring]]]

[[[multiple-button-wiring]]]

--- collapse ---

---
title: Button importeren
---

--- code ---
---
language: python filename: sensory-gadget.py line_numbers: false line_number_start: 1
line_highlights: 1
---

from picozero import Button

--- /code ---

--- /collapse ---

\[[[single-button-pins]]\] \[[[multiple-button-pins\]]]

--- collapse ---

---
Title: Roep een andere functie aan wanneer elke knop wordt ingedrukt
---

Je kunt meerdere knoppen hebben die elk een andere functie aanroepen wanneer ze worden ingedrukt.

Zorg ervoor dat je de functienamen van je project gebruikt, zonder haakjes.

--- code ---
---
language: python filename: sensory-gadget.py line_numbers: false line_number_start:
line_highlights:
---

happy_button.when_pressed = happy sad_button.when_pressed = sad angry_button.when_pressed = angry

--- /code ---

--- /collapse ---

--- collapse ---

---
Title: Ga naar de volgende functie wanneer er op een knop wordt gedrukt
---

Gebruik een `optie` variabele om de huidige stemming bij te houden, zodat je kunt beslissen welke functie je daarna wil aanroepen.

Zorg ervoor dat de functienamen overeenkomen met de humeurfuncties die je in de vorige stap hebt gedefinieerd.

--- code ---
---
language: python filename: sensory-gadget.py line_numbers: false line_number_start:
line_highlights:
---
option = 0 # Store the current option

def choice(): # Call the next function and update the option global option if option == 0: energised() # Your first mood elif option == 1: calm()      # Your second mood elif option == 2: focused()   # Your third mood elif option == 3:    
rgb.off()

    # Move to the next option
    if option == 3:
        option = 0
    else:
        option = option + 1

button.when_pressed = choice # Call the choice function when the button is pressed

--- /code ---

--- /collapse ---

### Schakelaar

[[[crafted-switch-button-wiring]]]

[[[multiple-crafted-switch-button-wiring]]]

--- collapse ---

---
title: Switch importeren
---

--- code ---
---
language: python filename: sensory-gadget.py line_numbers: false line_number_start: 1
line_highlights: 1
---

from picozero import Switch

--- /code ---

--- /collapse ---

\[[[single-switch-pins]]\] \[[[multiple-switches-pins\]]]

### Potentiometer

\[[[potentiometer-wiring]]\] \[[[potentiometer-pin\]]]

--- collapse ---

---
title: Potentiometer importeren
---

--- code ---
---
language: python filename: sensory-gadget.py line_numbers: false line_number_start: 1
line_highlights: 1
---

from picozero import Pot

--- /code ---

--- /collapse ---

[[[potentiometer-function-value]]]

--- /task ---

--- task ---

**Test:** Test de in- en uitgangen om ervoor te zorgen dat alles werkt zoals verwacht.

Gebruik de **foutopsporing** taak onderaan deze stap als je problemen tegenkomt.

--- /task ---

### Maak je gadget

--- task ---

[[[mount-components]]]

[[[diffuse-leds]]]

--- collapse ---

---
title: Gebruik tape om de verbindingsdraden op hun plaats te houden
---

Gebruik plakband of isolatietape om de verbindingsdraden op hun plaats te houden zodat het toestel bij elkaar blijft.

Je kunt de tape later verwijderen als je de onderdelen opnieuw wilt gebruiken.

--- /collapse ---

[[[using-craft-knife]]]

[[[joining-jumper-wires]]]

[[[drop-switch]]]

[[[pull-switch]]]

[[[taping-components]]]

--- /task ---

--- task ---

**Test:** Laat iemand anders jouw project zien en vraag feedback. Wil je iets aan je gadget veranderen?

--- /task ---

--- task ---

**Fouten oplossen:** Mogelijk vind je enkele fouten in jouw project die je moet oplossen. Hier zijn enkele veelvoorkomende fouten.

\[[[debug-pico-code]]\] \[[[debug-pico-hardware\]]] [[[pico-debug-led]]]

Code wordt uitgevoerd, maar er gebeurt niets:
+ Controleer of je ingangen correct zijn aangesloten en of je de juiste pin in je code hebt gebruikt.
+ Kijk in de Thonny-shell of er berichten zijn over variabelen of functies die niet worden gedefinieerd; je bent misschien vergeten om de voorbeelden aan te passen aan je code.
+ Controleer je code zorgvuldig. Je zou `print` commando's kunnen toevoegen om je te helpen begrijpen wat er gebeurt.
+ Controleer of je je functies hebt aangeroepen.

--- collapse ---

---
Title: Roep een functie aan.
---

--- code ---
---
language: python filename: sensory-gadget.py line_numbers: false line_number_start: 1
line_highlights: 7
---
def happy(): # Your first mood rgb.color = (0, 255, 0) # Your first colour

def sad(): # Your second mood rgb.color = (255, 0, 0) # Your second colour

happy()

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Mijn LED licht niet op als ik mijn functie aanroep
---

Controleer of de pinnen in je code overeenkomen met de pinnen waarop je LED is aangesloten.

--- /collapse ---

--- collapse ---

---
Title: Mijn RGB-LED geeft de verkeerde kleur aan
---

Controleer je code om er zeker van te zijn dat je kleurwaarden in de juiste volgorde staan. Gebruik de ['RGB kleur gids'](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} om te controleren of de code overeenkomt met de kleur die je verwacht.

--- /collapse ---

--- collapse ---
---
Title: Mijn geluiden worden niet afgespeeld of worden niet afgespeeld zoals ik had verwacht
---

Je code werkte voordat je je sensorische gadget samenstelde. Het is onwaarschijnlijk dat je code in dit stadium zal worden gebroken. Het merendeel van de fouten zal afkomstig zijn van bedrading en componenten.

+ Controleer of de componenten op de juiste pinnen zijn aangesloten (je zou deze eerder moeten hebben genoteerd, ze worden bovenaan je code weergegeven)
+ Zoek naar losse aansluitingen en zet deze vast met tape
+ Controleer of je geen geleidende elementen van je circuit hebt bedekt met plakband of lijm

--- /collapse ---

--- collapse ---

---
title: De hoofdmelodie wordt te laat afgespeeld wanneer ik op een knop druk
---

Wanneer je een gebeurtenis gebruikt zoals `when_pressed` om een functie uit te voeren, wordt die functie uitgevoerd totdat deze is voltooid en stopt de andere code.

Als je een melodie met een gebeurtenis ("event") wilt starten, kun je `play` gebruiken met `wait=False`. De functie wordt voltooid en de melodie blijft spelen zonder de code die in je hoofdcode wordt uitgevoerd te vertragen.

--- code ---
---
language: python line_numbers: true line_number_start:
line_highlights:
---

sound = [ [523, 0.1], [None, 0.1], [523, 0.4] ]

def annoying_sound(): speaker.play(sound, wait=False) # Don't delay the main code

button.when_pressed = annoying_sound

--- /code ---

--- /collapse ---

--- collapse ---
---
Title: Mijn draden zijn niet lang genoeg nu ze in mijn sensorische gadget zitten
---

Nu je je sensorische gadget hebt gemaakt, heb je mogelijk extra lange draden nodig om je component aan je Raspberry Pi Pico-pinnen te bevestigen. Bekijk de instructies hierboven om 'verbindingsdraden te verbinden om ze te verlengen'.

--- /collapse ---

--- collapse ---
---
Title: Mijn draden of onderdelen blijven niet op hun plaats
---

Sommige verbindingen zijn sterker dan andere, dus het kan zijn dat je tape moet gebruiken om je draden verbonden te houden met je componenten of om je componenten op hun plaats te houden. Bekijk de bovenstaande instructies om 'draden en onderdelen te beschermen met tape'.

--- /collapse ---

Mogelijk vind je een fout die hier niet wordt vermeld. Kun je erachter komen hoe je het kunt oplossen?

We horen graag over je fouten en hoe je ze hebt opgelost. Gebruik de feedback knop onderaan deze pagina als je een andere bug in je project hebt gevonden.

--- /task ---



