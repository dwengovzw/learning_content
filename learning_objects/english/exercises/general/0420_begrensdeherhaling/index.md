---
hruid: g_begrensdeherhaling
version: 3
language: en
title: "Begrensde herhaling"
description: "Begrensde herhaling"
keywords: ["oefeningen", "lussen"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# dwenguinoBlockly
## Bounded repetition

To perform a bounded repetition, use the following block:

![](embed/begrensdeherhaling.png "Bounded repetition")

You set the number of repetitions using a *counter* that is given a starting and stopping value. This counter was named 'i' in the example, starts at 0, and 1 is added to it per repetition. The repetition stops when the stopping value is reached.

*What is the stopping value in the example? How many times is this loop repeated?*

For exercise 3 of the buzzer, you can shorten each part that needs to be repeated by using a bounded repetition. Because each part must be played twice (1 repetition), set the stopping value to 1.

Solution:

![blockly](@learning-object/begrensdeherhaling_m/nl/3)

*Also try this out on a real Dwenguino if it works in the simulator.*