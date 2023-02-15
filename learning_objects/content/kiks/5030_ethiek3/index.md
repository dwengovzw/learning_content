---
hruid: kiks_ethiek3
version: 3
language: nl
title: "Energie"
description: "Energie"
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Energie

In deze tijden van energieschaarste en klimaatverandering staan we best stil bij het feit dat AI-systemen **energie verbruiken**. Zulke systemen voeren immers miljarden berekeningen per seconde uit. Het licht uitdoen via een commando aan Siri kost meer energie dan het licht een uur laten branden. 

<div class="alert alert-box alert-success">
    Als je aan <b>Siri</b> het commando geeft om het licht uit te doen, dan wordt er meer dan één AI-systeem in gang gezet. Op het moment dat je ‘Hey Siri’ zegt, wordt het systeem achter Siri geactiveerd en wordt de gesproken opdracht opgeslagen. Deze opname wordt doorgestuurd naar een datacentrum. Achtereenvolgens wordt je spraakopdracht omgezet naar getypte tekst, wordt er bepaald welke actie er ondernomen moet worden, en wordt de vereiste instructie teruggestuurd naar je smartphone. Je smartphone geeft een gepaste instructie aan je verlichtingsinstallatie waarop tot slot het licht bij jou in de kamer uitgaat.
</div> 

Andere voorbeelden van verborgen (AI-gebaseerde) energieverbruikers zijn:
- een slimme thermostaat;
- de rijhulp in je auto die waarschuwt als je van het rijvak afwijkt; 
- een gps;
- woordsuggestie op je smartphone. 

Is het gebruik van een systeem wel nodig of zelfs gewenst? Wegen de voordelen op tegen de nadelen, in het bijzonder de energiekost en de negatieve impact op het milieu? 

Iedere keer als je iets opzoekt op het internet, een tekst automatisch laat vertalen, of suggesties krijgt op een webshop, is er een AI-systeem aan het werk dat energie verbruikt. Een constante in de meest energieverslindende toepassingen is dat ze **cloudgebaseerd** zijn. Om de AI-toepassing te kunnen **uitvoeren**, wordt er data gestuurd naar een datacentrum bestaande uit vele computers. Daar wordt de data verwerkt en teruggestuurd.<br>
Zo’n datacentrum verbruikt uiteraard heel veel energie: elektriciteit om de servers te laten werken, met als neveneffect dat ze warm worden, en een systeem om de ruimte te koelen.<br>
De datacentra wereldwijd zijn naar schatting verantwoordelijk voor 0,3 % tot 2 % van de totale uitstoot aan broeikasgassen. Er werd geschat dat ze in 2018 205 TWh aan elektriciteit verbruikten, nl. 1 % van het wereldverbruik. 

![Datacentrum](embed/datacenter.jpg "Datacentrum")
<center>A picture of a 123Net Datacenter walkway in Southfield, MI (2011). 123net, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons. https://en.m.wikipedia.org/wiki/File:123Net_Data_Center_%28DC2%29.jpg </center>
    
![Google datacenter Iowa](embed/googledatacenteriowa.jpg "Googe datacentrum Iowa")   
<center>Google Data Center, Council Bluffs Iowa. chaddavis.photography from United States, CC BY 2.0 <https://creativecommons.org/licenses/by/2.0>, via Wikimedia Commons https://commons.wikimedia.org/wiki/File:Google_Data_Center,_Council_Bluffs_Iowa_%2849062863796%29.jpg </center>

<div class="alert alert-box alert-success">
    Elke Google <b>zoekopdracht</b> verbruikt een klein beetje energie. Maar veel kleintjes maken een grote hoeveelheid en het hoeft niet gezegd dat er enorm veel zoekopdrachten plaatsvinden, miljoenen per minuut en biljoenen per jaar. Volgens Google zorgt elke zoekopdracht voor een CO<sub>2</sub> uitstoot van 0,2 g, wat per jaar zou overeenkomen met de uitstoot van het draaien van één was.
