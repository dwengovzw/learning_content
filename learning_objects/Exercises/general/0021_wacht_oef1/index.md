---
hruid: g_wacht_oef1
version: 3
language: nl
title: "Oefening Wacht 1"
description: "Oefening Wacht 1"
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
teacher_exclusive: false
---
## Wacht

OPGAVE 1.1

Schrijf een programma dat het volgende doet:

* Laat "Hallo mensen" op het lcd-scherm verschijnen gedurende 1 seconde (1000 ms).
* Laat "Ik ben Dwenguino" op het lcd-scherm verschijnen voor 2 seconden (2000 ms).
* Herhaal.

<div class="alert alert-box alert-danger">
Let erop dat je hiervoor de code in het <em>'herhaal'-deel</em> van het <em>'zet klaar/herhaal'-blok</em> plaatst!<br>
Het programma herhaalt enkel code die in het <em>'herhaal'-deel</em> staat.
</div>

***

OPGAVE 1.2

Als je het lcd-scherm correct geprogrammeerd hebt, zou je het volgende probleem moeten ondervinden: 

> <span style="color:green">H&nbsp;a&nbsp;l&nbsp;&nbsp;l&nbsp;o&nbsp;&nbsp;&nbsp;&nbsp;m&nbsp;e&nbsp;&nbsp;n&nbsp;s&nbsp;e&nbsp;n</span><br>
<span style="color:red">&nbsp;I&nbsp;k&nbsp;&nbsp;&nbsp;&nbsp;b&nbsp;e&nbsp;n&nbsp;&nbsp;&nbsp;&nbsp;D&nbsp;w&nbsp;e&nbsp;n&nbsp;g&nbsp;u&nbsp;i&nbsp;n&nbsp;o</span><br>
<span style="color:green">H&nbsp;a&nbsp;l&nbsp;&nbsp;l&nbsp;o&nbsp;&nbsp;&nbsp;&nbsp;m&nbsp;e&nbsp;&nbsp;n&nbsp;s&nbsp;e&nbsp;n</span><span style="color:red">&nbsp;u&nbsp;i&nbsp;n&nbsp;o</span><br>
<span style="color:red">&nbsp;I&nbsp;k&nbsp;&nbsp;&nbsp;&nbsp;b&nbsp;e&nbsp;n&nbsp;&nbsp;&nbsp;&nbsp;D&nbsp;w&nbsp;e&nbsp;n&nbsp;g&nbsp;u&nbsp;i&nbsp;n&nbsp;o</span><br>
<span style="color:green">H&nbsp;a&nbsp;l&nbsp;&nbsp;l&nbsp;o&nbsp;&nbsp;&nbsp;&nbsp;m&nbsp;e&nbsp;&nbsp;n&nbsp;s&nbsp;e&nbsp;n</span><span style="color:red">&nbsp;u&nbsp;i&nbsp;n&nbsp;o</span><br>
...

Los het probleem op m.b.v. het <em>'maak lcd-scherm leeg'-blok</em>: 

![alt](embed/maaklcdleeg.png "maak lcd-scherm leeg")