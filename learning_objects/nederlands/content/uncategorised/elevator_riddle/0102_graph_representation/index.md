---
hruid: org-dwengo-elevator-riddle-analyzing-2
version: 1
language: nl
title: "Kiezen van een datastructuur"
description: "Wanneer we gegevens willen verwerken met de computer moeten we die voorstellen in een datastructuur."
keywords: ["grafen", "algoritme", "computationeel denken", "clustering", "datastructuur"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
difficulty: 5
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 3
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
]
teacher_exclusive: false
---

# Kiezen van een datastructuur

Het probleem voorstellen met een gekende datastructuur geeft ons de mogelijkheid om alle algoritmische technieken die bestaan op die datastructuur te gebruiken. Het kiezen van een gepaste datastructuur kan het dus makkelijker maken om het probleem op te lossen.

|  | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** |
| ----------- | ----------- |----------- | ----------- |----------- | ----------- |----------- | ----------- |----------- |
| **4** | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| **5** | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 3 | 
| **6** | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 
| **7** | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 4 | 
| **8** | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 
| **9** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 
| **10** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **11** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |


Als je al een beetje kennis hebt van informaticawetenschappen, komt deze soort matrix je misschien bekend voor. Deze matrix heeft immers dezelfde structuur als de bogenmatrix of adjacentiematrix van een graaf (**patroonherkenning**). We kunnen deze matrix dus ook grafisch voorstellen als een graaf (Afbeelding 1). Een graaf is een verzameling van knopen (= de cirkels), deze worden verbonden  met bogen (= de lijnen tussen de cirkels). Een knoop stelt een verdieping voor. Een boog stelt het aantal verplaatsingen tussen de twee aangrenzende knopen/verdiepingen voor.

| ![Grafische weergave van de graaf met verplaatsingen tussen de verdiepingen.](embed/verplaatsingen_chaos_with_labels.png "Grafische weergave van graaf met verplaatsingen tussen de verdiepingen.") | 
| ---- |
| **Afbeelding 1**: Voorstelling verplaatsingen tussen verdiepingen als graaf. |

