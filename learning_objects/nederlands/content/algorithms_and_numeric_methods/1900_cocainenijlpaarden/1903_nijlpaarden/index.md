---
hruid: anm_1903
version: 1
language: nl
title: "Populatiegroei wiskundig modelleren a.d.h.v. Lesliematrix"
description: "Populatiegroei wiskundig modelleren a.d.h.v. Lesliematrix"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# Populatiegroei wiskundig modelleren a.d.h.v. Lesliematrix

Het vorige model geeft aan in welke mate de populatie verder zou kunnen aangroeien. Het geeft echter niet weer hoeveel mannelijke en hoeveel vrouwelijke nijlpaarden er zijn, en hoe bijvoorbeeld de verhouding jonge versus oude dieren is. 

Om dit te bekijken kan je een wiskundig model maken dat gebaseerd is op een *Lesliematrix*.

## Lesliematrix: voorbeeld
Vertrek van het volgende probleem:

Stel dat je een populatie dieren hebt van een soort die maximum twee jaar oud wordt.<br>
60 % van de nuljarigen wordt 1 jaar, en 40 % van de eenjarigen wordt 2 jaar. In het tweede levensjaar krijgen de vrouwtjes gemiddeld 5 nakomelingen en in het derde levensjaar krijgen ze er gemiddeld 3. <br>
Momenteel zijn er 204 dieren in hun eerste levensjaar, 60 dieren zijn een jaar oud en 36 zijn in hun derde levensjaar.<br>
Bekijk deze populatie dieren binnen 5 jaar.

De evolutie van deze populatie kan je modelleren a.d.h.v. een graaf:
![graaf](embed/graafvb.png)

Vervolgens kan je deze graaf vertalen naar een matrix:
![Lesliematrix](embed/leslievb.png)

Een dergelijke matrix wordt een Lesliematrix genoemd. Het is een speciaal geval van een zogenaamde *overgangsmatrix*.

Ook de huidige populatie kan je voorstellen m.b.v. een matrix, namelijk, de volgende kolommatrix:
![bevolkingsmatrix](embed/bevolkingsmatrixvb.png)

Wanneer je de Lesliematrix vermenigvuldigt met deze kolommatrix bekom je het aantal nul-, een- en tweejarige dieren na een periode van een jaar:
![matrices vermenigvuldigen](embed/vermenigvuldigenvb.png)

Inderdaad:
![uitleg](embed/uitlegvb.png)

Voor een periode van twee jaar betekent dat:
![tweejaar](embed/tweejaarvb.png)

Dus voor een periode van vijf jaar:
![algemeen](embed/algemeenvb.png)

Voor het rekenwerk kan je ook gebruikmaken van Python. Open daarvoor de tweede notebook. 

[![](embed/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=6100 "Cocaïnenijlpaarden notebooks")


## Lesliematrix betreffende de nijlpaarden

**Informatie i.v.m. maximale leeftijd en vruchtbaarheid [1]**

<img width="877" height="723" alt="tabel1" src="https://github.com/user-attachments/assets/20f440d0-fd1f-422f-8f31-a7d822a2ab36" />

**Overlevingscijfers [1]**

Gebruik de derde notebook om de nijpaardenpopulatie te modelleren m.b.v. een Lesliematrix.

Denk eerst na over hoe je de Lesliematrix die je nodig hebt om de nijlpaardenpopulatie te modelleren, zal opstellen.  

[![](embed/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=6100 "Cocaïnenijlpaarden notebooks")

### Bronnen
[1] Subalusky, A.L., Sethi, S.A., Anderson, E.P. et al. Rapid population growth and high management costs have created a narrow window for control of introduced hippos in Colombia. *Sci Rep 13*, 6193 (2023). https://doi.org/10.1038/s41598-023-33028-y


