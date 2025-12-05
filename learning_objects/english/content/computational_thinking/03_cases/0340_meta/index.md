---

hruid: m_ct03_40
version: 3
language: en
title: "Binary Decision Tree - Healthcare Data"
description: "Representation of labeled healthcare data using a binary decision tree"
keywords: ["decision tree", "healthcare data", "AI", "binary tree"]
educational_goals: [
    {source: Source, id: id},
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/ct-schema
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
    '[http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen](http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen)'
]
teacher_exclusive: true
-----------------------

<context>
**Problem Statement**<br>
Represent labeled healthcare data using a binary decision tree that can assist in diagnosing or determining a treatment.
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>Analyze examples of binary decision trees in healthcare.</li>
    <li>Identify the elements of a decision tree: root, nodes, branches, leaves.</li>
    <li>Study how a decision tree works: splitting data based on a criterion (e.g., Gini index).</li>
    <li>Design an algorithm to build a binary decision tree:</li>
        <ul>
            <li>Determine the best root for the first split.</li>
            <li>For each branch, determine the most suitable yes-no question for further splits.</li>
            <li>Repeat until datasets are homogeneous.</li>
        </ul>
    <li>Preprocess the data into the required format for implementation.</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>Real-world data are often represented as a directed, rooted graph (usually binary).</li>
    <li>Splits follow the same pattern: a yes-no question produces two subsets, repeated until homogeneity is reached.</li>
    <li>Using a dispersion measure such as the Gini index follows the same recurring pattern.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>Irrelevant patient data (name, address) are ignored.</li>
    <li>The binary decision tree is an abstract model of the solution.</li>
    <li>Transparency: every split and decision can be explained.</li>
    <li>Abstraction is also applied in:</li>
        <ul>
            <li>representing dispersion as a number;</li>
            <li>formulating yes-no questions with mathematical expressions.</li>
        </ul>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
Algorithm for building a binary decision tree:<br>
<ol>
    <li>Choose the root that provides the best split. Create branches for yes and no outcomes.</li>
    <li>For each branch, choose the next yes-no question that gives the best split and create new branches.</li>
    <li>Repeat iteratively for all newly created branches.</li>
    <li>Stop when the datasets are homogeneous (all elements belong to the same class).</li>
</ol>
</algorithms>
<implementation>
**Program**<br>
Can be executed with or without a computer.<br>
For Python implementation or notebooks, see the **AI in Healthcare** project.
</implementation>
