---
hruid: org_dwengo_gripit_programmeren_uploaden
version: 1
language: nl
title: "Code uploaden"
description: "Hoe zet ik een programma vanuit DwenguinoBlockly op de Halberd?"
keywords: ["upload", "uploaden", "fiche", "gripit", "halberd", "programmeren"]
educational_goals: [
    {source: Source, id: id}
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

<div class="dwengo_content fiche">
    <h1 class="title">Code uploaden</h1>
    <h2 class="subtitle">Hoe zet ik een programma vanuit DwenguinoBlockly op de Halberd?</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">1. De binaire code downloaden</h3>
            <p class="info_item_content">
                Selecteer in het menu eerst het Halberd-bord. Klik vervolgens op de knop om je programma te compileren en te downloaden. Op de afbeelding hieronder is de bordkeuze aangeduid met een blauwe rechthoek en de compileer- en downloadknop met een rode rechthoek.
            </p>
            <p class="info_item_content">
                <img src="./img/overzicht_menu.png" alt="Afbeelding van het menu van DwenguinoBlockly: de bordkeuze voor de Halberd is aangeduid met een blauwe rechthoek en de knop om code te compileren en te downloaden met een rode rechthoek." title="Op deze afbeelding duidt de blauwe rechthoek de bordkeuze aan en de rode rechthoek de compileer- en downloadknop."></img>
            </p>
            <p class="info_item_content">
                Na het klikken verschijnt er een tandwiel op de plaats van de knop. Je programma wordt dan op de server gecompileerd. Dit kan even duren, dus wacht tot het UF2-bestand automatisch wordt gedownload naar de map 'Downloads'. Dit bestand bevat de binaire code: de vertaling van je programma naar een taal die de Halberd begrijpt.
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">2. USB-kabel aansluiten</h3>
            <p class="info_item_content">
                Verbind de computer met de Halberd via de USB-kabel.
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">3. De Halberd in programmeermodus zetten</h3>
            <p class="info_item_content">
                Druk twee keer snel na elkaar op de knop op de Halberd die op de afbeelding hieronder is aangeduid. De Halberd start nu zijn UF2 USB-bootloader en verschijnt als een USB-apparaat in de Verkenner van Windows.
            </p>
            <p class="info_item_content">
                <img src="./img/halberd_board_button.png" alt="De knop op de Halberd waarmee je de USB-bootloader start." title="Druk twee keer snel na elkaar op deze knop om de USB-bootloader te starten."></img>
            </p>
            <p class="info_item_content">
                Druk je slechts een keer op deze knop, dan reset de Halberd en start het programma dat erop staat opnieuw vanaf het begin.
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">4. Bestand overzetten</h3>
            <p class="info_item_content">
                Open de USB-schijf met de naam 'HALBERD' in de Verkenner van Windows. Sleep het gedownloade UF2-bestand uit de map 'Downloads' naar deze USB-schijf.
            </p>
            <p class="info_item_content">
                <img src="./img/Halberd_in_verkenner.png" alt="De USB-schijf HALBERD in de Verkenner van Windows." title="De USB-schijf HALBERD in de Verkenner van Windows."></img>
            </p>
            <p class="info_item_content">
                Soms verschijnt er daarna een foutmelding van Windows omdat de verbinding met de Halberd onverwacht wegvalt. Dat is normaal: de Halberd start opnieuw op om je programma uit te voeren. Je mag deze foutmelding gewoon wegklikken.
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">5. Het programma uitvoeren</h3>
            <p class="info_item_content">
                Zodra het UF2-bestand is overgezet, start de Halberd automatisch opnieuw op en voert hij je programma uit.
            </p>
        </div>
    </div>
</div>
