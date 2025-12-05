---
content_type: text/markdown
copyright: CC BY dwengo
description: How can we read a DNA sequence?
estimated_time: 10
hruid: org-dwengo-waisda-soc-netwerken-graaf-dna-sequencing
keywords:
- grafen
- Euleriaans pad
- DNA
- sequencing
- RNA
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
title: DNA-sequencing
version: 1
---
# DNA-sequencing

DNA and RNA are very small, complex molecules. A DNA strand has a diameter of only a few nanometers, but can be up to billions of nucleotides long. It is therefore not easy to "read" such a DNA or RNA strand. Nevertheless, scientists devised various techniques to do this for the order of nucleotides in a DNA or RNA sequence.

### Sanger sequencing

An example of a sequencing technique is Sanger sequencing. This technique uses a chemical process to read the sequence. The technique mimics the natural copying process of DNA in the cell in a test tube, but adds special versions of the A, C, G, and T nucleotides that prematurely stop the copying process. Each of these special versions of A, C, G, and T is also given a unique dye so that they are easy to distinguish from each other and from the original nucleotides.

Sanger sequencing combines the following reagents in a test tube:
- The DNA sequence you want to read (a double helix up to 1000 nucleotides long).
- A *primer*, which is a short piece of DNA that will bind to the beginning of the DNA sequence you want to read. The primer is used as a "starting point" for the copying process.
- DNA polymerase. This is an enzyme that will attach to the *primer* and from that starting point copy the DNA strand nucleotide by nucleotide. For this it uses free nucleotides from the environment.
- The nucleotides A, C, G, and T.
- The modified (colored) versions of the A, C, G, and T nucleotides (at a much lower concentration than the number of "regular" nucleotides).

By combining these substances a *polymerase chain reaction* (PCR) can be started. This reaction will copy the DNA.

The chemical process proceeds as follows:

1. The substances in the test tube are heated to a temperature at which the double helix of the DNA sequence falls apart into two single strands (denaturation).
2. The mixture is cooled again. The *primer* can then bind to the single DNA strands.
3. The temperature is then raised again. This allows the DNA polymerase to start copying the strand and thus build a new DNA strand (DNA synthesis). The enzyme uses the available nucleotides in the mixture for this, both the "regular" and the colored versions. When a "regular" nucleotide is added to the new strand, the copying process continues. If a modified nucleotide is added to the strand, the copying process stops. The dye of this nucleotide also indicates which nucleotide the sequence ended with.
4. The copying process is repeated multiple times so that there is a copy of the DNA for every possible stop position. There will thus be a strand of 1 nucleotide, of as many nucleotides as the DNA sequence, and all lengths in between. Each of these strands has a colored label at the end that indicates what the last nucleotide in that sequence is.
5. The mixture with all copies of different lengths passes, under the influence of an electric field, through a thin tube (a capillary). Smaller molecules move through the tube faster than larger ones. As a result, a sequence sorted by length comes out of the end of the tube. This process is called *capillary electrophoresis*.
6. At the end of the tube there is a detector that can detect the dye at the end of a sequence. By recording the succession of colors you can read the DNA sequence.

The technique can read DNA sequences of up to 1000 nucleotides in a precise and reliable way. Most DNA and RNA sequences, however, are much longer: they can consist of millions to billions of nucleotides. Therefore, other techniques are needed to read an entire DNA or RNA sequence. One of these techniques is **shotgun sequencing**.

### Shotgun sequencing

**Shotgun sequencing** is used to read DNA sequences longer than 1000 nucleotides. In shotgun sequencing you cut a DNA strand into random pieces that are shorter than 1000 nucleotides. You read each of those pieces using a sequencing technique for short pieces of DNA (e.g., Sanger sequencing). You do this for a number of copies of the original DNA. In the read DNA fragments you then look for overlap in order to reconstruct the original sequence.

Below you can see an example of a sequence that has been split and read multiple times.

<table style="font-family: monospace">
    <tr>
        <th></th><th>Sequence</th>
    </tr>
    <tr>
        <td>DNA strand</td><td>GTGCGAGCTTTTAGTACCCTTGATA</td>
    </tr>
    <tr>
        <td rowspan=3>Shotgun sequences 1st read</td><td>GTGC