---
hruid: PN_StandaardiserenM-v1
version: 3
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
target_ages: [14, 15, 16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: "https://kiks.ilabt.imec.be/jupyterhub/?id=0302"
estimated_time: 50
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-andere-talen', 
    'http://ilearn.ilabt.imec.be/vocab/ondniv/sec-gr2-doorstroom-aso'
]
teacher_exclusive: true
---
