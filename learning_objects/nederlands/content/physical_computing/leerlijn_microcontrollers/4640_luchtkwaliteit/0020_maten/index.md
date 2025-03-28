---
hruid: org-dwengo-pc-luchtkwaliteit-maten
version: 1
language: nl
title: "Maten voor luchtkwaliteit"
description: "Hoe kan ik de luchtkwaliteit meten?"
keywords: ["dwenguino", "microcontroller", "wifi", "i2c", "webserver", "internet", "co2", "luchtkwaliteit"]
content_type: "text/markdown"
estimated_time: 8
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-digitale-competenties-en-mediawijsheid',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-algebra-analyse',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-redeneren',

]
copyright: "CC BY dwengo"
target_ages: [16, 17, 18]
teacher_exclusive: False
---


## Maten voor luchtkwaliteit

Er zijn heel wat factoren die de luchtkwaliteit in een ruimte kunnen beïnvloeden. Deze worden opgedeeld in drie grote groepen:

* **Chemische parameters**: De lucht bevat verschillende chemische stoffen die, in te hoge concentraties, een negatief gezondheidseffect kunnen hebben. Zo zal een te hoog CO<sub>2</sub> percentage in de lucht hoofdpijn, duizeligheid en kortademigheid veroorzaken. Andere volatiele organische stoffen (VOS) zoals ethanol of aceton kunnen vrijkomen uit bouwmaterialen en de lucht vervuilen. Deze VOS kunnen misselijkheid en hardkloppingen veroorzaken.
* **Fysische parameters**: Parameters zoals temperatuur en luchtvochtigheid hebben ook een belangrijke invloed op de kwaliteit van de binnenlucht. Een te hoge luchtvochtigheid kan bijvoorbeeld concentratieproblemen veroorzaken.
* **Biologische parameters**: In de lucht komen allerlei schimmels, virussen en bacteriën voor. Deze kunnen ons besmetten via onze luchtwegen.

Zowel de chemische als fysische parameters van de luchtkwaliteit kunnen we makkelijk meten aan de hand van sensoren. Biologische parameters kunnen we niet eenvoudig meten. Gelukkig kunnen we het risico op een besmetting met een virus of bacterie beperken door ervoor te zorgen dat een ruimte voldoende geventileerd wordt. Om te bepalen hoeveel er geventileerd moet worden, kunnen we het CO<sub>2</sub> gehalte in de lucht gebruiken. 

In dit leerpad gebruiken we twee sensoren om de volgende parameters te meten:
* Het <strong>CO<sub>2</sub></strong> gehalte in ppm (deeltjes per miljoen).
* De hoeveelheid <strong>volatiele organische stoffen (VOS)</strong>, dit is een combinatie van de concentratie van de stoffen: ethanol, waterstof, aceton, CO en tolueen.
* De **air quality index (AQI)**: Dit is een maat dat berekend wordt op basis van van de gemeten concentraties van giftige stoffen in de lucht. De sensor die we gebruiken geeft een waarde voor de luchtkwaliteit terug van 1 tot en met 5. Met 1 een perfecte luchtkwaliteit en 5 een zeer ongezonde luchtkwaliteit. 
* De **temperatuur**.
* De **luchtvochtigheid**.

Voor het meten van temperatuur, luchtvochtigheid en CO<sub>2</sub> gehalte, maken we gebruik van de SCD40 CO<sub>2</sub> sensor. Voor het meten van VOS en AQI, gebruiken we een ENS160 sensor.


<div class="dwengo-content sideinfo">
    <h2 class="title">Air Quality Index (AQI)</h2>
    <div class="content">
        <p>De Air Quality Index (AQI) is een overkoepelende maat voor hoe goed of hoe slecht de luchtkwaliteit is. Deze wordt berekend op basis van verschillende metingen. In onderstaande tabel zie je een interpretatie van die waarde.</p>
        <table>
            <tr style="background-color:gray">
                <th>Waarde</th>
                <th>Beschrijving</th>
                <th>Advies</th>
                <th>Maximale blootstellingstijd</th>
            </tr>
            <tr style="background-color:IndianRed">
                <td>5</td>
                <td>Ongezond</td>
                <td>Intense ventilatie nodig.</td>
                <td>Aantal uren</td>
            </tr>
            <tr style="background-color:orange">
                <td>4</td>
                <td>Slecht</td>
                <td>Verhoog de ventilatie en ga op zoek naar de bron.</td>
                <td>&lt; 1 maand</td>
            </tr>
            <tr style="background-color:gold">
                <td>3</td>
                <td>Matig</td>
                <td>Verhoog de ventilatie en ga op zoek naar de bron.</td>
                <td>&lt; 12 maand</td>
            </tr>
            <tr style="background-color:lightgreen">
                <td>2</td>
                <td>Goed</td>
                <td>Blijf voldoende ventileren.</td>
                <td>Geen limiet</td>
            </tr>
            <tr style="background-color:LightSkyBlue">
                <td>1</td>
                <td>Perfect</td>
                <td>Geen actie nodig.</td>
                <td>Geen limiet</td>
            </tr>
        </table>
    </div>
</div>






