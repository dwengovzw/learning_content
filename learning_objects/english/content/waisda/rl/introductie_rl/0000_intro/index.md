---
content_type: text/markdown
copyright: CC BY dwengo
description: Get acquainted with reinforcement learning.
estimated_time: 5
hruid: org-dwengo-waisda-rl-introductie-rl-intro
keywords:
- AI
- "re\xEFnforcement learning"
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
title: Introduction
version: 1
---
# Learning from data

AI systems usually learn by searching for rules and patterns in data. In the [learning path on recognizing emotions](https://dwengo.org/learning-path.html?hruid=org-dwengo-waisda-beelden-emoties-herkennen&language=nl&te=true&source_page=%2Fwaisda%2F&source_title=%20wAIsda?#org-dwengo-waisda-beelden-emoties-herkennen-intro;nl;1) the computer, for example, learns rules to distinguish smiling and surprised smileys from one another. In the [learning path in which you solve the murder mystery](https://dwengo.org/learning-path.html?hruid=org-dwengo-waisda-taal-murder-mistery&language=nl&te=true&source_page=%2Fwaisda%2F&source_title=%20wAIsda?#org-dwengo-waisda-taal-murder-mystery-intro;nl;1), the computer looks for patterns in the characters’ writing style. In both learning paths the algorithm uses a dataset; for recognizing emotions these were images, for detecting writing styles these were different texts. Many of the AI systems we use today work because they have learned from large amounts of data. But how much data is that? Below you can see the size of the datasets that were needed to train certain AI systems.

- The ImageNet model behind Google’s Teachable Machine was trained with 1,281,167 training images, 50,000 validation images, and 100,000 test images. ([https://www.image-net.org/download.php](https://www.image-net.org/download.php))
- GPT-3, the predecessor of ChatGPT, was trained among other things using the CommonCrawl dataset. This is an open-source dataset that contains the text of more than 2.7 billion websites ([https://commoncrawl.org/overview](https://commoncrawl.org/overview)). 
- Dall-e, the OpenAI model that can generate images, was trained with a dataset containing approximately 650 million images ([see OpenAI paper](https://arxiv.org/pdf/2204.06125)).

You can see that AI systems need enormous amounts of data to learn a task. That stands in stark contrast to how we as humans learn. People manage to learn without having to see millions to billions of examples. Think, for example, of a baby learning to crawl. The baby is able to learn to crawl even without ever having seen examples<sup>(1)</sup>. As humans we therefore use different techniques to learn than the techniques most AI systems use. 

The way people learn has inspired computer scientists to develop AI systems that do not learn based on large amounts of data, but rather on interaction with their environment. These systems make use of **reinforcement learning**. In this learning path you will get acquainted with the basic principles of **reinforcement learning**.




(1) Adolph, Karen E., and John M. Franchak. "The development of motor behavior." Wiley Interdisciplinary Reviews: Cognitive Science 8.1-2 (2017): e1430.