---
hruid: org-dwengo-waisda-soc-netwerken-graaf-dna-sequencing
version: 1
language: nl
title: "DNA-sequencing"
description: "Hoe kunnen we een DNA sequentie lezen?"
keywords: ["grafen","Euleriaans pad", "DNA", "sequencing", "RNA"]
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

# DNA-sequencing

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
4. Het kopieerproces wordt meerdere keren herhaalt zodat er een kopie van het DNA is voor elke mogelijke stoppositie. Er zal dus een streng zijn van 1 nucleotide, van evenveel nucleotiden als de DNA sequentie en alle lengtes tussenin. Elk van deze strengen heeft op het einde een gekleurd label dat aangeeft wat de laatste nucleotide in die sequentie is.
5. Het mengsel met alle kopieën van verschillende lengte passeert, onder de invloed van een elektrisch veld, door een dun buisje (een capillair). Kleinere moleculen bewegen sneller door het buisje dan grotere. Daardoor komt er op het einde van de buis een sequentie uit die op lengte gesorteerd is. Dit proces heet capillaire elektroforese.
6. Op het einde van de buis staat een detector die de kleurstof op het einde van de sequentie kan detecteren. Door de opeenvolging van kleuren te registeren kan je de DNA sequentie lezen.


De techniek kan DNA sequenties van maximum 1000 nucleotiden op een precieze en betrouwbare manier lezen. Toch zijn de meeste DNA en RNA sequenties veel langer, miljoenen tot miljarden nucleotiden. Daarom zijn er nog andere technieken nodig om een volledige DNA of RNA sequentie uit te lezen. Een van deze technieken is **shotgun sequencing**.

### Shotgun sequencing


**Shotgun sequencing** wordt gebruikt om DNA sequenties van meer dan 1000 nucleotiden lang te kunnen lezen. Bij shotgun sequencing knip je een dna streng in willekeurige stukken die korter zijn dan 1000 nucleotiden. Elk van die stukken lees je dan uit met een sequencing techniek voor korte stukken DNA (bv. Sanger sequencing). Dit doe je voor een aantal kopieën van het originele DNA. In de uitgelezen fragmenten DNA ga je dan op zoek naar overlap om zo de originele sequentie te kunnen reconstrueren.

Hieronder zie je een voorbeeld van een sequentie die meerdere keren is opgesplitst en uitgelezen.

<table style="font-family: monospace">
    <tr>
        <th></th><th>sequentie</th>
    </tr>
    <tr>
        <td>DNA streng</td><td>GTGCGAGCTTTTAGTACCCTTGATA</td>
    </tr>
    <tr>
        <td rowspan=3>Shotgun sequenties 1e lezing</td><td>GTGC---------------------</td>
    </tr>
    <tr>
        <td>----GAGCTTTTAG-----------</td>
    </tr>
    <tr>
        <td>--------------TACCCTTGATA</td>
    </tr>
    <tr>
        <td rowspan=3>Shotgun sequenties 2e lezing</td><td>GTGCGAGCTTTT-------------</td>
    </tr>
    <tr>
        <td>------------AGTACCCTTG---</td>
    </tr>
    <tr>
        <td>----------------------ATA</td>
    </tr>
    <tr>
        <td rowspan=3>Shotgun sequenties 2e lezing</td><td>GTGCG--------------------</td>
    </tr>
    <tr>
        <td>-----AGCTTTTAGTACCCTTGA--</td>
    </tr>
    <tr>
        <td>-----------------------TA</td>
    </tr>
</table>

In de tabel zie je dat de sequentie drie keer gelezen wordt aan de hand van shotgun sequencing. Shotgun sequencing zal de DNA streng opdelen in willekeurige stukjes en elk van die stukjes afzonderlijk inlezen. De letters in de tabel geven aan welk deel van de sequentie gelezen werd. De streepjes staan er enkel om visueel aan te tonen welk deel van de DNA streng werd ingelezen. In de praktijk weet je niet van waar het gelezen deeltje DNA komt. 

Het resultaat van bovenstaande shotgun sequencing is een lijst met korte stukjes DNA. Daarvan zie je hieronder een voorbeeld.


<table>
    <tr>
        <th>Deeltje van de sequentie</th>
    </tr>
    <tr>
        <td>GTGC<td>
    </tr>
    <tr>
        <td>GAGCTTTTAG</td>
    </tr>
    <tr>
        <td>TACCCTTGATA</td>
    </tr>
    <tr>
        <td>GTGCGAGCTTTT</td>
    </tr>
    <tr>
        <td>AGTACCCTTG</td>
    </tr>
    <tr>
        <td>ATA</td>
    </tr>
    <tr>
        <td>GTGCG</td>
    </tr>
    <tr>
        <td>AGCTTTTAGTACCCTTGA</td>
    </tr>
    <tr>
        <td>TA</td>
    </tr>
</table>

De uitdaging is nu om deze korte stukjes DNA terug samen te voegen tot de volledige DNA streng. 