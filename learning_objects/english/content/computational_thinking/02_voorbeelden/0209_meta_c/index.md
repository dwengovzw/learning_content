---
hruid: m_ct02_09c
version: 3
language: en
title: "Soortgelijk schema uit de literatuur"
description: "Soortgelijk schema uit de literatuur"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/ct-schema
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

<context>
**Problem Statement**<br>
Students take a test in teams using a Snap! program. Each question corresponds to a certain distance. For a correct answer, the team moves forward that distance; for an incorrect answer, the team is penalized.
</context>
<decomposition>
**Decomposition**<br>
Certain subtasks in the test have been extracted to be defined using user-defined functions in the program.
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
While playing, students must notice the repeating patterns in the game and become familiar with the game mechanics, e.g., what happens with a correct answer.
</patternRecognition>
<abstraction>
**Abstraction**<br>
Teachers show a block that corresponds to a user-defined function and explain how encapsulating an algorithm in this way is considered an abstraction.
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
Students use algorithms during the course of the game.  
</algorithms>
<implementation>
Students do not need to program themselves. The teachers wrote the Snap! program.
</implementation>
