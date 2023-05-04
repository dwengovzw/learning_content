---
hruid: aiz_etdigitalecompetentiezorg
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
# Digitale competentie en mediawijsheid 
## Eindtermen digitale competentie en mediawijsheid, en het '*AI in de Zorg*'-project 

*Eindterm 4.1 (tweede en derde graad) - Zelfvertrouwen* 

Men moet geen bolleboos zijn in wiskunde en wetenschappen, noch moet men een kei zijn in programmeren om met de notebooks van AI in de Zorg aan de slag te gaan.<br>
Door de leerlingen positieve ervaringen te bieden in een voor hen waarschijnlijk ongekend domein dat echter maatschappelijk relevant is en gelinkt is aan hun leefwereld - iedereen moet wel eens naar de dokter of het ziekenhuis -, kan hun zelfvertrouwen betreffende informaticawetenschappen, in het bijzonder programmeren en artificiële intelligentie, een boost krijgen.<br>
De leerlingen uit niet-STEM-richtingen zien door te werken met de notebooks van het project ‘AI in de Zorg’ in dat sommige programmeeropdrachten ook voor hen haalbaar domein zijn.<br>
Ook leerlingen uit STEM-richtingen krijgen meer zelfvertrouwen doordat ze erin slagen gekende principes van programmeren en concepten van computationeel denken toe te passen in een nieuwe probleemstelling. 


*Eindterm 4.2 (tweede en derde graad) - Compatibiliteit tussen digitale infrastructuur en toepassingen (tweede graad) - Standaardfunctionaliteiten/Functionaliteiten* 

In de notebooks van het ‘AI in de Zorg’-project wordt er gewerkt met datasets. De leerlingen verwerken de data met Python om te komen tot een beslissingsboom. Ze kunnen daarvoor een beroep doen op bestaande Python-modules, maar moeten er wel voor zorgen dat de gebruikte data compatibel zijn met de functionaliteiten van de aangewende module. De data moeten in het juiste formaat worden aangeboden aan het regelgebaseerd AI-systeem. Daartoe moeten de data soms eerst voorbereid worden: bv. patiënten waarvan gegevens ontbreken, verwijderen uit de dataset, en de waarden van categorische variabelen omzetten naar numerieke waarden. Gelukkig bestaan ook daar reeds eenvoudige functies voor die de leerlingen kunnen inzetten. De data worden dan tekst wordt dan gebruikt om een beslissingsboom te genereren a.d.h.v. eenvoudige functies aanwezig in de gebruikte module.<br>
De leerlingen maken kennis met bestanden met de extensie ‘ipynb’, die enkel met geschikte software geopend kunnen worden.<br>
Men kan aan de leerlingen meegeven dat bv. ook in Natural Language Processing-toepassingen de tekst waarmee een AI-systeem moet werken, in het juiste formaat aangeboden moet worden. Een chatbotchatbot of een digitale assistenten kunnen hierbij als voorbeeld gegeven worden. Een chatbot werkt bv. met getypte tekst die eerst voorverwerkt wordt vooraleer een AI-systeem ermee aan de slag gaat; een digitaal geluidsbestand moet eerst worden omgezet naar tekst d.m.v. spraakherkenningssoftware (spraak naar tekst) vooraleer de assistent de vraag kan analyseren en vervolgens een passend antwoord kan genereren.<br>
Hetzelfde geldt als men het elektronisch patiëntendossier inspreekt, i.p.v. van de tekst te typen. 


*Eindterm 4.3 (tweede en derde graad) - Digitale structuur en toepassingen om digitaal te communiceren* 

<ul><li>De chatbot voor het anamnesegesprek is een voorbeeld van digitale communicatie.</li></ul>
<ul><li><em>Wearables</em> zijn ook een vorm van digitale communicatie, zij het tussen digitale systemen. De geautomatiseerde vorm van het EWS valt hier ook onder.</li></ul>
<ul><li>Als leerlingen een <em>fitness tracker</em> gebruiken, doen ze dat dan doelgericht? Weten ze wat er met de verzamelde data gebeuren?</li></ul>


*Eindterm 4.4 (tweede graad) - De bit als basiseenheid van data* 

