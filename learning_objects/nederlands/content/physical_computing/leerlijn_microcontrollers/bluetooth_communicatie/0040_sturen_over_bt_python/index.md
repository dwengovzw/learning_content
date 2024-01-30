---
hruid: leerlijn_bluetooth_pc_send
version: 1
language: nl
title: "Bluetooth communicatie (computer)"
description: "Hoe stuur en ontvang je data op de Dwenguino."
keywords: ["bluetooth", "UART", "serieel", "µC"]
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

# Bluetooth communicatie: data sturen vanop de computer

Vanop de computer kan je met de volgende code makkelijk gegevens sturen naar de microcontroller.

<pre>
<code class="lang-python">

    # Importeer de serial bibliotheek.
    import serial
    import time

    # Kies de juiste seriële poort en baud rate
    serial_port = 'COM4'
    baud_rate = 9600

    # Open a serial connection
    ser = serial.Serial(serial_port, baud_rate, timeout=1)

    try:
        while True:
            # Vraag aan de gebruiker om data in te geven
            data_to_send = input("Voer data in (typ 'stop' om te stoppen): ")

            # Controleer of de gebruiker wil stoppen
            if data_to_send.lower() == 'stop':
                break

            # Schrijf de data naar de seriële poort
            ser.write(data_to_send.encode())

            # Wacht eventjes (optioneel)
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nDe gebruiker heeft het programma gestopt.")

    finally:
        # Close the serial connection
        ser.close()
        print("De Seriële verbinding is gesloten.")

</code>
</pre>