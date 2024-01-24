---
hruid: leerlijn_bluetooth_pc_receive
version: 1
language: nl
title: "Bluetooth communicatie (Computer)"
description: "Hoe ontvang ik gegevens over Bluetooth via Python op de computer."
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

# Bluetooth communicatie: data ontvangen via Python

## Systeemvereisten

Hier veronderstellen we dat je een computer hebt met een Bluetooth verbinding en een Python3 installatie. Om gegevens te ontvangen via Bluetooth, gebruiken we de pyserial bibliotheek. Deze kan je installeren met het commando:

<pre>
    <code class="lang-bash">pip install pyserial</code>
</pre>

Voor je op de computer gegevens kan ontvangen van een Bluetooth module, moet je die module pairen met je computer. Dit doe je zo:

* Zorg ervoor dat de Bluetooth module stroom krijgt. Hiervoor kan je de module aansluiten op de Dwenguino en de Dwenguino van stroom voorzien via de USB-kabel.
* Zoek op Windows via het startmenu naar de instelling *Bluetooth-&-apparaten*.
* Zorg ervoor dat Bluetooth aan staat.
* Zoek onder *Apparaten* naar *Apparaatinstellingen" en zet dit op *Geavanceerd*. Dit zorgt ervoor dat Windows alle Bluetooth apparaten zal weergeven.
* Klik op de knop *Voeg een Bluetooth of ander apparaat toe*.
* Klik op *Bluetooth*.
* De computer zal je vragen om de pin code van de Bluetooth module in te geven. Voor de HC-06 module is dit *1234*. Voor andere modules zijn veelvoorkomende codes: *0000*, *1111* of *0123*.
* Zoek het nummer van de COM poort waarmee je Bluetooth module verbonden is. Ga daarvoor bij de *Bluetooth-&-apparaten* instellingen naar *Meer Bluetooth instellingen*.
* Ga naar de tab *COM Poorten*.
* Zoek in de lijst de COM poort voor jou apparaat.

## Data lezen via Python

Wanneer je alle systeemvereisten in orde hebt gebracht, kan je een Python programma schrijven die gegevens leest via Bluetooth. Je kan dit programma schrijven en uitvoeren via je favoriete code editor. Wij gebruiken hiervoor Visual Studio Code. Hieronder zie je de code die nodig is om lijnen tekst te lezen die binnenkomen over de Bluetooth verbinding.

<pre>
<code class="lang-python">

# Importeer de pyserial bibliotheek
import serial

# Configureer de seriële poort
# Deze instelling hangt af van je computer
serial_port = 'COM4'  
# Stel de baud rate in. Deze moet dezelfde zijn als in je Dwenguino programma.
baud_rate = 9600      

# Initialize serial connection
ser = serial.Serial(serial_port, baud_rate)

# Blijf lezen van de seriële poort en print de ontvangen gegevens
while True:
    print('Wachten op gegevens...')
    line = ser.readline().decode('utf-8').strip()
    print(line)

</code>
</pre>


