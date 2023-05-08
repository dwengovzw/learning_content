---
hruid: g_wacht_oef1
version: 3
language: en
title: "Exercise Delay 1"
description: "Exercise Delay 1"
keywords: ["oefeningen", "wacht"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [10, 11, 12]
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
teacher_exclusive: false
---
## Delay

EXERCISE 1.1

Write a program that does the following:

* Displays "Hello people" on the LCD screen for 1 second (1000 ms).
* Displays "I am dwenguino" on the LCD screen for 2 seconds (2000 ms).
* Repeat.

<div class="alert alert-box alert-danger">
Note that you need to place the code in the <em>'loop'-part</em> of the <em>'setup/loop'-block</em> for this!<br>
The program only loops code that is inside the <em>'loop'-part</em>.
</div>

***

EXERCISE 1.2

If you have programmed the LCD screen correctly, you should experience the following problem:

> <span style="color:green">H&nbsp;e&nbsp;l&nbsp;&nbsp;l&nbsp;o&nbsp;&nbsp;&nbsp;&nbsp;p&nbsp;e&nbsp;&nbsp;o&nbsp;p&nbsp;l&nbsp;e</span><br>
<span style="color:red">&nbsp;I&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;a&nbsp;m&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;D&nbsp;w&nbsp;e&nbsp;n&nbsp;g&nbsp;u&nbsp;i&nbsp;n&nbsp;o</span><br>
<span style="color:green">H&nbsp;e&nbsp;l&nbsp;&nbsp;l&nbsp;o&nbsp;&nbsp;&nbsp;&nbsp;p&nbsp;e&nbsp;&nbsp;o&nbsp;p&nbsp;l&nbsp;e</span><span style="color:red">&nbsp;n&nbsp;o&nbsp;</span><br>
<span style="color:red">&nbsp;I&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;a&nbsp;m&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;D&nbsp;w&nbsp;e&nbsp;n&nbsp;g&nbsp;u&nbsp;i&nbsp;n&nbsp;o</span><br>
<span style="color:green">H&nbsp;e&nbsp;l&nbsp;&nbsp;l&nbsp;o&nbsp;&nbsp;&nbsp;&nbsp;p&nbsp;e&nbsp;&nbsp;o&nbsp;p&nbsp;l&nbsp;e</span><span style="color:red">&nbsp;n&nbsp;o&nbsp;</span><br>
...

Solve the problem using the <em>'clear lcd screen'-block</em>: 

![alt](embed/maaklcdleeg.png "clear lcd screen")