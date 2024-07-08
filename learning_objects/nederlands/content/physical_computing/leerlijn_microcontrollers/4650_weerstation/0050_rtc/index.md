---
hruid: leerlijn_uc_introductie_weerstation_rtc
version: 1
language: nl
title: "Real time clock (RTC)"
description: "Hoe kunnen we de tijd bijhouden op de Dwenguino."
keywords: ["Microcontroller", "µC", "weerstation", "rtc", "real time clock", "tijd"]
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
estimated_time: 3
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# De real time clock

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

    #include <Dwenguino.h>
    #include <Wire.h>
    #include <DS3231-RTC.h>

    DS3231 mijnRTC;
    RTClib rtcLib;

    String menuItemLabels[] = {"Jaar", "Maand", "Dag", "Dag week", "Uur", "Minuut", "Seconde"};

    unsigned char menuLocatie = 0; 

    const unsigned char AANTAL_MENU_ITEMS = 7;
    const unsigned char JAAR = 0;
    const unsigned char MAAND = 1;
    const unsigned char DAG = 2;
    const unsigned char DVW = 3;
    const unsigned char UUR = 4;
    const unsigned char MINUUT = 5;
    const unsigned char SECONDE = 6;

    unsigned char debounce = 0;

    // De default instelling voor jaar, maand, dag, dVW, uur, minuut en seconde.
    unsigned char tijdsinstelling[AANTAL_MENU_ITEMS] = {24, 7, 5, 5, 12, 0, 0};
    unsigned char tijdsinstellingMaxima[AANTAL_MENU_ITEMS] = {3000, 12, 31, 7, 24, 60, 60};

    // Knop omhoog
    ISR(INT7_vect){
        if (debounce == 0){
            menuLocatie = (menuLocatie + 1)%AANTAL_MENU_ITEMS;
        }
        debounce = 2;
    }

    // Knop rechts
    ISR(INT6_vect){
        if (debounce == 0){
            tijdsinstelling[menuLocatie] = 
                (tijdsinstelling[menuLocatie] + 1)
                %tijdsinstellingMaxima[menuLocatie];
                debounce = 2; 
        }
    }

    // Knop onder
    ISR(INT5_vect){
        if (debounce == 0){
            menuLocatie = (menuLocatie - 1)%AANTAL_MENU_ITEMS;
            debounce = 2; 
        }
    }

    // Knop links
    ISR(INT4_vect){
        if (debounce == 0){
            tijdsinstelling[menuLocatie] = 
                (tijdsinstelling[menuLocatie] - 1)
                %tijdsinstellingMaxima[menuLocatie];
                debounce = 2;
        }
    }

    void zetKnopInterruptsAan(){
        pinMode(SW_N, INPUT_PULLUP);
        pinMode(SW_E, INPUT_PULLUP);
        pinMode(SW_S, INPUT_PULLUP);
        pinMode(SW_W, INPUT_PULLUP);
        SREG |= 1<<SREG_I;  // Zet globale interrupts aan.
        //N,S
        EIMSK |= ((1<<INT7)|(1<<INT6)|(1<<INT5)|(1<<INT4));
        EICRB &= ~((1<<ISC70)|(1<<ISC60)|(1<<ISC50)|(1<<ISC40));
        EICRB |= ((1<<ISC71)|(1<<ISC61)|(1<<ISC51))|(1<<ISC41);
    }

    void zetKnopInterruptsUit(){
        EIMSK &= ~((1<<INT7)|(1<<INT6)|(1<<INT5)|(1<<INT4));
    }


    void printStringNaarLCD(unsigned char rij, unsigned char kolom, String tekst){
        dwenguinoLCD.setCursor(kolom, rij);
        dwenguinoLCD.print(tekst);
    }

    void stelTijdIn(){
        mijnRTC.setClockMode(false);  // 24h klok
            
        mijnRTC.setYear(tijdsinstelling[JAAR]);
        mijnRTC.setMonth(tijdsinstelling[MAAND]);
        mijnRTC.setDate(tijdsinstelling[DAG]);
        mijnRTC.setDoW(tijdsinstelling[DVW]);
        mijnRTC.setHour(tijdsinstelling[UUR]);
        mijnRTC.setMinute(tijdsinstelling[MINUUT]);
        mijnRTC.setSecond(tijdsinstelling[SECONDE]);
    }

    void openTijdsinstellingsmenu(){
        zetKnopInterruptsAan();
        dwenguinoLCD.clear(); // Maak scherm leeg
        
        pinMode(SW_C, INPUT_PULLUP);

        // Toon het menu zolang de SW_C knop niet wordt ingedrukt. 
        while (digitalRead(SW_C)){
            // Teken controls
            printStringNaarLCD(0, 15, '^');
            printStringNaarLCD(1, 15, 'v' - 1);
            printStringNaarLCD(1, 0, "<");
            printStringNaarLCD(1, 7, ">");
            printStringNaarLCD(0, 2, menuItemLabels[menuLocatie]);
            printStringNaarLCD(1, 2, String(tijdsinstelling[menuLocatie]));
            delay(100);
            dwenguinoLCD.clear(); // Maak scherm leeg
            if (debounce > 0){
                debounce--;
            }
        }
        zetKnopInterruptsUit();
    }

    void setup() {
        initDwenguino(); // Initialiseer de basisfuncties van de Dwenguino

        // Start de serial poort
        Serial.begin(9600);
        
        // Start de I2C interface
        Wire.begin();

        // Stel tijd in via waarden RTC
        DateTime now = rtcLib.now();
        tijdsinstelling[JAAR] = now.getYear();
        tijdsinstelling[MAAND] = now.getMonth();
        tijdsinstelling[DAG] = now.getDay();
        tijdsinstelling[DVW] = now.getWeekDay();
        tijdsinstelling[UUR] = now.getHour();
        tijdsinstelling[MINUUT] = now.getMinute();
        tijdsinstelling[SECONDE] = now.getSecond();
    }

    void stuurTijdOverSerieel(){
        DateTime now = rtcLib.now();

        Serial.print(now.getYear(), DEC);
        Serial.print('/');
        Serial.print(now.getMonth(), DEC);
        Serial.print('/');
        Serial.print(now.getDay(), DEC);
        Serial.print(' ');
        Serial.print(now.getHour(), DEC);
        Serial.print(':');
        Serial.print(now.getMinute(), DEC);
        Serial.print(':');
        Serial.print(now.getSecond(), DEC);
        Serial.println();
        
        Serial.print(" since midnight 1/1/1970 = ");
        Serial.print(now.getUnixTime());
        Serial.print("s = ");
        Serial.print(now.getUnixTime() / 86400L);
        Serial.println("d");
    }

    void loop() {
        printStringNaarLCD(0, 0, "N:Tijd sturen");
        printStringNaarLCD(1, 0, "S:Tijd instellen");
        delay(500);
        dwenguinoLCD.clear(); // Maak scherm leeg

        // Stuur tijd door over serieel wanneer de noord knop wordt ingedrukt.
        if (!digitalRead(SW_N)){
            stuurTijdOverSerieel();
        } else if (!digitalRead(SW_S)){
            openTijdsinstellingsmenu();
            stelTijdIn();
        }    
    }

</code>
    </pre>
</div>