---
available: true
content_type: text/markdown
copyright: Dwengo
description: Notebooks on digital images
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 100
hruid: pn_db_kleur
keywords:
- Python
- STEM
- Wiskunde
- AI Op School
- Computationeel denken"
language: en
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
title: Color
version: 3
---
# Images in Colour

In this notebook, you will become familiar with the mathematics underlying colour digital images. Instead of matrices, tensors are used.

[![](embed/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=1502_en "Color Notebooks")

----
Colours occur in a spectrum.
![](embed/spectrum.png "Color spectrum")

The colours that humans see can be approximated by a combination of red (R), green (G), and blue (B) shades.<br>
Colours can be digitally represented using RGB. In that case, a separate table is needed for the red, green, and blue components; together, these form a 3D grid.

![](embed/rgb.png "RGB")

![](embed/raster.png "3D grid")

The colours on a television set, for example, are also constructed using RGB, as you can see in the following zoomed-in photo of a part of a television image.

![](embed/RGBtelevisie.jpg "RGB")
