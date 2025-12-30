---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: ChatGPT
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct04_03
keywords:
- ''
language: fr
licence: dwengo
return_value:
  callback_schema:
    att: test
    att2: test2
  callback_url: callback-url-example
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
target_ages:
- 12
- 13
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: true
title: ChatGPT
version: 3
---
# ChatGPT 3.5

En novembre 2022, OpenAI a lancé ChatGPT. Et bien que GPT existe depuis 2018 et que des applications basées sur de grands modèles de langage soient présentes depuis un certain temps sur le World Wide Web, beaucoup ont pris conscience que l’intelligence artificielle n’est pas de la science-fiction. <br>
Depuis lors, les journaux en parlent abondamment et une application (commerciale) après l’autre est développée. ChatGPT a déjà des applications dans différents domaines, comme le recrutement de nouveaux employés et la génération automatique de sites d’actualités. En même temps, ChatGPT suscite aussi des inquiétudes, comme la diffusion de désinformation.<br>
L’arrivée de ChatGPT a un grand impact, par exemple sur l’enseignement. Ainsi, les enseignants se méfient de la fraude potentielle des élèves. Ils se montrent, par exemple, plus soupçonneux lorsque les élèves rendent un texte fluide ; de nombreux enseignants repensent donc les tâches données à leurs élèves. D’un autre côté, ils utilisent eux-mêmes ChatGPT pour élaborer des exercices.

Dans ce parcours d’apprentissage, vous approfondirez l’un des aspects de ChatGPT : un aspect qui contribue de manière essentielle à l’impact du système d’IA.

**Impact : Comme les réponses de ChatGPT sonnent de manière fluide et assurée, elles sont souvent considérées à tort comme correctes.**<br>

<div class="alert alert-box alert-info">
    Murray Shanahan dit que nous devons bien comprendre ce que fait un grand modèle de langage. "Veronderstel dat we de volgende prompt geven aan een LLM: “The first person to walk on the Moon was”,  en stel dat het antwoordt met “Neil Armstrong”. Wat vragen we hier eigenlijk? Het is belangrijk om in te zien dat we eigenlijk niet vragen wie de eerste persoon was die op de maan wandelde. De vraag die we echt stellen aan het model is de volgende vraag:  Gegeven de  statistische verdeling van de woorden in de uitgebreide publieke corpus van (Engelse) tekst, welke woorden volgen er het meest waarschijnlijk op de reeks “The first person to walk on the Moon was ”? Een goed antwoord op deze vraag is “Neil Armstrong” (Source : Talking About Large Language Models, Murray Shanahan, 2022).
</div>

## Principes de la pensée computationnelle

![ct-schema](@learning-object/m_ct04_03/nl/3)

## Discussion de l'impact

- ChatGPT 3.5 comporte différents aspects : le modèle de langage sur lequel il est basé, les données d’entraînement et l’interface que les gens utilisent pour communiquer avec le modèle.
- Former un modèle de langage nécessite beaucoup d’énergie ; c’est aussi un aspect à prendre en compte. L’utilisation de ChatGPT consomme également de l’énergie.
- Parce que ChatGPT 3.5 fonctionne sous forme de dialogue, le système est très accessible. En raison des similitudes avec une app comme WhatsApp, par exemple, ChatGPT paraît très familier. Cette accessibilité est l’une des raisons pour lesquelles ChatGPT est autant utilisé.
- ChatGPT 3.5 sert en réalité à générer des textes. Parce qu’il est basé sur un grand modèle de langage, ChatGPT convient aussi, par exemple, pour résumer des textes, transformer des textes dans un autre style, réécrire pour un autre public cible et traduire.
- Les gens utilisent toutefois ChatGPT 3.5 aussi pour des choses auxquelles le système n’est pas destiné :
    - utiliser ChatGPT comme moteur de recherche ;
    - résoudre des problèmes mathématiques ;
    - se confier (des recherches ont montré que les étudiants qui n’avaient pas tendance à frauder avant l’existence de ChatGPT ne le font généralement pas non plus aujourd’hui, mais que les jeunes se tournent vers ChatGPT en cas de problèmes émotionnels).
