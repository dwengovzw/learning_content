---

hruid: m_ct03_30
version: 3
language: en
title: "Clothes Hanger"
description: "Clothes Hanger"
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
Make three clothes hangers for adults, two for children, and four for babies.
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>Which materials?</li>
    <li>Which software? <span style="color: yellowgreen">→ parameterized CAD design</span></li>
    <li>Which parameters are needed?</li>
    <li>Which machine will be used? <span style="color: yellowgreen">→ CNC machine</span></li>
    <li>Which dimensions are suitable?</li>
    <li>Which curvature is suitable?</li>
    <li>...</li>
</ul>
</decomposition>
<patternRecognition>
 **Pattern Recognition**<br>
The shape of a clothes hanger is independent of the size.
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>The parameterized CAD drawing is an abstraction of the three sizes of clothes hangers.</li>
    <li>Essentially, a clothes hanger is represented by the values of the chosen parameters.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
To change from one size to another, certain parameters in the software must be adjusted. The computer performs the necessary calculations and automatically adapts the design.
</algorithms>
<implementation>
**Program**<br>
No implementation. This is (for now) an unplugged example.
</implementation>
