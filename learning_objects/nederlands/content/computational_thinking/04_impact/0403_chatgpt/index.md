---
hruid: ct04_03
version: 3
language: nl
title: "ChatGPT"
description: "ChatGPT"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [12, 13, 14, 15, 16, 17, 18]
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
# ChatGPT

In november 2022 lanceerde OpenAI ChatGPT. En hoewel GPT er al is sinds 2018 en toepassingen op grote taalmodellen al enige tijd aanwezig zijn op het world wide web, kwamen velen tot het besef dat kunstmatige intelligentie toch geen sciencefiction is. <br>
Sindsdien staan de kranten er vol van en wordt de ene na de andere (commerciële) toepassing ontwikkeld. ChatGPT heeft reeds toepassingen in verschillende domeinen, zoals het aanwerven van nieuw personeel en het automatisch genereren van nieuwssites. Tegelijkertijd brengt ChatGPT ook zorgen met zich mee, zoals het verspreiden van desinformatie.<br>
De komst van ChatGPT heeft een grote impact, bijvoorbeeld op het onderwijs. Zo zijn leerkrachten op hun hoede voor het mogelijk frauderen van leerlingen. Ze zijn bijvoorbeeld sneller achterdochtig als leerlingen een vlotte tekst indienen; heel wat leerkrachten herdenken daarom de opdrachten voor hun leerlingen. Anderzijds gebruiken ze zelf ChatGPT om oefeningen op te stellen. 

In dit leerpad ga je dieper in op een van de aspecten van ChatGPT: een aspect dat van wezenlijk belang is voor de impact van het AI-systeem. 

**Impact: Omdat de antwoorden van ChatGPT vlot en zelfzeker klinken, worden deze antwoorden vaak onterecht als correct aangezien.**<br>

<div class="alert alert-box alert-info">
    Murray Shanahan zegt dat we goed moeten beseffen wat een groot taalmodel doet. "Veronderstel dat we de volgende prompt geven aan een LLM: “The first person to walk on the Moon was”,  en stel dat het antwoordt met “Neil Armstrong”. Wat vragen we hier eigenlijk? Het is belangrijk om in te zien dat we eigenlijk niet vragen wie de eerste persoon was die op de maan wandelde. De vraag die we echt stellen aan het model is de volgende vraag:  Gegeven de  statistische verdeling van de woorden in de uitgebreide publieke corpus van (Engelse) tekst, welke woorden volgen er het meest waarschijnlijk op de reeks “The first person to walk on the Moon was ”? Een goed antwoord op deze vraag is “Neil Armstrong” (Bron: Talking About Large Language Models, Murray Shanahan, 2022).
</div>

Het komt dus voor dat ChatGPT 'hallucineert', anders gezegd: onzin verkoopt.


## Principes van computationeel denken

![ct-schema](@learning-object/m_ct04_03/nl/3)

 
* ChatGPT kan worden opgesplitst in verschillende componenten, zoals het taalmodel zelf, de trainingsgegevens, en de interface die mensen gebruiken om met het model te communiceren.

* ChatGPT gebruikt patroonherkenning om natuurlijke taal te begrijpen en te genereren. Het model leert patronen in tekstdata en gebruikt deze om zinnen te vormen die coherent en relevant zijn.



## Bespreking van de impact



De training van ChatGPT is een combinatie van gesuperviseerd, ongesuperviseerd en versterkend leren:
- Gesuperviseerd leren: Hij heeft eerst allemaal digitale teksten aangeboden gekregen, bv. wikipedia, boeken die online staan, online discussiefora … Daarin heeft hij allerlei patronen in herkend. A.d.h.v.  al die teksten leerde hij teksten genereren, gebaseerd op een gegeven stuk tekst. Dus gegeven een stuk tekst, leerde hij voorspellen welke woorden er het meest waarschijnlijk erop volgen. Vervolgens heeft men het model geleerd om ook met dialoog om te gaan, m.a.w. leren antwoorden op een prompt. - Ongesuperviseerd leren: Vervolgens heeft men hem teksten laten genereren. Mensen hebben dan telkens 3 teksten gerangschikt: goed – beter – best, naar wat zij de meest wenselijke of menselijke tekst vinden. Op basis daarvan heeft men ongesuperviseerd een scoresysteem getraind. Dit scoresysteem heeft dus zelf moeten achterhalen aan welk patroon de meest wenselijke output beantwoordt.  - Versterkingsgebaseerd leren: op basis van dat scoresysteem heeft het systeem zichzelf verbeterd om zo menselijk mogelijk te antwoorden op een prompt.

