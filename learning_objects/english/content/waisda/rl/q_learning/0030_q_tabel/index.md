---
content_type: text/markdown
copyright: CC BY dwengo
description: What is the Q-table
estimated_time: 3
hruid: org-dwengo-waisda-rl-agent-trainen-q-tabel
keywords:
- AI
- "re\xEFnforcement learning"
- versterkend leren
- q-learning
- q-tabel
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
title: Q-table
version: 1
---
# The Q-table

The value function \\((Q(T_t, A_t)\\)) tells us how good action \\(A_t\\) is in state \\(T_t\\). One of the simplest ways to represent this function is by means of a table. For every possible state in our world we add a row to the table, and for every possible action we add a column. In the figure below you see a Q-table for 5 actions and 7 states. The value in the table indicates how good the action at the top of the column is when the agent is in the state to the left of the row. In the image you can see at the top left how good action 2 is in state 3.

![](img/q_table_example.png)

Using this table we can execute a certain policy. The policy could, for example, be to choose in every state the action with the highest possible Q value.

<div class="dwengo-content assignment">
<h2 class="title">Assignment</h2>
<div class="content">
Given the Q-table and the policy we described above, which action will the agent take when it is in state 6?
</div>
</div>

<div class="dwengo-content sideinfo">
<h2 class="title">The <code class="language-python">argmax</code> function</h2>
<div class="content">
When we want to select the best action in the current state in the Q-table, we first look at which row corresponds to this state. In this row we search for the best action. This action corresponds to the index of the highest value in the row. To find this index, you can use the <code class="language-python">argmax()</code> function in Python. 
</div>
</div>