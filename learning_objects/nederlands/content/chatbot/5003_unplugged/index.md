---
hruid: cb5_unplugged3
version: 3
language: nl
title: "Afstand"
description: "Afstand"
keywords: ["voorbeeld", "voorbeeld2"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-digitale-media-en-toepassingen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-stem-onderzoek', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek'
]
teacher_exclusive: true
---

# Afstand

![](@youtube/https://www.youtube.com/embed/JKGJ1u4Fk78)

*De regelgebaseerde chatbot zoekt elke 'vraag' op in zijn 'woordenboek'. 
Soms staat een vraag echter niet in het 'woordenboek' van de regelgebaseerde chatbot en weet hij niet wat antwoorden.
Om te vermijden dat de chatbot geen antwoord geeft, zal men ervoor zorgen dat de chatbot op zoek gaat naar een vraag die erop gelijkt. Hoe pak je dat aan? Tip:'Robots houden van getallen.' Als je de gelijkenis tussen twee vragen kunt weergeven door een getal, dan kan je de chatbot a.d.h.v. dat getal laten berekenen welke van de mogelijke vragen het best 'gelijkt' op de gestelde vraag. De chatbot zal dan het antwoord geven die hoort bij de gelijkende vraag. In de praktijk zullen gelijkende vragen echter niet altijd een gelijkende betekenis hebben.*

Om te kijken hoe goed bepaalde woorden op elkaar gelijken, zal de chatbot een **getal** uitrekenen:<br>
het aantal letters dat moet veranderd worden om de woorden gelijk te maken, gedeeld door het aantal leters van het langste woord.<br>
Dat getal wordt **afstand** genoemd. 

*De leerlingen proberen dit zelf uit op eenvoudige voorbeelden. Je kan hier gemakkelijk extra oefeningen op verzinnen.*

Deze oefeningen sluiten aan bij **minimumdoelen** voor de **finaliteit arbeidsmarkt**. 

<span style="color: yellowgreen">(06.01 Finaliteit arbeidsmarkt) De leerlingen voeren met functioneel gebruik van ICT eenvoudige berekeningen uit met gehele getallen, decimale getallen, breuken, procenten en verhoudingen in betekenisvolle contexten.</span>

<span style="color: yellowgreen">(06.06 Finaliteit arbeidsmarkt) De leerlingen lossen vanuit betekenisvolle contexten problemen op door wiskundige concepten en vaardigheden in te zetten.</span>

# Oefeningen bij afstand

Om te kijken hoe goed bepaalde woorden op elkaar gelijken, zal de chatbot een **getal** uitrekenen:<br>
het aantal letters dat moet veranderd worden om de woorden gelijk te maken, gedeeld door het aantal leters van het langste woord.<br>
Dat getal wordt **afstand** genoemd. 

**Voorbeeld**<br>
koken en haken -> er moeten twee letters veranderd worden: een 'k' en de 'h'. Beide woorden hebben 5 letters, het langste woord heeft dus 5 letters.<br>
De afstand = 2/5 = 0,4.<br>
<br>
koken en koren -> er moet 1 letter veranderd worden: een 'k'. Beide woorden hebben 5 letters, het langste woord heeft dus 5 letters.<br>
De afstand = 1/5 = 0,2.<br>  
<br>
Dit betekent dat 'koken' meer op 'koren' gelijkt dan op 'haken'.
<br>
koken en kokers -> er moet een letter veranderd worden en er moet een letter worden toegevoegd. Het langste woord heeft 6 letters.<br>
De afstand = 2/6 = 0,33333...<br>
<br>
Dit betekent dat 'koken' meer op 'kokers' gelijkt dan op 'haken', maar er minder op gelijkt dan op 'koren'.

<br>
<br>

*Laat de leerlingen dit uitproberen op andere woorden.*
