---
hruid: g_voorwaardelijkeherhaling
version: 4
language: en
title: "Conditional Loop"
description: "Conditional Loop"
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: False
---
# dwenguinoBlockly
## While loops

To perform a while loop, you use the following block:

![](embed/vh.png "while loop")  

In contrast to the for loop, here we set a start condition instead of a start and stop value. If the start condition is met, the loop will start. Once started, the contents of the loop will be repeated until the start condition is no longer met.

For exercise 4 of the buzzer, we will set the start condition to be that a button must be pressed. As long as this is the case, the buzzer will produce the desired tone. As soon as you release the button, this tone should stop.

Solution:

![blockly](@learning-object/zoemer_m4/en/3) 

*Also test this on a real dwenguino if it works in the simulator.*