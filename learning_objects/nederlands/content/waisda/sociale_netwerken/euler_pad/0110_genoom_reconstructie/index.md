---
hruid: org-dwengo-waisda-soc-netwerken-graaf-reconstructie
version: 1
language: nl
title: "Genoom reconstructie"
description: "Hoe kunnen we aan de hand van een De Bruijn graaf het volledige genoom reconstrueren."
keywords: ["grafen","Euleriaans pad", "DNA", "sequencing", "RNA", "De Bruijn"]
content_type: "text/markdown"
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# Het genoom reconstrueren

Wanneer je voldoende deeltjes van een DNA sequentie hebt gelezen met shotgun sequencing en deze hebt toegevoegd aan de De Bruijn graaf, kan je de volledige DNA sequentie vinden door het euleriaans pad te zoeken in de graaf. In de volgende notebook ga je zelf aan de slag met het genoom van de MS2 bacteriofaag. Je krijgt een lijst van deeltjes van het genoom die gelezen zijn aan de hand van shotgun sequencing. In de notebook zal je leren hoe je op basis van deze data het volledige genoom van MS2 kan samenstellen.

[![](images/Knop.png "Knop")](https://kiks.ilabt.imec.be/hub/tmplogin?id=waisda_sociale_netwerken_euler "Notebook transfer learning")

<div class="dwengo-content sideinfo">
<h2 class="title">De MS2 bacteriofaag</h2>
<div class="content">
De MS2 bacteriofaag is een virus dat bacteriën aanvalt. Het is interessant voor onderzoekers omdat het een zeer kort genoom heeft dat bestaat uit maar 3569 nucleotiden. Dit genoom codeert de informatie voor het vormen van maar vier verschillende eiwitten. Het volledige virus is dus eigenlijk opgebouwd uit vier bouwblokken. 

Het genoom van de MS2 bacteriofaag is het eerste genoom dat volledig gesequenced kon worden. Dat gebeurde in 1976 door Walter Fiers en zijn team aan de Universiteit Gent.
</div>
</div>