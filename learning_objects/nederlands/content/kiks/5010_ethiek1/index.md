---
hruid: kiks_ethiek1
version: 3
language: nl
title: "Bias"
description: "Bias"
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
teacher_exclusive: true
---

# Bias

Bias komt voor als de data niet representatief zijn. Als men bv. enkel groene appels als voorbeelden geeft aan een deep learning-systeem, dan zal het model geen rode
appels herkennen. Of als men bij de training enkel foto’s van honden onder een stralend blauwe hemel aanbiedt, dan zal het deep learning-model een hond in de regen
niet bij de klasse ’hond’ indelen.

Als de gebruikte data gekleurd zijn door een aanwezige bias in de maatschappij, zoals stereotypen, dan zal dit ook doorgegeven worden aan het ML-systeem.
Men moet er dus over waken dat het model daardoor niet discriminerend wordt voor bepaalde bevolkingsgroepen. Als men bv. enkel vrouwelijke verplegers in
de dataset stopt, dan zullen mannen niet als verpleger worden geclassificeerd.

Een model wordt nochtans getest voor het in gebruik genomen wordt. De testdata kunnen echter dezelfde bias bevatten als de trainingdata.
