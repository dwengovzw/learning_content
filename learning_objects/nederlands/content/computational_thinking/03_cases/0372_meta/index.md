---
hruid: m_ct03_72
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
![Maatregelen COVID-19](covid19maatregelen.png)<br>
*Buitenplan 5 maart 2021*.<br>Afbeelding © NCCN, Brussel, België.
<div style="position:absolute;right:0px;width:40%;height:100px;margin-top:-100px;margin-right:20px">
Kunnen we het effect van de COVID-19-maatregelen inschatten voordat we ze invoeren?
</div>
</context>
<decomposition>
We identificeren 3 deelproblemen (**decompositie**):
1. Model voor verspreiding
2. Menselijke interacties voorstellen 
3. Simuleren van de verspreiding a.d.h.v. het model
</decomposition>
<patternRecognition>
De verspreiding van de pest, cholera, COVID-19 ... gedraagt zich gelijkaardig. We onderscheiden daarbij: vatbare individuen, geïnfecteerden en resistente individuen. (**patroonherkenning**)<br><br>
Interacties tussen mensen kunnen we op dezelfde manier voorstellen als verbindingen tussen steden (wegen), nl. met een graaf. (**patroonherkenning**)
</patternRecognition>
<abstraction>
We stellen de interacties tussen de mensen **abstract** voor door een graaf.
    ![Sociaal netwerk](sociaalnetwerk.png)
De evoluties in de aantallen vatbare individuen, geïnfecteerden en resistente individuen worden **abstract** voorgesteld door differentiaalvergelijkingen.  
![Stelsel differentiaalvergeljkingen epidemie](differentiaalvergelijkingenepidemie.png)
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

