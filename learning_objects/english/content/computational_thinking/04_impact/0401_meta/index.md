---

hruid: m_ct04_01
version: 3
language: en
title: "Profiling"
description: "Profiling"
keywords: [""]
educational_goals: [
    {source: Source, id: id},
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/ct-schema
available: true
target_ages: [12, 13, 14, 15, 16, 17, 18]
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
System for personalized advertising on an online platform (recommendation algorithm). 
</div>
</context>
<decomposition>
**Decomposition**<br>
- User personality profile: interests, opinions, preferences, nature ... 
- Collecting and storing data about the user:
    - Social media posts
    - Purchase behavior
    - Click behavior  
- Profiles of other users
- An algorithm to derive personality traits from language use (NLP)
- An algorithm to recognize patterns in purchase and click behavior
- An algorithm to identify related profiles  
- A recommendation algorithm 
</decomposition>
<patternRecognition>
**Pattern recognition**<br>
- Patterns in purchase and click behavior 
- Analyzing the user's language to derive personality traits, such as age 
- Comparing users to identify related profiles 
</patternRecognition>
<abstraction>
**Abstraction**<br>
Users are reduced to certain personality traits and their purchase and click behavior.
</abstraction>
<algorithms>
**Algorithmic thinking**<br>
- Algorithms are used to create a personality profile: these are algorithms for *natural language processing*, i.e., language technology. 
- Other algorithms recognize patterns in purchase and click behavior.
- Using additional algorithms, related profiles are identified. 
- The personality profile, patterns in purchase and click behavior, and the purchase and click behavior of users with a related profile serve as input for a recommendation algorithm that provides personalized advertising.<br>
</algorithms>
