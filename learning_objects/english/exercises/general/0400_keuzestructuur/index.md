---
hruid: g_ks
version: 3
language: en
title: "Uitleg Keuzestructuur"
description: "Uitleg Keuzestructuur"
keywords: ["oefeningen", "keuzestructuur"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [12, 13, 14]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# dwenguinoBlockly
## Conditional Statements: If-Then

To make your robot a social robot, it will need to be able to react to certain stimuli: a person approaching, a loud noise, etc. Think, for example, of sliding doors that open when someone is nearby.

To let your robot respond to such stimuli, you use a conditional statement. Conditional statements always consist of a **condition**, *IF*, and an associated **action**, *THEN*. Often, an **alternative action**, *ELSE*, is also provided, which is executed if the condition is not met.

***

In the simulator, you can find the blocks for a conditional statement in the category ![](embed/cat_logica.png "category logic"). The simplest form of this block is the *'IF-THEN'* block.

![](embed/keuzestructuur1.png "IF-THEN block")

However, you can make this block as long as you want, depending on the number of conditions your robot has to take into account. How to do this is briefly shown below.

![](embed/keuzestructuur2.png "IF-THEN-ELSE")

<div class="alert alert-box alert-danger">
As mentioned earlier, you can make this block as long as you want, but be careful not to make your program unnecessarily complicated!
</div>

***

To program conditions for a conditional statement, you use the blocks below:

![](embed/block_and_or.png "AND-OR block")
![](embed/block_operations.png "mathematical operations block")

When you combine these, you can program very simple conditions such as *"if the distance is greater than 0, but less than 20, then ..."* 

![](embed/combo_andor_operations.png "combination of conditions")