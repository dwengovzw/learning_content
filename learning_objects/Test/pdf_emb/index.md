---
hruid: test-v7
version: 5
language: nl
title: "This is a title"
description: "This is a description"
keywords: ["voorbeeld", "voorbeeld2"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
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
content_location: example-location
estimated_time: 20
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
---
# ook vernieuwd! (en nu helemaal)
[pdf](@pdf/pdfs/vergadering.pdf "dit is een pdf")
![](@pdf/pdfs/vergadering.pdf)