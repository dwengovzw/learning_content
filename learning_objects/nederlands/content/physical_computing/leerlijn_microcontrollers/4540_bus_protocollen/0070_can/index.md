---
hruid: org-dwengo-pc-bus-protocollen-introductie-can
version: 1
language: nl
title: "CAN bus"
description: "Wat zijn bus protocollen en waarvoor dienen ze?"
keywords: ["dwenguino", "microcontroller", "bus", "communicatie", "i2c", "spi", "uart", "can"]
content_type: "text/markdown"
estimated_time: 35
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

# CAN bus

CAN staat voor *Controlled area network* en werd in 1986 uitgebracht door het duitse bedrijf Bosch. CAN werd specifiek ontworpen voor de communicatie tussen geïntegreerde schakelingen in auto's. CAN bus is een zeer betrouwbaar protocol omdat het moet voldoen aan heel wat veiligheidsvoorschriften. 

## Bedrading

De CAN bus maakt net als I²C gebruik van twee draden voor de communicatie. De draden krijgen in CAN de namen <code class="lang-cpp">CANH</code> (CAN high) en <code class="lang-cpp">CANL</code> (CAN low). Alle apparaten zijn zowel met <code class="lang-cpp">CANH</code> als <code class="lang-cpp">CANL</code> verbonden.  Hieronder zie je een voorbeeld van vier apparaten die aangesloten zijn op een CAN bus. De lijnen worden op het einde aan elkaar gekoppeld met een weerstand om refelecties in het signaal te vermijden.

![Can bus voorbeeld](images/can.svg)

## Werking

CAN maakt, net als I²C gebruik van twee draden voor de communicatie. Maar in tegenstelling tot I²C is can een **multi-master** protocol. Alle apparaten op de bus kunnen dus het initiatief nemen om te sturen. Dit kan ervoor zorgen dat er botsingen zijn op de bus wanneer twee apparaten tegelijk gegevens willen sturen. Om deze botsingen op te lossen, krijgen apparaten een ID nummer. Apparaten met een lager ID nummer, krijgen voorang op apparaten met een hoger ID nummer.

Om gegevens te sturen worden zowel de <code class="lang-cpp">CANH</code> en <code class="lang-cpp">CANL</code> draden gebruikt. Het is dus niet mogelijk om op hetzelfde moment in twee richtingen te sturen. Het gaat hier dus over een **half-duplex** protocol. 

Omdat het bij CAN belangrijk is dat signalen correct ontvangen kunnen worden, zijn er in het CAN protocol specifieke mechanismen ingebouwd om het protocol betrouwbaarder te maken. Zo maakt CAN gebruik van differentiële signalen en wordt er aan de gegevens een cyclic redundancy check (CRC) toegevoegd. 

### Differentiële signalen.

In zowel I²C als SPI worden de bits die verstuurd moeten worden op de bus omgezet naar spanningen van 5V of 0V. 5V komt overeen met bitwaarde 1, 0V met bitwaarde 0. In een wagen wordt de CAN bus echter bloodgesteld aan ruis. Verschillende componenten in de wagen, zoals vibraties van de motor of magnetische velden opgewekt door de speakers, kunnen ruis veroorzaken. Deze ruis kan ervoor zorgen dat het voltage op de bus afwijkt van de verstuurde waarde. Hierdoor kunnen fouten optreden in de communicatie. Hieronder zie je een voorbeeld van een perfecte blokgolf zonder ruis.

![Gewone blokgolf](images/square_wave.svg)

Merk op dat zo'n signaal in de praktijk nooit voorkomt. Er zal altijd wat ruis zitten op het signaal. Daarom zal de microcontroller niet kijken of het signaal exact 5V of 0V is maar zal een waarde boven de 2.5V gelezen worden als een 1 en een waarde onder 2.5V als een 0. Wanneer er nu echter veel ruis zit op het signaal, is het mogelijk dat er een verkeerde waarde gelezen wordt. Op onderstaande afbeelding kan je zien dat er tussen 4 en 8 ms zo veel ruis is dat het signaal op sommige plaatsen de grens van 2.5V overschrijdt. 

