---
available: true
content_type: text/markdown
copyright: dwengo
description: Capteur sonar
difficulty: 3
estimated_time: 1
hruid: ct03_18
language: fr
licence: dwengo
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
target_ages:
- 12
- 13
- 14
teacher_exclusive: true
title: "Capteur \xE0 ultrasons (1)"
version: 3
---
# Fonctionnement du capteur sonar

Un capteur sonar mesure la distance à un objet. Pour cela, il utilise des ultrasons qui sont réfléchis par les objets. En mesurant le temps entre l’émission et la réception du signal sonore, on peut, à l’aide d’une formule, calculer très précisément la distance à l’objet. Dans ce cas, vos élèves réfléchissent au fonctionnement du capteur sonar à partir des principes de la pensée computationnelle.

**Public cible:** Premier degré, voies A et B

**Discipline:** ...

**Prérequis:**<br>
* Les élèves connaissent le concept de *vitesse*
* Éventuellement, les élèves savent que la vitesse est un rapport entre la distance et la durée

Un **déroulement** possible de l’étude de cas est le suivant:<br><br>

*Phase 1: leçon sur l’écholocalisation*<br>
<ul>
    <li>Les chauves-souris détectent des proies et des obstacles grâce à l’écholocalisation. La chauve-souris émet un signal sonore. Celui-ci est réfléchi par l’objet, puis la chauve-souris le reçoit à nouveau.
    <li>Les scientifiques s’en sont inspirés pour concevoir un composant électronique permettant de déterminer automatiquement la distance à un objet.</li>
</ul>

*Phase 2: le sonar fonctionne exactement de la même manière*<br>
<ul>
    <li>Vous expliquez aux élèves que le sonar fonctionne selon le principe de l’écholocalisation.
    <li>Si les élèves le comprennent, ils devraient, par reconnaissance de motifs, pouvoir conclure que le sonar devra émettre et recevoir un signal sonore (ultrasonore).
    <li>Les élèves complètent le schéma avec les concepts de base.</li>
</ul>

*Phase 3: formule*<br>
<ul>
    <li>La vitesse du son est d’environ 340 mètres par seconde.
    <li>Calculer la distance pour une durée donnée entre l’émission et la réception du signal. Les élèves utilisent les unités correctes pour le temps et la distance.
    <li>Les élèves établissent une formule pour calculer la distance, qui pourrait être programmée dans l’unité de calcul du système numérique.
    <li>Les élèves complètent davantage le schéma avec les concepts de base.</li>
</ul>

![ct-schema](@learning-object/m_ct03_18/nl/3)