---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Sea level - trend line
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct03_42
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
- 12
- 13
- 14
teacher_exclusive: true
title: Sea level - trendline (2,3)
version: 3
---
# Evolution of the sea level in Ostend

**Visualizing a scatter plot and a trend line.**

*In the context of climate change, students work with 'real' data. They start from a challenge. They have to search for the data themselves, visualize it by means of a scatter plot, and look for a possible trend line.*

**Target group:** 
* 2nd or 3rd grade - dual track
* 2nd or 3rd grade - academic track

**Subject:** 
* Mathematics - Sciences - STEM
* Computer Science

**Prior knowledge:** 
* Students can gather information via the internet. 
* Students know that the shape of the scatter plot is an indication of a possible trend line. 
* Students can visualize a scatter plot and a trend line in Python. 

A possible **progression** of the case study is as follows:<br><br>

*Phase 1*<br>
<ul>
    <li>Students brainstorm about the problem.
    <li>They partially fill in the framework of the basic concepts.</li>
</ul>

*Phase 2*<br>
<ul>
    <li>Students collect data from the internet on sea level in Ostend over the past decades.</li>
</ul>

*Phase 3*<br>
<ul>
    <li>Students visualize the data in a scatter plot. Due to the size of the dataset, they use Python for this.
    <li>They further complete the framework of the basic concepts.
    <li>Students realize that the data reflect a trend and that this trend can be approximated by a linear relationship.
    <li>Students have a trend line generated via linear regression.
</ul>

![ct-schema](@learning-object/m_ct03_42/nl/3)


### Minimum objectives (Source: onderwijsdoelen.be)

<span style="color: yellowgreen">(06.06 Academic track) Students apply the Pythagorean theorem to solve geometric problems in the plane and in space.</span>

<span style="color: yellowgreen">(04.05 Academic track; Dual track, Labor market track) Students analyze the impact of digital systems on society based on principles of computational thinking.</span>

Through this case you will work with the principles of computational thinking. With this case you therefore partially address this attainment target.

### Specific minimum objectives (Source: onderwijsdoelen.be)

<span style="color: yellowgreen"><strong>Algorithms and programming</strong></span><br>
<span style="color: yellowgreen">(07.01.01 Academic track) Students program self-designed solutions to concrete problems.</span><br>
Target group: Business-supporting Computer Science, Economics-Mathematics, Greek-Mathematics, Information and Communication Sciences, Latin-Mathematics, Technological Sciences and Engineering, Sciences-Mathematics<br>
<span style="color: yellowgreen">(07.02.01) Students program self-designed solutions to concrete problems.</span>
Target group: Biotechnological and Chemical STEM Sciences, Construction and Wood Sciences, Mechatronics

### Annulled attainment targets (Source: onderwijsdoelen.be)
<span style="color: yellowgreen">(4.5 Academic track) Students design algorithms to solve problems digitally.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: create

<span style="color: yellowgreen">(4.5 Dual track) Students solve a well-defined problem digitally by adapting a provided algorithm. </span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: create

<span style="color: yellowgreen">(6.19 Academic track) Students investigate the relationship between two numerical quantities in a dataset using a scatter plot.
</span>
&nbsp;&nbsp;&nbsp;&nbsp;With ICT
&nbsp;&nbsp;&nbsp;&nbsp;Constructing and interpreting a scatter plot
&nbsp;&nbsp;&nbsp;&nbsp;Determining and interpreting the trend line with accompanying formula 
&nbsp;&nbsp;&nbsp;&nbsp;Determining and interpreting the correlation coefficient for a linear relationship

&nbsp;&nbsp;&nbsp;&nbsp;The attainment target is achieved both with and without context.

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: analyze

<span style="color: yellowgreen">(6.9.1 Threshold objectives Biotechnology) Students investigate the relationship between two numerical quantities in a dataset using a scatter plot.
</span>
&nbsp;&nbsp;&nbsp;&nbsp;With ICT
&nbsp;&nbsp;&nbsp;&nbsp;Constructing and interpreting a scatter plot
&nbsp;&nbsp;&nbsp;&nbsp;Determining and interpreting the trend line with accompanying formula 

&nbsp;&nbsp;&nbsp;&nbsp;The attainment target is achieved with context.

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: analyze


<span style="color: yellowgreen">(6.53 Academic track) Students apply a scientific method to develop knowledge and to answer questions.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: analyze

<span style="color: yellowgreen">(12.3.1 Threshold objectives Biotechnological Sciences) Students apply a scientific method to develop knowledge and answer questions.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: apply
    
<span style="color: yellowgreen">(6.54 Academic track; 6.30 Dual track) Students analyze natural and technical systems using various STEM concepts. </span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: analyze

<span style="color: yellowgreen">(6.55 Academic track; 6.31 Dual track) Students design a solution to a problem by applying concepts and practices from different STEM disciplines in an integrated way.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Including context
&nbsp;&nbsp;&nbsp;&nbsp;* Each STEM discipline is addressed at least once in an integrated manner.

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: create

<span style="color: yellowgreen">(6.57 Academic track)Students investigate, on the basis of concrete societal challenges, the interaction between STEM disciplines themselves and between STEM disciplines and society.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Including context
&nbsp;&nbsp;&nbsp;&nbsp;* Contexts such as climate change, renewable energy, care and health, education, water supply, mobility, livable and sustainable cities, and ocean pollution are covered.
&nbsp;&nbsp;&nbsp;&nbsp;* The sustainable development goals as formulated by the international community are provided (SDGs, sustainable development goals).

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: analyze

<span style="color: yellowgreen">(6.33 Dual track)Students explain, on the basis of concrete societal challenges, the interaction between STEM disciplines themselves and between STEM disciplines and society.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Including context
&nbsp;&nbsp;&nbsp;&nbsp;* Contexts such as climate change, renewable energy, care and health, education, water supply, mobility, livable and sustainable cities, and ocean pollution are covered.
&nbsp;&nbsp;&nbsp;&nbsp;* The sustainable development goals as formulated by the international community are provided (SDGs, sustainable development goals).

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: understand

<span style="color: yellowgreen">(13.3 Academic track; 13.3 Dual track) Students deploy an appropriate search strategy when selecting digital and non-digital sources to answer an information question.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: analyze

<span style="color: yellowgreen">(13.5 Academic track; 13.5 Dual track) Students assess digital and non-digital sources and information for reliability, correctness, and usefulness in function of an information question and on the basis of criteria.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: evaluate

<span style="color: yellowgreen">(13.9 Academic track; 13.9 Dual track) Students present processed information in a self-chosen digital and a non-digital presentation form.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: apply

<span style="color: yellowgreen">(13.10 Academic track; 13.10 Dual track) Students manage information themselves in a structured way, digitally and non-digitally.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: apply


<span style="color: yellowgreen">(13.11 Academic track; 13.11 Dual track) After analyzing a provided problem, students formulate a research question and a hypothesis.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: create

<span style="color: yellowgreen">(13.12 Academic track; 13.12 Dual track) Students carry out a research technique to obtain digital and non-digital data in function of a research question.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: apply

<span style="color: yellowgreen">(13.13 Academic track; 13.13 Dual track) Students execute a self-chosen and appropriate solution strategy in function of a study or a problem.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: evaluate

<span style="color: yellowgreen">(13.14 Academic track; 13.14 Dual track) Students formulate a conclusion for a research question and an answer to a hypothesis based on their own research results.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitive dimension: mastery level: create