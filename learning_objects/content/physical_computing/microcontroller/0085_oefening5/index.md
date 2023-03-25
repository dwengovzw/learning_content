---
hruid: pc_micro_p2_oef5
version: 3
language: nl
title: "Oefening 5"
description: "Oefening 5"
keywords: ["Microcontroller"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [12, 13, 14]
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
# Practicum 2 - Timers en Interrupts

## Oefening 5: Timer interrupts voor accurate wachttijden⚡

In deze laatste oefening gaan we ook de delay bij het wachten op de stimulus vervangen. We zullen hiervoor gebruik maken van een timer. Bovendien gaan we nu de timer koppelen aan een interrupt. Op die manier kunnen we veel preciezer de LEDs aansturen én ondertussen een animatie afspelen op het scherm om aan de gebruiker duidelijk te maken dat de countdown naar de stimulus (de LEDs) begonnnen is.


### Timer interrupts

Om een interrupt te koppelen aan de timer zullen we gebruik maken van de Output Compare units, waarover jullie meer vinden in sectie 15.6 van de datasheet. Concreet kan je in het OCRnX register (OCR van Output Compare Register) een bepaalde waarde schrijven, waarna de OCnx vlag gemanipuleerd wordt als het TCNTn register de waarde bereikt heeft. Wat er precies met de flag gebeurt (de operation mode van de compare unit) kan je zelf instellen. Neem daarvoor een kijkje in tabel 15.1 op pagina 137.


### Opdracht 5.1 - Een timer interrupt gebruiken voor het meetsysteem

Concreet zullen we net zoals in oefening 2 een timer starten, deze keer op het moment dat de wachttijd ingaat. We gebruiken de Compare Match A van **Timer 3**. De vlag OCnx wordt OC3A en het register is het OC3AR (of beter het OC3ARH en OC3ARL register aangezien het een 16-bit klok is). Daarvoor moeten we volgende stappen ondernemen:

* **Configureer nu de COM3A (Compare Operation Mode) bits om de OC3A flag hoog te zetten bij een match**.
* Om met deze flag een interrupt te genereren moeten we nu de interrupt-specifieke mask bit enablen en opnieuw een interrupt vector schrijven. Het eerste doe je in het TIMSK3 register. **Ga op in hoofdstuk 15 op zoek naar de specifieke bit die je moet zetten.**
* **Ga in de interrupt tabel kijken om te zien welke interrupt gelinkt is aan de OC3A flag en schrijf een ISR door gebruik te maken van dezelfde macro als daarnet.** De ISR zet nu de LEDs aan waardoor je zeker bent dat ze exact aangaan na de gevraagde wachttijd.
* In het programma vervang je nu het oproepen van de _delay functie door het inschakelen van de klok (zet de prescaler op een waarde != 0) én het schrijven van de gewenste waarde naar het OC3AR register. Tijdens het wachten komt er nu op de onderste rij van het LCD een letter naar keuze die heen en weer beweegt met intervallen van 50ms. Vergeet ook niet om de Timer terug uit te schakelen in de interrupt routine.

Meet nu opnieuw een aantal keer je reactietijd. Als je alles goed gedaan hebt, zijn je reactietijden ongeveer hetzelfde maar beweegt er nu een letter op het scherm tussen het indrukken van de W knop en de E knop.