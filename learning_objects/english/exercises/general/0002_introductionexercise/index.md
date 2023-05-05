---
hruid: g_inleidendeoefening
version: 3
language: en
title: "Je eerste programma"
description: "Inleidende oefening"
keywords: ["oefeningen"]
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-vaktaal'
]
teacher_exclusive: false
---
# dwenguinoBlockly
## Your first program
Now that you know where everything is, you can start programming!

* In the *simulator menu*, select the scenario for the drawing robot ![alt](embed/scenario_tekenrobot.png "drawing robot scenario").

* In the *toolbox*, go to the category ![alt](embed/cat_dwenguino.png "dwenguino category") and look for the *'lcd screen' block*: <br><br>![alt](embed/inloef1.png "lcd block")

* Drag this block to the *code area* and snap it into the 'set up' section of the *'set up/repeat'* block: <br><br>![alt](embed/inloef2.png "click lcd")

* You just wrote your first program!

* Run this program with the simulator by clicking on ![alt](embed/simmenu_play.png "simulator play") in the *simulator menu*.

* To stop the simulation, click in the *code area* or on ![alt](embed/simmenu_stop.png "simulator stop").

<div class="alert alert-box alert-success">
After this exercise, you have the basics of how the environment works. You can take blocks from the <em>toolbox</em> and add them to a program in the <em>code area</em>. You know how to execute that code in the simulator and you can switch scenarios in that simulator.
</div>

<div class="alert alert-box alert-success">
Once a program works in the simulator, you can also try it out on a real dwenguino! The next section describes in detail how to upload a program from the simulator to the dwenguino.
</div>