---
hruid: org_dwengo_gripit_hackathon_pid_regeling
version: 1
language: nl
title: "Hoe werkt een PID-regelaar?"
description: "Ontdek terugkoppeling en de P-, I- en D-termen aan de hand van de druksensor van een grijper."
keywords: ["gripit", "hackathon", "pid", "regeling", "feedback", "sensor"]
educational_goals: []
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [17, 18]
difficulty: 3
estimated_time: 30
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

# Hoe werkt een PID-regelaar?

Je hebt de sensorwaarden van de grijper bekeken. Hoe kan de grijper die metingen gebruiken om zich aan een voorwerp aan te passen? Een **regelaar met terugkoppeling** meet het resultaat, vergelijkt het met een doel en past de aansturing aan. Vergelijk dit met fietsen op een helling: je kijkt naar je snelheid en past je inspanning aan.

## Van meting naar correctie

<img src="./img/feedback.svg" alt="Regellus: de gemeten sensorwaarde y en het doel r vormen de fout e. De regelaar berekent de aansturing u voor de servo; de sensor meet opnieuw." title="Terugkoppeling van sensor naar regelaar"></img>

In de afbeelding is `r` de gewenste sensorwaarde, `y` de meting, `e` de afwijking en `u` de aansturing. De servo en grijper beïnvloeden de fysieke druk `p`; de sensor zet die om naar meting `y`. In deze grijper berekent de firmware specifiek `e = y - r`: de gemeten ADC-waarde min de doelwaarde. Andere regelaars gebruiken soms de omgekeerde afspraak; ook de richting van de aansturing moet dan aangepast worden.

De druksensor geeft een ruwe ADC-waarde in **counts**, geen kracht in newton. Bij deze sensor daalt de waarde wanneer de druk toeneemt. Voorbeeld met doel `r = 1250`:

| Meting `y` | Fout `e = y - r` | Betekenis voor deze grijper |
|---|---:|---|
| 1600 | +350 | Minder druk dan het doel; de regelaar vraagt een sluitende beweging. |
| 1250 | 0 | De meting is gelijk aan het doel. |
| 1100 | -150 | Meer druk dan het doel; de regelaar vraagt een openende beweging. |

Dit zijn illustratieve waarden, geen veilige instellingen. De aansturing is hier een **servohoeksnelheid** in graden per seconde, niet rechtstreeks een kracht. De afstandssensor wordt wel doorgestuurd, maar is niet de terugkoppeling voor deze drukregelaar.

## Drie manieren om naar de fout te kijken

Een PID-regelaar telt drie bijdragen op: `u = Kp × e + Ki × I + Kd × D`. De letters `Kp`, `Ki` en `Kd` zijn instelbare versterkingen; `I` en `D` zijn de opgebouwde fout en de verandering van de fout. De eenheid van elke bijdrage moet samen overeenkomen met die van `u`.

<img src="./img/pid_termen.svg" alt="Drie opeenvolgende foutmetingen 100, 60 en 40. P gebruikt de laatste fout, I telt de rechthoeken op en D kijkt naar de daling tussen de laatste twee." title="P, I en D bij drie foutmetingen"></img>

Stel dat de fout tijdens drie gelijke intervallen van 0,1 seconde achtereenvolgens 100, 60 en 40 counts is. De rechthoeken tonen een vereenvoudigd voorbeeld: hun breedte is telkens 0,1 s.

### P: de huidige fout

**Proportioneel** reageert op de fout van nu: `P = Kp × e`. Bij `Kp = 0,04` en `e = 40` is `P = 1,6 graden/s`. Een grotere fout geeft een grotere correctie. Te veel versterking kan echter overschieten of heen-en-weer bewegen veroorzaken; te weinig kan de reactie traag maken.

### I: de fout die zich opstapelt

De **integrale** term houdt rekening met eerdere fouten. Een digitale regelaar kan na elk interval `I = I + e × Δt` berekenen. Begin je hier bij nul, dan is na drie intervallen `I = (100 + 60 + 40) × 0,1 = 20 count·s`. De I-bijdrage is `Ki × I`: een fout die blijft bestaan kan zo meer invloed krijgen. Een negatieve fout vermindert de som.

Als de servo al aan een grens zit, kan verder opstapelen tot een te grote latere correctie leiden: dat heet *integral windup*. De voorbeeldfirmware begrenst de integraal en voorkomt verder opstapelen wanneer de fout de servo verder voorbij een snelheids- of bewegingsgrens zou duwen. Ook wist ze de geschiedenis bij een moduswisseling en in de dode zone.

### D: hoe snel de fout verandert

De **differentiële** term kijkt naar de helling: `D = (e_nieuw - e_vorig) / Δt`. Hier is dat `(40 - 60) / 0,1 = -200 count/s`. Bij een positieve `Kd` levert dit een negatieve bijdrage: de fout neemt al af, dus de correctie wordt geremd. Een hoge D-versterking kan meetruis juist sterk versterken. Voor de eerste meting is er geen vorige fout; de firmware gebruikt dan een D-bijdrage van nul.

De drie bijdragen zijn geen voorspelling van de uiteindelijke positie: het effect hangt ook af van de grijper, de sensor, de grenzen en de tijd tussen metingen.

## Van formule naar voorbeeldfirmware

Het voorbeeld `parallel_gripper_servo_with_sensors_pid` heeft `kp = 0.04`, maar `ki = 0` en `kd = 0`. **Standaard werkt dus alleen P**; de code bevat ook berekeningen voor I en D, maar die dragen niets bij zolang hun versterkingen nul zijn.

Bij `y = 1600`, `r = 1250` en een interval van 0,01 s is de fout `350` counts. P vraagt dan `0,04 × 350 = 14 graden/s`; zonder begrenzing verandert de gewenste servohoek in dat interval met `14 × 0,01 = 0,14 graad`. De firmware begrenst de snelheid en de servohoek en gebruikt de werkelijk verstreken tijd, met minstens 10 ms tussen updates. Dit is een rekenvoorbeeld, geen fysiek gemeten beweging.

Rond het doel is er een **dode zone**: bij een fout van hoogstens 10 counts in beide richtingen wordt niet bijgestuurd. Voor een voltooid sluitcommando moet de meting er 100 ms onafgebroken binnen blijven. Lukt dat niet binnen 10 seconden, dan meldt de firmware een mislukking en houdt ze de laatst aangestuurde hoek vast.

## Denk zelf mee

1. De doelwaarde blijft 1250 en de meting wordt 1300. Bereken de fout en de P-snelheid bij `kp = 0,04`. Welke richting vraagt de regelaar?
2. De fouten zijn achtereenvolgens 30 en 10 counts, met 0,1 s ertussen. Wat is de verandering per seconde? Is de fout aan het groeien of dalen?
3. Waarom is een waarde die 100 ms binnen de dode zone blijft overtuigender dan één meting binnen die zone?

**Controle:** 1. `+50` counts en `+2 graden/s`, dus sluiten. 2. `(10 - 30) / 0,1 = -200 count/s`; de fout daalt. 3. Eén meting kan toevallig binnen de zone vallen door ruis; ook 100 ms is geen garantie voor een veilige greep.

In het volgende leerobject onderzoek je de firmware en de besturing vanuit Python. Verander de versterkingen of de drukdoelwaarde niet op een echte grijper zonder begeleiding, kalibratie en een onafhankelijke manier om de voeding uit te schakelen.
