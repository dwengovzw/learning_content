---

hruid: m_ct04_07
version: 3
language: en
title: "Sentiment analysis"
description: "Sentiment analysis"
keywords: [""]
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
**Problem statement**<br>
Represent labelled data from the healthcare sector using a decision tree that can help with making a diagnosis or determining a treatment.
</div>
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>Look for a pattern in the examples (a directed rooted graph, a binary decision tree).</li>
    <li>Which elements make up a decision tree?</li>
    <li>What is the functioning of a decision tree?</li>
    <li>How do you construct a decision tree?
        <ul>
            <li>How can you represent the degree of dispersion using a number.</li>
            <li>Which calculations lead to the correct split?</li>
            <li>How do you formulate a yes/no question using logical (mathematical) expressions?</li>
            <li>Designing an algorithm to construct a binary decision tree.</li>
        </ul>
    </li>
    <li>The implementation of the algorithm in the computer.</li>
    <li>Preprocessing the data into the desired format.</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern recognition**<br>
<ul>
    <li>The real-life examples show that such data are often represented by a directed rooted graph, usually binary. In other words, a binary decision tree is suitable for representing data.</li>
    <li>A binary decision tree starts from a root and a yes/no question. This question results in a split of the data into two sets that show as little dispersion across the categories as possible. This continues in an analogous way with successive yes/no questions. In this way, the tree is built up with branches and nodes. Finally, the leaves of the decision tree represent the possible decisions.</li>
    <li>Recognising that splitting data based on the Gini index always follows the same pattern.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>The decision tree does not take irrelevant patient data into account, such as name, place of residence, etc.</li>
    <li>The decision tree is an abstract representation of the solution in the form of a graph. It is a model of the solution</li>
    <li>This representation is also transparent.</li>
    <li>Abstraction also occurs:
        <ul>
            <li>when representing the degree of dispersion using a number; and</li>
            <li>when formulating a yes/no question using a mathematical expression.</li>
        </ul>
    </li>
</ul>
</abstraction>
<algorithms>
**Algorithmic thinking**<br>
Algorithm to construct a binary decision tree.<br>
<ol>
    <li>Determine which root yields the best split. Create branches for the possible outcomes of the yes/no question.</li>
    <li>For each branch, determine which yes/no question is best suited for the next split. Create branches for the possible outcomes of the yes/no questions.</li>
    <li>Repeat the previous step for the newly created branches.</li>
    <li>Stop repeating when the resulting sets are homogeneous, i.e. contain only elements from one and the same class.</li>
</ol>

*This is an iterative process: the same technique is applied each time to determine the root and the nodes.* </algorithms> <implementation>
**Program**<br>
The notebook ‘Heart disease’ in the learning path <a href="/learning-path.html?hruid=aiz1_zorg&language=nl&te=true&source_page=%2Fcare%2F&source_title=%20AI%20in%20de%20Zorg#aiz_oefenen;nl;3"><strong>AI in healthcare – Decision tree</strong></a> contains an exercise in which you generate a decision tree using ‘real’ data. </implementation>
