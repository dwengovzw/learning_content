---
hruid: g_startpagina
version: 3
language: en
title: "Introduction"
description: "Introduction"
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
## A programming environment

The programming environment with a simulator is available online at [https://blockly.dwengo.org](https://blockly.dwengo.org/?lang=en "link simulator").

Below you can see a screenshot of the environment with a description of the different parts.

![](embed/en_simulator_sr.png "Simulator components")

1. **Toolbox**<br>In this menu you can find the different code blocks. The menu is divided into categories, each containing a specific type of blocks. In ![alt](embed/cat_dwenguino.png "category Dwenguino"), for example, you can find all the blocks that are specific to the dwenguino.

2. **Code field**<br>This is where your program is displayed. The *'setup/loop'* block is already present. <br><br>![alt](embed/en_setuploop.png "Image of the setup/loop block")

> Only code placed in the ‘setup’ and 'loop' parts of this block will be executed. Code placed elsewhere will not be executed. To program, drag blocks from the *toolbox* to the *code field* and click them into the *'setup/loop'* block.

3. **Main menu**<br>With this menu you can perform actions such as saving your code (with ![alt](embed/menu_download.png "download menu")), loading code (with ![alt](embed/menu_upload.png "upload menu")), or opening and closing the simulation environment (with ![alt](embed/menu_hide.png "hide menu")).

4. **Simulation menu**<br>Here you can find the buttons to start and stop the simulation with the buttons ![alt](embed/simmenu_play.png "simulator play") and ![alt](embed/simmenu_stop.png "simulator stop"). <br><br>It also allows you to choose a specific scenario within which to run the code. In the example, the scenario of the drawing robot (spirograph) is selected. You can recognize this by the icon ![alt](embed/scenario_tekenrobot.png "drawing robot scenario").

5. **Simulation window**<br>In this window you can see a virtual robot and often also a virtual microcontroller board, the dwenguino, or components with which you can test your code. Because the drawing robot scenario is selected in the image, you can see a drawing robot with a dwenguino in the top right corner. 

<div class="alert alert-box alert-success">
So, in the <em>toolbox</em> you can find the blocks you need to create programs. You need to drag these blocks from the toolbox and then click them into the desired order in the <em>code field</em>.
</div>