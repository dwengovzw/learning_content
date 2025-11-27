---

hruid: m_ct03_42
version: 3
language: en
title: "Sea Level - Trend Line"
description: "Predicting future sea levels in Ostend using trend lines"
keywords: ["sea level", "trend line", "linear regression", "Python"]
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
Analyze how the sea level in Ostend is likely to evolve in the future.
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>Collect data: historical sea level measurements in Ostend (via open data or meteorological sources).</li>
    <li>Visualize the data in a scatter plot.</li>
    <li>Determine the trend line: linear or polynomial model depending on the shape of the plot.</li>
    <li>Choose software for analysis and visualization (e.g., Python with modules like NumPy and Matplotlib).</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>Examine the shape of the scatter plot: a linear or non-linear pattern determines the type of trend line.</li>
    <li>Repeated calculations or sub-algorithms can be encapsulated in a function (e.g., a function to calculate the coefficients of the trend line).</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>The trend line is a model that reflects the rising trend of fluctuating sea levels and allows predictions. The model abstracts from small variations.</li>
    <li>Functions in the software are abstractions of sub-algorithms that perform specific calculations.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
Steps to visualize the trend line in Python:
<ol>
    <li>Define the form of the equation of a line or polynomial.</li>
    <li>Create a function to determine the coefficients of the trend line fitting the data points.</li>
    <li>Read in the historical sea level data.</li>
    <li>Determine the trend line using the data and the coefficient function.</li>
    <li>Visualize the data points and trend line using a graph.</li>
</ol>
</algorithms>
<implementation>
**Program**<br>
For a worked example of implementation in Python, refer to the learning path ['Climate'](https://www.dwengo.org/learning-path.html?hruid=pn_klimaatverandering&language=nl&te=true&source_page=%2Fstem%2F&source_title=%20STEM#pn_inleiding_klimaat;nl;3) from the lesson theme ['Python in STEM'](https://www.dwengo.org/stem/).
</implementation>
