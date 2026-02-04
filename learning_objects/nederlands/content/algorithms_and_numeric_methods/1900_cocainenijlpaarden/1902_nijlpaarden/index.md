---
hruid: anm_1902
version: 1
language: nl
title: "Groei van de populatie"
description: "Exponentiële groei"
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
estimated_time: 20
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
Opmerking: Voor meer uitleg over regressie kan je terecht in de leerpaden van het thema *Python in de Wiskundeles*: [Lineaire regressie](https://dwengo.org/learning-path.html?hruid=maths_lineaireregressie&language=nl&te=true&source_page=%2Fmath_with_python%2F&source_title=%20Python%20in%20de%20Wiskundeles#pn_inleiding_lineaireregressie;nl;3) en [Regressielijnen](https://dwengo.org/learning-path.html?hruid=pn_regressie&language=nl&te=true&source_page=%2Fmath_with_python%2F&source_title=%20Python%20in%20de%20Wiskundeles#pn_voorkennis_regressielijnen;nl;3).

# Groei van de populatie

Enkele jaren terug poogden onderzoekers om de populatie nijlpaarden in kaart te brengen [1]. Ze publiceerden de volgende grafiek:

![41598_2023_33028_Fig3_HTML](https://github.com/user-attachments/assets/cc7d2ba7-f04d-48ea-9907-ef34f0558ede)

| Jaartal | Aantal nijlpaarden |
| --------| :-------:|
| 1994    |  4     |
| 2006    | 16     |
| 2009    | 28     |
| 2014    | 50     |
| 2016    | 60     |
| 2020    | 75     |

1994: 3 vrouwtjes en 1 mannetje van 23 jaar oud

In de notebook ga je op zoek naar een **wiskundig model** om de populatiegroei voor te stellen. <br>
Beantwoord eerst de volgende vragen:

- Gebaseerd op de gegeven grafiek, welke soort functie zal er vermoedelijk geschikt zijn om de populatiegroei te modelleren?
- Welk functievoorschrift hoort bij zo'n functie?
- Hoe zal je de parameters in het voorschrift van de gezochte functie bepalen?    

[![](embed/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=6100 "Cocaïnenijlpaarden notebooks")
en kies de eerste notebook (0100).

### Bronnen
[1] Subalusky, A.L., Sethi, S.A., Anderson, E.P. et al. Rapid population growth and high management costs have created a narrow window for control of introduced hippos in Colombia. *Sci Rep 13*, 6193 (2023). https://doi.org/10.1038/s41598-023-33028-y
 

