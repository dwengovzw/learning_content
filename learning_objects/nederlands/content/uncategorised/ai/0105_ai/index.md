---
hruid: un_ai5
version: 3
language: nl
title: "Soorten training"
description: "ML en DL"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [12, 13, 14, 15, 16, 17, 18]
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

# Soorten training

## Supervised, unsupervised en reinforcement learning

Binnen ML onderscheidt men verschillende types van leren: supervised, unsupervised en reinforcement learning.<br>
- Bij supervised en unsupervised learning vertrekt men van een set voorbeelden.<br>
![voorbeeldenappelpeer](https://user-images.githubusercontent.com/48352335/222242428-3021670a-b3e7-403b-8752-e1bef9f83668.png)

- Bij **supervised learning** zijn de data gelabeld. Het systeem leert dus uit een dataset waarbij elk gegeven bestaat uit twee componenten: een input gekoppeld aan een *label* (de verwachte output) (zie Figuur). Het labelen van de voorbeelden gebeurt vaak manueel door mensen, men noemt dat *annoteren*. Het systeem voert een algoritme uit dat er geleidelijk aan voor zorgt dat het systeem focust op relevante patronen in de data. <br>
![soortenmlsupervised](https://user-images.githubusercontent.com/48352335/222239255-ee4fa9d7-f181-445a-af3b-d87c529fb530.png)<br>
![ailerendappelsperen](https://user-images.githubusercontent.com/48352335/222241196-beaa3f95-d30e-4315-a17b-171cad288b95.png)

- Bij **unsupervised learning** bevat de dataset *geen labels*. Het AI-systeem moet op zoek naar kenmerken bij de verschillende voorbeelden en moet ze zo, door het ontdekken van patronen, verdelen in klassen. Men kan het systeem bv. ongelabelde foto’s aanbieden van appels en peren. Het systeem gaat op zoek naar patronen om zo het 
![kenmerken](https://user-images.githubusercontent.com/48352335/222240504-2357f827-ec15-42e4-a209-94fcbd142ccf.png)<br>
![soortenmlunsupervised](https://user-images.githubusercontent.com/48352335/222239480-09ab805d-da4f-4cd2-acf0-23241c2b4c3d.png)

- Bij **reinforcement learning** streeft het AI-systeem naar een *beloning*. Om bv. goed te worden in een bepaalde videogame, gaat het AI-systeem het spel heel veel spelen en daaruit leren welke acties het beter vermijdt en welke het best onderneemt om te kunnen winnen. Zo werd Google DeepMind’s AlphaGo Zero in 2017 via reinforcement learning een topspeler in Go, nog beter dan AlphaGo die de beste menselijke speler eerder al versloeg.
