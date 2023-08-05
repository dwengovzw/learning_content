---
hruid: ct9_4
version: 3
language: nl
title: "Home assistant"
description: "Home assistant"
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
# Spraakassistent en reclame

**Wat is de impact van het gebruik van een spraakassistent op de reclame die we te zien krijgen? Worden we collectief afgeluisterd?**

De volgende vraag hoor je wel vaker: Luisteren spraakassistenten de hele tijd naar wat we zeggen? En doen ze daar dan ook iets mee? Is het toevallig dat ik reclame krijg over een bepaald product, nu ik daar me een vriendin over gesproken heb?<br>
Om hierop een duidelijk antwoord te kunnen geven, bekijk je eerst enkele aspecten van de werking van zo'n *voice assistant*, zoals Siri, Alexa of Google assistent.   

> **Leestips:**<br>

## Principes van computationeel denken

![ct-schema](@learning-object/m_ct_impact_4/nl/3)


## Bespreking van de impact

-  Indien een spraakassistent voortdurend actief zou meeluisteren, dan zou de **batterij** van je smartphone of ander toestel steeds snel leeg zijn.
-  Indien een spraakassistent voortdurend actief zou meeluisteren - **actief meeluisteren betekent dat alles wat de assistent hoort ook opgeslagen wordt** - om daar iets mee te doen - wat betekent dat elk geluidsfragment omgezet wordt naar getypte tekst - dan zou dat gaan over een **enorme hoeveelheid data** in de cloud. Het is onmogelijk dat de verstrekkers van zulke systemen van alle gebruikers alles bewaren.
-  Je moet dus het onderscheid maken tussen actief en passief luisteren. De spraakassistent luistert steeds passief mee en bij het 'horen' van een trigger-woord zal deze overschakelen naar actief luisteren. Op dat moment wordt wat de assistent hoort, ook opgeslagen, en elk geluidsfragment wordt omgezet naar getypte tekst. Deze tekst wordt dan aangeboden aan een AI-systeem die er iets mee doet. Dat alles gebeurt in een oogwenk.
-  Dus krijg je reclame over een product dat je eerder met een vriendin besprak, dan is dat toeval.
-  Heb je echter **iets gevraagd aan de spraakassistent**, en je krijgt in dat verband achteraf reclame, dan is het een ander verhaal.
-  Je kan de indruk krijgen dat je afgeluisterd wordt als je plots reclame krijgt voor een product dat je de dag ervoor nog besprak met een vriendin. Dit valt echter te verklaren
    -  door het *Baader-Meinhoffenomeen* (omdat je er de dag voordien over sprak, valt de advertentie meer op) (bron: factcheck);
    -  *confirmation bias* (je vermoeden dat je afgeluisterd wordt, is bevestigd door de advertentie);
    -  of je kan het toeschrijven aan *lookalike audiences* (via **patroonherkenning** worden jou dezelfde interesses toegedicht als van iemand met een soortgelijk profiel). 
-  Ook dit verdient voldoende aandacht: Hoe worden de data die de systemen verzamelen, bewaard, gebruikt, gedeeld en verwijderd?
    - Een rapport uit 2019 van het Capgemini Research Institute geeft aan dat een goede samenwerking tussen de in-car voice assistant, de home assistant en de digitale assistent op de smartphone van de gebruikers gewenst is. Dan zouden ze bv. met de in-car voice assistant de garagepoort kunnen openen en de verwarming thuis kunnen aanzetten. Maar zo’n integratie brengt ook aspecten van privacy met zich mee:
er worden dan immers data gedeeld tussen meerdere toepassingen (Walch, 2020). In theorie zou de digitale assistent op de smartphone zo te weten kunnen komen waar de gebruiker geweest is met de auto.
    - Waar zal de data terechtkomen? Kan dat gevolgen hebben later bij het aanvragen voor een lening bijvoorbeeld?

-----------------------------
## Gerelateerde voorbeelden: 

-----------------------------
### Werking 

In het leerpad  wordt [de werking] uit de doeken gedaan.

Om via gesproken taal over en weer te kunnen communiceren met een digitale assistent, zoals Siri op een iphone, Alexa thuis en de
voice assistant in de auto, is zowel spraakherkenningstechnologie (spraak naar tekst) als spraaksynthesesoftware (tekst naar spraak) nodig. De spraaksynthesesoftware is er om de spraakassistent te laten spreken, de spraakherkenningssoftware opdat hij de mens die tegen hem spreekt, zou begrijpen. 

