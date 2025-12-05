---
content_type: text/markdown
copyright: CC BY dwengo
description: How does the Eulerian path help in reading DNA sequences?
estimated_time: 5
hruid: org-dwengo-waisda-soc-netwerken-graaf-euler-dna
keywords:
- grafen
- Euleriaans pad
- DNA
- voorstellingen
- python
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
title: DNA and RNA
version: 1
---
# Reading DNA and RNA

By finding an Eulerian path in a graph, you can solve many real-world problems. We already saw how it could solve the problem of the bridges of Königsberg. However, finding an Eulerian path is also useful in other applications, such as in reading DNA and RNA.
DNA and RNA are a way for nature to represent genetic information. It does so by means of long sequences of nucleotides. 

### DNA

DNA or deoxyribonucleic acid is found in our cell nuclei and contains the information on how our bodies can make proteins that are essential for life. It consists of four different nucleotides: Adenine (**A**), Thymine (**T**), Cytosine (**C**), and Guanine (**G**). These four nucleotides form two long chains (strands) that "curl up" into a double helix to become DNA (see image). 

![](images/DNA_Double_Helix.png)

Below you can see an example of a segment of such a DNA sequence that consists of two strands.

Strand 1: A T G C C G T A

Strand 2: T A C G G C A T 

Note that only Adenine (A) and Thymine (T), or Guanine (G) and Cytosine (C), can bind to each other. An A on one strand will therefore always bind with a T on the other, and similarly for G and C.

### RNA

RNA or ribonucleic acid is used by the cell to copy information from the DNA and bring it out of the nucleus. There, the RNA can be used by the cell to make a protein. RNA also consists of four nucleotides. Three of them overlap with DNA: Adenine (**A**), Cytosine (**C**), and Guanine (**G**). Thymine (**T**) is replaced in RNA by Uracil (**U**). RNA therefore consists of a sequence of A, C, G, and U.