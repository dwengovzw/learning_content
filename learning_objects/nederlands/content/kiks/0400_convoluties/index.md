---
hruid: kiks_convoluties
version: 3
language: nl
title: "Convoluties en andere technieken"
description: "Convoluties en andere technieken"
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

# Convoluties en andere technieken
Met convoluties kan je op zoek gaan naar verschillende kenmerken in een afbeelding. Je kan er bv. randen mee detecteren, ruis in een beeld mee verminderen of het contrast in een beeld verzachten. Convoluties worden toegepast in de zogenaamde convolutionele netwerken. <br>
De eerste notebook gaat hier dieper op in.

Behalve convoluties worden er ook nog andere technieken gebruikt, zoals ReLU en max pooling. <br>Daar gaat de tweede notebook over. 

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=1712 "Convoluties")

---
> De convolutie is een wiskundige bewerking die enkel gebruikmaakt van optellen en vermenigvuldigen. Het komt erop neer dat men aan een pixel een bepaald gewicht geeft en men daaraan gewogen waarden van de omliggende pixels toevoegt.

Met convoluties kan men op zoek gaan naar verschillende kenmerken in een afbeelding. Men kan er bv. verticale en horizontale lijnen mee detecteren, ruis in een beeld mee verminderen of het contrast in een beeld verzachten. In elke laag van het convolutionele neurale netwerk wordt de representatie van de gegevens door de convoluties getransformeerd in een nieuwe representatie van de gegevens.

![Doel convoluties](embed/convolutiedoel.png "Doel convoluties")
