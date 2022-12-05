---
hruid: g_wacht_vb1
version: 3
language: nl
title: "Voorbeeld Wacht 1"
description: "Voorbeeld Wacht 1"
keywords: ["oefeningen", "wacht"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [10, 11, 12]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
## Wacht

OPGAVE 1

Schrijf een programma dat het volgende doet:

* Laat "Hallo mensen" op het lcd-scherm verschijnen gedurende 1 seconde (1000 ms).
* Laat "Ik ben Dwenguino" op het lcd-scherm verschijnen voor 2 seconden (2000 ms).
* Herhaal.

Oplossing:

![blockly](@learning-object/wacht_m1/nl/3)

<div class="alert alert-box alert-success">
Het <em>'wacht'-blok</em> dat <strong>na</strong> een bepaalde instructie staat, geeft weer hoelang de computer moet <strong>wachten</strong> vooraleer deze met de volgende instructie mag beginnen.
</div>


<div class="alert alert-box alert-danger">
Let erop dat je hiervoor de code in het <em>'herhaal'-deel</em> van het <em>'zet klaar/herhaal'-blok</em> plaatst!<br>
Op die manier zal alle code in het <em>'herhaal'-deel</em> blijven herhaald worden.
</div>

***

Je merkt op dat de simulator inderdaad afwisselt tussen "Hallo mensen" en "Ik ben Dwenguino". Deze oneindige herhaling veroorzaakt echter een nieuw probleem: 

![alt](embed/lcdvoorbeeld.png "Voorbeeld tekst")

Dit probleem wordt veroorzaakt doordat het lcd-scherm niet alle karakters refresht, maar enkel de karakters die veranderen.

> <span style="color:green">H&nbsp;a&nbsp;l&nbsp;&nbsp;l&nbsp;o&nbsp;&nbsp;&nbsp;&nbsp;m&nbsp;e&nbsp;&nbsp;n&nbsp;s&nbsp;e&nbsp;n</span><br>
<span style="color:red">&nbsp;I&nbsp;k&nbsp;&nbsp;&nbsp;&nbsp;b&nbsp;e&nbsp;n&nbsp;&nbsp;&nbsp;&nbsp;D&nbsp;w&nbsp;e&nbsp;n&nbsp;g&nbsp;u&nbsp;i&nbsp;n&nbsp;o</span><br>
<span style="color:green">H&nbsp;a&nbsp;l&nbsp;&nbsp;l&nbsp;o&nbsp;&nbsp;&nbsp;&nbsp;m&nbsp;e&nbsp;&nbsp;n&nbsp;s&nbsp;e&nbsp;n</span><span style="color:red">&nbsp;u&nbsp;i&nbsp;n&nbsp;o</span>

Om dit op te lossen, gebruik je het *'maak lcd-scherm leeg'-blok* om het lcd-scherm telkens leeg te maken voordat er nieuwe tekst verschijnt:

![blockly](@learning-object/wacht_m2/nl/3)
