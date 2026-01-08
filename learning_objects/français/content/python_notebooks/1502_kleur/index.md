---
available: true
content_type: text/markdown
copyright: dwengo
description: Carnets sur ...
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 50
hruid: pn_db_kleur
keywords:
- Python
- STEM
- Wiskunde
- AI Op School
- Computationeel denken"
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
- http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-getallenleer
- http://ilearn.ilabt.imec.be/vocab/curr1/s-mediawijsheid
- http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-algebra-analyse
- http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-kansrekenen-statistiek
target_ages:
- 14
- 15
- 16
- 17
- 18
title: Couleur
version: 3
---
# Images en couleur

Dans ce notebook, vous découvrirez les mathématiques derrière les images numériques en couleur. Au lieu de matrices, on utilise maintenant des tenseurs.

[![](embed/Knop.png "Bouton")](https://kiks.ilabt.imec.be/hub/tmplogin?id=1502_fr "Notebooks couleur")

------------
Les couleurs se présentent dans un spectre. 
![](embed/spectrum.png "Spectre des couleurs")

Les couleurs que les êtres humains voient peuvent être approximées par une combinaison de teintes rouge (R), verte (G) et bleue (B). <br>
Les couleurs peuvent être représentées numériquement par RGB. Il faut alors un tableau pour chacune des teintes rouge, verte et bleue ; ceux-ci forment une grille 3D. 

![](embed/rgb.png "RGB")

![](embed/raster.png "Grille 3D")

Les couleurs d’un téléviseur sont également construites à l’aide du RGB, comme on peut le voir sur la photo suivante, zoomée, d’une partie d’une image télévisée. 

![](embed/RGBtelevisie.jpg "RGB")