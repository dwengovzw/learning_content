---
hruid: Temp-v1
version: 3
language: nl
title: "T"
description: "T"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

p.introduction {
  width: 350px;
  font-size:25px;
  line-height:1.3;
}

p.introduction span {
  background-color: #f48024;
  color: #1d1d1e;
  border-radius: 10px;
  -webkit-box-decoration-break: clone;
  box-decoration-break: clone;
  padding: 0 5px 0 5px;
}

<p class="introduction">Hi so <span>This is what I did but not sure how to go from here</span> and here is another <span>highlighted span</span></p>

<div class="alert alert-box alert-success">
    In deze notebook kan je je eigen microfoto's uploaden en testen met het <em>deep learning</em>-systeem dat besproken wordt in de paper <em>From leaf to label: a robust automated workflow for stomata detection</em> van <em>Sofie Meeus</em>, <em>Jan Van den Bulcke</em> en <em>Francis wyffels</em>.
</div>