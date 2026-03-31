---
hruid: pc_toestandsautomaten1
version: 3
language: nl
title: "Probleemstelling"
description: "Hoe kan je systemen gemakkelijk omzetten naar code"
keywords: ["toestandsautomaat", "toestandsdiagram", "finite state machine", "toestand", "definitie"]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [10, 11, 12]
difficulty: 3
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Probleemstelling

Wat een bepaalde machine of bepaald systeem moet doen, hangt vaak af van zijn vorige en huidige acties. Bij het programmeren moet je dus niet alleen rekening houden met de huidige invoer, maar ook met de geschiedenis van het systeem.

Zonder een duidelijke structuur, leidt dit snel tot ingewikkelde en moeilijk leesbare code. Er worden dan veel geneste if/else-structuren en losse variabelen gebruikt. Zo'n code wordt ook wel *spaghetticode* genoemd, en zorgt voor een aantal problemen:
- Moeilijk af te leiden in welke situatie - **toestand** - het systeem zich bevindt
- Verschillende afhankelijkheden tussen blokken code
- Ongewilde gevolgen indien (een deel van) de code wordt aangepast

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Hieronder is het gedrag van een verkeerslicht geschreven in code. Het volledige gedrag wordt verder in dit leerpad opgegeven als oefening op toestandsdiagrammen. Er is met opzet veel spaghetticode geschreven. Bekijk de code eens goed. Kun jij volgende vragen snel afleiden uit wat je ziet?
        <ul>
          <li>Wat gebeurt er indien er op de knop wordt gedrukt en het licht rood is?
          <li>Kunnen alle 3 de lichten tegelijk uit staan?
          <li>In hoeveel situaties - <b>toestanden</b> - kan het verkeerslicht zich bevinden?</li>
        </ul>
    </div>
</div>

```python
button_pressed = False
light_green = True
light_orange = False
light_red = False

orange_timer = 0
red_timer = 0

while True:
  # knop indrukken
  if detect_button_press():
    button_pressed = True

  # als knop ingedrukt en licht is groen → oranje
  if button_pressed and light_green:
    light_green = False
    light_orange = True
    orange_timer.start()        # start oranje timer
    print("ORANJE")

  # overgang oranje → rood
  if light_orange:
    if orange_timer >= 4:
      light_orange = False
      light_red = True
      red_timer.start()         # start rode timer
      print("ROOD")

  # overgang rood → groen
  if light_red:
    if red_timer >= 20:
      light_red = False
      light_green = True
      button_pressed = False
      print("GROEN")

  # extra logica (maakt het erger)
  if button_pressed and light_red:
    # knop doet hier eigenlijk niets, maar staat er toch
    print("Wachten...")

  if not light_green and not light_orange and not light_red:
    light_green = True
```