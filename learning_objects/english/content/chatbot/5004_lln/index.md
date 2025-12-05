---
available: true
content_type: text/markdown
copyright: dwengo
description: exercise at a distance
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 5
hruid: cb5_unplugged4lln
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
teacher_exclusive: false
title: Exercise on distance
version: 3
---
# Distance

To see how similar certain words are to each other, the chatbot will calculate a **number**:<br>
the number of letters that must be changed to make the words the same, divided by the number of letters in the longest word.<br>
This number is called **distance**. 

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

**Exercise**<br>
Try this yourself on other words.