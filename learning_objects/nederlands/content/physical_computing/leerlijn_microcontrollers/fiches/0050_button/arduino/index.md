---
hruid: leerlijn_fiches_arduino_knoppen
version: 1
language: nl
title: "Knoppen"
description: "Leer de knoppen gebruiken"
keywords: ["Knoppen", "fiche", "arduino"]
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
    <h1 class="title">Knoppen</h1>
    <h2 class="subtitle">Programma's starten m.b.v. knoppen</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
            <p class="info_item_content">
                <img src="img/button1.jpeg" alt="Een afbeelding van de knoppen." title="Een afbeelding van de knoppen."></img>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Type</h3>
            <p class="info_item_content">
                Invoer 
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Pinnen</h3>
            <p class="info_item_content">
                N.v.t.
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
                Je kan deze bijvoorbeeld gebruiken om bepaalde delen van je programma niet te laten uitvoeren tot je dit expliciet aangeeft door een knop in te drukken.
            </p>
        </div>
        <div class="example_item item">
            <h3 class="example_item_title">Voorbeeld: led gaat pas branden wanneer je een knop indrukt.</h3>
            <p class="example_item_content">
<pre>
<code class="language-cpp">
    
// constants won't change. They're used here to set pin numbers:
const int buttonPin = 2;  // the number of the pushbutton pin
const int ledPin = 13;    // the number of the LED pin

// variables will change:
int buttonState = 0;  // variable for reading the pushbutton status

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    // turn LED on:
    digitalWrite(ledPin, HIGH);
  } else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
  }
}
</code>
</pre> 
            </p>
        </div>
    </div>
</div>



