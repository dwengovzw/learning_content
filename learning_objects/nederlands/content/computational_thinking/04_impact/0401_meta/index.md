---
hruid: m_ct04_01
version: 3
language: nl
title: "Profilering"
description: "Profilering"
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
Systeem voor gepersonaliseerde reclame op online platform (aanbevelingsalgoritme). 
</div>
</context>
<decomposition>
**Decompositie**<br>
- Persoonlijkheidsprofiel van de gebruiker: interesses, opinies, voorkeuren, natuur ... 
- Data verzamelen en opslaan over de gebruiker:
    - Socialemediaposts
    - Koopgedrag
    - Klikgedrag  
- Profielen van andere gebruikers
- Een algoritme om persoonlijkheidskenmerken af te leiden uit taalgebruik (NLP)
- Een algoritme om patronen te herkennen in koop- en klikgedrag
- Een algoritme om verwante profielen te herkennen  
- Een aanbevelingsalgoritme 
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
- Patronen in koop- en klikgedrag 
- Het taalgebruik van de gebruiker analyseren om er persoonlijkheidskenmerken uit af te leiden, zoals leeftijd 
- Vergelijken van gebruikers om verwante profielen op te sporen 
</patternRecognition>
<abstraction>
**Abstractie**<br>
De gebruikers worden herleid tot bepaalde persoonlijkheidskenmerken en hun koop- en klikgedrag.
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
- Er worden algoritmes gebruikt om een persoonlijkheidsprofiel op te stellen: dat zijn algoritmes voor *natural language processing*, m.a.w. taaltechnologie. 
- Andere algoritmes herkennen patronen in het koop- en klikgedrag.
- Met behulp van nog andere algoritmes worden er verwante profielen opgespoord. 
- Het persoonlijkheidsprofiel, patronen in koop- en klikgedrag, en het koop- en klikgedrag van gebruikers met een verwant profiel dienen als input voor een aanbevelingsalgoritme dat voor gepersonaliseerde reclame zal zorgen.<br>
</algorithms>


