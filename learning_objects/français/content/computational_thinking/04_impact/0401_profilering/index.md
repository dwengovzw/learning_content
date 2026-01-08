---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Profilage
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct04_01
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
title: Profilage
version: 3
---
# Profilage via les réseaux sociaux

Les plateformes de réseaux sociaux établissent un profil de personnalité de leurs utilisateurs.<br>
Ce profil peut contenir, par exemple, les intérêts, les opinions, la nature et les préférences d’une personne.<br>
L’utilisation d’un profil de personnalité peut avoir un impact de plusieurs façons sur les utilisateurs de la plateforme. La publicité personnalisée en est un exemple. 

**Impact : publicité personnalisée**<br>
Les entreprises étudient les publications sur les réseaux sociaux pour se faire une idée de la personnalité de quelqu’un. Elles tentent ensuite, en s’appuyant sur ces informations, de convaincre l’utilisateur d’effectuer un certain achat. C’est une manière de personnaliser la publicité. On en vient ainsi à recommander des services et des produits à l’aide d’algorithmes de recommandation. Les algorithmes de recommandation peuvent exercer une forte influence sur le comportement d’achat en ligne (e-commerce). 

## Principes de la pensée computationnelle

![schéma-ct](@learning-object/m_ct04_01/nl/3)

## Cadre de l’impact sur la société

![image](embed/kaderprofilering.png)

## Discussion de l’impact

- **Possibilité de stocker beaucoup de données** : Les publications sur les réseaux sociaux sont soigneusement conservées par la plateforme concernée et restent liées à l’utilisateur. Outre les publications sur les réseaux sociaux, les comportements d’achat et de clic sont également enregistrés.

 - **Schémas** : Les publications sur les réseaux sociaux ainsi que les comportements d’achat et de clic d’un utilisateur sont utilisés pour établir un profil de cette personne. Les algorithmes de recommandation formulent des recommandations, par exemple, sur la base de certains **schémas** présents dans le comportement de clic et d’achat de l’utilisateur. L’expérience sur la plateforme de réseaux sociaux est également personnalisée en fonction du comportement d’achat et de clic d’**utilisateurs aux intérêts « similaires »**.<br>
À partir des publications de quelqu’un sur les réseaux sociaux, on peut déduire les intérêts et les opinions de l’auteur, et peut-être même la nature et les préférences de cette personne. L’usage de la langue y est en effet lié.<br>

