---
content_type: text/markdown
copyright: CC BY dwengo
description: Explanation of rule-based AI system and definition according to the EU
estimated_time: 2
hruid: org-dwengo-jommeke-definitie-ai-systeem-regels
keywords:
- AI
- Regelgebaseerd
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
title: Rule-based AI system
version: 1
---
A rule-based AI system?
===============

Rule-based AI systems operate, as the name suggests, on the basis of rules. These rules are **devised by experts** in a field and programmed on the computer by a programmer. An example of such a rule-based system is the application ["Do I need to see a doctor"](https://www.moetiknaardedokter.be/).

![Do I need to see a doctor?](img/moet_ik_naar_dokter.png "Do I need to see a doctor?")

This application asks a series of questions to the user and decides, based on the answers, what action should be taken. Should the person not see a doctor, should they see a doctor immediately, can they go to the doctor tomorrow, or must they go to the emergency department now.

Such a system works using a decision tree. Below you can see an example of such a tree. 

![Example decision tree](img/beslissingsboom.png "Example decision tree")

To make a decision, we traverse the tree from top to bottom. Each box contains a question. If the answer to that question is **yes**, then you follow the **left line** downward. If the answer to the question is **no**, you follow the **right line** downward. When you reach the very bottom of the tree, you will see which action the person must take.