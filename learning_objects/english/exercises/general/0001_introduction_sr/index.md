---
hruid: g_startpagina_sr
version: 3
language: en
title: "Introductie"
description: "Introductie"
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
## A programming environment

The programming environment with simulator is available online at [https://blockly.dwengo.org](https://blockly.dwengo.org "simulator link").

Below you will see a screenshot of the environment with a description of the different components.

![](embed/en_simulator_sr.png "Simulator Components")

1. **Toolbox**<br> In this menu you can find the different code blocks. The menu is divided into categories, each containing a specific type of blocks. In ![alt](embed/cat_input.png "input category"), for example, you can find all the blocks related to input.

2. **Code area**<br> This is where your program is located. The *'setup/loop' block* is already in place. <br><br>![alt](embed/en_setuploop.png "Setup/loop block")

> Only code placed in the 'setup/loop' part of this block will be executed. Code placed elsewhere will not be executed. To program, simply drag and drop blocks from the *toolbox* to the *code area* and snap them into place in the *'setup/loop'* block.

3. **Main menu**<br> With this menu you can perform actions such as saving your code (with ![alt](embed/menu_download.png "download menu")), loading code (with ![alt](embed/menu_upload.png "upload menu")), or opening and closing the simulation environment (with ![alt](embed/menu_hide.png "hide menu")).

4. **Simulation menu**<br> Here you can find the buttons to start and stop the simulation with the buttons ![alt](embed/simmenu_play.png "play simulator") and ![alt](embed/simmenu_stop.png "stop simulator"). <br><br> It also allows you to choose a specific scenario within which to run the code. In the example, the scenario of the social robot is selected. You can recognize this by the icon of the social robot ![alt](embed/scenario_socialerobot.png "social robot scenario").

5. **Simulation window**<br> In this window you will see a virtual robot and often a virtual microcontroller board, the Dwenguino, or components with which you can test the code. Because the scenario of the social robot is selected in the image, you can see various components at the top and a virtual social robot that you can program at the bottom. Please note that in order to simulate a program, you must first add the necessary components.

<div class="alert alert-box alert-success">
In the <em>toolbox</em>, you can find the blocks you need to create programs. You should drag these blocks out of the toolbox and then snap them into place in the desired order in the <em>code area</em>.
</div>