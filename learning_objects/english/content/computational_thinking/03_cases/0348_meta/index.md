---

hruid: m_ct03_48
version: 3
language: en
title: "Sentiment Analysis"
description: "Sentiment Analysis"
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
Develop an AI system that classifies social media reviews according to sentiment (positive, neutral, negative).  
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>Explore the problem:
        <ul>
            <li>What is the sentiment of a text?</li>
            <li>Which techniques exist to determine the sentiment of a text, and what are their pros and cons?</li>
            <li>Which technique is most suitable for you? (Choose between a rule-based or data-driven AI system; here we choose rule-based.)</li>
        </ul>
    </li>
    <li>What is needed?
        <ul>
            <li>Sentiment lexicon in Dutch.</li>
        </ul>
    </li>
    <li>How to tackle the problem concretely? Subtasks:
        <ul>
            <li>Learn to work with the lexicon (How to find a word and its sentiment score in it?);</li>
            <li>Choose a representation for the review that the computer can work with, selecting an appropriate datatype (preprocess review: tokenize, remove capitalization and punctuation, represent words using dictionary form and part-of-speech);</li>
            <li>Determine sentiment score for each word by matching with the sentiment lexicon;</li>
            <li>Determine the overall sentiment of the review (How to compute this from the individual word scores?).</li>
        </ul>
    </li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>Using a lexicon and techniques such as tokenization, lemmatization, and part-of-speech tagging are common in language technology, e.g., for cyberbullying detection, author identification, automatic translation, and text generation.</li>
    <li>Rule-based cyberbullying detection and sentiment analysis follow similar algorithms. Only the lexicon differs.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>In a rule-based system, the sentiment of a word is represented numerically between -2 and 2.</li>
    <li>Details of the review are abstracted away, e.g., ignoring capitalization and punctuation. Tokenization reduces the text to its words. Lemmatization and part-of-speech reduce words to dictionary form and type.</li>
    <li>Preprocessing allows using a data structure suitable for efficient lookup.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
An **algorithm** to determine the sentiment of a review:<br>
<ul>
    <li>Create a list of dictionary forms of the words in the review, including their part-of-speech. Ignore punctuation and capitalization.</li>
    <li>Match the words in this list with the sentiment lexicon. Lookup each word in the lexicon, considering its part-of-speech. Store each word’s sentiment score in a list.</li>
    <li>Sum the sentiment scores in the list. The total is the review’s sentiment score.</li>
    <li>Determine the sentiment of the review using a mathematical expression (score > 0, = 0, < 0).</li>
</ul>
</algorithms>
<implementation>
**Program**<br>
This activity can be done without a computer. You can work with students to create a rule-based algorithm and test it unplugged. If you want to program, it can be done via Dwengo’s Python notebooks.
</implementation>
