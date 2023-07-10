---
hruid: pc_theremin8
version: 3
language: nl
title: "Theremin bouwen"
description: "Theremin bouwen"
keywords: ["Microcontroller"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
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

# Theremin

## Theremin bouwen

Na de virtuele theremin is het nog een kleine stap naar een fysiek exemplaar. Het meeste denkwerk i.v.m. het programma is immers al gebeurd. 
Bij de bouw van een fysieke theremin zal je wel nog een beperkt aantal elektronische schakelingen moeten maken.
Daarna komt een extra uitdaging: je programma finetunen zodat je een instrument bekomt dat nog leuker is.

***

Eens je met de theremin begint te spelen, zal je gauw merken dat de het volledige spectrum een beetje teveel van het goede is. De hoge tonen worden al snel schril en het is moeilijk om de theremin nauwkeurig in te zetten daar je frequenties met stappen van 59 Hz springen. Hier kan je een mouw aan passen door de factor bij de afstand te verminderen.

Hieronder vind je een voorbeeld waarbij de factor is aangepast van 59 naar 10.

![blockly](@learning-object/theremin_8/nl/3)

<div class="alert alert-box alert-success">
Door de factor bij de afstand aan te passen, kan je het bereik van de theremin inperken tot lagere tonen en tegelijk de nauwkeurigheid van de theremin verbeteren.<br><br>

Door de factor van 59 naar 10 te veranderen wordt het bereik 210 - 2200, wat meer dan voldoende is om een degelijk instrument te maken.
Het verschil in nauwkeurigheid is ook opmerkzaam. De tonen zullen nu slechts met 10 Hz verschillen i.p.0v. 59 Hz, wat de theremin ook veel beter doet klinken.
</div>