---
hruid: org-dwengo-pc-luchtkwaliteit-webinterface
version: 1
language: nl
title: "Webinterface"
description: "Hoe kan ik de luchtkwaliteit meten?"
keywords: ["dwenguino", "microcontroller", "wifi", "i2c", "webserver", "internet", "co2", "luchtkwaliteit"]
content_type: "text/markdown"
estimated_time: 20
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

# Webinterface

We kunnen de data nu opvragen vanuit een webapplicatie en weergeven op een HTML pagina in de browser. Hieronder zie je een eenvoudig voorbeeld van hoe je dat kan doen. In dit voorbeeld wordt om de tien seconden een meting van de luchtkwaliteit opgevraagd. Het resultaat van de meting wordt dan weergegeven op de pagina.

```html
        <!DOCTYPE html>
        <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Luchtkwaliteitsmeter</title>
            </head>
            <body>
                <h1>Luchtkwaliteitsmeter</h1>
                <p id="meting">Laden...</p>
                <script>
                    // Functie om de luchtkwaliteit op te vragen.
                    function getLuchtkwaliteit() {
                        // Stuur een GET request naar de Dwenguino.
                        fetch('http://192.168.135.6/luchtkwaliteit') 
                            .then(response => {
                                if (!response.ok) {
                                    throw new Error('Netwerk antwoord was niet ok');
                                }
                                // Vorm de response om naar tekst.
                                return response.text();
                            })
                            .then(data => {
                                // Log de waarde in de console.
                                console.log('Antwoord:', data); 
                                // Plaats de waarde in de HTML.
                                document.querySelector('#meting').textContent = data;
                            })
                            .catch(error => {
                                console.error('Fout bij fetch operatie:', error);
                            });
                    }
                    // Doe een eerste meting
                    getLuchtkwaliteit();
                    // Vraag om de 10 seconden de luchtkwaliteit op.
                    setInterval(getLuchtkwaliteit, 10000);  
                </script>
            </body>
        </html>

```

Je kan deze website zelf uitvoeren door een document te maken op je computer met de naam *index.html*. Open dit bestand eerst met een teksteditor (bv. kladblok of VSCode) en plak bovenstaande HTML in het bestand. Sluit het bestand en open het met je internetbrowser.

<div class="dwengo-content important">
<h2 class="title">Rekenkracht</h2>
<div class="content">
De Dwenguino heeft maar een beperkte rekenkracht. Deze zal dus maar een beperkt aantal requests per tijdseenheid kunnen verwerken. <strong>Let dus op dat je het tijdsinterval niet te kort maakt! Anders zal de Dwenguino de requests niet meer snel genoeg kunnen verwerken!</strong>
</div>
</div>