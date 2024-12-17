---
hruid: org-dwengo-waisda-soc-netwerken-graaf-euler-dna
version: 1
language: nl
title: "DNA en RNA"
description: "Hoe helpt het euleriaand pad bij het lezen van DNA sequenties?"
keywords: ["grafen","Euleriaans pad", "DNA", "voorstellingen", "python"]
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

# Lezen van DNA en RNA

Door een Euleriaans pad te vinden in een graaf, kan je heel wat problemen uit de echte wereld oplossen. We zagen al hoe het het probleem van de bruggen van Koningsbergen kon oplossen. Het vinden van een euleriaans pad is echter ook nuttig in andere toepassingen.

## DNA en RNA

DNA en RNA zijn een manier van de natuur om genetische informatie voor te stellen. Dat doet het aan de hand van lange sequenties van nucleotiden. 

### DNA

DNA of Desoxyribonucleïnezuur zit in onze celkernen en bevat de informatie over hoe ons lichaam eiwitten kan maken die essentieel zijn voor het leven. Het bestaat uit vier verschillende nucleotiden: Adenine (**A**), Thymine (**T**), Cytosine (**C**) en Guanine (**G**). Deze vier nucleotiden vormen twee lange kettingen (strengen) die in een dubbele helix "opkrullen" tot DNA. Hieronder zie je een voorbeeld van een stukje van zo'n DNA sequentie die bestaat uit twee strengen.

Streng 1: A T G C C G T A
Streng 2: T A C G G C A T 

Merk op dat enkel Adenine (A) en Thymine (T) of Guanine (G) en Cytosine (C) kunnen binden met elkaar. Een A op de ene streng zal dus altijd binden met een T op de andere, idem voor G en C.

### RNA

RNA of Ribonucleïnezuur wordt door de cel gebruikt om informatie uit het DNA te kopiëren en buiten de celkern te brengen. Daar kan het RNA gebruikt worden door de cel om een eiwit te maken. RNA bestaat ook uit vier nucleotiden. Drie daarvan overlappen met DNA: Adenine (**A**), Cytosine (**C**) en Guanine (**G**). Thymine (**T**) wordt in RNA vervangen door Uracil (**U**). En RNA streng bestaat dus uit een opeenvolgen van A, C, G en U.

## Sequencing

DNA en RNA zijn zeer kleine complexe moleculen. Een DNA streng heeft een diameter van maar enkele nanometers maar kan tot miljarden nucleotiden lang zijn. Het is dus niet eenvoudig om zo'n DNA of RNA streng te "lezen". Toch bedachten wetenschappers verschillende technieken om de opeenvolging van nucleotiden in een DNA of RNA sequentie te lezen. 

### Sanger sequencing

Een voorbeeld van zo'n sequencing techniek is *Sanger sequencing*. Deze techniek zal een chemisch process gebruiken om de sequentie te kunnen lezen. De techniek bootst het natuurlijk kopieerproces van DNA in de cel na in een proefbuis maar voegt er speciale versies van de A, C, G en T nucleotiden aan toe die het kopieerproces vroegtijdig stoppen. Aan elk van deze speciale versies van A, C, G en T wordt ook een unieke kleurstof toegevoegd.

Sanger sequencing combineert de volgende stoffen in een proefbuis:
- De DNA sequentie die je wil lezen (Een dubbele helix van maximum 1000 nucleotiden lang).
- Een *primer*, dit is een kort stukje DNA dat zich zal binden aan de de voorkant van de DNA sequentie die je wil lezen. De primer wordt gebruikt als "startpunt" voor het kopieerproces.
- DNA polymerase enzym. Dit is een enzym zal zich hechten aan de *primer* en vanaf dat startpunt de DNA streng, nucleotide na nucleotide kopiëren. Daarvoor gebruikt het *vrije* nucleotiden uit de omgeving.
- De nucleotiden, A, C, G en T.
- De aangepaste versie van de A, C, G en T nucleotiden (in veel lagere concentratie dan het aantal "gewone" nucleotiden).

Door deze stoffen te combineren kan een *Polimerase chain reaction* (PCR) gestart worden. Deze reactie zal het DNA kopiëren. 

Het chemisch proces verloopt als volgt:

1. De stoffen in de proefbuis worden opgewarmd tot een temperatuur waarop de dubbele helix van de DNA sequentie uiteenvalt in twee losse strengen (denaturatie).
2. Het mengsel wordt dan weer afgekoeld zodat de *primer* zich kan hechten aan de losse DNA strengen.
3. De temperatuur wordt weer verhoogd zodat het DNA polymerase enzym de streng kan kopiëren en dus een nieuwe DNA streng kan bouwen (DNA synthese). Daarvoor gebruikt het enzym de beschikbare nucleotiden in het mengsel. Wanneer een "gewone" nucleotide wordt toegevoegd aan de nieuwe streng, dan blijft het kopieerproces doorgaan. Als een aangepaste nucleotide wordt toegevoegd aan de streng, dan stopt het kopieerproces. De kleurstof van deze nucleotide geeft ook aan met welke nucleotide de sequentie eindigt.
4. Het kopieerproces wordt meerdere keren herhaalt zodat er een kopie van het DNA is voor elke mogelijke stoppositie. Er zal dus een streng zijn van 1 nucleotide lang, van evenveel nucleotiden als de DNA sequentie en alle lengtes tussenin. Elk van deze strengen heeft op het einde een gekleurd label dat aangeeft wat de laatste nucleotide in die sequentie is.
5. Het mengsel met alle kopieën van verschillende lengte wordt dan door een dunne buis met gel gegoten. De gel zorgt ervoor dat kortere strengen sneller door de buis stromen dan langere strengen. Op het einde van de buis komen de sequenties er dus op lengte gesorteerd uit. 
6. Op het einde van de buis staat een detector die de kleurstof op het einde van de sequentie kan detecteren. Door de opeenvolging van kleuren te registeren kan je de DNA sequentie lezen.


De techniek kan DNA sequenties van maximum 1000 nucleotiden op een precieze en betrouwbare manier lezen. Toch zijn de meeste DNA en RNA sequenties veel langer, miljoenen tot miljarden nucleotiden. Daarom zijn er nog andere technieken nodig om een volledige DNA of RNA sequentie uit te lezen. Een van deze technieken is **shotgun sequencing**.

### Shotgun sequencing