Data worden aan de computer gegeven in een digitaal formaat. Concreet betekent dit dat de data worden omgezet naar getallen, die op hun beurt worden voorgesteld door een rij van nullen en enen. Zo’n nul of zo’n één is een bit. Bv. de natuurlijke getallen van 0 t.e.m. 255 kunnen worden voorgesteld door een rij van 8 nullen en enen, bv. 35 is 00100011 (een rij van acht nullen en enen is een byte).<br>
Bijvoorbeeld, *one hot encoding*: bij tekst (bv. voor een elektronisch patiëntendossier) wordt aan de computer een lijst van woorden meegegeven in een bepaalde volgorde. Met een rij van nullen en een één, bijvoorbeeld 0000000000000001000000000...0 , kan een bepaald woord dan aan de computer gegeven worden. In het voorbeeld staat de 1 op de zestiende plaats in de rij wat betekent dat het woord het zestiende woord in de woordenlijst is. Om aan de computer kenbaar te maken welke van de woorden in de woordenlijst voorkomen in een patiëntendossier, kan dan een rij nullen en enen, zoals 0010111010000001000000100...0 , worden in het dossier staat.<br>
meegegeven. Dat betekent dat het derde, vijfde, zesde, zevende, negende, zestiende, drieëntwintigste ... woord Nog een voorbeeld is medische beeldvorming. Voor een computer is een foto niets anders dan een tabel met getallen. De computer kan daardoor heel snel door te rekenen het verschil tussen twee foto’s ontdekken en zelfs heel subtiele veranderingen opsporen en signaleren aan de radioloog.<br>
Voor de EWS-score worden waarden van lichaamsparameters aan de computer gegeven, dat kunnen natuurlijk getallen (type int) zijn, of decimale getallen (type float) of ook tekst (type string). 


*Eindterm 4.4 (tweede en derde graad) - Zenden, ontvangen, verwerken, opslaan, afspraken tussen digitale systemen* 

Om aan de slag te gaan met een notebook, wordt de URL ingegeven in de webbrowser. Deze URL bevat een protocol (HTTPS; wat wijst op een veilige verbinding) en een domeinnaam (kiks.ilabt.imec.be/jupyter).<br>
De webbrowser legt via het internet contact met een DNS-server om het IP-adres (een numeriek internetadres) op te zoeken van de server van AI Op School. Vervolgens wordt de boodschap van de gebruiker (de client, hier de webbrowser van de computer van de leerling of leerkracht) doorgegeven aan de webserver van AI Op School. Er wordt namelijk aan deze server gevraagd om toegang te geven tot de notebooks van AI Op School.<br>
Het *Hypertext Transfer Protocol* (HTTP) is een computerprotocol waarin afspraken zijn vastgelegd zodat een computer (in dit geval de computer van de leerling of leerkracht) en een andere computer (hier de webserver van AI Op School) met elkaar kunnen communiceren.<br>
*HyperText Transfer Protocol* Secure (HTTPS) is niets anders dan een uitbreiding van het HTTP-protocol om de uitwisseling van gegevens ook op een veilige manier te laten gebeuren. Het HTTPS-protocol versleutelt de gegevens.<br>
De server geeft dan toegang tot de notebook van het ‘AI in de Zorg’-project. Het gewenste project kan worden geselecteerd en nadien ook de gewenste notebook. Bij het doorlopen van de notebook communiceert de webbrowser voortdurend met de server, bv. bij het uitvoeren van een Python-script. Hierbij maakt de notebook bv. gebruik van de CPU (rekeneenheid) of de GPU (nog meer rekenkracht) van de server. 

De leerling kan een notebook downloaden en opslaan op een eigen computer. Om de notebook opnieuw te kunnen openen op de eigen computer, zal op die computer wel geschikte software geïnstalleerd moeten zijn.<br>
Als een leerling een notebook wil uitprinten, dan moet de computer van de leerling kunnen communiceren met de printer. Ook hier is een protocol voor nodig. 


*Eindterm 4.4 (tweede graad) - Algoritme* 

De Python-scripts in de notebooks bevatten algoritmes die werden opgesteld om een beslissingsboom te bekomen.<br>
In het bijzonder wordt voor het manueel opstellen van een beslissingsboom een ‘verdeel en heers’-algoritme gebruikt. In deze unplugged activiteit ondervinden de leerlingen het iteratief proces, dat de computer ook en veel sneller kan uitvoeren, aan den lijve. De leerlingen stellen manueel een beslissingsboom op a.d.h.v. de gini-index en vertrekkende van gelabelde data. Nadien geven ze dezelfde data aan de computer waarmee ze met Python dezelfde beslissingsboom genereren. Python werkt in de notebook ook met de gini-index; de leerlingen worden er mee geconfronteerd dat de computer het veel sneller kan.<br> 
Voorbeelden: 

