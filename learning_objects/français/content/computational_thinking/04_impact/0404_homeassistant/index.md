---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Home assistant
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct04_04
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
teacher_exclusive: true
title: Home assistant
version: 3
---
# Assistant vocal et publicité

Allons-nous tous utiliser un assistant vocal dans un avenir proche ? Depuis l'arrivée de ChatGPT, de plus en plus de personnes en sont convaincues. <br>
Depuis quelques années déjà, nous pouvons faire appel à des assistants vocaux, tels que Siri, Alexa ou l'Assistant Google. Certains les utilisent volontiers pour appeler quelqu'un en voiture, allumer le chauffage à la maison ou demander la météo. Les personnes qui se sentent seules trouvent dans un assistant vocal un interlocuteur. Un tel *voice assistant* peut donc avoir un impact de plusieurs façons. <br>
Un exemple en est développé ci-dessous.

**Quel est l'impact de l'utilisation d'un assistant vocal sur la publicité que nous voyons ? Sommes-nous collectivement écoutés ?**

On entend souvent la question suivante : Les assistants vocaux écoutent-ils en permanence ce que nous disons ? Et en font-ils ensuite quelque chose ? Est-ce un hasard si je reçois de la publicité pour un certain produit, après en avoir parlé avec une amie ?<br>
Pour pouvoir y répondre clairement, il faut d'abord examiner certains aspects du fonctionnement d'un tel *voice assistant*, comme Siri, Alexa ou l'Assistant Google.   

## Principes de la pensée computationnelle

![ct-schema](@learning-object/m_ct04_04/nl/3)


## Discussion de l'impact

