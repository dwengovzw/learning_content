---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Practice notebooks
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: aiz_oefenen
keywords:
- ''
language: en
licence: dwengo
return_value:
  callback_schema:
    att: test
    att2: test2
  callback_url: callback-url-example
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
target_ages:
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: false
title: Practice notebooks
version: 3
---
# Practice notebooks
In the 'AI in Healthcare' project you have a few datasets with 'real' data. 

You can get started with a set of exercises that make use of this 'real' data. These data are stored in data files that are often substantial; we work with csv files. Here, csv stands for _comma separated values_.<br>
Such a csv file is essentially a large table in which each column, for example, contains the values of a specific health parameter for a large number of patients. One particular column contains a 'label', the class to which the patient belongs, e.g., 'ends up in intensive care'.

-------

The 'Hartaandoening' notebook contains such an exercise. <br>
Cardiovascular diseases are a major cause of death. Heart failure, for example, is a common condition. The heart.csv dataset contains values for 11 parameters that can be used to predict possible heart disease. High blood pressure, diabetes, and elevated cholesterol are known factors that increase the risk of a heart condition. This dataset is a combination of 5 datasets from the US and Europe and contains values from 918 individuals.

You will read and preprocess the data table using functionality from the Python modules pandas and NumPy. So you will apply what you learned in the 'Dataframe' section of this learning path. Once you have obtained the desired parameters and the label in a NumPy array, everything proceeds in the same way as in the example notebook. Ultimately, a decision tree is generated based on the given large dataset.

[![](embed/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=3020_en "Notebooks Sentiment Analysis")

-----

You can do similar exercises with the datasets titanic.csv, kyphosis.csv, heartca.csv, borstkanker.csv, and grieperig.csv.