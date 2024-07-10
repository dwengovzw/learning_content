---
hruid: leerlijn_fiches_arduino_ledmatrix
version: 1
language: nl
title: "Ledmatrix"
description: "Figuren maken met de ledmatrix"
keywords: ["led", "ledmatrix", "fiche", "arduino"]
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
    <h1 class="title">Led-matrix</h1>
    <h2 class="subtitle">Figuren tonen op de led-matrix</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
            <p class="info_item_content">
                <img src="img/ledmatrix.png" alt="Een afbeelding van een ledmatrix." title="Een afbeelding van het ledmatrix."></img>
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
                    <tr><td>VCC</td><td>De 5 V-voeding, soms ook aangeduid met een +.</td></tr>
                    <tr><td>GND</td><td>De referentiespanning of de grond, soms ook aangeduid met een -.</td></tr>
                    <tr><td>D</td><td>Een digitale pin die een binair signaal doorgeeft tussen het moederbord en de led-matrix. Het geeft aan welke leds al dan niet moeten branden.</td></tr>
                    <tr><td>CS</td><td>De chip select pin geeft aan of de binnenkomende data voor de beoogde chip is of niet.</td></tr>
                    <tr><td>CLK</td><td>De klok-pin (clock pin) zorgt ervoor dat het data- en klok signaal afzonderlijk kunnen ontvangen worden. Hierdoor zijn de leds niet onderhevig aan onderbrekingen door andere processen.</td></tr>
                </table>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
                De led-matrix is een vierkante 8x8 matrix met 64 leds in een vaste kleur (rood). De matrix is ideaal om bepaalde patronen te laten oplichten, zoals een oog of een mond van de robot of een ander symbool. Je kan de matrices ook met elkaar verbinden (maximaal 4), als je meerdere matrices tegelijk wil gebruiken. Je kan programmeren welke leds er tegelijk moeten oplichten.
            </p>
        </div>
        <div class="example_item item">
            <h3 class="example_item_title">Voorbeeld: led laten branden als sonar-sensor object detecteert tot een afstand van 100cm.</h3>
            <p class="example_item_content">
<pre>
<code class="language-cpp">
    
  // 2-dimensional array of row pin numbers:
  const int row[8] = {
    2, 7, 19, 5, 13, 18, 12, 16
  };

  // 2-dimensional array of column pin numbers:
  const int col[8] = {
    6, 11, 10, 3, 17, 4, 8, 9
  };

  // 2-dimensional array of pixels:
  int pixels[8][8];

  // cursor position:
  int x = 5;
  int y = 5;

  void setup() {
    // initialize the I/O pins as outputs iterate over the pins:
    for (int thisPin = 0; thisPin < 8; thisPin++) {
      // initialize the output pins:
      pinMode(col[thisPin], OUTPUT);
      pinMode(row[thisPin], OUTPUT);
      // take the col pins (i.e. the cathodes) high to ensure that the LEDS are off:
      digitalWrite(col[thisPin], HIGH);
    }

    // initialize the pixel matrix:
    for (int x = 0; x < 8; x++) {
      for (int y = 0; y < 8; y++) {
        pixels[x][y] = HIGH;
      }
    }
  }

  void loop() {
    // read input:
    readSensors();

    // draw the screen:
    refreshScreen();
  }

  void readSensors() {
    // turn off the last position:
    pixels[x][y] = HIGH;
    // read the sensors for X and Y values:
    x = 7 - map(analogRead(A0), 0, 1023, 0, 7);
    y = map(analogRead(A1), 0, 1023, 0, 7);
    // set the new pixel position low so that the LED will turn on in the next
    // screen refresh:
    pixels[x][y] = LOW;
  }

  void refreshScreen() {
    // iterate over the rows (anodes):
    for (int thisRow = 0; thisRow < 8; thisRow++) {
      // take the row pin (anode) high:
      digitalWrite(row[thisRow], HIGH);
      // iterate over the cols (cathodes):
      for (int thisCol = 0; thisCol < 8; thisCol++) {
        // get the state of the current pixel;
        int thisPixel = pixels[thisRow][thisCol];
        // when the row is HIGH and the col is LOW,
        // the LED where they meet turns on:
        digitalWrite(col[thisCol], thisPixel);
        // turn the pixel off:
        if (thisPixel == LOW) {
          digitalWrite(col[thisCol], HIGH);
        }
      }
      // take the row pin low to turn off the whole row:
      digitalWrite(row[thisRow], LOW);
    }
  }
</code>
</pre> 
            </p>
        </div>
    </div>
</div>



