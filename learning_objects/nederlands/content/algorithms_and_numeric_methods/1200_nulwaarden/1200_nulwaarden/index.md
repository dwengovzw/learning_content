---
hruid: anm_1200
version: 3
language: nl
title: "Nulwaarden"
description: "Nulwaarden"
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

# Nulwaarden 

![image](https://github.com/dwengovzw/learning_content/assets/48352335/24af4dc2-bf19-4490-a292-60022e233a8a)

Een nulwaarde van een functie \\(f\\) is een element \\(a\\) uit het domein van \\(f\\) waarvoor \\(f(a) = 0\\). 

## Halveringsmethode

Kies een punt \\(A\\) en een punt \\(B\\) op de grafiek van \\(f\\) aan weerszijden van de x-as. De grafiek van \\(f\\) zal de x-as snijden tussen \\(A\\) en \\(B\\). Wanneer je weet waar de grafiek de x-as ongeveer snijdt, dan kan je \\(A\\) en \\(B\\) gericht gaan kiezen. <br>
\\(A (a, f(a))\\) en \\(B (b, f(b))\\)

![image](https://github.com/dwengovzw/learning_content/assets/48352335/9aab0afb-121a-4018-ba34-fa92eff9c974)

Bepaal het midden \\(m_{1}\\) van \\([a, b]\\). Het punt \\(M_{1}\\) (\\(m_{1}\\),\\(f(m_{1}\\)) zal dichter bij het snijpunt met de x-as liggen dan \\(A\\) of \\(B\\).<br>
Door steeds dezelfde techniek toe te passen, wordt het nulpunt dichter en dichter benaderd.

![image](https://github.com/dwengovzw/learning_content/assets/48352335/0723a76e-416d-4114-975b-5bc5692ed64f)

## Methode van Newton

Kies een punt \\(A\\) op de grafiek van \\(f\\). Beschouw het snijpunt \\(S(s, 0)\\) van de raaklijn in \\(A\\) aan de grafiek van \\(f\\) met de x-as. <br>
Het punt \\(A'(s, f(s))\\) ligt dan dichter bij het snijpunt met de xa-s dan \\(A\\).<br>
Door steeds dezelfde techniek toe te passen, wordt het nulpunt dichter en dichter benaderd.

![newton](https://github.com/dwengovzw/learning_content/assets/48352335/28aedc24-5f27-403c-a64c-15ad3f28da68)
