---
content_type: text/markdown
copyright: CC BY dwengo
description: Which goal are we working towards?
estimated_time: 2
hruid: org-dwengo-waisda-rl-crawling-robot-de-robot
keywords:
- AI
- "re\xEFnforcement learning"
- versterkend leren
- kruipende robot
language: en
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
- http://ilearn.ilabt.imec.be/vocab/tref1/ict
target_ages:
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: false
title: The robot
version: 1
---
# The crawling robot

To give you an idea of the system we are going to build, you can watch a video of the crawling robot below.

<div class="iframe-container iframe-16-9">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/yq_cfXt0xLY?si=lvgGMjV2DX8aRpMC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>


In the video you can see that the robot moves by pulling itself forward with an arm. The arm consists of two joints; each joint has a motor that can move the arm. By moving the motors in the right way, the robot can crawl forward. The robot in the video already does a good job of crawling forward. The system learned this behavior by itself using Q-learning.