---
hruid: org-dwengo-pc-wifi-dwenguino-webserver
version: 1
language: nl
title: "Dwenguino als webserver"
description: "Hoe gebruik ik de Dwenguino als webserver??"
keywords: ["dwenguino", "microcontroller", "wifi", "uart", "webserver", "web", "internet"]
content_type: "text/markdown"
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-digitale-competenties-en-mediawijsheid',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-algebra-analyse',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-redeneren',

]
copyright: "CC BY dwengo"
target_ages: [16, 17, 18]
teacher_exclusive: False
---

# De Dwenguino als webserver

Hier gaan de de Dwenguino gebruiken als webserver. De Dwenguino zal dus constant via wifi luisteren naar HTTP berichten. Wanneer er een bericht toekomt, zal de Dwenguino het verwerken en een antwoord terugsturen.

## Een wifi netwerk

Voor we de Dwenguino met het netwerk kunnen verbinden, hebben we dus een wifi netwerk nodig. Op veel scholen is een wifi netwerk aanwezig dit netwerk kan je gebruiken om de Dwenguino mee te verbinden. Op veel scholen wordt het wifi netwerk echter sterker beveiligd. Dit kan ervoor zorgen dat je bijvoorbeeld enkel met een specifieke account kan verbinden met het netwerk of dat bepaalde berichten geblokkeerd worden. In dat geval kan je gebruik maken van een **smartphone met een mobiel hotspot**. Deze hotspot zal een eigen netwerk opzetten waarmee je zowel de Dwenguino als je computer kan verbinden. Jij hebt de controle over dit netwerk, zo is het makkelijker om alles correct in te stellen.

## Code voor de webserver

Hieronder zie je een basisprogramma waarmee je de Dwenguino kan gebruiken als webserver. In de commentaar staat uitgelegd wat de verschillende onderdelen van de code doen. De code zal verbinden met een wifi netwerk en ervoor zorgen dat de Dwenguino luistert naar HTTP berichten. Wanneer deze naar de /led url gestuurd worden, zal de Dwenguino LED13 aan of uit zetten.

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">


// Importeer de Dwenguino bibliotheken
#include <Dwenguino.h>
#include <DwenguinoWIFI.h>

// Wi-Fi gegevens
/* 
   Zorg ervoor dat je hier de naam
   en het wachtwoord van je wifi netwerk
   correct aanvult.
*/
const char* ssid = "Naam-van-het-wifi-netwerk";
const char* password = "Wachtwoord-van-het-wifi-netwerk";

// Hierin slaan we de huidige waarde van LED13 op.
unsigned char ledValue = 0;

/*
    Hier initialiseren we de DwenguinoWIFI bibliotheek.
    Deze krijgt de volgende parameters mee:
      - ssid: de naam van het wifi netwerk.
      - password: het wachtwoord van het wifi netwerk.
      - true: Zal ervoor zorgen dat er debug informatie
              over de netwerkverbinding wordt doorgestuurd
              naar de computer via de seriële poort.
              Je kan deze gegevens dan lezen in de 
              seriële monitor.

*/
DwenguinoWIFI DwenguinoWIFI(ssid, password, true);


/*
  Deze functie zal een http bericht verwerken. 
  We noemen een dergelijke functie een "handler" functie.
  Deze heeft de volgende parameters:
    - query: De parameters die achter de url komen. 
             Deze komen na het ? in de url.
             Bv. voor de volgende url
             dwengo.org?hruid=kiks3_dl_basis
             is de query
             hruid=kiks3_dl_basis
    - result: Een string variabele waarin je het resultaat
              dat teruggestuurd moet worden, kan kopiëren.
*/

void handleLEDToggle(char* query, char* result){
  ledValue ^= 1;
  digitalWrite(13, ledValue);
  strcpy(result, String(ledValue).c_str());
}


void setup() {
  // Start seriële communicatie voor debug info.
  Serial.begin(9600);  

  // Wacht 5s zodat je de seriële monitor kan opstarten.
  delay(5000);

  // Initialiseer de Dwenguino.
  initDwenguino();

  // Stel LED13 in als output.
  pinMode(13, OUTPUT);
  // Zet LED13 uit.
  digitalWrite(13, ledValue);

  /*
    Hier voegen we een route toe aan de webserver. We leggen
    hier eigenlijk vast hoe een url verwerkt moet worden door
    de Dwenguino.
      - De eerste parameter zal bepalen naar welke url er 
        geluisterd wordt. In dit geval ip_adres/led.
      - De tweede paramter verwijst naar de fuctie die het
        bericht moet verwerken. Hier de handleLEDToggle functie.
  */
  DwenguinoWIFI.routeManager.addRouteHandler("led", handleLEDToggle);
  
  // Initialiseer de wifi module
  DwenguinoWIFI.setupESP();


  Serial.println("Setup complete");
}

// Luister elke seconde of er een bericht ontvangen is.
void loop() {
  delay(1000);
  Serial.println("Ready to receive http requests.");
  DwenguinoWIFI.handleHTTPRequest();
}


</code>
    </pre>
</div>

## Route, query en handler

Er zijn drie belangrijke concepten die je moet begrijpen om je eigen webserver te kunnen bouwen zijn **routes**, **queries** en **handlers**. Routes en queries kunnen we makkelijk illustreren aan de hand van een voorbeeld url. De route en de query komen op het einde van de url. Deze informatie zegt aan de webserver hoe deze de request moet verwerken. De route legt vast door welke functie de request verwerkt zal worden. De query bevat de parameters die deze methode krijgt.

![Decompositie van url.](images/url_description_plain.png)