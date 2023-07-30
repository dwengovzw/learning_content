---
hruid: m_ct_cases3d
version: 3
language: nl
title: "Pythagoras - routeplanner"
description: "Pythagoras - routeplanner"
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
Automatiseer het berekenen van de schuine zijde van een rechthoekige driehoek als de rechthoekszijden gekend zijn.
</context>
<decomposition>
Subtaken (**decompositie**):<br>
1. Inzetten van de computer om de schuine zijde te berekenen. 
2. Formule? Gekend uit de stelling van Pythagoras.
3. Na de verwerking van de gegevens via de formule, is er een output. Hoe laat je de output proper verschijnen?
</decomposition>
<patternRecognition>

</patternRecognition>
<abstraction>

</abstraction>
<algorithms>
Het algoritme bevat (in deze volgorde) instructies om:
1. de gegevens;
2. die gegevens te verwerken met als doel het bekomen van de lengte van de schuine zijde;
3. de lengte van de schuine zijde te laten zien op het scherm. 

</algorithms>
<implementation>
**Programma in Python**
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
# invoer<br>
rhz1 = 3<br>
rhz2 = 4<br><br>
# verwerking<br>
schz = math.sqrt(rhz1**2 + rhz2**2)<br><br>
# uitvoer<br>
print("De lengte van de schuine zijde is: ", schz)
</p>
</div>
</implementation>
