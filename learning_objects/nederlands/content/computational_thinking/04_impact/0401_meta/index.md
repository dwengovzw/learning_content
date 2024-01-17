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
Systeem voor gepersonaliseerde reclame op online platform (aanbevelingsalgoritme). 
</div>
</context>
<decomposition>
Verkennen van het probleem. Wat heb je nodig? <br> Subtaken (**decompositie**):<br>
1. Persoonlijkheidsprofiel van de gebruiker: interesses, opinies, voorkeuren, natuur ... 
2. Data verzamelen over de gebruiker:
    - Socialemediaposts
    - Koopgedrag
    - Klikgedrag  
3. Profielen van andere gebruikers
4. Een algoritme om persoonlijkheidskenmerken af te leiden uit taalgebruik (NLP)
6. Een algoritme om patronen te herkennen in koop- en klikgedrag
7. Een algoritme om verwante profielen te herkennen  
8. Een aanbevelingsalgoritme 
</decomposition>
<patternRecognition>
    Meerdere vormen van **patroonherkenning** komen aan bod:
- Patronen in koop- en klikgedrag. 
- Het taalgebruik van de gebruiker analyseren om er persoonlijkheidskenmerken uit af te leiden, zoals leeftijd. 
- Vergelijken van gebruikers om verwante profielen op te sporen. 
</patternRecognition>
<abstraction>
De gebruikers worden herleid tot bepaalde persoonlijkheidskenmerken en hun koop- en klikgedrag (**abstractie**).<br>
</abstraction>
<algorithms>
- Er worden **algoritmes** gebruikt om een perssonlijkheidsprofiel op te stellen: dat zijn algoritmes voor *natural language processing*, m.a.w. taaltechnologie. 
- Andere algoritmes herkennen patronen in het koop- en klikgedrag.
- Met behulp van nog andere **algoritmes** worden er verwante profielen opgespoord. 
- Het persoonlijkheidsprofiel, patronen in koop- en klikgedrag, en het koop- en klikgedrag van gebruikers met een verwant profiel dienen als input voor een aanbevelingsalgoritme dat voor gepersonaliseerde reclame zal zorgen.<br>
</algorithms>
<implementation>
</implementation>

