---
hruid: anm_1501
version: 3
language: nl
title: "Afgeleiden"
description: "Afgeleiden"
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

# De definitie van een afgeleide

De afgeleide van \\(f\\) in \\(a\\) is per definitie de richtingscoëfficiënt van de raaklijn in \\(a\\) aan de grafiek van \\(f\\).<br>
Men noteert de afgeleide van \\(f\\) in \\(a\\) kort als \\(𝑓′(𝑎)\\). 
Dus \\(𝑓′(𝑎) = \text{rico} \; 𝑡\\), met \\(t\\) de raaklijn in het punt \\((a, f(a))\\) aan de grafiek van \\(f\\). 

![image](https://github.com/dwengovzw/learning_content/assets/48352335/c77daeb7-d16d-48f8-8a01-1d66b997168f)

De rico van een stijgende rechte is positief, van een dalende rechte negatief. <br>
In een punt waar de grafiek stijgt, zal de afgeleide dus positief zijn. In een punt waar de grafiek daalt, zal de afgeleide negatief zijn.

![image](https://github.com/dwengovzw/learning_content/assets/48352335/00b6ba1a-f1a2-43d2-9685-c4038b792686)

Beschouw de snijlijn s. <br>
Als 𝑥→𝑎, dan s →𝑡. <br>
Dus dan rico s →rico 𝑡  <br>
m.a.w. rico s →𝑓′(𝑎) 

![image](https://github.com/dwengovzw/learning_content/assets/48352335/47a96f2e-94fc-4b30-8e8a-74fc5850db9c)

-----

In het leerpad [Limieten](https://dwengo.org/learning-path.html?hruid=anm11&language=nl&te=true&source_page=%2Falgorithms%2F&source_title=%20Algoritmes#anm_1100;nl;3) leerde je hoe je een limiet numeriek kan benaderen. In dit leerpad gebruik je die techniek om met afgeleiden te werken.

Gezien de definitie van de afgeleide als limiet van het differentiequotiënt is het duidelijk dat dit kan. 

-------------

# Afgeleide functie

Als men in elk punt van een functie f de afgeleide bepaalt, dan heeft men een nieuwe functie, nl. de **afgeleide functie** \\(f’\\).  
\\(f’(x)\\) is positief voor een \\(x \\)waarin \\(f\\) stijgt en negatief voor een \\(x\\) waarin \\(f\\) daalt. 

