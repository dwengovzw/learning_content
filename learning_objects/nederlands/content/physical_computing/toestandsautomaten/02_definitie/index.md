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
estimated_time: 10
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

Toestandsautomaten zorgen ervoor dat er geen ongewilde afhankelijkheden zijn tussen de toestanden. Er zit structuur in de code, waardoor het meteen duidelijk is in welke toestand het systeem zich bevindt en dus wat de machine aan het doen is.

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Hieronder staat opnieuw een programma voor hetzelfde verkeerslicht, deze keer geschreven aan de hand van een toestandsautomaat. Probeer zelf de vragen opnieuw te beantwoorden. Was dit nu gemakkelijker? Welke van de twee codes vind je duidelijker?
    </div>
    <ul>
          <li>Wat gebeurt er indien er op de knop wordt gedrukt en het licht rood is?
          <li>Kunnen alle 3 de lichten tegelijk uit staan?
          <li>In hoeveel situaties - <b>toestanden</b> - kan het verkeerslicht zich bevinden?</li>
        </ul>
</div>

```cpp
// mogelijke toestanden
enum Toestanden {GROEN, ORANJE, ROOD};

unsigned int timer = 0;

// eerste toestand initialiseren
Toestanden toestand = GROEN;

void loop() {
  if (toestand == GROEN) {
    if (detecteer_knop()) {
      toestand = ORANJE; // ga over van groen licht naar oranje
      timer.start();     // start de timer
    }
  }

  else if (toestand == ORANJE){
    if (timer >= 4) {
      toestand = ROOD;   // ga over van oranje licht naar rood
      timer.reset();     // reset de timer
      timer.start();     // start de timer
    }
  }

  else if (toestand == RED) {
    if (timer >= 20) {
      toestand = GROEN;  // ga over van rood licht naar groen
      timer.reset();     // reset de timer
    }
  }
}
```