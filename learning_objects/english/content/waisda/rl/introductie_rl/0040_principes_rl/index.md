---
content_type: text/markdown
copyright: CC BY dwengo
description: Get to know reinforcement learning.
estimated_time: 7
hruid: org-dwengo-waisda-rl-introductie-rl-principes
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
title: Principles of Reinforcement Learning (3)
version: 1
---
# Principles of reinforcement learning

We let you play the game because we can use it to explain all the basic principles of reinforcement learning. These principles are:

- **The agent** is the one who learns to play the game. Here, you are the agent (pronounced the English way). If we were to train an AI system to play the game, then that AI system would be the agent.
- **The environment** is the world in which the **agent** will learn. Here, the world is the game itself. In our game, the world consists of two paddles and a ball.
- The environment also has a **state**, which is how the world looks at that moment. The state of our game could be, for example: paddle 1 is at height 5, the ball is at position (6, 9), and paddle 2 is at height 9.
- **The actions**: as the **agent**, you can influence the **state** of the **environment**. In the game, you do this by pressing the buttons and moving your paddle up or down. By moving your paddle, you can also indirectly influence the position of the ball.
- **A reward**: during the game we receive a reward when we influence the world positively and we are punished (= a negative reward) when we influence it negatively. In humans and animals, a reward corresponds to feelings of happiness and pain. 
- **The policy**: this is the strategy that the **agent**—that is, you—is applying at that moment. The policy determines which action you will take in a given **state** of the **environment**.
- **The value function**: while the **reward** gives you an idea of which **actions** were good or bad in a particular **state**, the **value function** says something about what is good in the long term. 
- **Exploration and exploitation**: during learning, the agent has to trade off **exploring** new actions and **exploiting** known actions (to take advantage of them). When the agent does not **explore**, it cannot learn anything new. The agent is, as it were, stuck in a certain mindset. When the agent does not **exploit** knowledge, it constantly performs random actions. The agent will therefore not learn but only exhibit random behavior. In reinforcement learning, the art is to find the right balance between **exploration** and **exploitation**.

Many of these principles are relatively abstract. In the remainder of this learning path, we explain the principles in more detail.