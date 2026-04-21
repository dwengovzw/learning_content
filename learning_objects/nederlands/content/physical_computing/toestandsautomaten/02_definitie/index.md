---
hruid: pc_toestandsautomaten2
version: 3
language: nl
title: "Definitie"
description: "Wat zijn toestandsautomaten en hoe werken ze?"
keywords: ["toestandsautomaat", "toestandsdiagram", "finite state machine", "toestand", "definitie"]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [13, 14, 15, 16, 17, 18]
difficulty: 3
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Definitie toestandsautomaat

Het geziene programma is niet overzichtelijk. Er zijn veel variabelen en if/else-structuren. Bovendien is het gedrag bij een bepaalde situatie niet altijd geheel duidelijk.

Als oplossing kan je bij het programmeren gebruik maken van een **toestandsautomaat**. De **toestandsautomaat** (ook wel Finite State Machine genoemd) is een abstract model voor een bepaalde machine of systeem. Het bestaat uit twee elementen:
- Een eindig aantal toestanden.
- Transities tussen toestanden.

De **toestanden** beschrijven de huidige omgeving waarin de machine zich bevindt. Elke toestand is een samenvatting van de acties die de automaat al uitgevoerd heeft. De machine kan zich maar in één toestand tegelijk bevinden.

Toestandsautomaten zorgen ervoor dat er geen ongewilde onafhankelijkheden zijn tussen de toestanden. Er zit structuur in de code, waardoor het meteen duidelijk is in welke toestand het systeem zich bevindt en dus wat de machine aan het doen is.

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Hieronder staat opnieuw een programma voor hetzelfde verkeerslicht, deze keer geschreven aan de hand van een toestandsautomaat. Probeer zelf de vragen opnieuw te beantwoorden. Was dit nu gemakkelijker? Welke van de twee codes vind je duidelijker?
    </div>
</div>

```Python
# mogelijke toestanden
GREEN = "GREEN"
ORANGE = "ORANGE"
RED = "RED"

timer = 0

# eerste toestand initialiseren
state = GREEN

while True:
  if state == GREEN:
    if detect_button_press():
      state = ORANGE
      timer.count()             # start de timer
      print("ORANJE")

  elif state == ORANGE:
    if timer >= 4:
      state = RED
      timer = 0
      timer.count()
      print("ROOD")

  elif state == RED:
    if timer >= 20:
      state = GREEN
      timer = 0
      print("GROEN")
```