- ChatGPT est très rapide, permettant à une personne mal intentionnée de générer beaucoup de fausses nouvelles en peu de temps et de les diffuser ensuite.
- ChatGPT ne comprend donc pas un texte comme un humain le comprend. ChatGPT utilise la reconnaissance de motifs pour comprendre et générer le langage naturel. Le modèle apprend des schémas dans des données textuelles et les utilise pour former des phrases cohérentes et pertinentes. Pour ce faire, le système calcule. ChatGPT 3.5 n’a (pour l’instant) pas accès au World Wide Web et ne dispose donc pas des dernières informations. ChatGPT 3.5 ne pourra donc pas étayer ses affirmations par des sources. Il arrive donc que ChatGPT « hallucine », autrement dit : dise des absurdités. (*Si vous demandez des sources à ChatGPT, il les inventera.*)
- ChatGPT répond de manière « humaine » et paraît aimable et courtois. Le pas vers « l’humanisation », c.-à-d. le traitement du système comme une personne, est donc vite franchi.  - Une étude de Følstad & Brandtzaeg de 2020 montre qu’une conversation avec un chatbot peut aussi porter sur des banalités, ou sur les sentiments et la vie de quelqu’un. Certains utilisateurs relèvent le défi de tester le chatbot : dans quelle mesure le chatbot est-il capable de réagir comme un humain ? Mais pour d’autres, le chatbot est une manière de passer la journée ; bien qu’ils sachent qu’ils conversent avec une machine, la discussion est considérée comme une interaction sociale précieuse.
- Bien que le système réponde d’une manière assurée, on peut souvent le convaincre facilement qu’il a tort, en raison de sa nature courtoise et italiquepleasingitalique, (même quand ce n’est pas le cas).
  
> La plupart des chatbots de services clients qui existaient déjà étaient des systèmes basés sur des règles. Dans de tels chatbots, différents scénarios sont explicitement programmés. Cela entraîne automatiquement des limites auxquelles les utilisateurs doivent s’adapter. Par exemple, si on formule une question différemment de ce qui est programmé, le chatbot ne reconnaîtra pas la question. De tels chatbots sont souvent impopulaires.
> Une même question peut, par exemple, être posée de différentes manières. Par exemple « Va-t-il pleuvoir toute la journée aujourd’hui ? » ou « Est-ce que ça va être une journée maussade aujourd’hui ? ».
Pour comprendre une question, une connaissance du monde, connaissance du monde physique, peut être nécessaire. Par exemple « Est-ce que demain il fera un temps à bikini ? ».
> De l’humour, de l’ironie ou du sarcasme peuvent être dissimulés dans un message. Par exemple « Youpi, mon train est encore bien à l’heure ».  
- La satisfaction d’une conversation avec un chatbot peut contribuer à la satisfaction client ou la compromettre en partie. Les gens attendent d’un chatbot qu’il soit efficace, qu’il ait une personnalité amicale et polie, et qu’il donne des réponses rapides et solides. Parce que ChatGPT répond à ces critères, certaines entreprises envisagent d’utiliser ChatGPT comme chatbot du service clientèle. Lorsque le chatbot hallucine, le client n’en tire aucun bénéfice. En outre, les utilisateurs veulent que soit indiqué clairement qu’ils discutent avec un bot et non avec un humain ; ils s’attendent à ce que ce soit signalé. Les entreprises qui déploient ChatGPT comme chatbot pourraient facilement passer cela sous silence, surtout si les systèmes deviennent encore meilleurs à l’avenir.

  
**Réflexion :** les textes générés par l’IA générative se retrouvent également en ligne ; il est réaliste que ces textes servent de données d’entraînement pour de nouveaux systèmes. La mésinformation et la désinformation ne risquent-elles pas ainsi d’être renforcées ?

-----

