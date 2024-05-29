---
hruid: leerlijn_fiches_arduino_lcd
version: 1
language: nl
title: "Lcd-scherm"
description: "Tekst laten verschijnen op het lcd-scherm"
keywords: ["lcd", "lcd-scherm", "fiche", "arduino"]
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

<div class="dwengo_content fiche">
    <h1 class="title">Lcd-scherm</h1>
    <h2 class="subtitle">Tekst weergeven</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
            <p class="info_item_content">
                <img src="img/dwenguino_lcd.png" alt="Een afbeelding van een lcd-scherm." title="Een afbeelding een lcd-scherm."></img>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Type</h3>
            <p class="info_item_content">
                Uitvoer, digitale actuator 
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Pinnen</h3>
            <p class="info_item_content">
                <table>
                    <tr><td>RS</td><td>Een <em>register select</em> pin die controleert naar waar in het geheugen van het LCD je de date schrijft.</td></tr>
                    <tr><td>R/W</td><td>Een <em>Read/Write</em> pin die lees- of schrijfmodus selecteert.</td></tr>
                    <tr><td>Enable</td><td>Een <em>Enable</em> pin die het mogelijk maakt om naar de registers te schrijven.</td></tr>
                    <tr><td>D0 - D7</td><td>8 datapinnen. De staat van deze pinnen zijn de bits die je naar een register schrijft (in schrijfmodus) of de waarden die je leest (in leesmodus).</td></tr>
                    <tr><td>VCC</td><td>De 5 V-voeding, soms ook aangeduid met een +.</td></tr>
                    <tr><td>GND</td><td>De referentiespanning of de grond, soms ook aangeduid met een -.</td></tr>
                </table>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
                Het lcd-scherm kan tekst weergeven. Hiermee kan bijvoorbeeld een boodschap worden meegedeeld.<br>
                Op het lcd-scherm van de dwenguino passen maximaal 32 karakters, zoals letters of cijfers, verspreid over twee regels. Je kan dus 16 karakters per regel tonen.<br>
                <br>
                De helderheid van het scherm is aanpasbaar. Je kan dit zelf regelen door aan de gele schroef te draaien (zie figuur) met een schroevendraaier, terwijl het lcd-scherm aanstaat.
            </p>
        </div>
        <div class="example_item item">
            <h3 class="example_item_title">Voorbeeld: Laat "Hallo robot" op het lcd-scherm verschijnen.</h3>
            <p class="example_item_content">
<pre>
<code class="language-cpp">
    
// include the library code:

#include <LiquidCrystal.h>


// initialize the library by associating any needed LCD interface pin

// with the arduino pin number it is connected to

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);


void setup() {

  // set up the LCD's number of columns and rows:

  lcd.begin(16, 2);

  // Print a message to the LCD.

  lcd.print("hello, world!");

}


void loop() {

  // set the cursor to column 0, line 1

  // (note: line 1 is the second row, since counting begins with 0):

  lcd.setCursor(0, 1);

  // print the number of seconds since reset:

  lcd.print(millis() / 1000);

}
</code>
</pre> 
            </p>
        </div>
    </div>
</div>



