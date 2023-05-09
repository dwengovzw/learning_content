---
hruid: sr2_programma
version: 3
language: en
title: "Program your robot"
description: "Program your robot"
keywords: ["Sociale Robot", "AI Op School", "STEM", "Computationeel denken", "Grafisch programmeren"]
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
estimated_time: 30
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-technologie-en-technieken'
]
teacher_exclusive: false
---
# Program your own robot

Congratulations! Now that you have some programming skills, you can start programming your own robot.

Review again what your robot needs to do and write it down in pseudocode.

**Example**  
*What it needs to do*  
If the robot doesn't see anything, it keeps its arms up and blinks its eyes. 
If someone approaches closer than 20 cm, the robot starts waving.

*pseudocode*  
**IF** someone is at 20 cm **THEN** wave and blink eyes  
**ELSE** arms up and eyes normal  

Once you have the pseudocode, write and test the different subprograms you need to achieve this. These subprograms should:

- keep the arms still
- display the eyes
- wave the arms
- blink the eyes
- read the sonar sensor, with an "*If - Then - Else*" block to attach conditions

When you then put all the subprograms together, you have the full program for the robot!