<ul><li>Sommige notebooks bevatten enkel een algoritme dat de data inleest en daarop gebaseerd een beslissingsboom genereert.</li></ul> 
<ul><li>In andere notebooks is datzelfde algoritme uitgebreid met enkele instructies om de data voor te bereiden.</li></ul>
<ul><li>In de chatbot-notebook checkt een algoritme of de gestelde vraag voorkomt in de dataset, waarop hij een overeenkomstig antwoord teruggeeft.</li></ul> 

Er zijn ook enkele notebooks die voorbereiden op de notebooks over beslissingsbomen en over chatbots. In deze notebooks passen de leerlingen een gegeven algoritme aan of stellen ze er zelf een op. 


*Eindterm 4.4 (tweede graad) - Input, verwerking, output* 

Voorbeelden: 

<ul><li>In de notebooks vertrekt men van data (de input), dit zijn bij AI in de Zorg meestal patiëntengegevens. Deze gegevens worden verwerkt: de data worden voorverwerkt waarna ze in het juiste formaat kunnen worden aangeboden aan het AI-systeem. Vervolgens gaat het AI-systeem met de data aan de slag. Dit leidt tot slot tot een output: de beslissingsboom.</li></ul> 
<ul><li>Eens men beschikt over een beslissingsboom, gebruikt men die om over een nieuwe, niet eerder geziene patiënt een voorspelling te maken, bijvoorbeeld: Loopt deze patiënt risico op een hartaanval? Zal een bepaalde patiënt de dag na de operatie al naar huis kunnen? De gegevens van de nieuwe patiënt zijn de invoer, deze gegevens worden ingevoerd in de beslissingsboom en volgen dan een pad, afhankelijk van de antwoorden op de opeenvolgende vragen, totdat een blad bereikt wordt; dat is de verwerking. De informatie die het blad verstrekt, is de uitvoer.</li></ul> 
<ul><li>Bij de notebook over de chatbot geeft de gebruiker een vraag in; dat is de input. Vervolgens speurt het AI-systeem in de databank naar die vraag of een die er niet teveel van verschilt; dat is de verwerking. Tot slot geeft de chatbot een antwoord aan de gebruiker, dat antwoord is de output.</li></ul> 


*Eindterm 4.4 (tweede graad) - Foutmeldingen* 

Als de leerlingen in hun Python-script data gebruiken die niet voldoen aan het formaat dat de gebruikte functies vragen, dan zullen ze een foutmelding te zien krijgen in de notebook ten gevolge van het compatibiliteitsprobleem. 


*Eindterm 4.4 (derde graad) - Databanken, digitale systemen - Beoordelen bouwstenen* 

In de notebooks genereert een regelgebaseerd systeem een beslissingsboom gebaseerd op grote datasets die manueel moeilijk te verwerken zijn. De data zijn opgeslagen in een csv-bestand.<br>
In het project ‘AI in de Zorg’ komen digitale systemen aan bod, zoals wearables, monitorsystemen in ziekenhuizen.<br>
Door de chatbot-notebook te doorlopen en de activiteiten rond chatbots te doen, zien leerlingen in dat nog veel van de huidige chatbots werken a.d.h.v. een groot databestand met vragen en antwoorden erin. 


*Eindterm 4.4 (derde graad) - Analoge en digitale voorstellingen* 

Zoals eerder vermeld wordt bij digitale assistenten een digitaal geluidsbestand eerst omgezet naar tekst d.m.v. spraakherkenningssoftware (spraak naar tekst) vooraleer de assistent de vraag kan analyseren en vervolgens een passend antwoord kan genereren. Dat digitaal geluidsbestand is zelf al een omzetting van een opname van een bepaald stemgeluid (een analoog geluidsbestand). Door de omzetting van analoog naar digitaal gaat steeds informatie verloren.<br?>
Spraakherkenningssoftware wordt ook gebruikt als men bv. een elektronisch patiëntendossier inspreekt of een robot aanspreekt. Het stemgeluid (een analoog geluidsbestand) wordt omgezet naar getypte tekst of naar een formaat dat de robot kan begrijpen. 


*Eindterm 4.5 (tweede en derde graad) - Concepten van computationeel denken* 

In de notebooks: decompositie (verschillende zaken moeten worden aangepakt bij het voorbereiden van de data) - algoritme - abstractie (gebruik van functies).<br>
Patroonherkenning: problemen uit heel verschillende contexten kunnen met een gelijksoortig AI-systeem worden aangepakt, hier een beslissingsboom. 


*Eindterm 4.5 (derde graad - Finaliteit doorstroom en dubbele finaliteit) - Digitale representatie van informatie* 

