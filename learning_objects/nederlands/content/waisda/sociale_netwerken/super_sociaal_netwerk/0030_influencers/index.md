---
hruid: org-dwengo-waisda-sociale-netwerken-super-sociaal-netwerk-influencers
version: 1
language: nl
title: "Influencers"
description: "Hoe detecteer ik welke mensen veel invloed hebben binnen het netwerk."
keywords: ["Sociale netwerken", "grafen", "AI", "Unsupervised learning", "influencers", ]
content_type: "text/markdown"
estimated_time: 2
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# Influencers

Er zijn verschillende maten om te bepalen wie er meer of minder invloed heeft binnen het sociale netwerk. Een eenvoudige methode is om te kijken naar het aantal connecties met anderen die een persoon heeft. Heeft die veel connecties, is die invloedrijker. 

## Graadcentraliteit

Hoeveel invloed een persoon heeft in een netwerk noemen we de *centraliteit*. Het woord verwijst naar hoe "centraal" een persoon staat binnen het netwerk. Er bestaan verschillenden manieren om de centraliteit te bepalen. Eén van die manieren is de **graadcentraliteit**. De graadcentraliteit van een knoop is gelijk aan het aantal bogen die uit die knoop vertrekt (de graad van die knoop). Hieronder zie je voor elke knoop in ons sociale netwerkje wat de graad van die knoop is.

!["Onder elke persoon in ons sociaal netwerkje staat de graad van die knoop."](img/voorbeeld_sociale_graaf_graadcentraliteit.svg)

Willen we weten wie het meeste invloed heeft binnen ons sociaal netwerk, dan kijken we welke knoop de hoogste graad heeft. In dit geval is dat Ren. Komt dit overeen met jou idee van wie de meest invloedrijke persoon is binnen het netwerk?

<div class="dwengo-content sideinfo">
<h2 class="title">Eigenwaardecentraliteit</h2>
<div class="content">
<p>
Naast graadcentraliteit zijn er nog heel wat andere manieren om de centraliteit van een persoon te bepalen. Eén zo'n manier is eigenwaardencentraliteit. Eigenwaardecentraliteit kijkt niet enkel naar hoeveel connecties een persoon heeft maar ook hoe waardevol deze connecties zijn. Als je bevriend bent met mensen die zelf veel vrienden hebben zal je immers meer invloed hebben dan wanneer je bevriend bent met "onpopulaire" mensen met weinig vrienden.
</p>
<p>
Je eigen invloed hangt in dit geval af van de invloed van de personen waarmee je verbonden bent. Let wel, de invloed van de personen waarmee je verbonden bent hangt ook af van je eigen invloed. Dit is een voorbeeld van een eigenwaardenprobleem. Heel wat problemen vallen onder de categorie van eigenwaardenproblemen. Denk bijvoorbeeld aan Google PageRank. Dit is het algoritme van Google die websites op het internet rangschikt volgens hun belang. 
</p>
</div>
</div>