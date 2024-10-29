---
hruid: anm_1701
version: 3
language: nl
title: "MacLaurinveelterm"
description: "Taylorreeksen"
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
teacher_exclusive: false
---

# MacLaurinveelterm voor $e^x$

### Stap 1: Benader $f(x) = e^x$ in $0$ door een eerstegraadsfunctie.

Beschouw de functie $f(x) = e^x$ in een basisomgeving van $0$.<br>
Benader ze door $f_{1}(x) = ax + b$ <br>
Voorwaarde: $f(0) = f_{1}(0)$ en $f'(0) = f_{1}'(0)$

Als je het stelsel van deze twee vergelijkingen oplost, ken je de waarden van $a$ en $b$, en dus ook de gezochte eerstegraadsfunctie.<br>

### Stap 2: Benader $f(x) = e^x$ in $0$ door een veeltermfunctie van de tweede graad.

Beschouw de functie $f(x) = e^x$ in een basisomgeving van $0$.<br>
Benader ze door $f_{2}(x) = ax^2 + b x + c$ <br>
Voorwaarde: $f(0) = f_{2}(0)$ en $f'(0) = f_{2}'(0)$ en $f''(0) = f_{2}''(0)$

Als je het stelsel van deze drie vergelijkingen oplost, ken je de waarden van $a$, $b$ en $c$, en dus ook de gezochte tweedegraadsfunctie.<br>

### Stap 3: Benader $f(x) = e^x$ in $0$ door een veeltermfunctie van de derde graad.

Bepaal zelf het functievoorschrift en het op te lossen stelsel van voorwaarden.

Je vindt: $e^x \thickapprox 1 + x + \frac{x^2}{2} + \frac{x^3}{6}$

### Stap 4: Benader $f(x) = e^x$ in $0$ door een veeltermfunctie van de vierde graad.

Bepaal zelf het functievoorschrift en het op te lossen stelsel van voorwaarden.

Je vindt: $e^x \thickapprox 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} $

### Stap 5: Benader $f(x) = e^x$ in $0$ door een veeltermfunctie van de n-de graad.

Vul zelf het gezochte functievoorschrift aan: $e^x \thickapprox 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + ... + \frac{...}{...}   $

### Toepassing: Benader hiermee het getal *e*

Merk op dat $e = e^{1}$
