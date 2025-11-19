---
content_type: text/markdown
copyright: CC BY dwengo
description: What is Q-learning
estimated_time: 3
hruid: org-dwengo-waisda-rl-agent-trainen-q-learning
keywords:
- AI
- "re\xEFnforcement learning"
- versterkend leren
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
title: Q-learning
version: 1
---
# Q-learning

There are quite a few different techniques to search for an optimal policy. In the remainder of this learning path we focus on **Q-learning**. In Q-learning we look for a **value function** \\(Q\\) that works well for our problem. \\(Q\\) tells us for every combination of a **state** and an **action** how good that action is in that state. If we write that as a formula, it looks as follows:

\\[
    Q(T_t, A_t)=\mathrm{How\ good\ is\ action\ }A_t\mathrm{\ in\ state\ }T_t
\\]

Here, \\(T_t\\) and \\(A_t\\) are, respectively, the state and the action at time \\(t\\).

There are different ways to represent the function \\(Q\\). In the remainder of this learning path we represent the \\(Q\\) function with a **Q-table**.