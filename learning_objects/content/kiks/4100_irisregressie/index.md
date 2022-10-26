---
hruid: KIKS_iris_regressie-v1
version: 3
language: nl
title: "Irisregressie"
description: "Irisregressie"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
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

# Irisregressie
De Iris dataset werd in 1936 door de Brit Ronald Fischer gepubliceerd. De dataset betreft drie soorten irissen (_Iris setosa_, _Iris virginica_ en _Iris versicolor_), 50 monsters van elke soort. Fischer kon de soorten van elkaar onderscheiden afgaande op vier kenmerken: de lengte en de breedte van de kelkbladen en de kroonbladen.

In de notebook hier wordt het lineair verband tussen de lengtes van de kelkblaadjes en de kroonblaadjes van de _Iris virginica_ bestudeerd. <br>
Je standaardiseert de gegevens en geeft ze weer in een puntenwolk. Je berekent de correlatiecoëfficiënt om te bekijken hoe sterk de lineaire samenhang tussen de twee kenmerken is. Vervolgens wordt de regressielijn gezocht en getekend.<br>
Met deze regressielijn wordt de lengte van een bloemblad voorspeld voor een gekende lengte van een kelkblad.<br>
In deze notebook bepaal je de regressielijn en de correlatiecoëfficiënt met de ingebouwde functies van de module SciPy en scikit-learn. In een volgende notebook wordt een machine learning-algoritme uit de doeken gedaan voor als je meer wilt weten.

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=1910 "Irisregressie")
