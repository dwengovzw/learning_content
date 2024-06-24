---
hruid: org-dwengo-pc-wifi-web-app
version: 1
language: nl
title: "Een webapplicatie"
description: "Hoe communiceer ik met de Dwenguino via mijn website?"
keywords: ["dwenguino", "microcontroller", "wifi", "uart", "webserver", "web", "internet", "webapplicatie"]
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

# Een webapplicatie

Om met een webserver te communiceren kunnen we een eenvoudige webapplicatie maken. Hier maken we een eenvoudige HTML pagina met JavaScript code. Deze website toont een knop. Wanneer er op de knop gedrukt wordt, zal een bericht gestuurd worden naar de webserver (http://192.168.135.6/led).


<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-html" data-filename="filename.cpp">

    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toggle LED</title>
    </head>
    <body>
        <button id="toggleButton">Toggle LED</button>

        <script>
            // Function to handle button click
            function toggleLed() {
                fetch('http://192.168.135.6/led')  // Sending GET request to the server
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return response.text();  // Assuming the response is plain text
                    })
                    .then(data => {
                        console.log('Response:', data);  // Logging the response
                        // You can add more handling here if needed
                    })
                    .catch(error => {
                        console.error('There has been a problem with your fetch operation:', error);
                    });
            }

            // Attach event listener to the button
            document.getElementById('toggleButton').addEventListener('click', toggleLed);
        </script>
    </body>
    </html>


</code>
    </pre>
</div>

Om deze applicatie te gebruiken, moet je de volgende stappen uitvoeren.

- Maak een bestand met de naam *index.html* en open het met een teksteditor (bv. Notepad of Gedit).
- Kopieer de code naar een bestand met de naam *index.html*.
- Pas het IP-adres aan naar dat van je webserver.
- Sla het *index.html* bestand op. 
- Open het *index.html* bestand met de browser.

Je zal een pagina zien met een knop. Als alles correct opgezet is, kan je door op de knop te drukken LED13 op de Dwenguino aan- en uitschakelen.

