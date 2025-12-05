---
content_type: text/markdown
copyright: CC BY dwengo
description: How do I program the robot?
estimated_time: 45
hruid: org-dwengo-waisda-rl-crawling-robot-programma
keywords:
- AI
- "re\xEFnforcement learning"
- versterkend leren
- kruipende robot
- elektronica
language: en
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
- http://ilearn.ilabt.imec.be/vocab/tref1/ict
target_ages:
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: false
title: The program
version: 1
---
# Programming the robot

To program the robot you can use our online programming environment. We do not explain in detail how to do that here. You can find all information about the programming environment and the basic programming principles at [dwengo.org/physical_computing](https://www.dwengo.org/physical_computing). Below you can find our code for the robot. In the comments we explain what the different parts do. We recommend going through the learning path on the basic principles of reinforcement learning before you start building and programming the crawling robot.

<div class="dwengo-content dwengo-code-simulator">
        <pre>
<code class="language-cpp">

    /**
    * @file robot_q_learning.ino
    * @brief Robot that learns to crawl using Q-learning.
    *
    * This code uses two servos to move a robot 
    * and a Q-learning algorithm to optimize the movement.
    */
    #include <Wire.h>
    #include <Dwenguino.h>
    #include <LiquidCrystal.h>
    #include <NewPing.h>
    #include <Servo.h>


    /** @brief Pin to which the ultrasonic sensor trigger is connected. */
    #define TRIGGER_PIN_A1 A1
    /** @brief Pin to which the ultrasonic sensor echo is connected. */
    #define ECHO_PIN_A0 A0
    /** @brief Maximum distance (in cm) measured by the ultrasonic sensor. */
    #define MAX_AFSTAND 200

    /** @brief Number of states in the Q-table. */
    #define AANTAL_TOESTANDEN 16
    /** @brief Number of possible actions in the Q-table. */
    #define AANTAL_ACTIES 8
    /** @brief Learning rate of the Q-learning algorithm. */
    #define ALPHA 0.5
    /** @brief Discount factor for future rewards. */
    #define GAMMA 0.5
    /** @brief Probability (in thousandths) to choose a random action (exploration). */
    #define EPSILON 100

    /** @brief Ultrasonic sensor object for distance measurements. */
    NewPing sonarA1A0(TRIGGER_PIN_A1, ECHO_PIN_A0, MAX_AFSTAND);

    /** @brief Servo angles for the first servo. Adjust according to your robot. */
    int hoekenServo1[] = {165, 150, 135, 120};
    /** @brief Servo angles for the second servo. Adjust according to your robot. */
    int hoekenServo2[] = {0, 50, 100, 150};

    /** @brief Current state of the robot (angle of servo1 and servo2). */
    int toestand[] = {hoekenServo1[0], hoekenServo2[1]};

    /** @brief Servo object for the first servo. */
    Servo servo1;
    /** @brief Servo object for the second servo. */
    Servo servo2;

    /** @brief Q-table for the Q-learning algorithm. */
    float Q[AANTAL_TOESTANDEN][AANTAL_ACTIES];

    /**
    * @brief Initialize the Q-table by filling it with zeros.
    */
    void initialiseer_q_tabel() {
        for (int s = 0; s < AANTAL_TOESTANDEN; s++) {
            for (int a = 0; a < AANTAL_ACTIES; a++) {
                Q[s][a] = 0.0f; 
            }
        }
    }

    /**
    * @brief Find the index of a given value in an array.
    * @param arr Array to search in.
    * @param lengte_van_de_array Length of the array.
    * @param waarde The value to search for.
    * @return The index of the value in the array, or -1 if not found.
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
    * @brief Determine the index of the current state in the Q-table.
    * @param toestand Array with the current servo angles.
    * @return Index of the state in the Q-table.
    */
    int zoek_positie_van_toestand(int toestand[]){
        int eerste_positie = zoekIndex(hoekenServo1, AANTAL_ACTIES/2, toestand[0]);
        int tweede_positie = zoekIndex(hoekenServo2, AANTAL_ACTIES/2, toestand[1]);
        int index_van_de_toestand = eerste_positie * 4 + tweede_positie;
        return index_van_de_toestand;
    }

    /**
    * @brief Find the best action for a given state based on the Q-table.
    * @param toestand_index Index of the state in the Q-table.
    * @return Index of the best action.
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
    * @brief Move a servo from start_hoek to eind_hoek in small steps.
    * @param servo Pointer to the Servo object.
    * @param start_hoek Start position of the servo.
    * @param eind_hoek End position of the servo.
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
    * @brief Execute an action based on the index in the Q-table.
    * @param actie_index Index of the action in the Q-table.
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
    * @brief Arduino setup function. Runs once at startup.
    */
    void setup()
    {
        initDwenguino();

        servo1.attach(40);
        servo2.attach(41);

        servo1.write(hoekenServo1[0]);
        servo2.write(hoekenServo2[0]);

        initialiseer_q_tabel();

        // Use measured distance as seed for random numbers.
        int afstand = sonarA1A0.ping_cm();
        randomSeed(afstand);
    }

    /**
    * @brief Arduino loop function. Runs continuously.
    */
    void loop()
    {
        long rand = random(1000);  ///< Generate a random number between 0 and 1000.
        int actie_index = 0;

        int toestand_index = zoek_positie_van_toestand(toestand);

        // Choose a random action with probability EPSILON/1000, otherwise the best action.
        if (rand < EPSILON){
            actie_index = random(AANTAL_ACTIES);
        } else {
            actie_index = zoek_de_beste_actie(toestand_index);
        }

        // Measure distance before the action.
        int gemeten_afstand = sonarA1A0.ping_cm();

        delay(100);  // Ensure the previous action has finished.

        voer_actie_uit(actie_index);  // Execute action.

        // Compute reward based on difference in distance.
        int nieuwe_afstand = sonarA1A0.ping_cm();
        int beloning = nieuwe_afstand - gemeten_afstand;

        // Filter out small rewards to reduce noise.
        if (beloning <= 2 && beloning >= -2){
            beloning = 0;
        }

        // Find the best action in the new state.
        int index_van_nieuwe_toestand = zoek_positie_van_toestand(toestand);
        int index_van_nieuwe_actie = zoek_de_beste_actie(index_van_nieuwe_toestand);

        // Update Q-table according to the Q-learning rule.
        Q[toestand_index][actie_index] = 
            Q[toestand_index][actie_index] + 
            ALPHA * (beloning + GAMMA * Q[index_van_nieuwe_toestand][index_van_nieuwe_actie] - Q[toestand_index][actie_index]);
    }


</code>
        </pre> 
        </div>


<div class="dwengo-content assignment">
<h2 class="title">Assignment</h2>
<div class="content">
<ul>
<li>Open the code in the Dwengo simulator.</li>
<li>Compile the code.</li>
<li>Transfer the .dw file with compiled code to your robot.</li>
<li>Analyze the result: does the robot learn? It can take up to 10 minutes before the robot learns a crawling pattern (gait in English).</li>
<li>Optionally modify the code to ensure the robot learns a gait faster.</li>
</ul>
</div>
</div>