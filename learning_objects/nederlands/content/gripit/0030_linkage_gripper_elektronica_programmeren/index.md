---
hruid: org_dwengo_gripit_linkage_gripper_elektronica_programmeren
version: 1
language: nl
title: "De parallellogram-grijper programmeren"
description: "Hoe sluit je de parallellogram-grijper aan en bestuur je hem met een programma?"
keywords: ["fiche", "gripit", "parallellogram-grijper", "elektronica", "programmeren", "servo"]
educational_goals: [
    {source: Source, id: id}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16, 17, 18]
difficulty: 1
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

<div class="dwengo_content fiche">
    <h1 class="title">Elektronica en programmeren van de parallellogram-grijper</h1>
    <h2 class="subtitle">Hoe sluit je de grijper aan en bestuur je hem?</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">De servo aansluiten</h3>
            <p class="info_item_content">
                De Halberd heeft vier aansluitingen voor servo's. Elke servo-aansluiting heeft drie pinnen: GND, 5V en PWM. Sluit de stekker van de servo aan door de draden te laten overeenkomen met de gekleurde stippen bij de pinlabels op de Halberd.
            </p>
            <p class="info_item_content">
                GND is de massapin, 5V voedt de servo en de PWM-pin stuurt de positie van de servo aan. Controleer voor je de Halberd inschakelt of elke draad bij het juiste label aangesloten is.
            </p>
            <img src="img/halberd_board_top_connector_servo_color_code.png" alt="Servo-aansluitingen op de Halberd met de pinlabels GND, 5V en PWM en gekleurde stippen die overeenkomen met de servodraden." title="Sluit de servodraden aan volgens de gekleurde stippen en pinlabels."></img>
            <p class="info_item_content">
                Voor de parallellogram-grijper sluit je de servo aan op een van deze vier servo-aansluitingen. Onthoud welke aansluiting je gebruikt, zodat je in je programma dezelfde PWM-aansluiting kunt selecteren.
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">De grijper programmeren</h3>
            <p class="info_item_content">
                                Met dit programma beweegt de servo die op SERVO_2 is aangesloten langzaam van 0 naar 90 graden en daarna terug naar 0 graden. De beweging wordt voortdurend herhaald. Zo opent en sluit de parallellogram-grijper. De vertraging van 10 milliseconden tussen twee hoeken zorgt voor een vloeiende beweging.
            </p>
                        <div class="dwengo-content dwengo-code-simulator">
                                <pre>
<code class="language-cpp" data-filename="parallellogram_grijper.cpp">
#include &lt;Wire.h&gt;
#include &lt;Dwenguino.h&gt;
#include &lt;LiquidCrystal.h&gt;
#include &lt;Servo.h&gt;

// Maak een servo-object voor de servo-aansluiting SERVO_2.
Servo servoOnPinSERVO_2;

void setup()
{
// Bereid de functies van de Dwenguino voor.
initDwenguino();
// Koppel het servo-object aan de aansluiting SERVO_2.
servoOnPinSERVO_2.attach(SERVO_2);
}

void loop()
{
// Beweeg de servo van 0 naar 90 graden.
for (int hoek = 0; hoek &lt; 90; hoek++) {
servoOnPinSERVO_2.write(hoek);  // Stuur de servo naar deze hoek.
delay(10);                       // Wacht even voor een vloeiende beweging.
}

// Beweeg de servo daarna terug van 90 naar 0 graden.
for (int hoek = 90; hoek &gt; 0; hoek--) {
servoOnPinSERVO_2.write(hoek);  // Stuur de servo naar deze hoek.
delay(10);                       // Wacht even voor een vloeiende beweging.
}
}
</code>
                                </pre>
                        </div>
        </div>
    </div>
</div>
