---

hruid: m_ct03_90
version: 3
language: en
title: "Meta"
description: "Meta"
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
---

<context>
**Problem Statement**<br>
The *Levenshtein distance* is a metric used to determine the difference between two words or sentences. To calculate the distance between two words, you count the number of letters that must be added, removed, or replaced to transform one word into the other. If we want to solve this problem using a computer, we use **computational thinking**. The computer can construct a matrix and fill it step by step with the distances between (parts of) word A and (parts of) word B. A detailed description can be found in the <a href="/learning-path.html?hruid=anm4&language=nl&te=true&source_page=%2Falgorithms%2F&source_title=%20Algoritmes#org_dewengo_levenshtein_algorithm;nl;1"><strong>algorithm learning path – The Levenshtein distance</strong></a>.
</context>
<decomposition>
**Decomposition**<br>
To calculate the Levenshtein distance using a computer, we perform the following steps:
<ol>
    <li>Build a matrix.</li>
    <li>Calculate the minimum number of operations required to transform one (part of a) word into the other.</li>
    <li>Determine the optimal sequence of operations to minimize changes.</li>
    <li>Compute the final distance between the two words.</li>
</ol>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
The Levenshtein distance is used by chatbots to match a user question that is not in their “dictionary” with the closest existing question. It is also used in genetics to find similarities between DNA sequences. In this context, sequences of letters C, G, A, and T represent DNA bases. Calculating the distance between these “words” helps identify similarities between DNA sequences.
</patternRecognition>
<abstraction>
**Abstraction**<br>
When computing the Levenshtein distance, we focus only on the number and type of operations needed to transform word A into word B. The actual characters, words, or meanings are ignored.
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
To calculate the Levenshtein distance correctly, a step-by-step plan or algorithm must be defined, which a computer can execute.
</algorithms>
<implementation>
**Program**<br>
An implementation of this algorithm can be found in the <a href="/learning-path.html?hruid=anm4&language=nl&te=true&source_page=%2Falgorithms%2F&source_title=%20Algoritmes#org_dewengo_levenshtein_algorithm_dynamic;nl;1"><strong>algorithm learning path – The Levenshtein distance</strong></a>.
</implementation>
