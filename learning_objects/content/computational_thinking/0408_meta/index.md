---
hruid: m_ct_cases8
version: 3
language: nl
title: "SIR"
description: "SIR"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/ct-schema
available: true
target_ages: [12, 13, 14]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

<context>
![image](https://user-images.githubusercontent.com/48352335/208769355-bb0d30c7-add2-4f5a-a6da-77ec9d9dec85.png)
<div style="position:absolute;right:0px;width:40%;height:100px;margin-top:-100px;margin-right:20px">
Kunnen we het effect van de COVID-19-maatregelen inschatten voordat we ze invoeren?
</div>
</context>
<decomposition>
We identificeren 3 deelproblemen:
1. Model voor verspreiding
2. Menselijke interacties voorstellen 
3. Simuleren van het model
</decomposition>
<patternRecognition>
De verspreiding van de pest en cholera gedragen zich gelijkaardig waarbij we een verschil maken tussen vatbare individuen, geïnfecteerden en resistente individuen …(**patroonherkenning**)<br><br>
Interacties tussen mensen kunnen we op dezelfde manier als verbindingen tussen wegen of kennis van leerlingen, nl. met een graaf. (**patroonherkenning**)
</patternRecognition>
<abstraction>
Tekst
</abstraction>
<algorithms>
Stappenplan (**algoritme**):
1. Definieer het SIR-model door een stelsel van differentiaalvergelijkingen (zoals links)
2. Kies samenstelling van de beginpopulatie
3. Kies het infectiepercentage
4. Kies het herstelpercentage
5. Kies een tijdsinterval
6. Los het stelsel numeriek op
</algorithms>
<implementation>
Voor het programma: zie de notebooks in leerpad 'Epidemie'.
</implementation>

