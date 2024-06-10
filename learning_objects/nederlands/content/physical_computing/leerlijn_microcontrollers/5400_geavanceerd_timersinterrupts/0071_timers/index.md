---
hruid: pc_micro_timers
version: 3
language: nl
title: "Timers"
description: "Timers"
keywords: ["Microcontroller", "timers"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# Timers

Alle info over de timers is ook terug te vinden in de hoofdstukken 13 tot 16 in de datasheet, maar die kunnen nogal overweldigend zijn. In de volgende paragrafen worden een aantal belangrijke concepten nog eens kort uitgelegd met een link naar de corresponderende delen van de datasheet.

In essentie is een Timer niet meer of minder dan een mechanisme in de microcontroller dat toelaat om bij te houden hoeveel klokcycli al verstreken zijn sinds het moment waarop de timer aangezet werd. Dat aantal wordt bijgehouden in een counter register waarvan de naam TCNTn is(waarbij n staat voor het nummer van de klok). Onze microcontroller heeft 4 Timers: Timer0 en Timer2 zijn 8-bit timers, wat wil zeggen dat zij maar tot 2^8 kunnen tellen, Timer1 en Timer3 zijn 16-bit timers, wat wil zeggen dat zij maximaal 2^16 ticks kunnen tellen. Info over de counter unit vind je bv. in sectie 15.4 voor de 16-bit timers.

Naast de counter unit zijn er extra functionaliteiten voorzien die het makkelijker maken om te reageren op bepaalde intervallen, bvb om een pin hoog te zetten telkens als er 100 ticks verstreken zijn. Dit zijn de zogenaamde *Modes of operation*. Hierover vind je meer in sectie 15.8 van de datasheet.

De *normal mode* is de standaard modus van de timer, m.a.w. je hoeft dus geen bits te configureren om deze mode te gebruiken. Lees sectie 15.8.1 van de datasheet om uit te vissen wat die modus precies inhoudt, al kan je het waarschijnlijk wel al afleiden uit de naam en de uitleg in de vorige paragraaf.

De CPU / IO klok van de microcontroller loopt aan 16MHz, zoals je weet. Een 16-bit timer kan daarom maar ongeveer 4µs tellen voor het TCNT register vol zit. Dat is niet bepaald lang en aarom is er ook nog de *prescaler* waarmee je de timers kan vertragen: het TCNTn register zal nu pas elke N klokcycli incrementeren. Meer over prescalers lees je op pagina 140 van de datasheet.