![trainingchatgpt](https://github.com/dwengovzw/learning_content/assets/48352335/252a8bf4-6ff2-4f60-b81b-a23d7919fb2f)

------
## Exemples liés : 

Il existe différents types de chatbots, par exemple :
- des chatbots qui répondent aux questions fréquemment posées, en quelque sorte un service d’assistance virtuel ;
- des chatbots qui traitent les plaintes ;
- des chatbots capables de s’attaquer à des problèmes plus complexes, comme le thérapeute virtuel Woebot (Health, 2021).

De plus en plus d’entreprises et d’organisations ont un chatbot sur leur site web pour améliorer leur prestation de services. Le grand avantage d’un chatbot est qu’il est toujours joignable, afin que les gens reçoivent rapidement une réponse à leurs questions. Si, par exemple, on commande un livre sur la boutique en ligne bol.com mais qu’aucun e-mail de confirmation ne suit, on peut le signaler au chatbot Billie sur le
site web. Selon bol.com, leur **service clientèle** est ouvert jour et nuit grâce à Billie.

Pour gagner du temps, l’**entretien d’anamnèse** chez le médecin est parfois remplacé par une conversation avec un chatbot, par exemple avec Bingli ; les informations pertinentes sont transmises au médecin (Bingli, 2021). 

Des millions de personnes discutent via WeChat ou une autre plateforme en ligne avec leur **petite amie virtuelle** Xiaoice, parfois par solitude (Davies, 2021).

On étudie également comment les chatbots peuvent être utilisés pour la recherche scientifique, par exemple en laissant les chatbots réaliser des interviews et en informant via des chatbots les personnes de l’impact que peut avoir la participation à une étude (Kenniscentrum Data & Maatschappij, 2020c,a).

Les possibilités d’utilisation des chatbots pour l’enseignement sont également explorées, par exemple pour les cours de langues étrangères.

-----------------------------
### Fonctionnement 
Dans le parcours d’apprentissage ['Chatbot'](https://dwengo.org/learning-path.html?hruid=cb1_chatbot&language=nl&te=true&source_page=%2Fchatbot%2F&source_title=%20Chatbot#cb_chatbot_inleiding;nl;3), le fonctionnement de ChatGPT est (en partie) expliqué.

-----------------------------
#### Conseils de lecture

[Utiliser ChatGPT de manière pertinente en classe](https://dwengo.org/backend/api/learningObject/getWrapped?hruid=cb_chatbot6&version=3&language=nl)

[Manuel du projet 'Chatbot'](https://dwengo.org/assets/files/chatbot/Chatbot_handleiding_eerstedruk.pdf) (paragraphe 4.3 'Satisfait du chatbot ?', p. 55-58)

[brAInfood : Protection des données et chatbots](https://data-en-maatschappij.ai/publicaties/brainfood-databescherming-en-chatbots)

#### Conseils de visionnage

[En conversation avec des robots - Eva Verhelst](https://youtu.be/Yit4JwGZjPs?si=L0tn4ET9VTZJAkzs)

[Mouvements des lèvres réalistes](https://youtu.be/pWMPBNGwmMY?si=706_myBZPkYsFxsC&t=142)

[Improbotics d’ERLNMYR](https://youtu.be/HEilrWTMTqM?si=fbi6ViiSMESJ6cv9) avec dossier pédagogique pour [enseignants](https://dwengo.org/assets/files/chatbot/Improbotics_lesmap_Leerkracht.pdf) et [élèves](https://dwengo.org/assets/files/chatbot/Improbotics_lesmap_Leerling.pdf).

-----
#### Sources

Bingli (2021). Bingli, l’interview médical intelligent. Consulté le 1 août 2021 via https://www.mybingli.com<br>
Brants, M. (2020). Vlaams Chatbot Onderzoek bij eindgebruiker. Thomas More. Consulté le 1 août 2021 via https://www.chatbotgids.com/post/vlaams-chatbot-onderzoek-bij-eindgebruiker<br>
Davies, S. (2021). Love bytes. A chatbot provides emotional support to lonely hearts and potentially mines data from millions of vulnerable users. Consulté le 9 avril
2021 via https://www.theworldofchinese.com/2021/03/love-bytes/<br>
Følstad, A. & Brandtzaeg, P. B. (2020). Users’ experiences with chatbots: findings from a questionnaire study. *Qual User Exp, 5*(3).<br>
Feine, J., Morana, S., & Gnewuch, U. (2019). Measuring Service Encounter Satisfaction with Customer Service Chatbots using Sentiment Analysis. *14th International Conference on Wirtschaftsinformatik.*<br>
Health, W. (2021). Welcome to the future of mental health. Consulté le 9 avril 2021 via https://woebothealth.com/<br>
Kenniscentrum Data & Maatschappij (2020a). Chatbots meer dan trouwe medewerkers van een helpdesk. Consulté le 31 mars 2021 via https://data-en-maatschappij.ai/nieuws/chatbots-meer-dan-trouwemedewerkers-van-een-helpdesk<br>
Kenniscentrum Data & Maatschappij (2020c). Tien tips om zeker te zijn dat je chatbot een meerwaarde heeft voor je doelgroep. Consulté le 31 mars 2021
via https://data-en-maatschappij.ai/nieuws/tien-tips-om-zeker-tezijn-dat-je-chatbot-een-meerwaarde-heeft-voor-je-doelgroep. Frederic Heymans.