> La personnalité peut être envisagée selon le modèle des cinq facteurs, où l’on considère les traits « extraverti », « agréable », « consciencieux », « névrosé » et « ouvert à l’expérience » (Schwartz et al., 2013).<br>L’usage de la langue est lié au sexe, à l’âge et à des traits de personnalité tels qu’être introverti ou extraverti (Schwartz et al., 2013 ; De Gussem & Daelemans, 2020). Ainsi, certains mots et groupes de mots sont plus caractéristiques de certains groupes d’âge, comme « devoirs » pour les adolescents et « famille et amis » pour les adultes, et il existe des sujets spécifiques dont on parle sur Facebook, tels que « famille » chez les femmes et « xbox » chez les hommes. Les personnes extraverties utilisent des mots plus longs que les personnes introverties, ainsi que beaucoup d’adjectifs.
Schwartz et al. illustrent cela par quelques nuages de mots qu’ils ont réalisés à partir de publications Facebook qu’ils ont analysées (voir la Figure 1 pour les adolescents). Schwartz et al. ont utilisé un jeu de données de 15 millions de messages Facebook de 75 000 volontaires. Le cluster central contient les mots caractéristiques du groupe : plus le mot est grand, plus il est typique ; plus le mot est foncé, plus il est fréquent. Les clusters autour montrent les sujets caractéristiques des messages Facebook.
> ![ado](https://github.com/dwengovzw/learning_content/assets/48352335/e25da6ad-0245-4ea4-ab2c-04e33040dfce)<br>
> <center>Figure 1 : Mots et sujets les plus caractéristiques pour les adolescents sur Facebook (Schwartz et al., 2013).</center>


 - **Algorithmes :** Avec le natural language processing (NLP), c’est-à-dire le traitement automatique du langage naturel, on vérifie par exemple dans des textes sur les réseaux sociaux si les personnes s’expriment positivement ou négativement à propos de certains produits ou entreprises. Les algorithmes de recommandation font en sorte que les utilisateurs reçoivent des publicités personnalisées. 



#### Sources
De Gussem, J. & Daelemans, W. (2020). Ben je wat je schrijft? *EOS Psyche & Brein Special*, (pp. 40–43).<br>
Schwartz, H., Eichstaedt, J., Kern, M., Dziurzynski, L., Ramones, S., Agrawal, M., Shah, A., Kosinski, M., Stillwell, D., Seligman, M., & Ungar, L. (2013). Personality, Gender,
and Age in the Language of Social Media: The Open-Vocabulary Approach. *PLOS ONE, 8*(9).


-------------------------------
## Exemples connexes : 

Sur la base du profil de l’utilisateur, par exemple sur les sites d’actualités, des informations personnalisées lui sont également proposées.<br> 
Comme les algorithmes de recommandation sont de plus en plus utilisés sur les **sites de journaux en ligne** et que les résultats d’un **moteur de recherche** sont eux aussi de plus en plus personnalisés, il convient d’être attentif à la **bulle de filtrage**. Lorsqu’on est soumis à une bulle de filtrage, la vision que l’on a du monde peut être déformée. Si, par exemple, on souhaite apprendre un sujet que l’on ne maîtrise pas, une telle bulle peut donner une image manquant de nuances.

Pour les **ressources humaines**, la personnalité d’un candidat est une donnée intéressante, certains profils étant en effet mieux adaptés à une fonction donnée que d’autres (De Gussem & Daelemans, 2020).<br>
L’entreprise gantoise Traicie travaille sur un système d’IA qui, sur la base des **lettres de motivation**, décide dans quelle mesure l’auteur possède les compétences requises pour un poste donné. Le système en déduit des traits de personnalité à partir de ce qu’a écrit le candidat et affirme utiliser pour cela un système impartial (*unbiased*).

L’étude des publications d’un utilisateur sur les réseaux sociaux est également utilisée pour estimer pour qui il voterait lors d’une prochaine **élection**. 

Les **banques** tiennent également compte de la personnalité d’un client, par exemple dans le cadre de l’octroi d’un prêt.

Algorithmes de recommandation sur Netflix. 

Algorithmes de recommandation pour les achats en ligne, comme sur Amazon, bol, coolblue et Zalando.  

Algorithmes de recommandation sur les réseaux sociaux, comme « qui suivre » sur Twitter.

-------------------------------
#### Suggestions de lecture 

En savoir plus sur la [bulle de filtrage](https://dwengo.org/backend/api/learningObject/getWrapped?hruid=cb_6002&version=3&language=nl) dans le parcours d’apprentissage [Journalisme](https://dwengo.org/learning-path.html?hruid=cb6&language=nl&te=true&source_page=%2Fchatbot%2F&source_title=%20Chatbot#cb_6000;nl;3) du [projet sur les technologies du langage](https://dwengo.org/chatbot/).  

De Gussem, J. & Daelemans, W. (2020). Ben je wat je schrijft? *EOS Psyche & Brein Special*, (pp. 40–43).

[De Volkskrant - 24/22/2018 - Emprunter de l’argent ? Vos comptes sur les réseaux sociaux seront d’abord passés au crible](https://www.volkskrant.nl/nieuws-achtergrond/geld-lenen-dan-worden-eerst-je-social-media-accounts-gescreend~b53b4a36/)

#### Suggestions de visionnage 

Regardez la [vidéo](https://trends.knack.be/kanaal-z/z-nieuws/taalgebruik-op-cv-onthult-persoonlijkheid/).
Visitez également le site web de [traicie](https://traicie.com/) et discutez de l’objectivité du système.