Data en informatie zijn niet hetzelfde. Een computer werkt met data, die op de juiste manier gerepresenteerd moeten zijn. De informatie wordt door de mens uit de data afgeleid door de data te interpreteren. 


*Eindterm 4.5 (tweede en derde graad - Finaliteit doorstroom en dubbele finaliteit) - Programmeertaal, programma, principes van programmeren, debuggen* 

De leerlingen zetten eenvoudige stappen in Python. Ze verwerven inzichten a.d.h.v. een voorbeeldprogramma en passen dat programma aan aan nieuwe contexten. Het kan ook dat ze het programma moeten uitbreiden met extra instructies om de data voor te verwerken.<br>
Sequentie komt aan bod in de notebooks, debuggen en ook het werken met ingebouwde functies.<br>
Leerlingen voeren de code voortdurend uit tijdens het doorlopen van de notebooks. Bij foutmeldingen dienen ze onmiddellijk de fout op te sporen en vervolgens de code of de data aan te passen. 


*Eindterm 4.5 (tweede en derde graad - Finaliteit doorstroom en dubbele finaliteit) - Elementen van programmeertalen* 

Begrippen zoals types (bv. *string*, *int*, *float* en *NumPy array*), variabelen (bv. variabelen die refereren aan de data of aan de gegenereerde beslissingsboom), en functies (bv. de ingebouwde functies die gebruikt worden) komen aan bod in de notebooks. Eventueel kunnen ook operatoren aan bod komen.<br>
Om een gegeven op te zoeken in een *NumPy array*, wordt bv. een vergelijkingsoperator of een logische operator gebruikt. Iets op het scherm laten verschijnen, gebeurt met de functie print(). 


*Eindterm 4.6/4.7 (tweede en derde graad) - Wederzijdse invloeden tussen individu en media en maatschappij op leren, werken en vrije tijd* 

In de inhoud van het ‘AI in de Zorg’-project komen deze wederzijdse invloeden ruimschoots aan bod. De wisselwerking tussen technologische ontwikkelingen en de maatschappij kunnen mooi geïllustreerd worden via de oorzaken van de AI-winters en -zomers. Ook de noden die ontstaan in de maatschappij, denk bv. aan het personeelstekort in de zorgsector, beïnvloeden de aanwezigheid en ontwikkeling van nieuwe technologie. Ethische aspecten, bv. het belang van sociaal contact, hebben zeker ook hun invloed. In de inhouden van het project worden toch wel wat voorbeelden omschreven. 


*Eindterm 4.6/4.7 (tweede en derde graad) - Datawijsheid, e-inclusie* 

Leerlingen beseffen door de projectinhouden hoe perssonlijke data door verschillende partijen kunnen worden aangewend en met elkaar in verband kunnen worden gebracht.<br>
Ze zien in dat data van veel patiënten verzamelen en verwerken kan leiden tot nieuwe inzichten die belangrijk kunnen zijn voor een betere gezondheidszorg. Anderzijds staan ze steel bij de privacy-aspecten die hiermee gemoeid zijn.<br>
Ze kunnen meer bewust omgaan met wearables, fitness trackers, en wie en waarom ze inzage geven in hun elektronisch patiëntendossier.<br>
COVID-19 heeft ook getoond dat patiëntendata belangrijk zijn voor het controleren van de pandemie. Ook e-inclusie staat hiermee in verband: niet iedereen heeft een smartphone om de ‘Coronalert’-app te gebruiken. 


*Eindterm 4.7/4.8 (tweede en derde graad) - Ethiek* 

Leerlingen zijn zich ervan bewust dat met nieuwe technologieën ook ethische aspecten kunnen opduiken. Omdat men in de zorgsector werkt met mensen, zijn de ethische vraagstukken daar prominent aanwezig. In het ‘AI in de Zorg’-project worden voorbeelden van ethische aspecten aangereikt die gebruikt kunnen worden als onderwerp voor een klasgesprek. 


*Eindterm 4.7/4.8 (tweede en derde graad) - Risico’s mediagedrag* 

De leerlingen zien in dat bij het verzamelen en verwerken van patiëntendata moet nagedacht worden over privacy issues en dat men daar bewust mee moet omspringen.<br>
In de context van de COVID-19 pandemie werd al meermaals duidelijk dat opvattingen over privacy al eens kunnen veranderen als de situatie verandert; denk bv. aan de app ‘Coronalert’ en het ‘Covid Safe Ticket’. Dat is op zich niet fout, maar leerlingen moeten zich daar wel bewust van zijn.