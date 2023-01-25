---
hruid: cb_eindtermen2
version: 3
language: nl
title: "Verwerking in het project"
description: "Verwerking in het project"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [12, 13, 14]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Digitale competentie en mediawijsheid 
## Eindtermen digitale competentie en mediawijsheid, en het '*Chatbot*'-project 

*Eindterm 4.1 (tweede en derde graad) - Zelfvertrouwen* 

Men moet geen bolleboos zijn in wiskunde en wetenschappen, noch moet men een kei zijn in programmeren om met Natural Language Processing aan de slag te gaan.<br>
Door de leerlingen positieve ervaringen te bieden in een voor hen waarschijnlijk ongekend domein dat echter maatschappelijk relevant is en gelinkt is aan hun leefwereld - leerlingen maken bv. veel gebruik van sociale media -, kan hun zelfvertrouwen
betreffende informaticawetenschappen, in het bijzonder programmeren en artificiële intelligentie, een boost krijgen.<br>
De leerlingen uit niet-STEM-richtingen zien door te werken met de notebooks van het project ‘Chatbot’ in dat taaltechnologie ook voor hen een haalbaar domein is.<br>
Ook leerlingen uit STEM-richtingen krijgen meer zelfvertrouwen doordat ze erin slagen gekende principes van programmeren toe te passen in een nieuwe probleemstelling.


*Eindterm 4.2 (tweede en derde graad) - Compatibiliteit tussen digitale infrastructuur en toepassingen (tweede graad) - Standaardfunctionaliteiten/Functionaliteiten*

In de notebooks van het Chatbot-project wordt er gewerkt met strings. Dat is het type dat Python gebruikt voor tekst. Die tekst wordt dan bewerkt en/of verwerkt door eenvoudige functies aan te wenden.<br>
De leerlingen maken kennis met bestanden met de extensie ‘ipynb’, die enkel met geschikte software geopend kunnen worden.

Bij de sentimentanalyse moet de tekst in het juiste formaat worden aangeboden aan het AI-systeem, anders kan het AI-systeem niets doen. Bv. in de notebook (die gebruikmaakt van een regelgebaseerd AI-systeem) wordt de tekst voorverwerkt, zoals het vervangen van de hoofdletters door kleine letters en het terugbrengen van de woorden tot hun woordenboekvorm.<br>
Men kan aan de leerlingen meegeven dat ook in andere Natural Language Processing-toepassingen de tekst waarmee een AI-systeem moet werken, in het juiste formaat aangeboden moet worden. Dat ligt voor de hand bij automatische cyberpestdetectie, aangezien dat eigenlijk volgens dezelfde principes werkt als sentimentanalyse. Maar ook bij digitale assistenten is het formaat van de data belangrijk: een digitaal geluidsbestand moet eerst worden omgezet naar tekst d.m.v. spraakherkenningssoftware (spraak naar tekst) vooraleer de assistent de vraag kan analyseren en vervolgens een passend antwoord kan genereren.


*Eindterm 4.3 (tweede en derde graad) - Digitale structuur en toepassingen om digitaal te communiceren*

De chatbot is een voorbeeld van digitale communicatie. Door de chatbot-notebook te doorlopen, begrijpen de leerlingen de beperkingen en de mogelijkheden van zo’n systeem en zijn ze beter in staat een chatbot op een website op een adequate manier
te gebruiken.<br>
Het project ‘Chatbot’ geeft ook suggesties voor mogelijke activiteiten in de klas die dit inzicht bevorderen.<br>
Door zich te verdiepen in de sentimentanalyse worden de leerlingen zich meer bewust van wat er allemaal komt kijken bij de sociale media en kunnen ze er op een meer bewuste manier berichten posten.


*Eindterm 4.4 (tweede graad) - De bit als basiseenheid van data*

