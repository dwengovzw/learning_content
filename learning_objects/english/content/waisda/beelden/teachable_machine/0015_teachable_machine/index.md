---
content_type: text/markdown
copyright: CC BY Dwengo
description: How does Google's Teachable Machine work?
estimated_time: 20
hruid: org-dwengo-waisda-beelden-teachable-machine-example
keywords:
- Neurale netwerken
- Imagenet
- Teachable machine
- fine tuning
language: en
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
- http://ilearn.ilabt.imec.be/vocab/tref1/ict
target_ages:
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: false
title: Teachable Machine
version: 1
---
# Google Teachable Machine

At [https://teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com) Google provides an application to tailor a *machine learning* model for classification to your own purpose. You can upload your own images to **tune** an AI system. For example, you can upload a number of images of cats and dogs to obtain a system that can distinguish images of cats and dogs.

## Misconception

A common misconception is that Teachable Machine will train a completely new AI system based on your data. **This is not true!** What the system actually does is **fine-tune** an **existing model**, which has already been trained to detect many objects, to achieve the best possible classification of your objects. Without using a pre-trained model, it would never be possible to train a system with only a limited number of images. It also wouldn’t be possible within a short time span.


<div class="dwengo-content assignment">
    <h2 class="title">Assignment</h2>
    <div class="content">
        <ul>
            <li>Find a number of objects of two types. For example, five ballpoint pens and five books.</li>
            <li>Visit <a href="https://teachablemachine.withgoogle.com">https://teachablemachine.withgoogle.com</a>.</li>
            <li>Create a new project for images; choose the standard model.</li>
            <li>Add a class (class) for the images of the ballpoint pens. Use the webcam to take a photo of each pen or upload some existing images of ballpoint pens.</li>
            <li>Add a second class for the images of the books. Again take photos with the webcam or upload some existing images of books.</li>
            <li>Click <strong>Train Model</strong>.</li>
            <li>In the meantime, find a few additional ballpoint pens and books.</li>
            <li>When the model has finished training, you can test it. Use the webcam and show one of the extra objects you fetched. Can the system classify the objects correctly?</li>
            <li>Also try a different kind of object. What is the result?</li>
        </ul>
    </div>
</div>