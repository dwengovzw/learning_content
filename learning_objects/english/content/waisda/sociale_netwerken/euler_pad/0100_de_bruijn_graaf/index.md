---
content_type: text/markdown
copyright: CC BY dwengo
description: How can we represent the result of shotgun sequencing using a De Bruijn
  graph?
estimated_time: 10
hruid: org-dwengo-waisda-soc-netwerken-graaf-de-bruijn-graaf
keywords:
- grafen
- Euleriaans pad
- DNA
- sequencing
- RNA
- De Bruijn
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
title: The 'De Bruijn' graph
version: 1
---
# The "De Bruijn" graph

To reconstruct the complete DNA strand based on the pieces of DNA that are the result of shotgun sequencing, you can use a De Bruijn graph. 

Before we construct such a graph, we first convert our pieces of DNA into a list of overlapping **k-mers**. A **k-mer** is a piece of DNA k nucleotides long. If k is 3, for example, then we make a list with pieces of DNA 3 nucleotides long (3-mers).

Taking the sequence GAGCTTTTAG as an example, we can convert it into 8 overlapping 3-mers: GAG, AGC, GCT, CTT, TTT, TTT, TTA, and TAG. 

![](img/splitting_dna_into_overlapping_sequences.svg)

Based on these k-mers we build the De Bruijn graph. For that, we take each k-mer, add the prefix of length k-1 as a node to the graph, add the suffix of length k-1 as a node to the graph, and connect them with an edge.

For GAG this yields the following graph:

![](img/de_bruijn_1.svg)

In this way we add each k-mer to the graph. 

AGC

![](img/de_bruijn_2.svg)

GCT

![](img/de_bruijn_3.svg)

CTT

![](img/de_bruijn_4.svg)

TTT

![](img/de_bruijn_5.svg)

TTT

![](img/de_bruijn_6.svg)

TTA

![](img/de_bruijn_7.svg)

TAG

![](img/de_bruijn_8.svg)

We add not only the k-mers for this one subsequence (GAGCTTTTAG), but also for all the other subsequences that we have read with shotgun sequencing. By adding enough pieces of DNA to the graph, you obtain a graph that represents the structure of the entire genome. 

<div class="dwengo-content sideinfo">
<h2 class="title">Directed graphs</h2>
<div class="content">
In the Königsberg graph, the edges between the nodes had no direction. For that problem it did not matter in which direction you crossed the bridge; both directions were possible. For some problems, however, it is necessary that you can traverse the edge in only one direction. Think, for example, of a slide. Via the stairs you can go up and back down, but via the slide itself you can in principle only go down. So the stairs have two directions, the slide only one. Below you see a graph that represents the possible ways to get onto and off a slide.

<img src="img/glijbaan.svg"></img>
</div>
</div>