Data worden aan de computer gegeven in een digitaal formaat. Concreet betekent dit dat de data worden omgezet naar getallen, die op hun beurt worden voorgesteld door een rij van nullen en enen. Zo’n nul of zo’n één is een bit. Bv. de natuurlijke getallen van 0 t.e.m. 255 kunnen worden voorgesteld door een rij van 8 nullen en enen, bv. 35 is 00100011 (een rij van acht nullen en enen is een byte). Bijvoorbeeld, one hot encoding: bij tekst wordt aan de computer een lijst van woorden meegegeven in een bepaalde volgorde. Met een rij van nullen en een één, bijvoorbeeld 0000000000000001000000000...0, kan een bepaald woord dan aan de computer gegeven worden. In het voorbeeld staat de 1 op de zestiende plaats in de rij wat betekent dat het woord het zestiende woord in de woordenlijst is. Om aan de computer kenbaar te maken welke van de woorden in de woordenlijst voorkomen in een bepaalde
klantenreview, kan dan een rij nullen en enen, zoals 0010111010000001000000100...0, worden meegegeven. Dat betekent dat het derde, vijfde, zesde, zevende, negende, zestiende, drieëntwintigste ... woord in de review staat.


*Eindterm 4.4 (tweede en derde graad) - Zenden, ontvangen, verwerken, opslaan, afspraken tussen digitale systemen*

