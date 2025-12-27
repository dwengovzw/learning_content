---
available: true
content_type: text/markdown
copyright: dwengo
description: "\xC9pid\xE9mie"
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: pn_epidemie3
keywords:
- voorbeeld
- voorbeeld2
language: fr
licence: dwengo
return_value:
  callback_schema:
    att: test
    att2: test2
  callback_url: callback-url-example
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-digitale-media-en-toepassingen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-kansrekenen-statistiek
- http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek
- http://ilearn.ilabt.imec.be/vocab/curr1/s-stem-onderzoek
target_ages:
- 16
- 17
- 18
title: "R\xE9seaux sociaux"
version: 3
---
# Réseaux sociaux

Le modèle SIR standard fait l'hypothèse irréaliste que deux individus pris au hasard ont chaque fois la même probabilité d'entrer en contact l'un avec l'autre et donc de transmettre éventuellement une maladie. En réalité, bien sûr, tout le monde ne fréquente pas les mêmes personnes. Nous avons tous des personnes avec lesquelles nous interagissons davantage (avec lesquelles nous sommes plus souvent en contact) qu'avec d'autres. L'ensemble de qui est en contact avec qui est appelé un réseau social (pensez à Facebook). Il semble évident que la structure d'un tel réseau aura une forte influence sur la dynamique de la propagation des maladies.

Les réseaux sociaux sont eux aussi modélisés mathématiquement. On s'appuie pour cela sur les « graphes ». Un graphe est constitué d'un ensemble de nœuds dont certains sont reliés par des arêtes. Dans l'exemple ci-dessous, les nœuds représentent les élèves. Les contacts entre élèves sont représentés par des segments de ligne entre les nœuds et sont appelés des arêtes. 

![https://royalsocietypublishing.org/doi/full/10.1098/rspb.2010.1807](embed/netwerkkinderen.png "Exemples de graphes colorés représentant des réseaux entre des enfants d'âges différents")
<sub>Source : https://royalsocietypublishing.org/doi/pdf/10.1098/rspb.2010.1807</sub>

Une figure est utile pour voir à quoi ressemble le réseau. Pour effectuer des calculs, d'autres représentations sont toutefois nécessaires. Un graphe peut être représenté mathématiquement par une matrice appelée matrice d'adjacence (anglais : adjacency matrix).

## Modèles de propagation des maladies en pratique

Les épidémies surviennent en permanence ; c'est pourquoi les organisations de santé publique du monde entier utilisent des modèles pour élaborer et évaluer des stratégies d'intervention. À l'aide de simulations, elles peuvent évaluer rapidement la situation et prendre des décisions importantes. 

Pour reconnaître une épidémie et y répondre, les professionnels de santé ont besoin d'informations intrinsèquement imprévisibles (quoi, où, combien de cas, combien mourront, où cela se propagera). Les interactions qui conduisent à l'apparition d'une maladie sont très complexes, de sorte que les résultats sont parfois inattendus ou contre-intuitifs. Des modèles sont nécessaires pour comprendre ces interactions et produire les prévisions quantitatives dont les acteurs de la santé publique ont besoin pour décider des stratégies d'intervention.

Le comportement humain lors de flambées de maladies change souvent radicalement. Les gens évitent les lieux bondés ou se précipitent vers des lieux très fréquentés comme les aéroports ou les gares s'ils tentent d'échapper à l'épidémie. La modélisation peut aider les professionnels de santé à anticiper et à comprendre ce type d'effets.

Les modèles peuvent également être utilisés pour déterminer comment allouer les ressources afin d'avoir les meilleures chances d'arrêter la propagation de la maladie — par exemple, si les vaccins sont limités, quel groupe de personnes doit être vacciné en priorité ? Les scientifiques peuvent utiliser des modèles pour comparer les résultats de différentes stratégies de contrôle. Les modèles peuvent aussi être couplés à des données climatiques à long terme et à des prévisions climatiques, afin de faire des prévisions d'épidémies plusieurs mois à l'avance. Cette approche est utilisée pour planifier des campagnes de vaccination, par exemple contre la grippe ou la rougeole.

Les scientifiques développent leur compréhension de la propagation des maladies à l'aide de données telles que les tendances comportementales, démographiques et épidémiologiques, mais il est souvent difficile de collecter des données fiables, et pour de nombreuses maladies il nous manque encore des informations essentielles sur leurs modes de propagation. La modélisation peut également aider dans ces cas, car les scientifiques peuvent tester différentes hypothèses pour tenter de combler les lacunes de leurs connaissances.

***

Dans ces notebooks, le modèle SIR est notamment appliqué à un réseau et vous allez vous-même simuler certaines situations dans le modèle.

[![](embed/Knop.png "Bouton")](https://kiks.ilabt.imec.be/hub/tmplogin?id=1221_fr "Notebooks Épidémie")