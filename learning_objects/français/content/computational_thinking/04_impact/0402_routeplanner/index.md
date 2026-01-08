---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: "Planificateur d'itin\xE9raire"
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct04_02
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
title: "Planificateur d'itin\xE9raire"
version: 3
---
# Planificateur d’itinéraire

Les planificateurs d’itinéraire sont une application numérique très utilisée. Ils ont de plusieurs manières un impact sur notre société.
Voici déjà un exemple.

**Impact : plus de trafic dans les quartiers résidentiels**<br>
Beaucoup de gens utilisent un système de navigation en voiture, par exemple pour se rendre rapidement quelque part où ils ne sont jamais allés, ou pour éviter les embouteillages.

Dans les médias, on trouve de nombreux articles qui attribuent l’augmentation du trafic dans les quartiers résidentiels à l’usage généralisé des systèmes de navigation.

> **Conseils de lecture :**<br>
> [L’appli de navigation Waze remplit les rues résidentielles bruxelloises](https://www.bruzz.be/analyse/navigatieapp-waze-laat-brusselse-woonstraten-vollopen-2019-09-18)<br>
> [Waze Asked to Stop Providing Drivers With Traffic Shortcuts Because of Obvious Reasons](https://www.autoevolution.com/news/waze-asked-to-stop-providing-drivers-with-traffic-shortcuts-because-of-obvious-reasons-215490.html)

## Principes de la pensée computationnelle

![ct-schema](@learning-object/m_ct04_02/nl/3)

## Visualisation d’un brainstorming possible en classe

![diagramRouteplanner](embed/diagramrouteplanner.png)

## Cadre de l’impact sur la société
(d’après le modèle de Michael T. Rücker. 2023. Modeling Conceptual Knowledge of Computing Impacts for K-12.)

![KaderRouteplanner](embed/kaderrouteplanner.png)

## Discussion de l’impact

-  L’une des raisons pour lesquelles les planificateurs d’itinéraire sont autant utilisés et peuvent donc avoir un impact, est le haut degré d’**abstraction** au sein du planificateur d’itinéraire. Si vous le souhaitez, vous pouvez simplement suivre les instructions de la route à suivre (le plan par étapes). Vous n’avez pas à vous occuper de chercher l’itinéraire sur une carte, en tenant compte par exemple des sens uniques, de l’orientation de la carte, etc. <br> En outre, vous recevez des informations supplémentaires telles que les embouteillages, les travaux routiers, où faire le plein, etc. <br> Un tel planificateur d’itinéraire offre donc une grande facilité d’utilisation.
    - Le planificateur d’itinéraire est tellement ancré dans les habitudes que les gens ne réfléchissent souvent pas au fait que son usage n’est pas toujours la meilleure façon de trouver son chemin. Parfois, il est d’ailleurs impossible d’utiliser un planificateur d’itinéraire, par exemple lorsqu’il n’y a pas de couverture internet ou lorsque la batterie de votre smartphone est à plat.
    - Comme les planificateurs d’itinéraire procèdent à beaucoup d’abstraction, vous ne disposez plus d’une vision complète de l’environnement. Cela peut aussi être un inconvénient par rapport à une carte papier qui donne bien plus de détails sur l’environnement et situe en outre un lieu donné dans une zone plus vaste. Les planificateurs d’itinéraire érodent en quelque sorte la conscience spatiale autour d’un endroit. 
    - Dépendre excessivement des planificateurs d’itinéraire numériques peut aussi être dangereux. Certains lieux sont insuffisamment détaillés ou inexacts, ce qui peut amener des personnes, par exemple, à monter sur une voie ferrée ou un escalier, à se retrouver au milieu de travaux routiers ou à rouler à contresens. Les planificateurs d’itinéraire numériques peuvent aussi contenir des erreurs, comme une vitesse maximale erronée autorisée sur une route donnée ou une rue en sens unique indiquée comme à double sens.
      > [La police de Heusden-Zolder met en garde contre l’utilisation du GPS lors de travaux routiers](https://www.vrt.be/vrtnws/nl/2021/09/23/politie-heusden-zolder-waarschuwt-voor-gebruik-van-gps-bij-wegen/)

-  L’utilisation d’un planificateur d’itinéraire par un si grand nombre de personnes peut aussi avoir des effets indésirables, comme un trafic supplémentaire dans les quartiers résidentiels lorsqu’un planificateur détourne la circulation automobile par ces quartiers pour éviter les embouteillages.
    - Il se peut que l’**algorithme** du planificateur d’itinéraire tienne compte de l’aspect de l’environnement « situé dans un quartier résidentiel », mais il est possible que cet aspect ne soit pas inclus comme paramètre dans l’algorithme. Pour déterminer l’itinéraire le plus court, le planificateur peut, par exemple, surtout tenir compte du paramètre distance ; d’autres paramètres, tels que le fait qu’une rue se trouve dans un quartier résidentiel, peuvent alors être ignorés.
    - Le système numérique derrière le planificateur d’itinéraire peut détecter certains **motifs**, comme un trajet généralement connu uniquement des habitants locaux et couramment utilisé par eux. Si le système ajoute cet itinéraire comme trajet possible, il deviendra également connu des automobilistes non locaux et pourra ainsi augmenter l’affluence dans un quartier résidentiel.

- Aspects éthiques :
    - Les planificateurs d’itinéraire utilisent des algorithmes qui calculent le trajet, souvent en tenant compte d’informations en temps réel, telles que les embouteillages, qu’ils tentent ensuite d’éviter. Les informations de trafic en temps réel peuvent provenir de plusieurs sources, par exemple la police ou un gestionnaire d’autoroute. Mais le système peut aussi obtenir des informations via les utilisateurs actuels du planificateur d’itinéraire. Cela implique un aspect de confidentialité. 
        - Enregistre-t-on à cette occasion l’endroit où se trouve l’utilisateur ?
        - Si les positions de l’utilisateur sont enregistrées, la question se pose de savoir ce que l’entreprise à l’origine du planificateur d’itinéraire fait de ces données.
    - Les planificateurs d’itinéraire font aussi de la publicité. 
        - Ainsi, il est déterminé quels magasins, stations-service, etc., sont affichés.
        - Ainsi, un touriste peut, via le planificateur d’itinéraire, par exemple, apprendre quels établissements se trouvent à proximité de l’hôtel.
        - Il est possible qu’il existe des accords avec des partenaires commerciaux pour les rendre présents autant que possible le long des itinéraires.
        - Le planificateur d’itinéraire a pour cela accès à des **bases de données** de restaurants, magasins, cinémas, etc. Ce sont d’autres bases de données que celles strictement nécessaires au fonctionnement du planificateur d’itinéraire. 
    - Les planificateurs d’itinéraire peuvent aussi tenir compte d’éléments auxquels on ne s’attend pas.
      > [La navigation Mercedes évite les quartiers à forte criminalité](https://www.ad.nl/auto/navigatie-mercedes-ontwijkt-criminele-buurten~a48a4169/)<br>

-----

## Exemples connexes : shopping en ligne, le secteur de la santé ...

Les planificateurs d’itinéraire mènent à de nouvelles attentes en matière de shopping en ligne, comme une **livraison** plus rapide des colis et la livraison par robots roulants ou drones. 

L’utilisation de planificateurs d’itinéraire peut faire en sorte qu’une entreprise minimise **les coûts et le temps** consacrés au transport et optimise son fonctionnement, p. ex. pour une entreprise de livraison ou une compagnie de taxis.
> ["Without location technology, delivering packages for Christmas would be a nightmare!"](https://www.here.com/learn/blog/last-mile-holiday-season-2021)

**Robots roulants** sont utilisés pour livrer, à proximité du supermarché, des denrées alimentaires et autres courses.
> [TESTÉ. Nous avons fait livrer nos courses par le robot de Carrefour : “Nous n’en croyons pas nos yeux”](https://www.nieuwsblad.be/cnt/dmf20230726_96924324)

Outre la vente, on a aussi réfléchi dans d’autres secteurs aux opportunités des systèmes de navigation.<br> Des robots et des drones peuvent, à l’aide d’un système de navigation numérique, trouver leur chemin.

Dans le **secteur de la santé**, on a par exemple envisagé le déploiement de **drones** médicaux pour le transport entre hôpitaux.  
> [Avec le Medical Drone Service, des allers-retours entre sites hospitaliers en quelques minutes](https://www.antoniusziekenhuis.nl/nieuwsoverzicht/met-medical-drone-service-minuten-heen-en-weer-tussen-ziekenhuislocaties-0)<br>

Auprès des **pompiers** de Genk, on utilise des drones pour mieux évaluer un incident.
> [Le projet pilote de Genk avec des safety drones fait des émules dans tout le pays](https://www.vrt.be/vrtnws/nl/2023/03/14/genks-proefproject-met-safety-drones-krijgt-navolging-in-het-hel/)<br>

Vous pouvez également traiter un autre exemple lié au trafic, tel que MobiliData, le système de **feux de circulation intelligents** qui passent au vert lorsque les services de secours approchent. Ce système utilise lui aussi des données sur le réseau routier. Et, tout comme le planificateur d’itinéraire, il a besoin de la position de l’utilisateur. Il n’est pas surprenant que non seulement les services de secours puissent se connecter à ces feux intelligents. Tout le monde peut utiliser l’application de trafic pour se connecter au système. Ainsi, il pourrait également donner la priorité aux cyclistes par mauvais temps.

-----------------------------
### Fonctionnement 
Dans le parcours d’apprentissage « Graphes », [le fonctionnement d’un planificateur d’itinéraire](https://www.dwengo.org/backend/api/learningObject/getWrapped?hruid=aiz_routeplanner&version=3&language=nl) est expliqué en détail.

-----------------------------
#### Conseils de lecture

[TomTom VIA53 : pour la navigation et éviter les embouteillages](https://www.intogadgets.nl/tomtom-via53-voor-navigatie-en-files-omzeilen/)<br>
[TomTom Mapmakers: Meet Leen D’hondt, Product Manager, TomTom Maps](https://developer.tomtom.com/blog/spotlight/tomtom-mapmakers-meet-leen-dhondt-product-manager-tomtom-maps/)<br>
[« Éviter, déplacer et verdir : comment pouvons-nous organiser le e-commerce de manière plus durable ? »](https://www.knack.be/nieuws/vermijden-verschuiven-en-verschonen-hoe-kunnen-we-e-commerce-duurzamer-organiseren/)<br>
[Delivery robots begin to look real](https://www.gpsworld.com/delivery-robots-begin-to-look-real/)<br>
[Autonomous Robots for Industry 4.0](https://starshipdeliveries.com/industry/)

#### Conseils de visionnage

[Delivery robotsStarship Completes One Million Autonomous Deliveries](https://youtu.be/tQZWe1JFR9g)<br>
[A Day in the Life of a Starship Robot](https://youtu.be/Z417CncwQsg)<br>
[Presentatie over o.a. werking delivery robots](https://youtu.be/6rq6Hx0PRAc)<br>
[World first: new drone network for smooth and safe traffic in Antwerp](https://youtu.be/w3bzDc5pEq0)

-----
##### Sources
Gugan, G., Haque A. (2023). Path Planning for Autonomous Drones: Challenges and Future Directions. *Drones, 7*(3):169.