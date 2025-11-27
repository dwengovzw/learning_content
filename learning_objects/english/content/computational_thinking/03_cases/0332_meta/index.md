---

hruid: m_ct03_32
version: 3
language: en
title: "Sentiment Analysis"
description: "Sentiment Analysis"
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
**Problem Statement**<br>
Design and build a closed lantern. You must use wood and plexiglass.  <br>
![Lantern](lantaarn.jpg) <br>
    Gnangarra. <em>Tranby House kerosene lamp</em> [Image]. CC BY 2.5 AU, via Wikimedia Commons.
</div>
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>Which type of wood is suitable?</li>
    <li>What dimensions will the lantern have?</li>
    <li>How can I make it possible to place a candle inside? (door, hinges)</li>
    <li>How will I decorate the glass?</li>
    <li>Which edge profiling will I use?</li>
    <li>What finish will I use? (paint? varnish? ...)</li>
    <li>How can I hang the lantern? What material is needed? How will I attach it?</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
The shape of the lantern is independent of the size. By adjusting one dimension in the CAD program, the other dimensions are automatically scaled proportionally.
</patternRecognition>
<abstraction>
**Abstraction**<br>
The parameterized CAD drawing is an abstraction of the real lantern. The lantern is reduced to its dimensions.
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
The decomposition, i.e., the choices that students make, leads to a step-by-step plan that they must follow to build the lantern. Each step involves choices of materials, tools, and techniques.
</algorithms>
<implementation>
**Program**<br>
This activity is done using the computer. CAD software is used.
</implementation>
