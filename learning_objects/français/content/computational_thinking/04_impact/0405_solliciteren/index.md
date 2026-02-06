---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Postuler
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct04_05
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
title: Postuler
version: 3
---
# Postuler

Postulera-t-on encore à l’avenir de manière classique ? Probablement pas. <br>
Le processus de candidature a en fait déjà profondément changé lorsque les employeurs ont commencé à examiner les futurs employés sur les réseaux sociaux. 

**Impact : Nouvelles façons de postuler**<br>

La numérisation a déjà un impact considérable sur le processus de candidature. Grâce à l’IA, vous pouvez recevoir sur certaines plateformes des offres d’emploi intéressantes dans votre boîte mail. De nouvelles formes de candidature émergent, comme l’utilisation d’entretiens vidéo. De plus, en tant que candidat, vous devez tenir compte du profilage et du fait que ce qui est publié sur les plateformes de réseaux sociaux sera encore consultable dans quelques années. 


## Principes de la pensée computationnelle

![ct-schema](@learning-object/m_ct04_05/nl/3)


## Discussion de l’impact
- À partir des publications sur les réseaux sociaux et des lettres de motivation, un profilage est effectué au moyen d’algorithmes d’intelligence artificielle. Pour les ressources humaines, la personnalité d’un candidat est une donnée intéressante, certains profils étant en effet mieux adaptés à une fonction donnée que d’autres (De Gussem & Daelemans, 2020).<br> 
Exemple : L’entreprise gantoise Traicie développe un système d’IA qui décide, à partir des lettres de motivation, dans quelle mesure l’auteur est apte pour le poste. Le système déduit pour ce faire des traits de personnalité de ce qu’a écrit le candidat. 
- Grâce à l’IA, vous pouvez recevoir sur certaines plateformes des offres d’emploi intéressantes dans votre boîte mail. 
Mais voyez-vous bien toutes les offres qui vous intéressent ?<br>
Exemple : Jusqu’en 2018, Amazon utilisait un système d’IA très applaudi mais depuis abandonné pour évaluer les candidats. Le système ne sélectionnait pas les femmes pour des postes technologiques. Cela s’expliquait par le fait qu’il avait été entraîné sur des données historiques : des candidatures des dix années précédentes, principalement d’hommes, puisqu’ils dominent encore le monde technologique. <br>
- Certaines entreprises, comme Unilever, utilisent un entretien vidéo pour recruter du nouveau personnel. Ces images sont analysées par un algorithme. Celui-ci tient compte non seulement de ce que dit le candidat, mais aussi, par exemple, des expressions faciales. Unilever affirme que le système repère les candidats les plus motivés et les plus adaptés au poste (Oostra, 2019 ; Wall Street Journal, 2018).<br>
- Les entreprises qui gèrent le processus de candidature à l’aide de l’IA s’appuient souvent sur l’objectivité supposée de ces systèmes. Mais tout système d’IA comporte des biais ; ces systèmes sont toujours empreints de parti pris, en raison de la manière dont ils sont développés. L’entreprise Traicie affirme également utiliser un système sans biais. Leur système d’IA décide, sur la base des lettres de motivation, dans quelle mesure l’auteur possède les compétences requises pour un certain poste.  

#### Conseils de visionnage et activités

- Regardez la [vidéo de Kanaal Z (De Winne, 2020)](https://kanaalz.knack.be/nieuws/taalgebruik-op-cv-onthultpersoonlijkheid/video-normal-1678309.html).<br>
Visitez également le [site web de Traicie](https://traicie.com/) et discutez de l’objectivité du système.

 - Dans cette [vidéo 'The Robots Are Now Hiring'](https://youtu.be/8QEK7B9GUhM), les nouvelles tendances en matière de recrutement sont évoquées (Wall Street Journal, 2018). <br>Discutez.

-------------------------------

## Explications supplémentaires
Dans le [projet Chatbot](https://dwengo.org/chatbot), des exemples sont donnés de nouvelles pratiques qui trouvent de plus en plus leur place dans le secteur des ressources humaines, comme le screening des réseaux sociaux. 

En en discutant en classe, les élèves prendront, espérons-le, conscience que ce qui est publié sur les plateformes de réseaux sociaux sera encore accessible dans quelques années lorsqu’ils postuleront. Mais cela va bien plus loin que cela. 

Les biais surviennent lorsque les données ne sont pas représentatives. Si, par exemple, on ne fournit à un système de DL que des pommes vertes comme exemples, le modèle ne reconnaîtra pas les pommes rouges. Ou si, lors de l’entraînement, on ne propose que des photos de chiens sous un ciel bleu éclatant, le modèle de deep learning ne classera pas un chien sous la pluie dans la catégorie « chien ». Si les données utilisées sont teintées par des biais présents dans la société, comme des stéréotypes, cela sera également transmis au système de ML. Il faut donc veiller à ce que le modèle ne devienne pas discriminatoire envers certains groupes de population. Si, par exemple, on ne met dans le jeu de données que des infirmières femmes, les hommes ne seront pas classés comme infirmiers. Un modèle est pourtant testé avant d’être mis en service. Cependant, les données de test peuvent contenir les mêmes biais que les données d’entraînement.

-------------------------------

#### Conseil de visionnage
Regardez la [vidéo de Furhat Robotics: Unbiased Recruiter Robot (Furhat Robotics, 2018)](https://youtu.be/rPKrdxiEkQ0)