---

hruid: m_ct03_10
version: 3
language: en
title: "Meta"
description: "Meta"
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
Visualize and interpret the conversations in Harry Potter and the Philosopher's Stone.
</div>
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>Which conversations do you record and which do you ignore?
    <li>Choose which factors you take into account: number of conversations, length of a conversation...
    <li>How do you represent the characters?
    <li>How do you represent the conversations?</li>
</ul> 
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>Such relationships are often represented by a graph.
    <li>You can see from the thickness of the edges which characters converse most often.
    <li>The main characters stand out both in the graph of chapter 11 and in the graph of the entire book.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>You focus on the conversations. You ignore the rest of the text.
    <li>You limit yourself to conversations that clearly take place between two or more characters. Mumbling, whispering, shouting... are ignored.
    <li>You do not take into account the length of a conversation.
    <li>Characters are represented by a node, conversations by an edge, and the number of conversations is represented by the thickness of the edge.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
<ul>
    <li>Record all characters and all conversations between two or more characters.
    <li>Represent the characters with a node.
    <li>Represent the conversations with an edge.
    <li>For each additional conversation between the same characters, make the edge thicker.</li>
</ul>
</algorithms>
<implementation>
**Program**<br>
No programming is done in this assignment.
</implementation>
