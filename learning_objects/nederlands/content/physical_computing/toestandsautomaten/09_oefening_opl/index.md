---
hruid: pc_toestandsautomaten9
version: 3
language: nl
title: "Oplossing"
description: "Oplossing op het omzetten van gedragsbeschrijving naar code."
keywords: ["toestandsautomaat", "toestandsdiagram", "finite state machine", "toestand", "dwenguino", "arduino", "python"]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [13, 14, 15, 16, 17, 18]
difficulty: 3
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Opdracht omzetting naar code: oplossing

![blockly](@learning-object/pc_toestandsautomaten9_meta/nl/1)

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
#include &lt;Wire.h&gt;
#include &lt;Dwenguino.h&gt;
#include &lt;LiquidCrystal.h&gt;
#include &lt;Servo.h&gt;<br>
int toestand;
int snelheid;<br>
#define BUTTON_PIN_SW_C SW_C
#define BUTTON_PIN_SW_N SW_N
#define BUTTON_PIN_SW_S SW_S<br>
Servo servoOnPin17;<br>
void setup() {
    initDwenguino();<br>
    pinMode(BUTTON_PIN_SW_C, INPUT_PULLUP);
    pinMode(BUTTON_PIN_SW_N, INPUT_PULLUP);
    pinMode(BUTTON_PIN_SW_S, INPUT_PULLUP);
    servoOnPin17.attach(17);
    toestand = 0;
    snelheid = 0;
}<br>
void loop() {
    if ((digitalRead(BUTTON_PIN_SW_C)) == PRESSED) {
        if (toestand == 1) {
            toestand = 0;
        } else {
            toestand = 1;
        }
    }
    if (toestand == 0) {
        servoOnPin17.writeMicroseconds(map(constrain(snelheid, -255, 255), -255, 255, 1500 - 500, 1500 + 500));
    } else if (toestand == 1) {
        if ((digitalRead(BUTTON_PIN_SW_N)) == PRESSED) {
            snelheid = snelheid + 50;
            if (snelheid > 250) {
                snelheid = 250;
            }
        }
        if ((digitalRead(BUTTON_PIN_SW_S)) == PRESSED) {
            snelheid = snelheid - 50;
            if (snelheid < -250) {
                snelheid = -250;
            }
        }
    }
    delay(100);
}
</code>
    </pre>
</div>