</div> 

<div class="alert alert-box alert-success">
    Als je een vraag stelt aan <b>ChatGPT</b>, dan stuurt je computer die vraag via het internet naar de servers van ChatGPT. Vervolgens gaat het AI-systeem op zoek naar het antwoord op jouw vraag. Dat antwoord wordt dan naar jouw computer gestuurd en verschijnt er op je scherm.
</div>

**Een nog grotere energiekost gaat echter naar het trainen van deze AI-systemen.** Om deze systemen te ontwikkelen, dus voordat ze gebruikt kunnen worden, worden ze getraind op aanzienlijke hoeveelheden data. Sinds de opkomst van deep learning is de hoeveelheid data gebruikt voor de training jaar na jaar gegroeid, en de hoeveelheid energie ervoor nodig dus toegenomen. 

<div class="alert alert-box alert-success">
    De <b>training van GPT-3</b> zou evenveel energie hebben gekost als nodig om 367,5 Belgische gezinnen een jaar lang van elektriciteit te voorzien (er wordt geschat dat de training van GPT-3 936 MWh heeft gevergd) en evenveel CO<sub>2</sub> hebben uitgestoten als 120 auto’s op een jaar. Bij zijn opvolger GPT-4, die er weldra aankomt, zal het nog veel meer zijn.
</div>

Maar het is niet allemaal slecht nieuws.<br>  
AI-systemen hebben hun **waarde** bv. al bewezen in de gezondheidszorg met toepassingen binnen de medische beeldvorming en met de ontwikkeling van operatierobots. 
Bovendien kunnen ze ook helpen om het klimaatprobleem aan te pakken. Wetenschappers zijn volop op zoek naar nieuwe technologische toepassingen om de hoeveelheid CO<sub>2</sub> in de atmosfeer te verminderen. Ze zoeken ook naar manieren om te kunnen omgaan met de gevolgen van de klimaatverandering. Hiertoe maken ze dankbaar gebruik van de kracht van AI-systemen die heel snel conclusies kunnen trekken gebaseerd op de waarden van een groot aantal parameters, veel meer parameters dan voor een mens werkbaar is.

Er wordt gelukkig veel geïnvesteerd in het zo energievriendelijk mogelijk maken van de datacentra. En gelukkig stijgt het energieverbuik van de datacentra niet in dezelfde mate als de vraag naar diensten van datacentra. Er is bv. de evolutie van kleinere, traditionele datacentra naar grotere, energie-efficiente cloud datacentra.<br>
Daarnaast is er ook een volledig onderzoeksdomein dat zich focust op de ontwikkeling van **zuinige computerchips**. 

**Samengevat, energieverbruik is een belangrijke maatschappelijke factor die we best in rekening brengen bij het creëren én gebruiken van AI-toepassingen. Dit zet aan het denken de volgende keer je een nieuwe vraag stelt aan ChatGPT of een tekening laat genereren door DALL·E 2.**

**Bronnen:**<br>
[https://www.nrdc.org/sites/default/files/gadget_report_r_19-07-b_13_locked.pdf](https://www.nrdc.org/sites/default/files/gadget_report_r_19-07-b_13_locked.pdf) <br>
[Data Centers on Wheels: Emissions From Computing Onboard Autonomous Vehicles](https://ieeexplore.ieee.org/document/9942310)<br>
Knack Elisa Hulstaert 15/1/2023 Steven Latré (Imec): ‘Als AI niet duurzamer wordt, is het gedoemd om te falen’<br>
Knack De gevaren van ChatGPT ’We dreigen collectief dommer te worden’ 23/1/2023 Elisa Hulstaert <br>
[How Much Energy Do Data Centers Really Use?](https://energyinnovation.org/2020/03/17/how-much-energy-do-data-centers-really-use/)<br>
[Operating on 24/7 Carbon-Free Energy by 2030.](https://sustainability.google/progress/energy/)
    
