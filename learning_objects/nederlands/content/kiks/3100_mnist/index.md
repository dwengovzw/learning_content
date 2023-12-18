---
hruid: kiks_mnist
version: 3
language: nl
title: "MNIST"
description: "MNIST"
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# MNIST
De MNIST-dataset bestaat uit 70.000 afbeeldingen van handgeschreven cijfers, elk 28 x 28 pixels in grijswaarden. 

![](embed/drie.jpg "Een drie uit de MNIST dataset")
<figure>
    <figcaption align = "center">Een drie uit de MNIST-dataset.</figcaption>
</figure>

Van de afbeeldingen in de MNIST-dataset worden er 60.000 gebruikt om een neuraal netwerk te **trainen** en 10.000 om het te **testen**.
Het uiteindelijke neurale netwerk dient om handgeschreven cijfers te kunnen herkennen die het netwerk niet eerder gezien heeft.

In een eerste notebook werk je met een **feedforward neuraal netwerk**.<br>
In een tweede notebook werk je met een **convolutioneel neuraal netwerk**; hier gebruik je naast een training- en testset ook een **valideringsset**.  <br>
Je kan de opbouw en de prestaties van deze netwerken met elkaar vergelijken. Door de parameters in deze netwerken aan te passen verwerf je inzichten in de invloed van deze parameters op de training en de prestaties. 

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=1810 "MNIST")
