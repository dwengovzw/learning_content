---
hruid: g_inleidendeoefening_sr
version: 3
language: en
title: "Your first program"
description: "Your first program"
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
# DwenguinoBlockly
## Your first program
Now that you know where everything is, you can start programming!

* In the *simulator menu*, select the scenario of the social robot ![alt](embed/scenario_socialerobot.png "social robot scenario").

* In the *toolbox*, go to the category ![alt](embed/cat_output.png "output category") and look for the *'LCD screen'-block*: <br><br>![alt](embed/firstprogram.png "LCD block")

* Drag this block to the *code field* and attach it to the ‘set up’ part of the *‘setup/loop’ block*: <br><br>![alt](embed/firstprogram2.png "click LCD")

* You just wrote your first program!

* Before you can test the program, you need to add the necessary components to the simulation window. To do this, in the simulation window, look for the icon below and click on the + button.<br><br>![](embed/lcdscreen.png "LCD screen")<br><br>Once the component appears, you can drag it to the desired location on the board.

* Run this program with the simulator by clicking on ![alt](embed/simmenu_play.png "simulator play") in the *simulator menu*.

* To stop the simulation, click in the *code field* or on ![alt](embed/simmenu_stop.png "simulator stop").

<div class="alert alert-box alert-success">
After this exercise, you have learned the basics of how the environment works. You can take blocks from the <em>toolbox</em> and add them to a program in the <em>code field</em>. You know how to execute that code in the simulator and you can switch between scenarios in that simulator.
</div>

<div class="alert alert-box alert-success">
Once a program works in the simulator, you can also try it out on a real dwenguino! Below is a detailed description of how to upload a program from the simulator to the dwenguino.
</div>