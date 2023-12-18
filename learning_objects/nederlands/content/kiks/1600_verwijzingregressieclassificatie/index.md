---
hruid: kiks_verwijzing
version: 3
language: nl
title: "Regressie en classificatie"
description: "Regressie en classificatie"
keywords: ["AI"]
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Regressie en classificatie

**Een machine learning-systeem verwerft met lerende algoritmes kennis uit data met de bedoeling uitkomsten te kunnen voorspellen betreffende nieuwe data.** 

<div class="alert alert-box alert-success">
        <ul>Het voorspellen gebaseerd op tendensen is een <b>regressieprobleem</b>.</ul>
        <ul>Het voorspellen van een klasse is een <b>classificatieprobleem</b>.</ul> 
Voorspellen betekent bijvoorbeeld dat er uit voorbije tendensen cijfers voor de toekomst gegenereerd worden (regressie) of dat een object bij een bepaalde categorie (klasse genoemd) wordt ingedeeld (classificatie).
</div>

<br><br> 
> **Concrete voorbeelden van regressie:** <br>
> - de prijs van een appartement voorspellen of beslissen (gebaseerd op de prijzen van appartementen die reeds verkocht zijn);<br>
> - uit het afnemen van de dikte van een gebergtegletsjer gedurende de voorbije decennia, de dikte van de komende jaren afleiden. <br>

> **Concrete voorbeelden van classificatie:** <br>
> - bepalen of een e-mail al dan niet spam is; <br>
> - van een foto kunnen zeggen of er al dan niet een huidmondje op staat.

![Regressie](embed/regressie.png "Regressie") 
<figure>
    <figcaption align = "center">Regressie.</figcaption>
</figure> 

![Classificatie](embed/classificatie.png "Classificatie") 
<figure>
    <figcaption align = "center">Classificatie.</figcaption>
</figure> 

Met machinaal leren kan men dus problemen van regressie en classificatie behandelen. Deze technieken worden voorgesteld in respectievelijk de leerpaden ['Classificatie'](https://www.dwengo.org/learning-path.html?hruid=kiks5_classificatie&language=nl&te=true&source_page=%2Fkiks%2F&source_title=%20KIKS#kiks_mnist;nl;3) en ['Regressie'](https://www.dwengo.org/learning-path.html?hruid=kiks6_regressie&language=nl&te=true&source_page=%2Fkiks%2F&source_title=%20KIKS#kiks_iris_regressie;nl;3).
