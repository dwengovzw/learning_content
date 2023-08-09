---
hruid: stem5_3
version: 3
language: nl
title: "Logistische groei"
description: "Logistische groei"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [12, 13, 14]
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
# Modelleren van een rupsenuitbraak volgens de logistische groei

Eerder bekeek je het exponentiële groeimodel om een populatie rupsen voor te stellen. Je stelde hierbij vast dat je ooit op een limiet moeten botsen: een tuin heeft geen onbeperkte draagkracht! In deze module bekijk je daarom de logistische groei. Dit model heeft een verrassende eigenschap: het kan chaotisch zijn, waardoor het voor bepaalde waarden totaal onvoorspelbaar is!

## Logistische groei

**Je zoekt een regel die rekening houdt met de draagkracht van het systeem.** Er wordt verwacht dat wanneer de populatiegrootte klein is, en er dus veel planten per rups zijn, onbelemmerde groei mogelijk is. Wanneer het aantal rupsen dicht bij de draagkracht \\(K\\) komt, moet de groei stoppen. De volgende regel kan hiervoor gebruikt worden:

\\[u_t = \left[1 + (a - 1) \left(1 - \frac{u_{t - 1}}{K}\right)\right] u_{t - 1} = \left[1 + r \left(1 - \frac{u_{t - 1}}{K}\right)\right] u_{t - 1}\\]

Dit is het recursieve voorschrift van een meetkundige rij, waarbij \\(a\\) de groeifactor en \\(r\\) het groeipercentage voorstelt. Ook hier geldt dat als je \\(u_0\\) kent, je stapsgewijs elk element uit de rij kan berekenen.

Uit het functievoorschrift stel je vast dat als \\(u_{t - 1}\\) klein is, het gedeelte tussen ronde haakjes ongeveer gelijk is aan \\(1\\). Je bekomt dan bij benadering terug de exponentiële groei:

\\[u_t = \left[1 + r \left(1 - \frac{u_{t - 1}}{K}\right)\right] u_{t - 1} \approx (1 + r) \cdot u_{t - 1} = a \cdot u_{t - 1}\\]

Herinner je dat \\(a\\) hierbij de groeifactor voorstelt. Wanneer \\(u_{t - 1}\\) bij benadering gelijk is aan \\(K\\), dan is het deel tussen ronde haakjes ongeveer gelijk aan \\(0\\), en zal de populatiegrootte in de volgende stap min of meer gelijk zijn:

\\[u_t = \left[1 + r \left(1 - \frac{u_{t - 1}}{K}\right)\right] u_{t - 1} \approx u_{t - 1}\\]

De populatiegrootte stabiliseert dus.

Een model waarbij de populatie aangroeit volgens het voorgestelde recursieve voorschrift wordt een **logistisch model** genoemd!

## Interactieve notebook

Nu ga je aan de slag met een interactieve online notebook, waarin je Python zal gebruiken om dit model grafisch voor te stellen.

[![Knop](embed/knop.png "https://colab.research.google.com/github/jvdrhoof/Insects/blob/main/hoofdstuk_2.ipynb")](https://colab.research.google.com/github/jvdrhoof/Insects/blob/main/hoofdstuk_2.ipynb)
