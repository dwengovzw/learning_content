---
hruid: org-dwengo-waisda-rl-agent-trainen-pong
version: 1
language: nl
title: "Pong"
description: "Versterkend leren toegepast op Pong"
keywords: ["AI", "reïnforcement learning", "versterkend leren", "q-learning", "q-tabel", "exploratie", "exploitatie"]
content_type: "text/markdown"
estimated_time: 15
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# Pong

In dit leerpad zag je hoe je een worm kon trainen om te kruipen met behulp van versterkend leren. Versterkend leren kan in heel wat contexten toegepast worden. Denk terug aan het Pong spelletje uit het vorige leerpad. Ook voor dat spel kunnen we een agent trainen. Die agent zal dan proberen om het spel te spelen. 

Hieronder kan je een agent trainen om het Pong spel te spelen. Pas daarvoor, net als bij de worm, de parameters van het trainingsproces aan tot je een goed resultaat krijgt. Volg onderstaande instructies.

1. Stel de parameters in van het leerproces.
2. Druk op de **Train** knop. De AI-agent zal nu proberen te leren om het spel te spelen. Daarvoor speelt deze tegen een optimale speler die nooit fouten maakt. Het leren verloopt achter de schermen, je ziet dus niet hoe dat verloopt.
3. Bekijk de prestaties. Wanneer de agent klaar is met leren zie je die een spel spelen tegen de optimale speler. De AI-agent speelt links, de optimale speler rechts. 
4. Herhaal stappen 1, 2 en 3 tot de AI-agent goed presteert tegen de optimale speler.
5. Daag zelf de AI-agent uit. Wanneer je denkt dat de AI-agent goed genoeg is, kan je zelf tegen de agent spelen. Druk daarvoor op de **Speel tegen de AI** knop. 

<iframe src="https://dwengo.org/pong" title="Voorbeeld van een convolutie" width="720px" height="800px"></iframe>

<div class="dwengo-content sideinfo">
<h2 class="title">Versterkend leren en kernfusie</h2>
<div class="content">
<p>Bij kernfusie moet hete plasma van meer dan 150 miljoen graden Celsius in de lucht gehouden worden met elektromagneten. Deze magneten moeten op elk moment het juiste magnetisch veld genereren om de plasma in de lucht te houden. Daarvoor moeten complexe controlesignalen naar de magneten gestuurd worden. Jonas Degrave, onderzoeker bij Google Deepmind en alumnus van het AI en robotica lab van de UGent, ontwikkelde zo'n controlesysteem dat gebruik maakt van versterkend leren<sup>1</sup>. Zijn werk publiceerde hij in het tijdschrift Nature.</p>
<img src="img/fusion.png"></img>  
<p>1. Degrave, Jonas, et al. "Magnetic control of tokamak plasmas through deep reinforcement learning." Nature 602.7897 (2022): 414-419.>
</div>
</div>