---

hruid: m_ct04_04
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
Does a voice assistant provide input to a recommendation algorithm for advertising?  
</div>
</context>
<decomposition>
**Decomposition**<br>
- Language technology
    - Speech-to-text
    - Text-to-speech
    - Text analysis
    - Text generation
- Data storage
- Energy consumption
- Privacy aspects
    - Text data are stored in order to be processed.
    - Are the data retained?
    - Who has access to the data?
    - Are the data shared?
        - E.g. turning on the heating using Siri requires cooperation between two digital systems. 
- Method to activate the assistant: 
    - spoken trigger.
- Recommendation algorithm for personalized advertising
</decomposition>
<patternRecognition>
**Pattern recognition**<br>
- Personalized advertising is done, among other things, on the basis of *lookalike audiences* (through pattern recognition, a person is attributed the same interests as someone with a similar profile)
</patternRecognition>
<abstraction>
**Abstraction**<br>
</abstraction>
<algorithms>
**Algorithmic thinking**<br>
- Speech recognition technology to convert speech into text
- Natural language processing to link meaning to the text
- Generative technology to possibly formulate a response
- Speech synthesis technology to convert text into speech
- (Optionally) an algorithm for sentiment analysis
- Recommendation algorithm for personalized advertising
</algorithms>
