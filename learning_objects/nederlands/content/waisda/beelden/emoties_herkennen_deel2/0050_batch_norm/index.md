---
hruid: org-dwengo-waisda-beelden-emoties-deel2-batchnorm
version: 1
language: nl
title: "Batch normalisatie"
description: "Wat is de batch normalisatie?"
keywords: ["lagen", "AI", "neurale netwerken", "batch normalisatie"]
content_type: "text/markdown"
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# Batch normalisatie

Batch normalisatie zal de invoer van de laag **normaliseren**. Dat wil zeggen dat de laag de waarden van de invoer zal omzetten naar waarden tussen bijvoorbeeld -1 en 1. Doen we dat niet, dan is het mogelijk dat elke afbeelding in een ander bereik door het netwerk gaat. Voor de ene afbeelding kan een laag dan een invoer met waarden tussen 0 en 1000 krijgen en voor een andere afbeelding een invoer tussen -10 en 0,01. Deze variatie zorgt ervoor dat het netwerk minder gemakkelijk leert. Om dit te vermijden ga je elke invoer dus omzetten naar een gelijkaardig bereik. 

Zo'n normalisatie kan je uitvoeren door van de waarde het gemiddelde af te trekken en dan te delen door de standaardafwijking.

1. Bereken het gemiddelde

\\[\mu = \frac{1}{m} \sum_{i=1}^{m}{x_i}\\]

2. Bereken de variantie

\\[\sigma^2 = \frac{1}{m} \sum_{i=1}^{m}{(x_i - \mu)^2}\\]

3. Normaliseer de waarde

\\[\hat{x}_i = \frac{x_i - \mu}{\sqrt{\sigma^2+\epsilon}}\\]


Hier is \\(\epsilon\\) een hele kleine waarde > 0 om ervoor te zorgen dat je nooit kan delen door nul.

Batch normalisatie zal het trainingsproces **stabieler maken**, zorgen dat het model **sneller convergeert** en het **minder gevoelig maken voor variaties** in de invoer.