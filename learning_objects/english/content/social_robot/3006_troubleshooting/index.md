---
hruid: sr3_troubleshooting
version: 3
language: en
title: "Testing and debugging"
description: "Testing and debugging"
keywords: ["Sociale Robot"]
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek'
]
teacher_exclusive: false
---
# Programming the physical robot
## Testing and debugging

When you are testing and debugging, it may be necessary to try different things before achieving the desired result. However, this requires a thoughtful approach. First, try to identify exactly what is going wrong and then come up with a solution. Test this solution and repeat the process if necessary.

**Example 1**  
Suppose you have used 2 LED matrices as eyes for the robot, but they have accidentally been swapped.

*Option 1*  
You switch the LED matrices in the physical robot to match the program.

*Option 2*  
You reprogram the eyes, but this time for the correct position.

**Example 2**  
The arms of the physical robot are not moving, while they functioned correctly in the simulator.

*Option 1*  
Check the wiring to see if wires have been swapped or disconnected.

*Option 2*  
Check if there are no parts of the robot blocking the arms from moving.

*Option 3*  
Detach the arms and check if the servo motors are working. Perhaps the arms are too heavy to move?

<div class="alert alert-box alert-success">
When testing and debugging, it is important to identify the cause of the error before coming up with a solution. This way you can search for a solution in a targeted way and make the process more efficient.
</div>

If you have time left, you can let your robot do additional things. Did you have anything in mind during the brainstorm?