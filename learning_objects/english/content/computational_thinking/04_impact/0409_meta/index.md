---

hruid: m_ct04_09
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
Keeping a bicycle path constantly well lit costs a lot of energy. By using smart lighting, it is possible to only use bright light when someone is near the street lighting.   
</div>
</context>
<decomposition>
**Decomposition**<br>
Regulating bicycle path lighting can be broken down into different components, such as detecting movement, adjusting the brightness of the lighting, and managing energy consumption. For this, components such as a street lamp and a motion sensor will be needed.
</decomposition>
<patternRecognition>
**Pattern recognition**<br>
Detecting movement is an important part of smart bicycle path lighting, but this detection can also be used in other contexts. Think of traffic detection to identify peak hours, or a security alarm that turns on a light when movement is detected at a suspicious time. 
</patternRecognition>
<abstraction>
**Abstraction**<br>
We want the street lamps to light up as soon as someone actually needs them. Whether the user is on a bicycle, scooter, or motorcycle is of little importance in principle. Therefore, it is only necessary to retain the essential information about motion detection. As soon as the motion sensor detects something, we can provide extra light, without taking irrelevant details about, for example, specific individuals into account.<br>
</abstraction>
<algorithms>
**Algorithmic thinking**<br>
For this example, an algorithm can be used to determine when the lighting should become brighter based on detected movement. This could, for example, be an algorithm that increases brightness when movement is detected and lowers it again after a certain time if no new movement is detected.
</algorithms>
<implementation>
... 
</implementation>
