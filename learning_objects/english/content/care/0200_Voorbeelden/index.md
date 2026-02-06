---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Example notebook
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: aiz_voorbeeld
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
title: Example notebook
version: 3
---
# Example notebook
You can take some bodily parameters into account to try to predict whether a patient is at risk of a heart attack. For known
patients, certain parameters can be found in the patient record.
The following table shows such parameters for six patients for whom it is known whether or not they had a heart attack (Shoemaker et al., 2001).
Using this (too limited) dataset, we show how to apply the divide-and-conquer algorithm in practice to create a decision tree.
This decision tree can then be used to check whether new patients are at risk of having a heart attack.

|**Patient number**|**Chest pain**|**Male**|**Smokes**|**Sufficient physical activity**|**Heart attack**|
|---------------|------------------------|-----|-------|----------------------------|------------|
|1|yes|yes|no|yes|yes|
|2|yes|yes|yes|no|yes|
|3|no|no|yes|no|yes|
|4|no|yes|no|yes|no|
|5|yes|no|yes|yes|yes|
|6|no|yes|yes|yes|no|

<figure>
    <figcaption align = "center"><b>Table: Parameters of importance for risk of heart attack</b></figcaption>
</figure>

The algorithm to construct a decision tree can also be programmed on a computer. To have a computer execute this algorithm, you must cast the different steps unambiguously into a computer program. That has already been done for you and is available via Python modules.
You will use these and thus, by means of a rule-based AI system, automatically generate a decision tree.

In the notebook you start from the same table with the parameters used to try to predict whether a patient is at risk of a
heart attack. To implement this in Python, you will need to enter this limited dataset into Python. This is done by entering a matrix. Such a matrix is nothing more than a table of numbers.

Note that the values of the variables in the table are categorical and that these will have to be converted for the computer into numeric or quantitative
variables. In the notebook, the values of the variables are entered as numeric values. For ‘no’ a ‘0’ is used and for ‘yes’ a ‘1’.

[![](embed/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=3010_en "Example notebook")

You can find additional explanation in chapter 8 of the manual.