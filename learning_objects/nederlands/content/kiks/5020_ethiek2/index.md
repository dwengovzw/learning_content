---
hruid: kiks_ethiek2
version: 3
language: nl
title: "Bias bij KIKS"
description: "Bias bij KIKS"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Bias bij KIKS

Het KIKS-model bevat ook een bias. De foto’s van de trainingset zijn zo gemaakt dat de huidmondjes erop ongeveer passen in een vak van **120 op 120 pixels**.
Deze voorbeelden zijn afdrukken van bladeren genomen met transparante nagellak. Dat heeft als gevolg dat het model het best zal presteren op afbeeldingen
van even grote huidmondjes in een gelijkaardige, **groengrijze kleur**.

Dat betekent ook dat als je een microfoto aan het netwerk aanbiedt met te kleine huidmondjes of met veel verschillende kleuren, het netwerk de huidmondjes op die foto misschien niet goed detecteert.
