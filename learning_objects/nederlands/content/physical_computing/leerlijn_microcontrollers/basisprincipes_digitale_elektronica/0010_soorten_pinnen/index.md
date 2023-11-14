---
hruid: leerlijn_invoer_basisprincipes_soorten_pinnen
version: 1
language: nl
title: "Soorten pinnen"
description: "Welke pinnen bestaan er op de µC en waarvoor worden ze gebruikt?"
keywords: ["pinnen", "basisprincipes", "microcontroller", "µC", "arduino", "dwenguino"]
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
estimated_time: 2
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Soorten pinnen

## Vcc, V+, +

**Vcc** staat voor *Voltage common collector* en geeft aan dat op deze pin een positieve spanning aanwezig is. Afhankelijk van de producent krijgt de **Vcc**  pin ook andere namen zoals V+, Vdd of gewoon +. De meeste elektronische componenten hebben een **Vcc** en **GND** aansluiting. Dit zijn de twee aansluitingen waarmee je de component van stroom voorziet. De **Vcc** aansluiting wordt altijd verbonden met een draad met een positieve spanning (bv. de plus kant van een batterij). Voor verbindingen met de VCC wordt gewoonlijk een **rode draad** gebruikt. 

## GND, -

De **GND** aansluiting wordt verbonden met een draad met een neutrale spanning (bv. de min kant van een batterij ofwel 0V). Voor verbindingen met de **GND** wordt gewoonlijk een **zwarte draad** gebruikt. 

## Signaal

Afhankelijk van de component zal die één of meerdere signaalpinnen hebben. Deze pinnen worden gebruikt om informatie uit te wisselen tussen de component en de microcontroller. De naam van deze pinnen hangt af van de component die je gebruikt. Bij eenvoudige componenten met maar één signaalpin is deze informatie meestal binair. Een knop geeft bijvoorbeeld een hoog signaal (5V) op de signaalpin als die ingedrukt is. Wanneer die niet ingedrukt is, dan geeft deze een laag signaal (0V).

Complexere componenten hebben vaak meerdere signaaldraden. Het LCD-scherm dat standaard voorzien is op het Dwenguino bord heeft bijvoorbeeld 12 signaalpinnen. Hieronder zie je een overzicht van een aantal componenten en de uitleg over hun pinnen.

<table>
    <tr>
        <th>
            <strong>Component</strong>
        </th>
        <th>
            <strong>Aansturen of uitlezen</strong>
        </th>
        <th>
            <strong>Pinnen</strong>
        </th>
    </tr>
    <tr>
        <td>
            <span>Geluidsensor</span>
            <img src="img/sound.png" alt="Afbeelding geluidsensor" title="Afbeelding geluidsensor"></img>
        </td>
        <td>
            Digitaal en analoog uitlezen
        </td>
        <td>
            GND = 0V
            Vcc = 5V
            D0 = digitale uitvoer
            A0 = analoge uitvoer
        </td>
    </tr>
</table>
