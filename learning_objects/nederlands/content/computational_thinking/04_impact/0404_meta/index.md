---
hruid: m_ct04_04
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
Geeft spraakassistent input aan aanbevelingsalgoritme voor reclame?  
</div>
</context>
<decomposition>
Verkennen van het probleem. Wat heb je nodig? <br> Subtaken (**decompositie**):<br>
- Taaltechnologie
    - speech-to-tect
    - text-to-speech
    - tekst analyseren
    - tekst genereren
- Dataopslag
- Energieverbruik
- Privacyaspecten
    - tekstdata worden opgeslagen om te kunnen verwerken
    - worden de data bewaard?
    - wie heeft toegang tot de data?
    - worden de data gedeeld?
        - bv. verwarming aanzetten m.b.v. Siri vergt samenwerking tussen twee digitale systemen 
- Manier om assistent te activeren 
    - gesproken trigger
- Aanbevelingsalgoritme voor gepersonaliseerde reclame
</decomposition>
<patternRecognition>
- Gepersonaliseerde reclame gebeurt o.a. op basis van lookalike audiences (via **patroonherkenning** worden aan een persoon dezelfde interesses toegedicht als van iemand met een soortgelijk profiel)
</patternRecognition>
<abstraction>
(**abstractie**)<br>
</abstraction>
<algorithms>
- Spraakherkenningstechnologie om spraak om te zetten naar tekst
- Natural language processing om betekenis te koppelen aan de tekst
- Generatieve technologie om eventueel een antwoord te formuleren
- Spraaksynthesetechnologie om tekst om te zetten naar spraak
- (Eventueel) een algoritme voor sentimentanalyse
- Aanbevelingsalgoritme voor gepersonaliseerde reclame
</algorithms>


