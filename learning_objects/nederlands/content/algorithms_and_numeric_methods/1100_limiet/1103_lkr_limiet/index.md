---
hruid: anm_1103
version: 3
language: nl
title: "Limiet van een functie"
description: "Limiet"
keywords: [""]
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
# Limiet van een functie

Heel intuïtief zit het zo: stel dat je weet dat de limiet van een functie bestaat, dan heb je genoeg aan 1 rij 'die op de functie ligt' om die limiet numeriek te benaderen.

![functielimiet](https://github.com/dwengovzw/learning_content/assets/48352335/0ea7256a-956f-4c48-8596-30ae91a5e3e9)

Op deze grafiek zie je dat: 

\\(\lim_{x \to +\infty} f(x) =  2 \\)

en

\\(\lim_{x \to -\infty} f(x) = +\infty\\).

Concreet betekent dat dat **elke** dalende rij 'die gelegen is op de grafiek van \\(f'\\) ook 2 als limiet heeft en dat **elke** stijgende rij 'die gelegen is op de grafiek van \\(f'\\) ook \\(+\infty\\) als limiet heeft. 
(Als de rij daalt, dan "beweegt' die zich op de functie van links naar rechts. Als de rij stijgt, dan "beweegt' die zich op de functie van rechts naar links.) 

---------
# Notebook

In de notebook ga je aan de slag met deze opdracht: 

Beschouw de funtie \\(f(x)=\frac{1}{x}\\).  <br>
Bepaal naar welk getal \\(f(x)\\) nadert bij heel grote en heel kleine waarden van \\(x\\). <br>
Bepaal naar welk getal \\(f(x)\\) nadert als \\(x\\) nadert naar \\(0\\).

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/hub/tmplogin?id=6515 "Limiet van een functie")
