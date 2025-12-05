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
target_ages: [12, 13, 14, 15, 16, 17, 18]
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
**Probleemstelling**<br>
De teksten die ChatGPT (3.5) genereert, zijn niet altijd correct. 
</div>
</context>
<decomposition>
**Decompositie**<br>
- Werking ChatGPT 3.5
    - Prompt 'begrijpen'.
    - Als een bepaalde tekst aan ChatGPT wordt aangeboden, m.a.w. een prompt, dan zal hij *berekenen* welke tekst er het meest waarschijnlijk op volgt.
    - ChatGPT werkt in een dialoogvorm.
    - ChatGPT is heel snel.
- Training ChatGPT 3.5
    - Vertrekken van een groot taalmodel dat heeft leren genereren a.d.h.v. teksten tot begin 2021
        - Massa's digitale teksten, bv. Wikipedia, Reddit, websites en Engelstalige boeken 
    - Leren omgaan met dialoog
        - Oorspronkelijke dataset werd vermengd met conversaties die opgemaakt werden door mensen
    - Kenmerken menselijke antwoorden detecteren. 
    - Leren 'menselijkere' antwoorden genereren.
    - Zoveel mogelijk vermijden dat ChatGPT racistische, seksistische teksten, of haatspraak zou gaan genereren.
- ChatGPT 3.5 heeft geen toegang tot het internet.
- Eenvoudige interface
- Ontwikkelaars gebruiken input van gebruikers om het systeem te verbeteren.
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
- Een groot taalmodel werkt op basis van *Natural Language Processing* (NLP); het zal natuurlijke taal begrijpen en genereren a.d.h.v. patronen.
- Toepassingen, zoals automatische vertaling en zoekachines, zijn net als ChatGPT gebaseerd op grote taalmodellen.
</patternRecognition>
<abstraction>
**Abstractie**<br>
Woorden, zinsdelen, zinnen, paragrafen zijn gerepresenteerd als *vectoren* die rekening houden met 'veel samen voorkomen', de betekenis, ...,  maar worden zo ook uit hun context gerukt. Als een bepaalde tekst aan ChatGPT 3.5 wordt aangeboden, m.a.w. een prompt, dan zal hij *berekenen* welke tekst er het meest waarschijnlijk op volgt. *Hij houdt daarmee dus geen rekening met het waarheidsgehalte*.
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
- ChatGPT 3.5 is ontstaan uit een groot taalmodel GPT-3.5 (Generative Pre-trained Transformer), een model dat geleerd heeft uit voorbeelden (*gesuperviseerd leren*). Voor de training van GPT 3.5 werden machine learning algoritmes gebruikt, waaronder NLP. 
- Men heeft mensen door ChatGPT 3.5 gegenereerde teksten laten ordenen van minder goed naar best. Op basis daarvan werd er *ongesuperviseerd* een scoresysteem ontwikkeld. 
- A.d.h.v. dat scoresysteem werd ChatGPT 3.5 via *versterkend leren* getraind op het 'menselijker' antwoorden op prompts.
- Bijkomende training om racisme, seksisme en haatspraak te vermijden.<br>
</algorithms>
