---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Iris Regression
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: kiks_iris_regressie
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
- 16
- 17
- 18
teacher_exclusive: true
title: Iris Regression
version: 3
---
# Iris Regression
The Iris dataset was published by the British Ronald Fischer in 1936. The dataset concerns three species of irises (_Iris setosa_, _Iris virginica_, and _Iris versicolor_), 50 samples of each species. Fischer was able to distinguish the species from each other based on four features: the length and width of the sepals and the petals.

In the first notebook here, the linear relationship between the lengths of the sepals and petals of the _Iris virginica_ is studied. <br>
You standardize the data and represent it in a scatter plot. You calculate the correlation coefficient to see how strong the linear relationship between the two features is. Subsequently, the regression line is sought and drawn.<br>
With this regression line, the length of a petal is predicted for a known sepal length.<br>
In this notebook, you determine the regression line and the correlation coefficient with the built-in functions of the SciPy and scikit-learn modules.<br><br>
In a subsequent notebook, a machine learning algorithm will be explained.

[![](embed/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=1910_en "Iris regression")