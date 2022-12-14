---
hruid: sr_Sonar
version: 3
language: nl
title: "Uitleg Sonar"
description: "Uitleg Sonar"
keywords: ["StartToDwenguino", "led"]
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

## Sonar-sensor
De sonar-sensor kan je gebruiken om de robot te laten 'zien'. Deze sensor meet de afstand tussen zichzelf en objecten. Als er iets op een bepaalde afstand van de robot gedetecteerd wordt, kan je hieraan bepaalde acties hangen. 

### In het echt

![](embed/sonar.png "Sonar-sensor")

### In de simulator

![](embed/Sonarsim.png "Sonar-sensor simulator")