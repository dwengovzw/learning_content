---
available: true
content_type: text/markdown
copyright: dwengo
description: "\xC9pid\xE9mie"
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: pn_epidemie1
keywords:
- voorbeeld
- voorbeeld2
language: fr
licence: dwengo
return_value:
  callback_schema:
    att: test
    att2: test2
  callback_url: callback-url-example
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-digitale-media-en-toepassingen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-kansrekenen-statistiek
- http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek
- http://ilearn.ilabt.imec.be/vocab/curr1/s-stem-onderzoek
target_ages:
- 16
- 17
- 18
title: "Mod\xE8les de propagation des maladies"
version: 3
---
# Modèles de propagation des maladies

Lors de l'apparition d'une maladie contagieuse, il est important de comprendre comment cette maladie peut se propager au cours des jours et des semaines suivants. Cela aidera à planifier l'utilisation optimale des ressources et du personnel afin d'enrayer la propagation de la maladie. De plus, avant de mettre ces mesures en œuvre, nous devons savoir comment elles peuvent influencer l'évolution de la maladie, afin que les mesures les plus efficaces et les moins coûteuses soient mises en place en premier.

Pour répondre à ces questions et à d'autres questions importantes, on utilise souvent des *modèles de propagation des maladies*. Ces modèles sont basés sur des équations mathématiques qui décrivent comment une maladie contagieuse se propage au fil du temps et/ou dans l'espace. Ils peuvent être utilisés pour répondre à des questions pertinentes, telles que :

* Sans intervention, la maladie s'éteindra-t-elle ou se propagera-t-elle de manière incontrôlée ?
* Combien de personnes doivent être vaccinées pour arrêter la propagation ?
* Comment le comportement des humains ou des animaux influence-t-il la propagation des maladies ?
* Quel effet auront différentes mesures de quarantaine ?

Étant donné que l'évolution dans le temps est cruciale en cas de propagation d'une maladie, presque tous les modèles de propagation des maladies sont de nature *dynamique*. Ils modélisent donc un changement au cours du temps. 
Dans ce projet, nous étudierons un type de modèle de propagation des maladies largement utilisé : le modèle SIR.

À chaque vague de la pandémie de COVID-19, le nombre d'infections ou le nombre d'hospitalisations connaît à un moment donné une croissance exponentielle. Dans ce projet, vous apprendrez, grâce à la régression, à déterminer une fonction exponentielle qui reflète cette tendance dans les données.