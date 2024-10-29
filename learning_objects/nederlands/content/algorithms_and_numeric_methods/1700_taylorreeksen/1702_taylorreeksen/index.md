---
hruid: anm_1702
version: 3
language: nl
title: "Taylor"
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

# Taylorontwikkeling

Omdat je niet altijd een functie wilt benaderen in 0, breid je deze techniek uit naar een andere waarde. Om het willekeurig te houden, noem je die waarde \\(a\\).

### Taylorveelterm
Als \\(f\\) \\(n\\) maal afleidbaar is in \\(a\\) dan kan je \\(f(x)\\) in de buurt van \\(a\\) benaderen door een Taylorontwikkeling:
\\[f(x) \thickapprox f(a)  + \frac{f'(a)}{1!} (x - a) +  \frac{f''(a)}{2!} (x - a)² + ... + \frac{f^{(n)}(a)}{n!} (x - a)^n\\]

### Benadering van *sin 61°*

\\(f(x) = sin \ x\\) en \\(x = \frac{61 \pi}{180}\\)<br>
60° ligt in de buurt van 61°, en de goniometrische getallen van 60° ken je (\\(cos \frac{\pi}{3} = \frac{1}{2}\\), \\(sin \frac{\pi}{3} = \frac{\sqrt{3}}{2}\\)).

\\(y = sin \ x\\) in de buurt van \\(a\\) benaderen met een Taylorveelterm:

\\[sin \ x \thickapprox sin \ a  + \frac{cos \ a}{1!} (x - a) -  \frac{sin \ a}{2!} (x - a)^2 - \frac{cos \ a}{3!} (x - a)^3 + ... + \frac{sin (a+\frac{n \pi}{2})}{n!} (x-a)^n\\]

\\(y = sin \frac{61 \pi}{180}\\) benaderen met een Taylorveelterm van de tweede graad (\\(n = 2\\)):  

\\[sin \frac{61 \pi}{180}  \thickapprox sin \frac{\pi}{3} + \frac{cos \frac{\pi}{3}}{1!} (\frac{61 \pi}{180} - \frac{\pi}{3}) -  \frac{sin \frac{\pi}{3}}{2!} (\frac{61 \pi}{180} - \frac{\pi}{3})^2\\]
dus \\[sin \frac{61 \pi}{180}  \thickapprox \frac{\sqrt{3}}{2} + \frac{1}{2} (\frac{\pi}{180}) -  \frac{\sqrt{3}}{4} (\frac{\pi}{180})²\\]
dus \\[sin \frac{61 \pi}{180}  \thickapprox 0,87452 ... \\]

### Oefening

#### Oefening 1 
Bepaal de eerste vier termen in x − 2 van de Taylorveelterm rond x = 2 van de volgende functies:<br>
\\(f(x) = e^{\frac{x}{2}}\\) en \\(f(x) = \sqrt x\\)

#### Oefening 2
Bereken een benadering voor \\(\sqrt[3]{9}\\)  aan de hand van een Taylorontwikkeling.
