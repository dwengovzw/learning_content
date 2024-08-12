---
hruid: pc_micro_p1_oef3
version: 3
language: nl
title: "Oefening 3"
description: "Oefening 3"
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
estimated_time: 30
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# Practicum 1

## Oefening 3: Tellers

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht 3.1</h2>
    <div class="content">
        Voor deze oefening bouw je verder op de code van de vorige oefening. In plaats van de lichtjes aan en uit te schakelen bij elke druk op de knop, gaan we nu een teller met 1 verhogen en dit getal binair uitschrijven naar de ledjes. Bij 16 moet de teller gereset worden. Gebruik steeds zo klein mogelijke datatypes.
    </div>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht 3.2</h2>
    <div class="content">
        <p>
            Schrijf nu een functie die dit 4-bit getal omzet naar Gray code. Surf naar <a href="https://en.wikipedia.org/wiki/Gray_code"><strong>deze pagina</strong></a> om hier meer informatie over te vinden. Gebruik waar mogelijk binaire operaties en geen vermenigvuldigingen of delingen die veel meer rekentijd in beslag nemen. (Hint: Je kan dit doen op 1 regel C-code met 2 operatoren) Toon de stand van de Gray code teller ook met de 4 leds.
        </p>
        <p>
            Pas nu je Gray code teller aan zodat, in plaats van te resetten bij 16, hij dan bij iedere druk op de knop aftelt tot je weer op nul komt. Vanaf dan wordt er terug opgeteld.
        </p>
    </div>
</div>