De gesproken taal van de gebruiker wordt automatisch omgezet naar geschreven tekst via spraakherkenningstechnologie (spraak naar tekst) zodat de digitale assistent ermee aan de slag kan. Spraakherkenningstechnologie is een AI-systeem dat geluid kan verwerken. Het werkt met een opname van geluid die wordt omgezet naar een digitaal bestand. Het AI-systeem analyseert dan dat bestand. Dat is zeker geen eenvoudige taak aangezien iedereen zich op zijn eigen manier uitdrukt, zelfs in dezelfde taal. Bovendien moet het systeem menselijke spraak kunnen onderscheiden van eventueel achtergrondlawaai. ML-systemen beginnen echter ook al dialecten van eenzelfde taal van elkaar te kunnen onderscheiden.

Om een digitale assistent of robot te laten spreken, wordt een tekstbestand met spraaksynthesesoftware omgezet naar geluid (zie ook de kader ‘Realistisch stemgeluid’). 

Alle technieken op getypte tekst, zoals sentimentanalyse, kunnen, zij het onrechtstreeks, ook toegepast worden op gesproken tekst. Het principe is net hetzelfde want spraaktekst wordt eerst omgezet naar geschreven tekst en daarop wordt sentimentanalyse uitgevoerd, net
zoals je dat rechtstreeks op geschreven tekst zou doen. Wat je zegt tegen de spraakassistent, kan dus ook gebruikt worden voor *profilering*; via een AI-systeem wordt er een profiel van jou opgesteld dat dan kan dienen om jou gepersonaliseerde reclame te sturen. Mogelijk kan je dit door bepaalde instellingen op het betreffende digitale toestel voorkomen; hiervoor bekijk je best het privacybeleid eens.   

Bij sommige apps heb je (impliciet) toestemming gegeven om je microfoon te gebruiken en mee te luisteren. Die apps zullen ook niet de hele tijd luisteren, maar occasioneel zullen ze dat wel doen als ze getriggerd worden. Wat deze triggers zijn, is niet altijd duidelijk, misschien het gebruik van een bepaalde functie of gebaseerd op je locatie. 

Wat je tegen de spraakassistent zegt, komt terecht in de cloud. Als je aan Siri het commando geeft om het licht uit te doen, dan wordt er meer dan één AI-systeem in gang gezet. Op het moment dat je ‘Hey Siri’ zegt, wordt het systeem achter Siri geactiveerd en wordt de gesproken opdracht opgeslagen. Deze opname wordt doorgestuurd naar een datacentrum. Achtereenvolgens wordt je spraakopdracht omgezet naar getypte tekst, wordt er bepaald welke actie er ondernomen moet worden, en wordt de vereiste instructie teruggestuurd naar je smartphone. Je smartphone geeft een gepaste instructie aan je verlichtingsinstallatie waarop tot slot het licht bij jou in de kamer uitgaat (Hulstaert, 2023).


-----------------------------
#### Leestips

[Apps kunnen meeluisteren, maar doen ze dat wel?](https://factcheck.vlaanderen/factcheck/apps-kunnen-meeluisteren-doen-wel)<br>
[VOICE ASSISTANTS](https://data-en-maatschappij.ai/publicaties/brainfood-databescherming-en-voice-assistants-1)<br>
[About lookalike audiences](https://www.facebook.com/business/help/164749007013531?id=401668390442328)

#### Luistertip

Radio 1. Bij Debecker. Gesprek vanaf minuut 3:09. ["We hoeven niet meteen bang te zijn dat apps ons constant afluisteren"](https://radio1.be/lees/we-hoeven-niet-meteen-bang-te-zijn-dat-apps-ons-constant-afluisteren) 

------------------------------
##### Bronnen

Capgemini Research Institute (2019). *Voice on the go. How can auto manufacturers provide a superior in-car voice experience.* Geraadpleegd op 9 augustus 2021 via https://www.capgemini.com/wp-content/uploads/2019/11/Report-%E2%80%93-Voice-on-the-Go.pdf<br>
Fabri M. (15 april 2019), *Apps kunnen meeluisteren, maar doen ze dat wel?* [Blogpost]. Factcheck Vlaanderen. Geraadpleegd op 5 augustus 2023 via https://factcheck.vlaanderen/factcheck/apps-kunnen-meeluisteren-doen-wel <br>
Hulstaert E. (15/1/2023). *Interview met Steven Latré (Imec): ‘Als AI niet duurzamer wordt, is het gedoemd om te falen’*, Knack. Geraadpleegd op  2023 via https://www.knack.be/nieuws/technologie/steven-latre-imec-als-ai-niet-duurzamer-wordt-is-het-gedoemd-om-te-falen/<br>
Walch, K. (2020). *The Unique Challenges Of Voice Assistants In Vehicles*. Geraadpleegd op 9 augustus 2021 via https://www.forbes.com/sites/cognitiveworld/2020/09/29/the-unique-challenges-of-voice-assistants-invehicles/
