---
available: true
content_type: text/markdown
copyright: dwengo
description: How learning chatbots work
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 30
hruid: cb5_unplugged6
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
title: How learning chatbots work
version: 3
---
# How does a learning chatbot work?

How learning chatbots work is explained [here](https://dwengo.org/backend/api/learningObject/getWrapped?hruid=cb_chatbot3&version=3&language=nl). Via *embeddings*, text is converted into vectors. 

Remember: <br>
* Semantically related texts are placed close together in the vector space. For example, because the words ‘cat’ and ‘dog’ often appear together with the word ‘veterinarian’ in texts, you can find the corresponding three vectors close to each other in the vector space.
* Similar relationships between words can also often be found in the vector space. Comparable relationships between elements can be represented by the same relative position between the elements.

The learning chatbot will use words that lie close to each other to form sentences. 

*Before the students start the exercises, it's best to discuss this mechanism with them.* <br>
*After the exercises, you can revisit how it works. You can also mention a spell checker. If, for example, a word in Word is underlined with a red squiggly line, you can ask for suggestions to correct the word. Can students explain how the system might determine those suggestions?* 

### Assignment 1

*This assignment uses features of the comic 'Jommeke'.*<br>
*Your students might not know 'Jommeke'.* <br>
* *You can then, for example, read one or two pages from a Jommeke comic with the students to introduce them to the characters.*
* *Or you can ask which comics they do read and adapt the exercise to the features of another comic.* 

Look at the first diagram. Read the text that ChatGPT wrote that belongs with the first diagram.

![jommeke field](https://github.com/dwengovzw/learning_content/assets/48352335/8daa9a5d-3886-4799-813e-10a64213fa2c)

![jommeke](https://github.com/dwengovzw/learning_content/assets/48352335/9bc4010f-459d-4010-96cb-a1ade5050ca0)

### Assignment 2

Now look at the second diagram. What text could ChatGPT write for this diagram? 

![emilia field](https://github.com/dwengovzw/learning_content/assets/48352335/25fcec34-9d31-4fc3-92c3-2835edec7f36)

[worksheet](embed/werkbladwieisemilia.pdf)

*Possible answer:*<br>
*Emilia is a cartoon by artist Kobe Devries. She has a seal and her best friend is Arsène.* 


### Assignment 3

Read the words in the field.

Place the cards in the field. The more closely words belong together, the closer you place them to each other. There are multiple correct answers. Maybe you came up with a unique solution to this problem!

![field](https://github.com/dwengovzw/learning_content/assets/48352335/953abce7-119a-4ca2-a7d2-382caccac749)

*An example solution (there are multiple solutions):*<br>
![filled field](https://github.com/dwengovzw/learning_content/assets/48352335/dad2251d-ce91-4ea0-bad8-42f8e1bcd714)<br>


### Assignment 4

*This assignment is about the 'Suske en Wiske' comics.*<br> 
*Your students might not know 'Suske en Wiske'. Bring along a few 'Suske en Wiske' comics, and the students will quickly see what doesn't add up.*

Read the text about Suske and Wiske.

![vectors and suske and wiske](https://github.com/dwengovzw/learning_content/assets/48352335/5a054655-f848-490e-9b03-33bb2479562b)

Do you notice anything odd in this text?

*Wiske doesn't have a blue bow, but a red one. Does Lambik even have a mustache?*<br>
*Learning chatbots are therefore prone to making up quite a lot!*
*Rule-based chatbots do not do that.*