---
hruid: g_sonar_vb1
version: 3
language: en
title: "Voorbeeld Sonar-sensor 1"
description: "Voorbeeld Sonar-sensor 1"
keywords: ["oefeningen", "sonar-sensor"]
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
teacher_exclusive: true
---
## Sonar sensor

EXERCISE 1

Before using the sonar sensor, you must first test it. Write a program to read the sonar sensor.

***

To read the sonar sensor (which measures distance), you use the LCD screen. The block of the sonar sensor simply represents a number that you can display on the screen.

To do this, you need the following blocks:

![](embed/block_sonar.png "sonar sensor block")
![](embed/block_text.png "text block")

When you combine these blocks, you get this:

![](embed/combo_text_sonar.png "text + sonar sensor")

The number from the sonar sensor is converted by the ![](embed/block_text.png "text block") to data that you can display on the LCD screen.

You can now replace the existing *'text'* block of the LCD screen with this new text block, resulting in the following program:

![blockly](@learning-object/sonar_m1a/nl/3)

***

However, in more complex programs, you will quickly notice that it is very crowded to use the *'sonar sensor'* block every time, as it is quite large. To remedy this and keep the program organized, you will use **variables**.

For this, you need the following blocks:

![](embed/block_variable.png "variable block")
![](embed/block_item.png "item block")

To improve the readability of your program, you should first rename the variable 'item' to something better. For example, since you are measuring distance here, you can use 'distance'. Use the help menu for this.

![](embed/rename_variable.png "rename variable")

Once you have done this, combine the *'sonar sensor'* block with ![](embed/block_variable.png):

![](embed/combo_variable_sonar.png "distance")

Once you have named a variable in a program, you can always call it using ![](embed/block_item.png "item block"). *Make sure you specify the correct variable!*

The end result for reading a sonar sensor looks like this:

![blockly](@learning-object/sonar_m1b/nl/3)

<div class="alert alert-box alert-success">
The values returned by the sonar sensor are now displayed on the LCD screen. If this doesn't work, troubleshoot to find the problem.
<ul>
<li>Is it the right program? (Check the code)</li>
<li>Is the sensor connected correctly? (Check the wiring)</li>
<li>Is the sensor working?</li>
</ul>
</div>