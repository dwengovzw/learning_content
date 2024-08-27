---
hruid: org-dwengo-waisda-beelden-teachable-machine-example-model
version: 1
language: nl
title: "Een AI-model"
description: "Hoe werkt de Teachable machine van Google."
keywords: ["Neurale netwerken", "Imagenet", "Teachable machine", "fine tuning"]
content_type: "text/markdown"
estimated_time: 2
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# AI-model

Op de pagina van Teachable Machine, zie je twee knoppen die verwijzen naar een **"model"**. De knoppen hebben respectievelijk de namen **Model trainen** en **Model exporteren**. **Wat is dat nu eigenlijk, een model?**

Een **AI-model** is een verzamelnaam voor verschillende soorten informatie die nodig zijn om het AI-model te doen werken. Het model bestaat uit **een architectuur, algoritmes voor de evaluatie en de geleerde parameters (de gewichten)**. Hieronder lichten we die verschillende concepten toe:

* **De architectuur**: De architectuur legt de structuur van het model vast. Er zijn verschillende soorten AI-modellen, allemaal met hun eigen architectuur. Een neuraal netwerk bestaat bijvoorbeeld uit een aantal lagen met verbindingen ertussen. Er bestaan ook andere AI-modellen bijvoorbeeld random forests, zo'n model bestaat niet uit lagen maar wel uit een verzameling van binaire bomen.
* **Algoritmes**: Er zijn verschillende algoritmes nodig om met een model te kunnen werken. Er zal een algoritme nodig zijn om het model iets te "leren" maar ook om het model een voorspelling te laten doen. Een bekend algoritme dat we gebruiken om neurale netwerken iets te leren is **backpropagation**.
* **De geleerde parameters**: De structuur van het model wordt vastgelegd door de architectuur. In deze structuur kunnen we waarden invullen. Meestal zijn dit gewoon getallen. Het trainingsalgoritme zal ervoor zorgen dat de waarden zodanig ingevuld worden dat je het model kan gebruiken om voorspellingen mee te doen.

![Voorbeeldarchtectuur van een neuraal netwerk.](images/nn_architecture_simple.png)

![Voorbeeld van de gewichten in een neuraal netwerk](images/nn_architecture_weights.png)

![Voorbeeld van agoritme van een neuraal netwerk](images/nn_architecture_algo_1.png)
![Voorbeeld van agoritme van een neuraal netwerk](images/nn_architecture_algo2.png)
![Voorbeeld van agoritme van een neuraal netwerk](images/nn_architecture_weights_algo3.png)