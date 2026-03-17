---
hruid: pc_toestandsautomaten1
version: 3
language: nl
title: "Definitie"
description: "Wat zijn toestandsautomaten en hoe werken ze?"
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

# Definitie toestandsautomaat

De toestandsautomaat (ook wel Finite State Machine genoemd) is een abstract model voor een bepaalde machine of systeem. Het bestaat uit twee elementen:
- Een eindig aantal toestanden.
- Transities tussen toestanden.

De toestanden beschrijven de huidige omgeving waarin de machine zich bevindt. Elke toestand is een samenvatting van de acties die de automaat al uitgevoerd heeft. De machine kan zich maar in één toestand tegelijk bevinden.

We kunnen een automaat voorstellen aan de hand van een toestandsdiagram. Voor elke toestand tekenen we een cirkel met daarin de naam en het nummer van de toestand. De overgangen tussen de toestanden geven we aan met behulp van pijlen tussen deze cirkels. Je ziet een voorbeeld op onderstaande afbeelding.

![toestandsdiagram](./embed/ttd.png)