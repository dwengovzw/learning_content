---
content_type: text/markdown
copyright: CC BY dwengo
description: How can we reconstruct the entire genome using a De Bruijn graph?
estimated_time: 90
hruid: org-dwengo-waisda-soc-netwerken-graaf-reconstructie
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
title: Genome reconstruction
version: 1
---
# Reconstructing the genome

When you have read enough fragments of a DNA sequence using shotgun sequencing and added them to the De Bruijn graph, you can find the complete DNA sequence by searching for the Eulerian path in the graph. In the following notebook, you will get to work with the genome of the MS2 bacteriophage. You will be given a list of fragments of the genome that were read using shotgun sequencing. In the notebook you will learn how, based on this data, you can assemble the complete genome of MS2.

[![](images/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=waisda_sociale_netwerken_dna_en "Notebook transfer learning")

<div class="dwengo-content sideinfo">
<h2 class="title">The MS2 bacteriophage</h2>
<div class="content">
The MS2 bacteriophage is a virus that attacks bacteria. It is of interest to researchers because it has a very short genome consisting of only 3569 nucleotides. This genome encodes the information for forming only four different proteins. The entire virus is therefore essentially built from four building blocks. 

The genome of the MS2 bacteriophage was the first genome that could be fully sequenced. This was done in 1976 by Walter Fiers and his team at Ghent University.
</div>
</div>