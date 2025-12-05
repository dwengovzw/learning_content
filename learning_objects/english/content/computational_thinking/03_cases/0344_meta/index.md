---

hruid: m_ct03_44
version: 3
language: en
title: "Stomata"
description: "Automatic counting of stomata on microscopic images using AI"
keywords: ["AI", "image recognition", "stomata", "deep learning"]
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
Automate counting of stomata on microscopic images (project 'KIKS').
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>How does a computer 'see' an image and process it?</li>
    <li>How are images provided to the computer (input)?</li>
    <li>Analyze the microscopic images in the dataset: color, resolution, format.</li>
    <li>Which AI system is suitable for classification (stomata or no stomata)?</li>
    <li>How should the training set be structured and labeled?</li>
    <li>How to obtain a suitable dataset and minimize bias?</li>
    <li>How to determine the required accuracy of the AI system?</li>
    <li>How can detected stomata be counted? (clustering, deduplication)</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>Object detection is often done with deep convolutional neural networks trained with labeled examples.</li>
    <li>Binary classification: stomata present or absent. The system learns to recognize stomata features.</li>
    <li>Bias in the dataset (pattern):
        <ul>
            <li>stomata are approximately 125 x 125 pixels;</li>
            <li>images have a gray-green color.</li>
        </ul>
    </li>
    <li>The same technique (*sliding window*) is used for dataset preparation and clustering detected stomata.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>A digital image is a 3D grid of numbers (pixels) for the computer, with color represented via RGB codes. Patterns such as stomata are recognized in these numerical arrays.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
For training:
<ul>
    <li>Algorithm to divide images into squares with or without stomata.</li>
    <li>Algorithm to train the neural network on these examples.</li>
</ul>
For counting stomata:
<ul>
    <li>Algorithm to divide the image into 125 x 125 pixel squares and feed them to the network.</li>
    <li>Algorithm to cluster multiple detections of the same stomata.</li>
    <li>Algorithm to count the total number of stomata.</li>
</ul>
</algorithms>
<implementation>
**Program**<br>
See the full implementations in the <a href="https://dwengo.org/kiks">KIKS project</a>.
</implementation>
