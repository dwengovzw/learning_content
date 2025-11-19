---
content_type: text/markdown
copyright: CC BY dwengo
description: Get acquainted with reinforcement learning.
estimated_time: 10
hruid: org-dwengo-waisda-rl-introductie-beloning-policy-waarde
keywords:
- AI
- "re\xEFnforcement learning"
- beloning
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
title: Reward, policy and value function
version: 1
---
# Reward

In reinforcement learning, the reward is the most important instrument to ensure that the **agent** can learn something. The reward that the **agent** receives depends on the **action** it took and the current **state** of the **environment**. In reinforcement learning we always talk about a **reward**. You can also punish the **agent**, which corresponds to giving a negative reward.

When we train an **agent** with reinforcement learning, the main goal of the agent is to maximize the rewards it receives. In our game, this corresponds to achieving the highest possible score. After all, the score is the sum of all previous rewards.

# The policy / the policy

The **policy** defines which **action** the **agent** will take in a given **state**. The **policy** therefore determines how the **agent** behaves. In reinforcement learning, we want to learn an optimal **policy** to perform a particular task. 

In the game, you come up with a **policy** with which you try to achieve the highest possible score. The **policy** could, for example, be to ensure that the two numbers on the screen are always equal. Another policy could be to try to ensure that the sum of the two numbers is always 14. 

When you apply a **policy**, you receive a reward for it. If that reward is positive, it strengthens your belief that your current behavior is good. If the reward is negative, it will prompt you to change your behavior and thus adjust your **policy**.

# The value function

The **value function** gives us an estimate of the magnitude of the **reward** you can expect in the long term when you take a particular **action** in a particular **state** under a given **policy**. This definition is rather abstract. By connecting it to the Pong game you played, it becomes easier to understand what the value function is for.

- Suppose we play the game and start with a score of 0.
- We devise a **policy** that ensures the two numbers on the screen always have the same value.
- Every **action** we take (move up, move down, or stay still) can yield a reward. That reward is +25 when we hit the ball, -10 when we miss the ball, and 0 when the ball is somewhere else on the field. 
- When the paddle is at position 5 and the ball at coordinate (6, 4), we will move the paddle down. In that case, however, we receive a **reward** of 0. So we don't know whether our **action** was good or bad. The **reward** only comes when we hit the ball.
- To still be able to estimate at any moment how good an **action** is, we use the **value function**. This **value function** will, in every **state**, estimate how good an **action** is in that **state**. The **value function** provides an estimate of the **reward** we will receive in the long term by taking an **action**, taking into account the **policy** we had chosen (here, to keep the numbers equal).

The policy and the value function are closely linked. The policy says what the agent should do, and the value function says how good that is.