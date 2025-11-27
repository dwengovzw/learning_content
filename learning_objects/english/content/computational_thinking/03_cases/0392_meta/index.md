---

hruid: m_ct03_92
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
-----------------------

<context>
**Problem Statement**<br>
Using computer vision, we can locate different objects in an image or video and identify them using classification techniques. This allows, for example, detecting the condition of tomatoes. With the YOLO algorithm, it is possible to automatically distinguish between rotten and good tomatoes.
</context>
<decomposition>
**Decomposition**<br>
To solve this problem with the YOLO algorithm, we need to create our own dataset to identify the condition of tomatoes. The steps are:
<ol>
    <li>Collect and label photos of tomatoes to create a dataset.</li>
    <li>Train the YOLO algorithm using this dataset.</li>
    <li>Test the algorithm with new images or live webcam footage.</li>
</ol> 
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
Once we can detect the condition of tomatoes, the same process can be applied to distinguish, for example, good from rotten pears. Beyond agriculture, computer vision is widely used in society: checking the quality of medication on a production line or detecting parts in a machine that require maintenance.
</patternRecognition>
<abstraction>
**Abstraction**<br>
A computer works in binary and does not “see” images like humans do; it sees numbers. An image consists of pixels, each with a color value represented numerically. Digital photos are grids of numbers, with RGB coding for colors: three tables of numbers for red, green, and blue, where each (R,G,B) triplet represents one pixel. The computer abstracts the image into numerical data.

![An image consists of pixels. Each pixel corresponds to a numerical value for the red, green, and blue components.](tensorappel.png) </abstraction> <algorithms>
**Algorithmic Thinking**<br>
We solve this problem using the **YOLO algorithm**. A detailed description can be found in the <a href="/learning-path.html?hruid=agri_landbouw&language=nl&te=true&source_page=%2Fagriculture%2F&source_title=%20AI%20in%20de%20Landbouw#agri_tomaten;nl;3"><strong>AI in Agriculture learning path – Deep Learning</strong></a>. </algorithms> <implementation>
**Program**<br>
An implementation to recognize tomatoes using computer vision can be found in the <a href="/learning-path.html?hruid=agri_landbouw&language=nl&te=true&source_page=%2Fagriculture%2F&source_title=%20AI%20in%20de%20Landbouw#agri_tomaten;nl;3"><strong>AI in Agriculture learning path – Deep Learning</strong></a>. </implementation>
