---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: ML and DL
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: un_ai5
keywords:
- ''
language: en
licence: dwengo
return_value:
  callback_schema:
    att: test
    att2: test2
  callback_url: callback-url-example
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
target_ages:
- 12
- 13
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: true
title: Types of Training
version: 3
---
# Types of Training

## Supervised, Unsupervised and Reinforcement Learning

Within machine learning (ML), there are different types of learning: supervised, unsupervised, and reinforcement learning.<br>
- In both supervised and unsupervised learning, you start from a set of examples.<br>
![voorbeeldenappelpeer](https://user-images.githubusercontent.com/48352335/222242428-3021670a-b3e7-403b-8752-e1bef9f83668.png)

- In **supervised learning**, the data are labeled. The system learns from a dataset where each piece of data consists of two components: an *input* linked to a *label* (the expected output) (see Figure). Labeling the examples is often done manually by people, a process called *annotating*. The system executes an algorithm that gradually ensures that the system focuses on relevant patterns in the data. <br>
![soortenmlsupervised](https://user-images.githubusercontent.com/48352335/222239255-ee4fa9d7-f181-445a-af3b-d87c529fb530.png)<br>
![ailerendappelsperen](https://user-images.githubusercontent.com/48352335/222241196-beaa3f95-d30e-4315-a17b-171cad288b95.png)

- In **unsupervised learning**, the dataset contains *no labels*. The AI system must therefore search for features among the different examples and divide them into classes by discovering patterns. For example, you might give the system unlabeled photos of apples and pears. The system searches for patterns to enable it to work out which pictures are apples, and which are pears.  
![kenmerken](https://user-images.githubusercontent.com/48352335/222240504-2357f827-ec15-42e4-a209-94fcbd142ccf.png)<br>
![soortenmlunsupervised](https://user-images.githubusercontent.com/48352335/222239480-09ab805d-da4f-4cd2-acf0-23241c2b4c3d.png)

- In **reinforcement learning**, the AI system aims for a *reward*. For instance, to become good at a certain video game, the AI system will play the game numerous times and learn which actions to avoid and which to undertake to allow it to win. Google DeepMind's AlphaGo Zero became a top Go player in 2017 through reinforcement learning. It is even better than AlphaGo, which had previously defeated the best human player of this game.<br>
Play this [game](https://dwengo.org/rl). It gives you an idea of reinforcement learning.  
