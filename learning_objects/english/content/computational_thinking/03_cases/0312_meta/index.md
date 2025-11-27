---

hruid: m_ct03_12
version: 3
language: en
title: "Jommeke"
description: "Jommeke"
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
**Problem Statement**<br>
Give the AI system a self-made drawing of Jommeke with elements you have deliberately added to mislead the system.
</div>
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>How does the system work?
        <ul>
            <li>The system is trained with images from Jommeke and therefore colors everything in the style of Jommeke.
            <li>The system will color line combinations it recognizes in the way it has learned.
            <li>The system first converts submitted images into black-and-white line drawings.</li>
        </ul>
    </li>
    <li>Which shapes are typical for Jommeke?
    <li>Which of these shapes can you use for objects other than those in the comics? (e.g., a plant with the shape of Jommeke's hair, a cloud shaped like a speech balloon.)
    <li>Since the system converts images to black-and-white line drawings, it is sufficient to provide a black-and-white drawing.</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>The system will recognize certain combinations of lines.
    <li>The system will also generalize to some extent, e.g., different hairstyles, different speech balloons...</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>We see the line combination on Jommeke’s head as 'hair'. The computer does not. For a computer, it is just a combination of lines.
    <li>The system may still generalize to different hairstyles, for example by taking context into account, such as where the lines are located in a scene. However, we do not know which elements the system considers ('black box').</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>

</algorithms>
<implementation>
**Program**<br>
Check the following <a href="https://www.dwengo.org/backend/api/learningObject/getWrapped?hruid=org-dwengo-jommeke-zelf-tekening-maken&version=1&language=nl">notebook</a> for the execution of this case.
</implementation>
