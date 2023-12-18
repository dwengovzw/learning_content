---
hruid: m_ct04_03
version: 3
language: nl
title: "Sentimentanalyse"
description: "Sentimentanalyse"
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
ChatGPT 
</div>
</context>
<decomposition>
Verkennen van het probleem. Wat heb je nodig? <br> Subtaken (**decompositie**):<br>
1. Werking groot taalmodel
2. Training groot taalmodel
3. Wat kan ChatGPT? 
4. Wat kan ChatGPT niet?
</decomposition>
<patternRecognition>
1. Natural Language Processing: natuurlijke taal begrijpen en genereren a.d.h.v. patronen. ChatGPT begrijpt dus geen tekst op een manier dat een mens tekst begrijpt. 
2. Verschillende toepassingen zijn net als ChatGPT gebaseerd op grote taalmodellen, bv. automatische vertaling en zoekachines. 
    (**patroonherkenning**)
</patternRecognition>
<abstraction>
Woorden, zinsdelen, zinnen, paragrafen zijn gerepresenteerd als vectoren die rekening houden met 'veel samen voorkomen', de betekenis, ... maar worden zo ook uit hun context gerukt. ChatGPT zal gegeven een bepaalde tekst berekenen welk woord er het best op volgt. Het komt dus voor dat ChatGPT 'hallucineert', en dus onzin verkoopt. (**abstractie**)<br>
</abstraction>
<algorithms>
Het **algoritme** achter ChatGPT is getraind aan de hand van massa's digitale teksten. Aan de hand van gelabelde voorbeelden is het model ook leren omgaan met dialoog. Om het systeem 'menselijkere' antwoorden op prompts te laten genereren heeft men mensen de gegenereerde teksten laten ordenen van minder goed naar best. Op basis daarvan heeft men een scoresysteem ontwikkeld dat gebruikt werd om ChatGPT door versterkend leren te verbeteren in die zin dat het meer menselijke antwoorden geeft. <br>
</algorithms>
<implementation>
</implementation>
