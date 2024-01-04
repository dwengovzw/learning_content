---
hruid: org-dwengo-elevator-riddle-brute-force-1
version: 1
language: nl
title: "Brute kracht"
description: "Als eerste oplossingsmethode kunnen we de brute kracht techniek (brute force) toepassen."
keywords: ["grafen", "algoritme", "computationeel denken", "clustering", "datastructuur", "brute force"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
difficulty: 5
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 2
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
]
teacher_exclusive: false
---

# Brute kracht

Als eerste oplossingsmethode kunnen we de brute kracht techniek (brute force) toepassen. Dit is een gekende techniek in de informaticawetenschappen. Deze bestaat erin om alle mogelijkheden uit te proberen en dan te controleren welke de beste was.
Concreet kunnen we de brute kracht techniek opdelen in verschillende deelproblemen (**decompositie**).
1. Het genereren van alle mogelijke manieren om de graaf te verdelen in twee grafen met een gelijk aantal knopen.
2. Voor een gegeven verdeling van de graaf berekenen hoe groot de **kost** is van de **knip** om tot die verdeling te komen.
3. De **knip** zoeken met de laagste **kost**.


