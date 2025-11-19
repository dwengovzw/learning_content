---
content_type: text/markdown
copyright: CC BY dwengo
description: Automatically colorize black-and-white Jommeke
estimated_time: 5
hruid: org-dwengo-jommeke-zelf-aan-de-slag
keywords:
- AI
- AI-systeem
- "artifici\xEBle intelligentie"
language: en
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-mediawijsheid
- http://ilearn.ilabt.imec.be/vocab/tref1/ict
- http://ilearn.ilabt.imec.be/vocab/curr1/c-digitale-competenties-en-mediawijsheid
- http://ilearn.ilabt.imec.be/vocab/onddoel/sec-gr1-astroom-digitale-competenties-en-mediawijsheid-4.5
target_ages:
- 12
- 13
- 14
- 15
- 16
title: Jommeke coloring
version: 1
---
# Try it yourself

![Jommeke banner](img/banner_jommeke_2.png)<br>
<sub>© Standaard Uitgeverij 2022</sub>

Jommeke is a Belgian comic series that was conceived and originally drawn by Jef Nys. Nowadays, we all know Jommeke as the boy with blond hair and a blue sweater, but did you know that the stories of Jommeke used to be drawn in black and white? Below you can see a number of examples of what the comic used to look like.<br>

![Old Jommeke image](img/jommeke_old/old0.png)
![Old Jommeke image](img/jommeke_old/old1.png)
![Old Jommeke image](img/jommeke_old/old2.png)
![Old Jommeke image](img/jommeke_old/old3.png)

<div class="alert alert-box alert-secondary">
At Ghent University, Simon Schellaert developed an AI system that makes it possible to colorize old Jommeke comics [1]. To teach the AI system how to colorize black-and-white images, you need a lot of example images for which you have both a black-and-white and a colored version. Because most Jommeke comics are in color, they must first be converted to black and white. Below you can see an example of an image that was converted to black and white.
</div>

![Jommeke monkeys original](img/jommeke_flow/origineel-apen-005.png "Original")
![Jommeke monkeys black and white](img/jommeke_flow/zwart-wit-apen-005.png "Converted to black and white by turning all colors white and retaining only black lines and areas.")
![Jommeke monkeys black and white](img/jommeke_flow/ingekleurd-apen-005.png "The version colorized by the AI system.")

In the example above, it is clear that the algorithm is able to colorize the black-and-white panel. But how good is the AI system? Is it as good as a human who creates the color illustrations? Does the system exhibit human intelligence and, if so, how intelligent is it?