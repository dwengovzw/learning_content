---
hruid: pc_toestandsautomaten7
version: 3
language: nl
title: "Oplossing"
description: "We zetten een automaatbeschrijving en toestandsdiagram over naar code op een dwenguino."
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

# Toestandsdiagrammen in de praktijk

Hieronder staat het volledig afgewerkte programma van de gegeven automaatbeschrijving.

![blockly](@learning-object/pc_toestandsautomaten7_meta/nl/1)

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

#include <Wire.h>
#include <Dwenguino.h>

#define BUTTON_PIN_SW_C SW_C

unsigned char toestandsnr = 0;

void setup()
{
  initDwenguino();
  pinMode(BUTTON_PIN_SW_C, INPUT_PULLUP);
}

void loop()
{
  if ((digitalRead(SW_C)) == PRESSED) {
    toestandsnr = toestandsnr + 1;
    if (toestandsnr == 9){
      toestandsnr = 0;
      }
    }
    if (toestandsnr == 0){
      LEDS = 0b00000000;
    } else if (toestandsnr == 1){
      LEDS = 0b00000001;
    } else if (toestandsnr == 2){
      LEDS = 0b00000010;
    } else if (toestandsnr == 3){
      LEDS = 0b00000100;
    } else if (toestandsnr == 4){
      LEDS = 0b00001000;
    } else if (toestandsnr == 5){
      LEDS = 0b00010000;
    } else if (toestandsnr == 6){
      LEDS = 0b00100000;
    } else if (toestandsnr == 7){
      LEDS = 0b01000000;
    } else if (toestandsnr == 8){
      LEDS = 0b10000000;
    }
    delay(100);
}
</code>
    </pre>
</div>