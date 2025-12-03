---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Fingerprints
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: aiz_vingerafdrukken
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
teacher_exclusive: true
title: Fingerprints
version: 3
---
# Fingerprints

**Prior knowledge:** The students know what a graph, vertices and edges are. Here a new type of graphs is introduced, namely the colored, weighted graph. 

### Forensic science
Forensic science is of great importance for enforcing the law. Think of DNA technology, chemical analyses, examining traces caused by bullets, and analyzing or identifying fingerprints.

In this part of the learning path, you take a closer look at fingerprints. 

### Fingerprint
A fingerprint is the pattern of ridges that a fingertip leaves when it comes into contact with a surface. Fingerprints are unique to each person and remain unchanged throughout life. Even identical twins can be distinguished by them. One should keep in mind, however, that as a person grows, the patterns also enlarge, and that fingerprints can change due to illness or an accident. As people age, the ridges may also become less distinct. About 300 years before Christ, fingerprints were already used in China to identify people. In the US and Europe, this only began in the 19th century.

The skin on the inside and the tips of the fingers shows certain patterns: the ridges on the skin and the spaces between them form loops, arches, and whorls. These patterns are formed in the embryonic and fetal phases of a developing human.
Because of the way the skin on the fingertips forms, distinctive features (minutiae) also arise within these patterns: deltas, forks or bifurcations (bifurcations), islands or dots (islands, dots), ridge endings (ridge endings), crossovers, upward and downward bifurcations (spurs, hooks), and eyes on the ridge (lake, eye). These can be seen on fingerprints. On high-quality fingerprints, you can look in even more detail and observe pores and sweat glands. 

![image](https://user-images.githubusercontent.com/48352335/211288516-0e8ed701-31aa-41da-b22a-979a653cca1a.png)<br>
Figure: Example lesson material project CSI, module f. https://www.slo.nl/thema/meer/doorstroom-vmbo/algemene/werken-algemene/3e-leerjaar/

![Fingerprints_Minutiae_Patterns_Representation](https://user-images.githubusercontent.com/48352335/211396289-098e5e5a-516c-41ea-9f83-b86935676b56.jpg)<br>
Figure: The most common fingerprint minutiae patterns. Inaki Rom, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons.

So when studying fingerprints, at the first level one looks at loops, arches, and whorls. Afterwards, one looks in more detail by observing the minutiae. 

### The use of fingerprints
Fingerprints are used to identify people, e.g., a perpetrator of a crime, or for authentication, such as access to a smartphone. 

### Computational thinking
Example: Because of the large number of fingerprints, it became infeasible for the FBI to quickly try to match an incoming fingerprint to one of the fingerprints in their database. The need to automate arose. The computer was the solution for this. <br>
The digital files were preferably not too large in terms of storage capacity. Moreover, it was also necessary to be able to send the files nationwide, so the files also had to be kept small for that reason. 

![vingerafdrukschema](https://user-images.githubusercontent.com/48352335/211395837-e8001d34-f79f-49f3-8e43-d6d824601976.png)

**Unplugged activity:** <br>
Source: https://ccicada.org/education/ccicada-education-modules/#Fingerprint <br>
- On an enlarged photo of a fingerprint, indicate the minutiae, determine their type, and measure the distance in cm. 
- Convert this into a graph.
- Give the students a set and have them apply the same to it.
- Then give the students a new fingerprint and see whether they can find an algorithm to match it.

![image](https://user-images.githubusercontent.com/48352335/211331634-cc6026fe-76a5-44b1-bdd7-5c0437b1f84a.png)<br>
Source: https://ccicada.org/education/ccicada-education-modules/#Fingerprint

Colored, weighted graph:
- Minutiae are the vertices
- Color the vertices: bifurcation green, ridge ending red, ridge crossing yellow, double bifurcation blue, spurs purple, ...
- Weighted: connect the vertices (those that are connected by the same ridge) and assign a weight to the edge, namely the distance between the vertices. 
(Other approaches are: assign coordinates to the vertices, record as the weight the number of ridges crossed ...)

Debrief: What are the limitations of the matching algorithm? How can the matching algorithm be improved? 

#### Learning objectives
- Apply basic concepts of graphs when analyzing fingerprints.
- Students develop an algorithm to match fingerprints with each other (identify a given fingerprint using a fingerprint dataset).
- Inquiry-based learning; critical and logical thinking.
- Illustrate the usefulness of mathematics.

After this section, students can …
- use basic concepts of graphs within this context
- characterize fingerprints
- abstract fingerprints into a graph
- analyze fingerprints using graphs
- develop an algorithm that matches a fingerprint to a graph 
- develop an algorithm to match a given fingerprint with a fingerprint from a dataset
- have improved their critical and logical thinking

#### Attainment targets
Graphs, computational thinking, interaction between society and STEM, media literacy, privacy.