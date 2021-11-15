---
hruid: PN_Epidemie2-v1
version: 3
language: nl
title: "SIR-model"
description: "Epidemie"
keywords: ["voorbeeld", "voorbeeld2"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [14, 15, 16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-andere-talen', 
    'http://ilearn.ilabt.imec.be/vocab/ondniv/sec-gr2-doorstroom-aso'
]
---

# Het SIR-model

Een epidemie wordt wiskundig gemodelleerd met het SIR-model.  
SIR staat voor *Susceptible* (vatbaar), *Infected* (geïnfecteerd) en *Resistant* (resistent of hersteld), de drie types individuen die in een gemeenschap voorkomen. 
Meestal zijn de individuen gewoon mensen, maar dit model kan ook aangewend worden om ziekte-uitbraak bij knaagdieren, vogels of zelfs planten te modelleren. 

A.d.h.v. het SIR-model simuleert men bv. hoe het aantal besmettingen zal evolueren of wat het effect is van vaccinatie. In deze notebook leer je het SIR-model kennen.

*** 

**Zelf aan de slag: de verspreiding van een ziekte doorheen een netwerk**

We hebben een Jupyter Notebook ontwikkeld met een interactief SIR-ziekteverspreidingsmodel. Je kan hiermee zelf aan de slag. Surf naar [onze Jupyter Notebook server](http://kiks.ilabt.imec.be/jupyter/) en kies *Simuleer Epidemie*. Druk vervolgens op *Spawn*. 
Open vervolgens de notebook *SimuleerEenEpidemie.ipynb*. Bekijk eventueel eerst onze [oefeningen programmeren](https://scholen.dwengo.org/nl/pythoninitiatie.html).

***

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=1220 "Notebooks Epidemie")
