---
hruid: extern-test-v1
version: 1
language: nl
title: "Testing external content as learning object"
description: "This is a description"
keywords: ["voorbeeld", "voorbeeld2"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by dwengo vzw.
licence: CC by dwengo vzw.
content_type: extern
available: true
target_ages: [10, 11, 12, 13, 14]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: "https://kiks.ilabt.imec.be/jupyterhub/?id=1"
estimated_time: 50
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