![Blokgolf met ruis](images/square_noise.svg)


In het CAN protocol wordt een minder ruisgevoelig systeem toegepast om bits om te zetten naar voltages. Dat systeem werkt met differentiële signalen. Daarvoor plaatst de CAN controller een tegenovergesteld signaal op <code class="lang-cpp">CANH</code> en <code class="lang-cpp">CANL</code>. Hieronder zie je een voorbeeld van zo'n signaal. 

![Differentieel signaal CAN bus](images/no_noise.svg)

Het eigenlijke signaal bekom je door het signaal op <code class="lang-cpp">CANL</code> af te trekken van <code class="lang-cpp">CANH</code>.

Door de twee signalen van elkaar af te trekken, kan je ruis op de lijn uit het signaal verwijderen. Meestal zal de ruis op de <code class="lang-cpp">CANH</code> en <code class="lang-cpp">CANL</code> lijnen gelijkaardig zijn omdat deze draden vlak naast elkaar liggen. Door het signaal op de twee lijnen van elkaar af te trekken, trek je ook de ruis van zichzelf af. Hieronder zie je daar een voorbeeld van:

![Ruis op differentieel signaal](images/noise.svg)

Wiskundig krijg je dan 
\\[\text{CANH} + \text{ruis} -(\text{CANL} + \text{ruis}) = \text{CANH} + \text{ruis} - \text{CANL} - \text{ruis} = \text{CANH} - \text{CANL}  \\]
Je ziet dus dat je de ruis van zichzelf aftrekt waardoor het verdwijnt. 

<div class="dwengo-content sideinfo">
<h2 class="title">Ethernet</h2>
<div class="content">

Je hebt waarschijnlijk wel al eens een ethernet kabel gezien. Met deze kabel koppel je je computer aan het internet.

<img src="images/ethernet_connector.jpg" alt="Voorbeeld van een ehternet connector"></img>

 Wanneer je de connector van deze kabel bekijkt, zie je acht draden. Dit zijn eigenlijk een combinatie van vier **twisted pairs**, letterlijk rond elkaar gedraaide paren. Elk van deze paren kan net als bij CAN gebruikt worden om data te versturen. Ethernet gebruikt net als CAN de techniek met differentiële signalen om ruis te beperken.


</div>
</div>

### Cyclic redundancy check (CRC)

Apparaten die verbonden zijn met de CAN bus zullen volgens een bepaalde structuur gegevens versturen. Deze structuur noemen we het data frame. Het data frame bestaat uit verschillende soorten informatie. Eerst komen er 20 bits die informatie geven over het data frame zelf. Zo bevatten ze de lengte van de data die zal komen en de prioriteit ven het bericht. Daarna volgen 0 tot 64 bytes aan data. Na de data volgen 28 bits die het bericht afsluiten. 15 van deze 28 bits bevatten de cyclic redundancy check (CRC). 

De CRC wordt bij het versturen berekend op basis van de data die verstuurd zal worden. De verzender zal de data delen door een vooraf afgesproken waarde. Deze gehele deling levert dan een rest op. Deze rest is de CRC en wordt meegestuurd met de data naar de ontvanger. De ontvanger zal de ontvangen data ook delen door de vooraf afgesproken waarde en controleren of de rest overeenkomt met de CRC in het data frame. Als dat zo is, is de kans groot dat de data correct ontvangen werd. Als de CRC niet overeenkomt met de bekomen rest, dan weet de ontvanger dat er een fout is opgetreden in de communicatie. Deze kan de informatie dan opnieuw opvragen aan de verzender.

## Op de microcontroller

De Dwenguino is niet ontworpen om te communiceren via een CAN bus. Er is geen hardware voorzien die de juiste signalen kan genereren. Daarom is het nodig om gebruik te maken van een CAN bus module zoals de MCP2525 en MCP2551. Die module kan je via SPI aansluiten op de microcontroller. Meer informatie kan je vinden op [deze github pagina](https://github.com/autowp/arduino-mcp2515).

