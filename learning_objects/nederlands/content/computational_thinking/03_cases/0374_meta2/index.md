---
hruid: m_ct03_74b
version: 3
language: nl
title: "Matchen vingerafdrukken"
description: "Matchen vingerafdrukken"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/ct-schema
available: true
target_ages: [12, 13, 14]
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

<context>
Je wil dat een computer vingerafdrukken met elkaar vergelijkt. Hoe doe je dat?
</context>
<decomposition>
Subtaken (**decompositie**):
<ol>
    <li>In welk formaat zullen de vingerafdrukken aan de computer worden gegeven? 
        <ul>
            <li>Digitale foto’s</li>
	        <li>Niet te groot omwille van opslagruimte en moet verzonden kunnen worden.</li>
        <ul>
    </li>
    <li>Karakterisatie: bepaal kenmerken (en eventueel aantal) die volstaan om de vingerafdruk te onderscheiden van andere vingerafdrukken, o.a. de herkenningspunten.  </li>
    <li>De foto’s moeten voorverwerkt worden (ruis verwijderen, zwart-wit maken, de lijnen versmallen tot 1 pixel breed). </li>
    <li>De gekozen kenmerken opsporen en aanduiden op de foto’s. Hoe kan dit met een algoritme gebeuren?</li>
    <li>De voorstelling abstraheren tot een graaf met de herkenningspunten als knopen, met elkaar verbonden als ze op eenzelfde lijn liggen, het type van herkenningspunt weergeven door een kleur, de afstand tussen deze punten als gewicht van de bogen gebruiken. Er is dus een nieuw type graaf nodig: een gekleurde, gewogen graaf.</li>
    <li>Twee soorten problemen: identificatie en authenticatie</li>
</ol>
</decomposition>
<patternRecognition>
Digitale beeldverwerking gebeurt typisch via de pixelwaarden, dus ook hier zal men de pixelwaarden gebruiken om bv. de herkenningspunten op te sporen. (**patroonherkenning**)

Om het probleem van inkleuring van kaarten aan te pakken, gebruikt men een graaf, waarbij buurlanden knopen zijn die met elkaar verbonden zijn. Hier kan men de herkenningspunten als knopen nemen van een graaf, waarbij herkenningspunten op eenzelfde lijn met elkaar worden verbonden. (**patroonherkenning**)
</patternRecognition>
<abstraction>
De herkenningspunten samen met andere kenmerken die vastgelegd worden om de vingerafdruk te onderscheiden van andere vingerafdrukken vormen een abstracte voorstelling van de vingerafdruk. (**abstractie**)<br>    
Men kan dit bv. samenvatten d.m.v. een abstracte visualisatie, bv. een gekleurde, gewogen graaf.
De herkenningspunten worden bepaald door van elk punt een getal te bepalen waaruit kan worden afgeleid welk soort punt het is. Dat getal is een abstractie van het type herkenningspunt.  
</abstraction>
<algorithms>
Er zijn meerdere algoritmes nodig.<br>
Een algoritme om <br>
<ul>
    <li>de ruis weg te halen;</li>
    <li>de foto’s zwart-wit te maken;</li>
    <li>de lijnen te verdunnen tot 1 pixel;</li>
    <li>de herkenningspunten op te sporen;</li>
    <li>de gekleurde, gewogen graaf op te stellen;</li>
    <li>een nieuwe vingerafdruk te matchen met een vingerafdruk in de dataset (voor identificatie);</li>
    <li>te controleren of de vingerafdruk overeenkomt met de vingerafdruk in de dataset (bij authenticatie);</li>
    <li>eventueel het scantoestel aan te sturen waarmee de foto’s worden gemaakt (detecteren dat er een vinger op ligt);</li>
    <li>de fotobestanden te comprimeren.</li>
</ul>
</algorithms>
<implementation>
Bij dit voorbeeld moet er niet geprogrammeerd worden.
</implementation>