Om aan de slag te gaan met een notebook, wordt de URL (bv. https://kiks.ilabt.imec.be/jupyterhub/?id=2110) ingegeven in de webbrowser. Deze URL bevat een protocol (HTTPS; wat wijst op een veilige verbinding) en een domeinnaam, bv. kiks.ilabt.imec.be. <br>
De webbrowser legt via het internet contact met een DNS-server om het IP-adres (een numeriek internetadres) op te zoeken van de server van AI Op School. Vervolgens wordt de boodschap van de gebruiker (de client, hier de webbrowser van de computer
van de leerling of leerkracht) doorgegeven aan de webserver van AI Op School. Er wordt namelijk aan deze server gevraagd om toegang te geven tot de notebooks van AI Op School.<br>
Het Hypertext Transfer Protocol (HTTP) is een computerprotocol waarin afspraken zijn vastgelegd zodat een computer (in dit geval de computer van de leerling of leerkracht) en een andere computer (hier de webserver van AI Op School) met elkaar kunnen communiceren.<br>
HyperText Transfer Protocol Secure (HTTPS) is niets anders dan een uitbreiding van het HTTP-protocol om de uitwisseling van gegevens ook op een veilige manier te laten gebeuren. Het HTTPS-protocol versleutelt de gegevens. <br>
De server geeft dan toegang tot de verschillende projecten die op de server staan. Het gewenste project kan worden geselecteerd en nadien ook de gewenste notebook. Bij het doorlopen van de notebook communiceert de webbrowser voortdurend met de server, bv. bij het uitvoeren van een Python-script. Hierbij maakt de notebook bv. gebruik van de CPU (rekeneenheid) of de GPU (nog meer rekenkracht) van de server.

De leerling kan een notebook downloaden en opslaan op een eigen computer. Om de notebook opnieuw te kunnen openen op de eigen computer, zal op die computer wel geschikte software geïnstalleerd moeten zijn. Als een leerling een notebook wil uitprinten, dan moet de computer van de leerling kunnen communiceren met de printer. Ook hier is een protocol voor nodig.


*Eindterm 4.4 (tweede graad) - Algoritme*

De Python-scripts in de notebooks bevatten algoritmes die werden opgesteld om bepaalde doelen te bereiken.

Voorbeelden:

<ul><li>In een notebook over sentimentanalyse gaat een algoritme elk woord in een review één voor één af en zet het om naar zijn woordenboekvorm.</li></ul> 
<ul><li>In de chatbot-notebook checkt een algoritme of de gestelde vraag voorkomt in de dataset, waarop hij een overeenkomstig antwoord teruggeeft.</li></ul> 

Er zijn ook enkele notebooks die voorbereiden op de notebooks over sentimentanalyse en over chatbots. In deze notebooks passen de leerlingen een gegeven algoritme aan of stellen ze er zelf een op.


*Eindterm 4.4 (tweede graad) - Input, verwerking, output*

Voorbeelden:

<ul><li>In de notebooks van sentimentanalyse vertrekt men van een klantenreview (de input). Deze gegeven tekst wordt verwerkt: de tekst wordt voorverwerkt waarna hij in het juiste formaat kan worden aangeboden aan het AI-systeem. Vervolgens analyseert het AI-systeem de review. Dit leidt tot slot tot een output: de review is positief, negatief of neutraal.</li></ul> 
<ul><li>Bij de notebook over de chatbot geeft de gebruiker een vraag in; dat is de input. Vervolgens speurt het AI-systeem in de databank naar die vraag of een die er niet teveel van verschilt; dat is de verwerking. Tot slot geeft de chatbot een antwoord aan
de gebruiker, dat antwoord is de output.</li></ul> 
                    
                    
*Eindterm 4.4 (derde graad) - Databanken - - Beoordelen bouwstenen*

Door de chatbot-notebook te doorlopen en de activiteiten rond chatbots te doen, zien leerlingen in dat nog veel van de huidige chatbots werken a.d.h.v. een groot databestand met vragen en antwoorden erin.<br>
In de context van chatbots kunnen de tekstgenererende AI-systemen zoals GPT-2 en GPT-3 worden besproken. Dankzij het internet en crawlers is men in staat immense databanken aan te leggen waarop deze systemen worden getraind.


*Eindterm 4.4 (derde graad) - Analoge en digitale voorstellingen*

Zoals eerder vermeld wordt bij digitale assistenten een digitaal geluidsbestand eerst omgezet naar tekst d.m.v. spraakherkenningssoftware (spraak naar tekst) vooraleer de assistent de vraag kan analyseren en vervolgens een passend antwoord kan genereren. Dat digitaal geluidsbestand is zelf al een omzetting van een opname van een bepaald stemgeluid (een analoog geluidsbestand). Door de omzetting van analoog naar digitaal gaat steeds informatie verloren.


*Eindterm 4.5 (tweede en derde graad) - Concepten van computationeel denken*

In de notebooks van sentimentanalyse: decompositie (verschillende zaken moeten worden aangepakt bij het voorbereiden van de data) - algoritme - abstractie (gebruik van functies).<br>
In de chatbot-notebook: decompositie (vraag - antwoord; deelprobleem: wat als de gestelde vraag niet in de dataset zit).<br>
In de inhoud van project ‘Chatbot’: patroonherkenning (sentimentanalyse en cyberpestdetectie; chatbot en digitale assistent; plagiaatdetectie en auteursherkenning; profilering (sollicitatie - gepersonaliseerde reclame en nieuws)).


*Eindterm 4.5 (derde graad - Finaliteit doorstroom en dubbele finaliteit) - Digitale representatie van informatie*

Data en informatie zijn niet hetzelfde. Een computer werkt met data, die op de juiste manier gerepresenteerd moeten zijn. De informatie wordt door de mens uit de data afgeleid door de data te interpreteren.


*Eindterm 4.5 (tweede en derde graad - Finaliteit doorstroom en dubbele finaliteit)- Debuggen*

Leerlingen voeren de code voortdurend uit tijdens het doorlopen van de notebooks. Bij foutmeldingen dienen ze onmiddellijk de fout op te sporen en vervolgens de code aan te passen.<br>
Bij de chatbot-notebook merken de leerlingen dat de chatbot niet steeds zo goed functioneert. Daar passen ze de code aan om de effectiviteit van het script te verbeteren.


*Eindterm 4.5 (tweede en derde graad - Finaliteit doorstroom en dubbele finaliteit) - Principes van programmeren*

Sequentie - herhalingsstructuren - keuzestructuren komen aan bod in de notebooks.


*Eindterm 4.5 (tweede en derde graad - Finaliteit doorstroom en dubbele finaliteit) - Elementen van programmeertalen*

Begrippen zoals types, variabelen, operatoren, functies komen aan bod in de notebooks.<br>
Om de strings te bewerken wordt bv. de +-operator gebruikt. Iets op het scherm laten verschijnen, gebeurt met de functie print().


*Eindterm 4.6/4.5 (tweede en derde graad) - Wederzijdse invloeden tussen individu en media en maatschappij op leren, werken en vrije tijd*

In de inhoud van het Chatbot-project komen deze wederzijdse invloeden ruimschoots aan bod.<br>
Bedrijven en organisaties screenen socialemediaposts om te proberen te achterhalen hoe tevreden hun klanten zijn van hun diensten en producten. Ze kunnen de informatie die ze bekomen door de automatische sentimentanalyse gebruiken om hun diensten en producten eventueel aan te passen. Ook politieke partijen en de overheid detecteren (on)tevredenheid over hun standpunten of hun beleid, en baseren zich hierop om eventueel dat beleid bij te sturen of bepaalde intenties toch niet of juist wel door te voeren.<br>
Posts op sociale media worden door het betreffende platform zorgvuldig bijgehouden en blijvend gelinkt aan de gebruiker. Aan de hand van het profiel van de gebruiker dat men op die manier opmaakt, worden gepersonaliseerde reclame en gepersonaliseerd
nieuws aan de gebruiker aangeboden. Ook op basis van het koop- en klikgedrag van gebruikers met ‘verwante’ interesses wordt de ervaring op het socialemediaplatform gepersonaliseerd. Aanbevelingsalgoritmes kunnen zo bijvoorbeeld een sterke invloed
uitoefenen op het online shopgedrag (e-commerce).<br>
Omdat aanbevelingsalgoritmes ook steeds meer gebruikt worden op websites van online kranten en ook het resultaat van een zoekmachine steeds meer gepersonaliseerd wordt, is men best alert voor de filterbubbel. Als men onderhevig is aan een filterbubbel
kan het beeld dat men heeft van de wereld misvormd zijn. Als men bv. wil leren over een onderwerp waar men niet vertrouwd mee is, dan kan men door zo’n bubbel een ongenuanceerd beeld krijgen.<br>
Dankzij automatische vertaling kan leren gemakkelijker en rijker worden, bv. omdat teksten in een andere taal nu ook toegankelijk zijn.


*Eindterm 4.6/4.5 (tweede en derde graad) - Datawijsheid*

Leerlingen beseffen door de projectinhouden hoe data die zij achterlaten op het world wide web door verschillende partijen kunnen worden aangewend en met elkaar in verband kunnen worden gebracht. Ze moeten beseffen dat omdat de reclame gepersonaliseerd is, ze er mogelijk vatbaarder voor zijn.


*Eindterm 4.7/4.6 (tweede en derde graad) - Ethiek*

Leerlingen zijn zich ervan bewust dat met nieuwe technologieën ook ethische aspecten kunnen opduiken. In het Chatbot-project worden voorbeelden van ethische aspecten aangereikt die gebruikt kunnen worden als onderwerp voor een klasgesprek.


*Eindterm 4.7/4.6 (tweede en derde graad) - Anonimiteit op het wereldwijde web*

Anonimiteit op het web kan drempels wegnemen, bv. om te gaan cyberpesten of om haatspraak te verspreiden. Anderzijds is men m.b.v. AI-systemen soms wel al in staat de anonieme auteur van een bepaalde tekst te achterhalen.


*Eindterm 4.7/4.6 (tweede en derde graad) - Dynamisch karakter van de digitale wereld*

Voorbeeld: digitale assistenten geraken steeds meer ingeburgerd thuis, via smartphone, in de auto. Robots komen steeds meer in beeld. Er is een wisselwerking tussen maatschappelijke noden en ontwikkelingen in de computerwetenschappen.


*Eindterm 4.8/4.7 (tweede en derde graad) - Risico’s mediagedrag*

In het Chatbot-project worden voorbeelden gegeven van nieuwe praktijken die steeds meer hun weg vinden naar de sector van human resource, zoals het screenen van sociale media. Leerlingen beseffen dat wat op socialemediaplatformen gepost wordt, er
binnen enkele jaren als zij gaan solliciteren nog steeds te vinden is.
