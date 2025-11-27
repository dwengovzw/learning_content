---

hruid: m_ct04_05
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
How is computational thinking embedded in the current recruitment process?  
</div>
</context>
<decomposition>
**Decomposition**<br>
The application process can be divided into several steps and aspects.
- For the potential employee: searching for vacancies, preparing application documents, communicating with potential employers, and managing social media accounts, etc.
- For the employer: defining the required competences, publishing the vacancy, and reviewing online profiles.    
</decomposition>
<patternRecognition>
**Pattern recognition**<br>
Pattern recognition is relevant when analysing online profiles and social media posts of applicants. Employers can use this data to form an image of the personality, interests, and behaviour of applicants.    
    This can influence decisions during the recruitment process. For example, if an applicant regularly posts negative comments about previous employers—if there is a pattern—this can be a red flag for potential employers. Such posts with negative content can be detected through automatic sentiment analysis.
</patternRecognition>
<abstraction>
**Abstraction**<br>
- Both a job vacancy and application documents such as a CV are abstractions of reality. A vacancy only provides information about the main lines of your tasks, just as a CV only represents the most important aspects of your knowledge and skills. <br>
- The profile that an application creates of you is also an abstraction of your personality. 
</abstraction>
<algorithms>
**Algorithmic thinking**<br>
- AI algorithms can be used to match vacancies with applicant profiles. These algorithms can take various criteria into account, such as education, experience, and skills, in order to find the best matches. This increases the likelihood of finding relevant vacancies for applicants and reduces the number of irrelevant results.
- AI algorithms can be used by potential employers to create profiles of applicants.
- An algorithm for automatic sentiment analysis can be applied to determine the sentiment of an applicant’s social media posts.
</algorithms>
