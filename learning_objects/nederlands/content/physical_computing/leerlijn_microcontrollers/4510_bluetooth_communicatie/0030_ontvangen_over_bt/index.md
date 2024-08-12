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

Wanneer je alle systeemvereisten in orde hebt gebracht, kan je een Python programma schrijven die gegevens leest via Bluetooth. Je kan dit programma schrijven en uitvoeren via je favoriete code editor. Wij gebruiken hiervoor Visual Studio Code. Hieronder zie je de code die nodig is om lijnen tekst die binnenkomen over de Bluetooth verbinding te lezen.

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


