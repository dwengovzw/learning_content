---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: The chaos explained
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: stem5_6
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
teacher_exclusive: false
title: The chaos explained
version: 3
---
# Chaos explained

Earlier we looked at the logistic growth model to represent a population of caterpillars. We found that the model is completely unpredictable for certain initial values \\(u_0\\)! In this module you will learn why this is the case.

## Interactive notebook

In this module you will dive right into an interactive online notebook, where you will use Python to create some interesting plots.

[![](embed/knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=6040_en "Differential equation")

## Beyond the insects

The logistic equation is extremely important, not because it is so biologically realistic, but because it is one of the simplest ways to generate a chaotic sequence. **Chaos theory, the science that small causes can have large, unexpected effects**, is a relatively young branch of mathematics. It could only flourish in the 20th century, when computers made it possible to quickly perform computational experiments (as you have done here).

One of the pioneers in this field was the meteorologist **Edward Lorenz**. While experimenting with a simple weather model, he rounded the numbers from six to three digits to speed up the calculations. To the dismay of the scientific community, which until then had assumed that this rounding would result only in a trivial rounding error, it was found to lead to **significantly different outcomes**. Today it is widely accepted that systems such as the weather (and fluid flows in general) are chaotic. This makes it virtually impossible to predict the weather accurately more than a week in advance. The graph below shows this:

![Weather forecast](embed/weersvoorspelling.png "https://randalolson.com/2014/06/21/we-can-only-forecast-the-weather-a-few-days-into-the-future/")<br>
Source: [https://randalolson.com/2014/06/21/we-can-only-forecast-the-weather-a-few-days-into-the-future/](https://randalolson.com/2014/06/21/we-can-only-forecast-the-weather-a-few-days-into-the-future/)

Here you see the average error between the predicted and the observed temperature as a function of the number of days into the future for which you try to predict the temperature. If you rely only on climatological data—for example, by checking how warm it typically is on this day of the year—you see that the error is 7 degrees Fahrenheit, or about 4 degrees Celsius (orange). If you predict that the temperature will not change in the coming days (blue), then only the next day do you obtain a forecast that is more accurate than the one based on climatological data. If you finally use advanced weather models (gray), you see that **the deviation between the predicted and the actual temperature increases the further ahead in time you try to forecast**. This shows that it is indeed difficult to predict the weather far in advance!