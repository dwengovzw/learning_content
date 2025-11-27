---

hruid: m_ct03_46b
version: 3
language: en
title: "Fingerprint Matching"
description: "Fingerprint Matching"
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
You want a computer to compare fingerprints. How can this be done?
</context>
<decomposition>
**Decomposition**<br>
<ol>
    <li>In what format will the fingerprints be provided to the computer? 
        <ul>
            <li>Digital photos</li>
	        <li>Not too large due to storage limitations and must be transmittable.</li>
        </ul>
    </li>
    <li>Characterization: determine the features (and possibly the number of features) that suffice to distinguish a fingerprint from others, e.g., the minutiae points.</li>
    <li>The photos need preprocessing (remove noise, convert to black-and-white, thin the lines to 1 pixel).</li>
    <li>Detect and mark the chosen features in the photos. How can this be done algorithmically?</li>
    <li>Abstract the representation into a graph with minutiae as nodes, connected if on the same line, feature type indicated by color, distance between points as edge weight. A new type of graph is required: a colored, weighted graph.</li>
    <li>Two types of problems: identification and authentication.</li>
</ol>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
Digital image processing typically works via pixel values, so here pixel values will be used to detect minutiae points.

To tackle map coloring problems, graphs are used, where neighboring countries are nodes connected by edges. Similarly, minutiae points can be taken as nodes in a graph, connected if they lie on the same line. </patternRecognition> <abstraction>
**Abstraction**<br>
The minutiae points together with other features chosen to distinguish the fingerprint form an abstract representation of the fingerprint.<br>
This can be summarized as an abstract visualization, e.g., a colored, weighted graph.
Each minutiae point can be represented by a number indicating its type. This number is an abstraction of the feature type. </abstraction> <algorithms>
**Algorithmic Thinking**<br>
Multiple algorithms are needed.<br>
Algorithms to:

<ul>
    <li>remove noise;</li>
    <li>convert the photos to black-and-white;</li>
    <li>thin the lines to 1 pixel;</li>
    <li>detect the minutiae points;</li>
    <li>create the colored, weighted graph;</li>
    <li>match a new fingerprint against the dataset (identification);</li>
    <li>verify if a fingerprint matches the dataset (authentication);</li>
    <li>optionally control the scanning device (detect finger placement);</li>
    <li>compress the photo files.</li>
</ul>
</algorithms>
<implementation>
**Program**<br>
No programming is required for this example.
</implementation>
