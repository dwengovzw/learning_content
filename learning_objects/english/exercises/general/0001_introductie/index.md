---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Introduction
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 5
hruid: g_startpagina
keywords:
- oefeningen
language: en
licence: dwengo
return_value:
  callback_schema:
    att: test
    att2: test2
  callback_url: callback-url-example
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-vaktaal
target_ages:
- 10
- 11
- 12
teacher_exclusive: false
title: Introduction
version: 3
---
# dwenguinoBlockly  
## A programming environment

The programming environment with simulator is available online at [https://blockly.dwengo.org](https://blockly.dwengo.org "simulator link").

Below you see a screenshot of the environment with a description of the different parts.

![](embed/simulator.png "Simulator components")

1. **Toolbox**<br>In this menu you can find the different code blocks. The menu is divided into categories, each containing a specific type of blocks. In ![alt](embed/cat_dwenguino.png "dwenguino category") you can, for example, find all blocks that are specific to the dwenguino.

2. **Code area**<br>This is where the program you create resides. The *'set up/repeat' block* is already there. <br><br>![alt](embed/b_zetklaarherhaal.png "Fig. set up/repeat")

> Only code placed in the ‘set up’ and 'repeat' sections of this block is executed. Code elsewhere is not executed. To program, drag blocks from the *toolbox* to the *code area* and snap them into the *‘set up/repeat’ block*. 

3. **Main menu**<br>This menu lets you perform actions such as saving your code (with ![alt](embed/menu_download.png "menu download")), loading it again (with ![alt](embed/menu_upload.png "menu upload")), or opening and closing the simulation environment (with ![alt](embed/menu_hide.png "hide menu")).

4. **Simulator menu**<br>Here you’ll find the buttons to start and stop the simulation with the buttons ![alt](embed/simmenu_play.png "simulator play") and ![alt](embed/simmenu_stop.png "simulator stop"). <br><br>It also allows you to choose a specific scenario within which you want to run the code. In the example, the drawing robot (spirograph) scenario is selected. You can recognize this by the icon ![alt](embed/scenario_tekenrobot.png "drawing robot scenario").

5. **Simulator window**<br>In this window you see a virtual robot and often also a virtual microcontroller board, the dwenguino, or components with which you can test the code. Because the drawing robot scenario is selected in the image, you see a drawing robot with a dwenguino at the top right.

<div class="alert alert-box alert-success">
In the <em>toolbox</em> you can find the blocks you need to create programs. You must drag these blocks out of it and then snap them together in the desired order in the <em>code area</em>.
</div>