![trainingchatgpt](https://github.com/dwengovzw/learning_content/assets/48352335/252a8bf4-6ff2-4f60-b81b-a23d7919fb2f)




------
Tevredenheid over een chatbotgesprek kan bijdragen aan de klantentevredenheid of die voor een stuk teniet doen. <br>
- Mensen verwachten van een chatbot dat die efficiënt is, en een vriendelijke, beleefde persoonlijkheid heeft. Het is daarom van belang dat reeds bij het begin van een conversatie met een chatbot wordt aangegeven waarmee de chatbot een gebruiker van dienst kan zijn.
- Gebruikers verwachten snelle en degelijke antwoorden van de chatbot, en wensen via de chatbot effectief tot een oplossing van een probleem te komen.
- Een chatbot herkent ook best een terugkerende gebruiker, zodat er eventueel ingepikt kan worden op een voorgaand gesprek.
- Gebruikers zijn geërgerd of gefrustreerd als de chatbot hun vraag niet begrijpt of naast de kwestie antwoordt.
- Bovenal willen gebruikers het duidelijk vermeld zien dat ze met een bot chatten en niet met een mens; ze verwachten dat dat wordt aangegeven.

Als een bedrijf of organisatie een chatbot op de website plaatst, dan wil men ook dat die zoveel mogelijk gebruikt wordt. De chatbot moet dus tegemoetkomen aan de noden van de gebruikers.
Vooraleer men een chatbot begint te ontwikkelen, moet men dus eerst de doelgroep afbakenen en hun noden vaststellen. Ook gaat men best na of het met de huidige technologie wel al mogelijk is om het vooropgestelde doel te bereiken. Men moet daarbij rekening houden met tal van zaken. 
- Eenzelfde vraag kan bijvoorbeeld op verschillende manieren gesteld worden. Bijvoorbeeld “Zal het vandaag de hele dag regenen?” of “Wordt het vandaag een miezerige dag?”.
Om een vraag te begrijpen kan wereldkennis, kennis van de fysieke wereld, nodig zijn. Bijvoorbeeld “Is het morgen bikiniweer?”.
- Er kan humor, ironie of sarcasme in een boodschap verscholen zitten. Bijvoorbeeld “Joepie, mijn trein is weer goed op tijd”.

De meest eenvoudige chatbots, waaronder de eerste chatbots zoals ELIZA, zijn regelgebaseerde systemen. Bij zulke chatbots zijn verschillende scenario’s expliciet
geprogrammeerd. Dit leidt automatisch tot beperkingen waardoor gebruikers zich moeten aanpassen aan de limieten van het systeem. Bijvoorbeeld als men een vraag aan de chatbot anders formuleert dan geprogrammeerd, dan zal de chatbot de vraag niet herkennen. Zulke chatbots zijn vaak niet populair, maar worden toch nog op veel websites gebruikt.
Moderne chatbots maken gebruik van Natural Language Processing (NLP), dus van machine learning; met deep learning herkent een chatbot wel al vragen met een soortgelijke inhoud.

M.b.v. NLP kan men ook proberen te achterhalen hoe tevreden een gebruiker is over een dienst geleverd door een chatbot of wat de gemoedstoestand van die gebruiker is. Men wendt daarvoor sentimentanalyse en emotiedetectie aan. Geschreven tekst kan immers indicaties bevatten van de emoties, intenties (bv. ook ironie) en opinies van de auteur. Indien het bijvoorbeeld
nodig zou blijken uit de sentimentanalyse, kan een chatbot een opgestart gesprek bijsturen of doorgeven aan een menselijke werknemer (Feine et al., 2019).

Sentimentanalyse en emotiedetectie komen ook goed van pas bij een chatbot ontwikkeld voor sociale interactie. Uit een onderzoek van Følstad & Brandtzaeg uit
2020 blijkt dat een chatbotgesprek ook over koetjes en kalfjes kan gaan, of over iemands gevoelens en leven. Sommige gebruikers gaan de uitdaging aan om
de chatbot te testen: in hoeverre is de chatbot in staat om als een mens te reageren. Maar voor anderen is de chatbot een manier om de dag door te komen; hoewel
ze zich ervan bewust zijn dat ze converseren met een machine, wordt de chat aangezien als een waardevolle sociale interactie.

-------------------------------
## Gerelateerde voorbeelden: 

Er zijn verschillende soorten chatbots, bijvoorbeeld: 
- chatbots die veelgestelde vragen beantwoorden, als het ware een virtuele helpdesk;
- chatbots die klachten behandelen;
- chatbots die aan de slag kunnen met moeilijkere problemen, zoals de virtuele therapeut Woebot (Health, 2021).

Steeds meer bedrijven en organisaties hebben een chatbot op hun website om hun dienstverlening te verbeteren. Het grote voordeel van een chatbot is dat die altijd bereikbaar is, zodat mensen snel een antwoord krijgen op hun vragen. Als men bijvoorbeeld een boek bestelt op de webshop bol.com, maar er volgt geen bevestigingsmail, dan kan men dat aankaarten bij de chatbot Billie op de
website. Volgens bol.com is hun **klantendienst** dankzij Billie dag en nacht open.

Om tijd te besparen wordt hier en daar het **anamnesegesprek** bij de dokter vervangen door een chatbotgesprek, bijvoorbeeld met Bingli; de zinvolle informatie wordt doorgespeeld aan de dokter (Bingli, 2021). 

Miljoenen mensen chatten via WeChat of een ander online platform met hun **virtuele vriendin** Xiaoice, soms uit eenzaamheid (Davies, 2021).

Men onderzoekt eveneens hoe chatbots kunnen worden ingezet voor wetenschappelijk onderzoek, bv. door chatbots interviews te laten afnemen en via chatbots mensen te informeren over de impact die deelname aan een onderzoek kan hebben (Kenniscentrum Data & Maatschappij, 2020c,a).

Ook de mogelijkheden om chatbots in te zetten voor onderwijs worden verkend, bijvoorbeeld voor lessen vreemde talen.

-----------------------------
### Werking 
In het leerpad ['Chatbot'](https://dwengo.org/learning-path.html?hruid=cb1_chatbot&language=nl&te=true&source_page=%2Fchatbot%2F&source_title=%20Chatbot#cb_chatbot_inleiding;nl;3) wordt de werking van ChatGPT (deels) uit de doeken gedaan.

-----------------------------
#### Leestips

[ChatGPT zinvol inzetten in de klas](https://dwengo.org/backend/api/learningObject/getWrapped?hruid=cb_chatbot6&version=3&language=nl)

[Handleiding project 'Chatbot'](https://dwengo.org/assets/files/chatbot/Chatbot_handleiding_eerstedruk.pdf) (paragraaf 4.3 'Tevreden over de chatbot?', p. 55-58)

[brAInfood: Databescherming & chatbots](https://data-en-maatschappij.ai/publicaties/brainfood-databescherming-en-chatbots)

#### Kijktips

[In gesprek met robots - Eva Verhelst](https://youtu.be/Yit4JwGZjPs?si=L0tn4ET9VTZJAkzs)

[Improbotics van ERLNMYR](https://youtu.be/HEilrWTMTqM?si=fbi6ViiSMESJ6cv9)  met lesmap voor [leerkrachten](https://dwengo.org/assets/files/chatbot/Improbotics_lesmap_Leerkracht.pdf) en [leerlingen](https://dwengo.org/assets/files/chatbot/Improbotics_lesmap_Leerling.pdf).

-----
#### Bronnen

Bingli (2021). Bingli, het slimme medische interview. Geraadpleegd op 1 augustus 2021 via https://www.mybingli.com<br>
Brants, M. (2020). Vlaams Chatbot Onderzoek bij eindgebruiker. Thomas More. Geraadpleegd op 1 augustus 2021 via https://www.chatbotgids.com/post/vlaams-chatbot-onderzoek-bij-eindgebruiker<br>
Davies, S. (2021). Love bytes. A chatbot provides emotional support to lonely hearts and potentially mines data from millions of vulnerable users. Geraadpleegd op 9 april
2021 via https://www.theworldofchinese.com/2021/03/love-bytes/<br>
Feine, J., Morana, S., & Gnewuch, U. (2019). Measuring Service Encounter Satisfaction with Customer Service Chatbots using Sentiment Analysis. *14th International Conference on Wirtschaftsinformatik.*<br>
Health, W. (2021). Welcome to the future of mental health. Geraadpleegd op 9 april 2021 via https://woebothealth.com/<br>
Kenniscentrum Data & Maatschappij (2020a). Chatbots meer dan trouwe medewerkers van een helpdesk. Geraadpleegd op 31 maart 2021 via https://data-en-maatschappij.ai/nieuws/chatbots-meer-dan-trouwemedewerkers-van-een-helpdesk<br>
Kenniscentrum Data & Maatschappij (2020c). Tien tips om zeker te zijn dat je chatbot een meerwaarde heeft voor je doelgroep. Geraadpleegd op 31 maart 2021
via https://data-en-maatschappij.ai/nieuws/tien-tips-om-zeker-tezijn-dat-je-chatbot-een-meerwaarde-heeft-voor-je-doelgroep. Frederic Heymans.
