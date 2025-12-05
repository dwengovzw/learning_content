---
available: true
content_type: text/markdown
copyright: dwengo
description: Distance
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: cb5_unplugged3
keywords:
- voorbeeld
- voorbeeld2
language: en
licence: dwengo
return_value:
  callback_schema:
    att: test
    att2: test2
  callback_url: callback-url-example
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-digitale-media-en-toepassingen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-stem-onderzoek
- http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek
target_ages:
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: true
title: Distance
version: 3
---
# Distance

![](@youtube/https://www.youtube.com/embed/JKGJ1u4Fk78)

*The rule-based chatbot looks up every 'question' in its 'dictionary'. 
Sometimes, however, a question is not in the rule-based chatbot's 'dictionary' and it doesn't know what to answer.
To prevent the chatbot from giving no answer, we will ensure that the chatbot looks for a question that resembles it. How do you approach that? Tip:'Robots love numbers.' If you can represent the similarity between two questions with a number, then you can have the chatbot, based on that number, calculate which of the possible questions most 'resembles' the asked question. The chatbot will then give the answer that belongs to the similar question. In practice, however, similar questions will not always have a similar meaning.*

To see how well certain words resemble each other, the chatbot will compute a **number**:<br>
the number of letters that must be changed to make the words identical, divided by the number of letters in the longest word.<br>
That number is called **distance**. 

*Students try this themselves on simple examples. You can easily come up with extra exercises here.*

These exercises align with **minimum objectives** for the **labor market finality**. 

<span style="color: yellowgreen">(06.01 Labor market finality) Students perform, through functional use of ICT, simple calculations with integers, decimal numbers, fractions, percentages and ratios in meaningful contexts.</span>

<span style="color: yellowgreen">(06.06 Labor market finality) Students solve problems from meaningful contexts by applying mathematical concepts and skills.</span>

# Exercises on distance

To see how well certain words resemble each other, the chatbot will compute a **number**:<br>
the number of letters that must be changed to make the words identical, divided by the number of letters in the longest word.<br>
That number is called **distance**. 

**Example**<br>
koken and haken -> two letters must be changed: a 'k' and the 'h'. Both words have 5 letters, so the longest word has 5 letters.<br>
The distance = 2/5 = 0.4.<br>
<br>
koken and koren -> 1 letter must be changed: a 'k'. Both words have 5 letters, so the longest word has 5 letters.<br>
The distance = 1/5 = 0.2.<br>  
<br>
This means that 'koken' is more similar to 'koren' than to 'haken'.
<br>
koken and kokers -> one letter must be changed and one letter must be added. The longest word has 6 letters.<br>
The distance = 2/6 = 0.33333...<br>
<br>
This means that 'koken' is more similar to 'kokers' than to 'haken', but less similar than to 'koren'.

<br>
<br>

*Have the students try this out on other words.*