---

hruid: m_ct03_70
version: 3
language: en
title: "Bus and Train"
description: "Bus and Train"
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
---

<context>
Next week there is a trip to Brussels planned by train.<br>
Find out where and when you need to depart to arrive on time in Brussels.
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>What is the nearest station?
        <ul>
            <li>Are there direct trains to Brussels or will we need to transfer?</li>
            <li>How do we get to the station? On foot, by bike, by bus?</li>
        </ul>
    </li>
    <li>Where in Brussels do we need to go? Which station should we get off at?</li>
    <li>At what times do trains depart for Brussels? 
        <ul>
            <li>Where can we find the train schedules?</li>
            <li>At what time should we then leave for the station?</li>
        </ul>
    </li>
    <li>Which platform should we board from?</li>
    <li>Are there delays or announced strikes?</li>
    <li>...</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>Planning a trip by bus or train is done in a similar way. An app can be used for either. Platforms and bus stops are represented abstractly, by a name or number.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>The platform is abstracted to a number, the platform number.</li>
    <li>The journey is abstracted to the route to follow: a sequence of locations (home, school, stations …).</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
<ul>
    <li>The route to follow: a list of consecutive times and corresponding locations.</li>
</ul>
</algorithms>
<implementation>
**Program**<br>
In this example, no programming is required. 
</implementation>
