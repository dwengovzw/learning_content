---
hruid: pn_toepassenpythagoras
version: 3
language: nl
title: "Toepassen op stelling van Pythagoras"
description: "Toepassen op stelling van Pythagoras"
keywords: ["Python", "Wiskunde"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-digitale-media-en-toepassingen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-meetkunde-en-metend-rekenen'
]
---
# Toepassen op de stelling van Pythagoras

De oefeningen bij de stelling van Pythagoras in het derde middelbaar zijn dikwijls te herleiden tot eenzelfde probleem: 2 zijden van een driehoek zijn gekend en de derde zijde moet berekend worden. 

Daarbij kan je twee types onderscheiden:
* ofwel zijn de 2 rechthoekszijden gegeven en moet de schuine zijde berekend worden;
* ofwel zijn 1 rechthoekszijde en de schuine zijde gegeven en moet de andere rechthoekszijde berekend worden.

Heb je beide types reeds eerder aangepakt, dan leidt het herkennen met welke van deze twee types je te maken hebt, rechtstreeks tot de oplossing van het probleem. Je moet enkel de eerder uitgewerkte oplossing nog aanpassen aan de nieuwe situatie. 

---
In deze notebooks zal je het nodige _rekenwerk overlaten aan de computer_. Je kan je dan ten volle concentreren op de gestelde problemen. 
 
Deze twee types van problemen vind je alvast terug in de eerste notebook. Om ze op te lossen volstaan twee _functies_ die je zelf zal definiëren in Python. Na het oplossen van de basisproblemen, zal je via _patroonherkenning_ de andere problemen aanpakken door de code bij de eerder opgeloste problemen aan te passen.  

In een tweede notebook vind je extra uitdagende oefeningen. Je wendt er bv. een _keuzestructuur_ aan en werkt er met de _afstand tussen twee punten_. 

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=0503 "Notebooks Pythagoras")

![](@youtube/https://www.youtube.com/watch?v=O2iGX2SLLAQ "Filmpje Pythagoras")

<div class="alert alert-box alert-secondary">
    In de laatste oefening van de tweede notebook gaat over het volgende:
<ul><li> De stelling van Pythagoras zegt:<br>als een driehoek rechthoekig is, dan volgt dat het kwadraat van de schuine zijde gelijk is aan de som van de kwadraten van de rechthoekszijden.</li></ul>
<ul><li> Volgens de wet van de <em>contrapositie</em> uit de logica, geldt dan:<br> 
als het kwadraat van de schuine zijde niet gelijk is aan de som van de kwadraten van de rechthoekszijden, dan is de driehoek niet rechthoekig. </li></ul>
<ul><li> M.b.v. de cosinusregel (in een willekeurige driehoek) kan je echter ook de omgekeerde stelling van Pythagoras bewijzen. Dus:<br>
als het kwadraat van de schuine zijde gelijk is aan de som van de kwadraten van de rechthoekszijden, dan is de driehoek rechthoekig. </li></ul>

Dus afhankelijk van welke leerstof er al gezien is, kan het resultaat dat in deze oefening geprint wordt, aaangepast worden.

 </div>
