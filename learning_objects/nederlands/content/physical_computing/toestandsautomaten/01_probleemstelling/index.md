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
target_ages: [13, 14, 15, 16, 17, 18]
difficulty: 3
estimated_time: 10
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

```cpp
bool knop_ingedrukt = false;

bool groen_licht = true;
bool oranje_licht = false;
bool rood_licht = false;

unsigned int oranje_timer = 0;
unsigned int rood_timer = 0;


void loop(){
  // knop indrukken
  if (detecteer_knop()) {
    knop_ingedrukt = true;
  }

  // als knop ingedrukt is en licht is groen → oranje
  if (knop_ingedrukt && groen_licht) {
    groen_licht = false;
    oranje_licht = true;
    oranje_timer.start();        // start timer voor oranje licht
    // Licht staat op oranje
  }

  // als het licht op oranje staat, na vier seconden → rood
  if (oranje_licht) {
    if (oranje_timer >= 4){
      oranje_licht = false;
      rood_licht = true;
      rood_timer.start();         // start timer voor rood licht
      // Licht staat op rood
    }
  }

  // als het licht op rood staat, na 20 seconden → groen
  if (rood_licht) {
    if (rood_timer >= 20){
      rood_licht = false;
      groen_licht = true;
      knop_ingedrukt = false;
      // Licht staat op groen
    }
  }

  // extra logica (maakt spaghetticode erger)
  if (knop_ingedrukt && rood_licht) {
    // knop doet hier eigenlijk niets
    Serial.println("Wachten...");
  }

  if (!groen_licht && !oranje_licht && !rood_licht) {
    groen_licht = true;
  }
}
```