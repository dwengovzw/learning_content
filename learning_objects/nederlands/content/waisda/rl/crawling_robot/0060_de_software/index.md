---
hruid: org-dwengo-waisda-rl-crawling-robot-programma
version: 1
language: nl
title: "Het programma"
description: "Hoe programmeer ik de robot?"
keywords: ["AI", "reïnforcement learning", "versterkend leren", "kruipende robot", "elektronica"]
content_type: "text/markdown"
estimated_time: 45
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# De robot programmeren

Om de robot te programmeren kan je gebruik maken van onze online programmeeromgeving. Hier leggen we niet in detail uit hoe je dat kan doen. Alle informatie over de programmeeromgeving en de basis programmeerprincipes kan je vinden op [https://www.dwengo.org/physical_computing](https://www.dwengo.org/physical_computing). Hieronder kan je onze code vinden voor de robot. In de commentaar leggen we uit wat de verschillende onderdelen doen. We raden je aan om het leerpad over de basisprincipes van versterkend leren door te nemen voor je begint met het bouwen en programmeren van de kruipende robot.

<div class="dwengo-content dwengo-code-simulator">
        <pre>
<code class="language-cpp">

    /**
    * @file robot_q_learning.ino
    * @brief Robot die leert kruipen met Q-learning.
    *
    * Deze code gebruikt twee servo's om een robot te laten bewegen 
    * en een Q-learning-algoritme om de beweging te optimaliseren.
    */
    #include <Wire.h>
    #include <Dwenguino.h>
    #include <LiquidCrystal.h>
    #include <NewPing.h>
    #include <Servo.h>


    /** @brief Pin waar de ultrasoon-sensor trigger op aangesloten is. */
    #define TRIGGER_PIN_A1 A1
    /** @brief Pin waar de ultrasoon-sensor echo op aangesloten is. */
    #define ECHO_PIN_A0 A0
    /** @brief Maximale afstand (in cm) die de ultrasoon-sensor meet. */
    #define MAX_AFSTAND 200

    /** @brief Aantal toestanden in de Q-tabel. */
    #define AANTAL_TOESTANDEN 16
    /** @brief Aantal mogelijke acties in de Q-tabel. */
    #define AANTAL_ACTIES 8
    /** @brief Learning rate van het Q-learning algoritme. */
    #define ALPHA 0.5
    /** @brief Discount factor voor toekomstige beloningen. */
    #define GAMMA 0.5
    /** @brief Kans (in duizendsten) om een willekeurige actie te kiezen (exploration). */
    #define EPSILON 100

    /** @brief Ultrasoon sensor object voor afstandsmetingen. */
    NewPing sonarA1A0(TRIGGER_PIN_A1, ECHO_PIN_A0, MAX_AFSTAND);

    /** @brief Servohoeken voor de eerste servo. Pas aan volgens jouw robot. */
    int hoekenServo1[] = {165, 150, 135, 120};
    /** @brief Servohoeken voor de tweede servo. Pas aan volgens jouw robot. */
    int hoekenServo2[] = {0, 50, 100, 150};

    /** @brief Huidige toestand van de robot (hoek van servo1 en servo2). */
    int toestand[] = {hoekenServo1[0], hoekenServo2[1]};

    /** @brief Servo object voor de eerste servo. */
    Servo servo1;
    /** @brief Servo object voor de tweede servo. */
    Servo servo2;

    /** @brief Q-tabel voor het Q-learning algoritme. */
    float Q[AANTAL_TOESTANDEN][AANTAL_ACTIES];

    /**
    * @brief Initialiseer de Q-tabel door overal nullen te schrijven.
    */
    void initialiseer_q_tabel() {
        for (int s = 0; s < AANTAL_TOESTANDEN; s++) {
            for (int a = 0; a < AANTAL_ACTIES; a++) {
                Q[s][a] = 0.0f; 
            }
        }
    }

    /**
    * @brief Zoek de index van een bepaalde waarde in een array.
    * @param arr Array waarin gezocht wordt.
    * @param lengte_van_de_array Lengte van de array.
    * @param waarde De waarde waarnaar gezocht wordt.
    * @return De index van de waarde in de array, of -1 als niet gevonden.
    */
    int zoekIndex(int arr[], int lengte_van_de_array, int waarde) {
        for (int i = 0; i < lengte_van_de_array; i++) {
            if (arr[i] == waarde) {
                return i;
            }
        }
        return -1;
    }

    /**
    * @brief Bepaal de index van de huidige toestand in de Q-tabel.
    * @param toestand Array met de huidige hoeken van de servo's.
    * @return Index van de toestand in de Q-tabel.
    */
    int zoek_positie_van_toestand(int toestand[]){
        int eerste_positie = zoekIndex(hoekenServo1, AANTAL_ACTIES/2, toestand[0]);
        int tweede_positie = zoekIndex(hoekenServo2, AANTAL_ACTIES/2, toestand[1]);
        int index_van_de_toestand = eerste_positie * 4 + tweede_positie;
        return index_van_de_toestand;
    }

    /**
    * @brief Zoek de beste actie voor een gegeven toestand op basis van de Q-tabel.
    * @param toestand_index Index van de toestand in de Q-tabel.
    * @return Index van de beste actie.
    */
    int zoek_de_beste_actie(int toestand_index) {
        float max_q = Q[toestand_index][0];
        int beste_actie = 0;
        for (int a = 1; a < AANTAL_ACTIES; a++) {
            if (Q[toestand_index][a] > max_q) {
                max_q = Q[toestand_index][a];
                beste_actie = a;
            }
        }
        return beste_actie;
    }

    /**
    * @brief Beweeg een servo van start_hoek naar eind_hoek met kleine stapjes.
    * @param servo Pointer naar het Servo-object.
    * @param start_hoek Startpositie van de servo.
    * @param eind_hoek Eindpositie van de servo.
    */
    void beweeg_servo(Servo* servo, int start_hoek, int eind_hoek){
        if (start_hoek > eind_hoek){
            for (int angle = start_hoek; angle >= eind_hoek ; angle -= 1){
                servo->write(angle);
                delay(10);
            }
        } else {
            for (int angle = start_hoek; angle <= eind_hoek ; angle += 1){
                servo->write(angle);
                delay(10);
            }
        }
    }

    /**
    * @brief Voer een actie uit op basis van de index in de Q-tabel.
    * @param actie_index Index van de actie in de Q-tabel.
    */
    void voer_actie_uit(int actie_index){
        if (actie_index >= 4){
            beweeg_servo(&servo2, toestand[1], hoekenServo2[actie_index-4]);
            toestand[1] = hoekenServo2[actie_index-4];
        } else {
            beweeg_servo(&servo1, toestand[0], hoekenServo1[actie_index]);
            toestand[0] = hoekenServo1[actie_index];
        }
    }

    /**
    * @brief Arduino setup-functie. Wordt één keer uitgevoerd bij opstarten.
    */
    void setup()
    {
        initDwenguino();

        servo1.attach(40);
        servo2.attach(41);

        servo1.write(hoekenServo1[0]);
        servo2.write(hoekenServo2[0]);

        initialiseer_q_tabel();

        // Gebruik gemeten afstand als seed voor willekeurige getallen.
        int afstand = sonarA1A0.ping_cm();
        randomSeed(afstand);
    }

    /**
    * @brief Arduino loop-functie. Wordt continu uitgevoerd.
    */
    void loop()
    {
        long rand = random(1000);  ///< Genereer een willekeurig getal tussen 0 en 1000.
        int actie_index = 0;

        int toestand_index = zoek_positie_van_toestand(toestand);

        // Kies een willekeurige actie met kans EPSILON/1000, anders de beste actie.
        if (rand < EPSILON){
            actie_index = random(AANTAL_ACTIES);
        } else {
            actie_index = zoek_de_beste_actie(toestand_index);
        }

        // Meet afstand vóór de actie.
        int gemeten_afstand = sonarA1A0.ping_cm();

        delay(100);  // Zorg dat de vorige actie is afgerond.

        voer_actie_uit(actie_index);  // Voer actie uit.

        // Bereken beloning op basis van verschil in afstand.
        int nieuwe_afstand = sonarA1A0.ping_cm();
        int beloning = nieuwe_afstand - gemeten_afstand;

        // Filter kleine beloningen weg om ruis te verminderen.
        if (beloning <= 2 && beloning >= -2){
            beloning = 0;
        }

        // Zoek de beste actie in de nieuwe toestand.
        int index_van_nieuwe_toestand = zoek_positie_van_toestand(toestand);
        int index_van_nieuwe_actie = zoek_de_beste_actie(index_van_nieuwe_toestand);

        // Update Q-tabel volgens Q-learning regel.
        Q[toestand_index][actie_index] = 
            Q[toestand_index][actie_index] + 
            ALPHA * (beloning + GAMMA * Q[index_van_nieuwe_toestand][index_van_nieuwe_actie] - Q[toestand_index][actie_index]);
    }


</code>
        </pre> 
        </div>


<div class="dwengo-content assignment">
<h2 class="title">Opdracht</h2>
<div class="content">
<ul>
<li>Open de code in de Dwengo simulator.</li>
<li>Compileer de code.</li>
<li>Zet het .dw bestand met gecompileerde code over naar je robot.</li>
<li>Analyseer het resultaat, leert de robot? Het kan tot 10 minuten duren voordat de robot een kruippatroon (gate in het Engels) leert.</li>
<li>Pas de code eventueel aan om ervoor te zorgen dat de robot sneller een gate leert.</li>
</ul>
</div>
</div>