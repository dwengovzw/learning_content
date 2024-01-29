---
hruid: leerlijn_project_lijnvolger_pid_i_en_d
version: 1
language: nl
title: "PID regeling (afstellen)"
description: "Hoe programmeer ik een pid regeling."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "pid"]
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
estimated_time: 15
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# De PID regeling afstellen

In de vorige stap van dit leerpad heb je \\(\mathrm{K_p}\\) afgesteld om ervoor te zorgen dat je robot de lijn kon volgen. Je kan deze P regeling zo afstellen dat je robot de lijn volgt. Toch kunnen er situaties zijn waarbij een P regeling niet voldoende is.

## De PI regeling

Bij een lange bocht kan het bijvoorbeeld voorkomen dat de P regeling er niet voor kan zorgen dat de robot voldoende draait. Op dat moment zal de gemaakte fout steeds groter worden tot de robot van de lijn afraakt. Om hiervoor te compenseren kan je een I componentent toevoegen aan de regeling. De integraalterm zal er ook voor zorgen dat het systeem sneller zal bijsturen wanneer het systeem een fout begint te maken.

## De PID regeling

Als laatste kan je ook nog een D term toevoegen aan je regeling. De P term kijk naar hoe snel de fout aan het veranderen is. Deze kan je gebruiken om het systeem te *dempen*. Je kan deze term gebruiken om oscillaties in de P controle te voorkomen. Hoe hoger de \\(\mathrm{K_d}\\) hoe sterker het systeem wordt gedempt. 

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Probeer je PID controller nu volledig af te stellen met een P, I en D component. Probeer ook eens de basissnelheid van de motoren te verhogen. Hoe snel kan je je robot een parcours laten afleggen?
    </div>
</div>

