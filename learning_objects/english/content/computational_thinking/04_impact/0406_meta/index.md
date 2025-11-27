---

hruid: m_ct04_06
version: 3
language: en
title: "Sentiment analysis"
description: "Sentiment analysis"
keywords: [""]
educational_goals: [
    {source: Source, id: id},
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/ct-schema
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
    '[http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen](http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen)'
]
teacher_exclusive: true
-----------------------

<context>
**Problem statement**<br>
We attach great importance to optimising agriculture, but how do we do this?
</div>
</context>
<decomposition>
**Decomposition**<br>
In precision agriculture, farming practices can be optimised using advanced technologies to increase efficiency and reduce environmental impact.
These agricultural practices can be divided into different components, such as sowing, fertilising, irrigating, crop protection, and harvesting. Each of these components can be further broken down into specific tasks and processes. For this purpose, advanced technologies such as GPS, sensors, drones, artificial intelligence, machine learning, and so on are used.
</decomposition>
<patternRecognition>
**Pattern recognition**<br>
An example of precision agriculture is the use of cameras to map the condition of plants and to check whether specific treatments are needed. Just as the condition of plants can be examined, it is possible to apply a similar approach to machine parts to check whether they are of good quality or require repairs.
</patternRecognition>
<abstraction>
**Abstraction**<br>
If we want to examine the condition of plants, we use photos to check them. You probably have a clear idea of what a photo is like, but a computer will not see a photo the way we do. A photo consists of pixels, and each pixel has a specific colour; that colour can be represented by a number. The computer therefore only sees numbers and thus makes an abstraction of the photos needed during an optimisation process.
</abstraction>
<algorithms>
**Algorithmic thinking**<br>
Algorithms are used to analyse the collected data and make decisions about optimising agricultural practices. This includes the use of machine learning and AI algorithms to identify patterns, make predictions, and provide recommendations for, for example, optimal sowing times, irrigation levels, fertilisation amounts, and treatments against pests and diseases.
</algorithms>
<implementation>
**Program**<br>
An implementation to recognise tomatoes using computer vision can be found in the <a href="/learning-path.html?hruid=agri_landbouw&language=nl&te=true&source_page=%2Fagriculture%2F&source_title=%20AI%20in%20de%20Landbouw#agri_tomaten;nl;3"><strong> learning path AI in agriculture – Deep learning</strong></a>.
</implementation>
