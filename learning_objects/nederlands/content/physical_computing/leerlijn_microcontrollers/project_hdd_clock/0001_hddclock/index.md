---
hruid: pc_hddclock1
version: 1
language: nl
title: "Een digitaal systeem"
description: "T"
keywords: ["Microcontroller"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
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

# HDD-klok

## Een digitaal systeem

Met behulp van een Dwenguino en enkele extra onderdelen kan je zelf een HDD klok programmeren. 

Een HDD klok is zoals de naam al verklapt een klok. Wat deze uniek maakt, is dat deze met behulp van LED lampjes en een snel draaiende schijf de illusie geeft van klok-wijzers die de tijd aangeven, net zoals bij een analoge klok.  

Het principe gaat als volgt; de klok maakt gebruik van een spindelmotor om een schijf, waar een smalle gleuf in gemaakt is, aan hoge snelheid te doen draaien. De smalle gleuf laat ons toe om LED-lampjes achter deze schijf te zien. Doordat de schijf zo snel draait en de ledlampjes net branden wanneer de smalle gleuf in de juiste positie staat, lijkt het alsof er wijzers weergegeven worden. 

Een vereenvoudigde, vertraagde weergave voor een schijf die de illusie geeft van een analoge wijzer om 12 uur is als volgt:
<img src="embed/clock.gif" alt="Werking HDD klok." title="Werking HDD klok."></img>  

***

Om een eenvoudige HDD klok te bouwen, gebruik je een Dwenguino die verbonden is aan een spindelmotor, een LED-strip en een snelheidssensor. De Dwenguino zal de spindelmotor met de schijf aan een hoge snelheid doen draaien en de LED-strip op het gepaste moment laten branden. De snelheidssensor wordt gebruikt om te weten waar de gleuf zich bevind op de schijf zodat de LED-lampjes juist getimed worden.