-  Si un assistant vocal écoutait activement en permanence, la **batterie** de votre smartphone ou d'un autre appareil se viderait très rapidement.
-  Si un assistant vocal écoutait activement en permanence – **écouter activement signifie que tout ce que l'assistant entend est également stocké** – pour en faire quelque chose – ce qui signifie que chaque fragment audio est converti en texte tapé – cela représenterait une **énorme quantité de données** dans le cloud. Il est impossible que les fournisseurs de tels systèmes conservent tout de tous les utilisateurs.
-  Il faut donc faire la distinction entre **écoute active et passive**. L'assistant vocal écoute toujours passivement et, lorsqu'il « entend » un mot déclencheur, il passe à l'écoute active. À ce moment-là, ce que l'assistant entend est également stocké, et chaque fragment audio est converti en texte tapé. Ce texte est ensuite soumis à un système d'IA qui en fait quelque chose. Tout cela se fait en un clin d'œil.
-  Donc, si vous recevez de la publicité pour un produit dont vous avez parlé auparavant avec une amie, c'est une coïncidence.
-  En revanche, si vous avez **demandé quelque chose à l'assistant vocal**, et que vous recevez ensuite de la publicité à ce sujet, c'est une autre histoire.
-  Vous pouvez avoir l'impression d'être écouté si vous recevez soudainement de la publicité pour un produit dont vous parliez encore la veille avec une amie. Cela peut toutefois s'expliquer
    -  par le *phénomène de Baader-Meinhof* ou *illusion de fréquence* (comme vous en avez parlé la veille, la publicité attire davantage l'attention) (source : factcheck) ;
    -  par le *biais de confirmation* (votre soupçon d'être écouté est confirmé par la publicité) ;
    -  ou vous pouvez l'attribuer aux *lookalike audiences* (par **reconnaissance de motifs**, on vous attribue les mêmes centres d'intérêt que quelqu'un ayant un profil similaire). 
-  Il faut également accorder suffisamment d'attention à ceci : Comment les données collectées par les systèmes sont-elles conservées, utilisées, partagées et supprimées ?
    - Un rapport de 2019 du Capgemini Research Institute indique qu'une bonne collaboration entre l'*in-car voice assistant*, le *home assistant* et l'assistant numérique sur le smartphone des utilisateurs est souhaitable. Ils pourraient, par exemple, ouvrir la porte du garage et allumer le chauffage à la maison avec l'*in-car voice assistant*. Mais une telle intégration comporte aussi des aspects liés à la vie privée :
des données sont alors partagées entre plusieurs applications (Walch, 2020). En théorie, l'assistant numérique sur le smartphone pourrait ainsi apprendre où l'utilisateur s'est rendu en voiture.
    - Où iront les données ? Cela peut-il avoir des conséquences plus tard, par exemple lors d'une demande de prêt ?
-----------------------------
### Fonctionnement 

Pour pouvoir communiquer dans les deux sens par la langue parlée avec un assistant numérique, comme Siri sur un iPhone, Alexa à la maison et l'assistant vocal dans la voiture, il faut à la fois une technologie de reconnaissance vocale (parole vers texte) et un logiciel de synthèse vocale (texte vers parole). Le logiciel de synthèse vocale permet à l'assistant vocal de parler, le logiciel de reconnaissance vocale pour qu'il « comprenne » la personne qui lui parle. 

La technologie de reconnaissance vocale est un système d'IA capable de traiter le son. Elle fonctionne avec un enregistrement audio qui est converti en un fichier numérique. La langue parlée de l'utilisateur est automatiquement convertie en texte écrit via la technologie de reconnaissance vocale (parole vers texte) afin que l'assistant numérique puisse l'exploiter. Le système d'IA analyse ensuite ce texte écrit. Ce n'est certainement pas une tâche simple, car chacun s'exprime à sa manière, même dans la même langue. En outre, le système doit pouvoir distinguer la parole humaine d'un éventuel bruit de fond. Les systèmes de ML commencent cependant aussi à distinguer les dialectes d'une même langue.

<div class="alert alert-box alert-info">
Ce que vous dites à l'assistant vocal finit dans le cloud. Si vous donnez à Siri la commande d'éteindre la lumière, plus d'un système d'IA est mis en marche. Au moment où vous dites ‘Hey Siri’, le système derrière Siri est activé et l'instruction vocale est enregistrée. Cet enregistrement est envoyé à un centre de données. Votre commande vocale est ensuite convertie en texte tapé, l'action à entreprendre est déterminée, et l'instruction requise est renvoyée vers votre smartphone. Votre smartphone envoie une instruction appropriée à votre installation d'éclairage, à la suite de quoi la lumière s'éteint finalement dans votre pièce (Hulstaert, 2023).
</div>

Chaque étape de ce processus coûte de l'énergie. 

Pour faire parler un assistant numérique ou un robot, un fichier texte est converti en son à l'aide d'un logiciel de synthèse vocale. 

Toutes les techniques appliquées au texte tapé, comme l'analyse de sentiment, peuvent également être appliquées, indirectement, au texte parlé. Le principe est exactement le même, car le texte vocal est d'abord converti en texte écrit, puis l'analyse de sentiment est effectuée, tout comme on le ferait directement sur du texte écrit. Ce que vous dites à l'assistant vocal peut donc aussi être utilisé pour le *profilage* ; un système d'IA dresse alors un profil de vous qui peut servir à vous envoyer de la publicité personnalisée. Il est peut-être possible d'éviter cela via certains réglages sur l'appareil numérique concerné ; pour ce faire, il est préférable de consulter la politique de confidentialité.   

Dans certaines applications, vous avez donné (implicitement) l'autorisation d'utiliser votre microphone et d'écouter. Ces applications n'écouteront pas non plus en permanence, mais elles le feront occasionnellement lorsqu'elles sont déclenchées. Ce qui constitue ces déclencheurs n'est pas toujours clair, peut-être l'utilisation d'une certaine fonctionnalité ou basé sur votre localisation. 

-----------------------------
#### Conseils de lecture

[Les applications peuvent-elles écouter, et le font-elles vraiment ?](https://factcheck.vlaanderen/factcheck/apps-kunnen-meeluisteren-doen-wel)<br>
[ASSISTANTS VOCAUX](https://data-en-maatschappij.ai/publicaties/brainfood-databescherming-en-voice-assistants-1)<br>
[À propos des lookalike audiences](https://www.facebook.com/business/help/164749007013531?id=401668390442328)<br>
[Ceci est pour tous ceux qui pensent que Facebook vous écoute](https://nos.nl/op3/artikel/2224246-deze-is-voor-iedereen-die-denkt-dat-facebook-je-afluistert)

#### Conseil d'écoute

Radio 1. Bij Debecker. Conversation à partir de 3:09. ["Nous n'avons pas à craindre que les applications nous écoutent constamment"](https://radio1.be/lees/we-hoeven-niet-meteen-bang-te-zijn-dat-apps-ons-constant-afluisteren) 

#### Conseil de visionnage

[Nous avons vérifié si Facebook vous écoute](https://nos.nl/op3/video/2224247-we-zochten-uit-of-facebook-met-je-meeluistert)

------------------------------
#### Sources

Capgemini Research Institute (2019). *Voice on the go. How can auto manufacturers provide a superior in-car voice experience.* Consulté le 9 août 2021 via https://www.capgemini.com/wp-content/uploads/2019/11/Report-%E2%80%93-Voice-on-the-Go.pdf<br>
Fabri M. (15 avril 2019), *Les applications peuvent-elles écouter, et le font-elles vraiment ?* [Billet de blog]. Factcheck Vlaanderen. Consulté le 5 août 2023 via https://factcheck.vlaanderen/factcheck/apps-kunnen-meeluisteren-doen-wel <br>
Hulstaert E. (15/1/2023). *Entretien avec Steven Latré (Imec) : « Si l'IA ne devient pas plus durable, elle est vouée à l'échec »*, Knack. Consulté en  2023 via https://www.knack.be/nieuws/technologie/steven-latre-imec-als-ai-niet-duurzamer-wordt-is-het-gedoemd-om-te-falen/<br>
Walch, K. (2020). *The Unique Challenges Of Voice Assistants In Vehicles*. Consulté le 9 août 2021 via https://www.forbes.com/sites/cognitiveworld/2020/09/29/the-unique-challenges-of-voice-assistants-invehicles/