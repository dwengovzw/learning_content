---
hruid: leerlijn_bluetooth_pc_requirements
version: 1
language: nl
title: "Systeemvereisten"
description: "Wat heb ik nodig om vanop de computer via Bluetooth te communiceren?"
keywords: ["bluetooth", "UART", "serieel", "computer", "Python"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16]
difficulty: 1
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Systeemvereisten

Hier veronderstellen we dat je een computer hebt met een Bluetooth verbinding en een Python3 installatie.

## Python 3

Op de computer zullen we gebruik maken van een Python programma om gegevens naar de µC te sturen en gegevens van de µC te ontvangen. Je kan Python gratis downloaden en installeren via de installer. Ga daarvoor naar (https://www.python.org/downloads/)[https://www.python.org/downloads/]. Vink tijdens het installatieproces aan dat je ook **pip** wil installeren alsook de Python editor **IDLE**. Je kan er ook voor kiezen om een andere editor te gebruiken bijvoorbeeld: Visual Studio Code of Thonny.

Om gegevens te ontvangen via Bluetooth, gebruiken we de pyserial bibliotheek. Deze kan je installeren met het commando:

<pre>
    <code class="lang-bash">pip install pyserial</code>
</pre>

Kopieer bovenstaande lijn en plak die in het Windows commandovenster. Druk daarna op enter. Je zal zien dat de pyserial bibliotheek geïnstalleerd wordt.

## Pairen van de module

Voor je op de computer gegevens kan ontvangen van een Bluetooth module, moet je die module pairen met je computer. Dit doe je zo:

* Zorg ervoor dat de Bluetooth module stroom krijgt. Hiervoor kan je de module aansluiten op de Dwenguino en de Dwenguino van stroom voorzien via de USB-kabel.
* Zoek op Windows via het startmenu naar de instelling *Bluetooth-&-apparaten*.
* Zorg ervoor dat Bluetooth aan staat.
* Zoek onder *Apparaten* naar *Apparaatinstellingen* en zet dit op *Geavanceerd*. Dit zorgt ervoor dat Windows alle Bluetooth apparaten zal weergeven.
* Klik op de knop *Voeg een Bluetooth of ander apparaat toe*.
* Klik op *Bluetooth*.
* De computer zal je vragen om de pin code van de Bluetooth module in te geven. Voor de HC-06 module is dit *1234*. Voor andere modules zijn veelvoorkomende codes: *0000*, *1111* of *0123*.
* Zoek het nummer van de COM poort waarmee je Bluetooth module verbonden is. Ga daarvoor bij de *Bluetooth-&-apparaten* instellingen naar *Meer Bluetooth instellingen*.
* Ga naar de tab *COM Poorten*.
* Zoek in de lijst de COM poort voor jou apparaat.
* Noteer via welke COM poort de Bluetooth module verbonden is.

Na deze stappen te doorlopen, ben je klaar om data te ontvangen en sturen via Bluetooth.

