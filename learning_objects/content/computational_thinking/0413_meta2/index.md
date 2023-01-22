---
hruid: m_ct_cases13b
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
1. In welk formaat zullen de vingerafdrukken aan de computer worden gegeven? 
    - Digitale foto’s
	- Niet te groot omwille van opslagruimte en moet verzonden kunnen worden.
2. Karakterisatie: bepaal kenmerken (en eventueel aantal) die volstaan om de vingerafdruk te onderscheiden van andere vingerafdrukken, o.a. de herkenningspunten.  
3. De foto’s moeten voorverwerkt worden (ruis verwijderen, zwart-wit maken, de lijnen versmallen tot 1 pixel breed). 
4. De gekozen kenmerken opsporen en aanduiden op de foto’s. Hoe kan dit met een algoritme gebeuren?
5. De voorstelling abstraheren tot een graaf met de herkenningspunten als knopen, met elkaar verbonden als ze op eenzelfde lijn liggen, het type van herkenningspunt weergeven door een kleur, de afstand tussen deze punten als gewicht van de bogen gebruiken. Er is dus een nieuw type graaf nodig: een gekleurde, gewogen graaf.
6. Twee soorten problemen: identificatie en authenticatie
</decomposition>
<patternRecognition>
Digitale beeldverwerking gebeurt typisch via de pixelwaarden, dus ook hier zal men de pixelwaarden gebruiken om bv. de herkenningspunten op te sporen. (**patroonherkenning**)

Om het probleem van inkleuring van kaarten aan te pakken, gebruikt men een graaf, waarbij buurlanden knopen zijn die met elkaar verbonden zijn. Hier kan men de herkenningspunten als knopen nemen van een graaf, waarbij herkenningspunten op een zelfde lijn met elkaar worden verbonden. (**patroonherkenning**)
</patternRecognition>
<abstraction>
De herkenningspunten samen met andere kenmerken die vastgelegd worden om de vingerafdruk te onderscheiden van andere vingerafdrukken vormen een abstracte voorstelling van de vingerafdruk. (**abstractie**)<br>    
Men kan dit bv. samenvatten d.m.v. een abstracte visualisatie, bv. een gekleurde, gewogen graaf.
De herkenningspunten worden bepaald door van elk punt een getal te bepalen waaruit kan worden afgeleid welk soort punt het is. Dat getal is een abstractie van het type herkenningspunt.  
</abstraction>
<algorithms>
    Er zijn meerdere algoritmes nodig.<br>
Een algoritme om ...<br>
- de ruis weg te halen
- de foto’s zwart-wit te maken
- de lijnen te verdunnen tot 1 pixel
- de herkenningspunten op te sporen
- de gekleurde, gewogen graaf op te stellen
- een nieuwe vingerafdruk te matchen met een vingerafdruk in de dataset (voor identificatie)
- te controleren of de vingerafdruk overeenkomt met de vingerafdruk in de dataset (bij authenticatie) 
- eventueel het scantoestel aan te sturen waarmee de foto’s worden gemaakt (detecteren dat er een vinger op ligt)
- de fotobestanden te comprimeren
</algorithms>
<implementation>
Bij dit voorbeeld moet er niet geprogrammeerd worden.
</implementation>
