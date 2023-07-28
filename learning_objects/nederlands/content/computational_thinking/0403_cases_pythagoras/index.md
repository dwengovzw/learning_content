---
hruid: ct_cases3
version: 3
language: nl
title: "Pythagoras - schuine zijde"
description: "Pythagoras - schuine zijde"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
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
# De stelling van Pythagoras: berekenen schuine zijde

### Doel

**Het berekenen van de schuine zijde bij gekende rechthoekszijden automatiseren.** 

<div class="alert alert-box alert-warning">
Eens de leerlingen over het programma beschikken, kunnen ze het gebruiken om complexe problemen op te lossen die zich herleiden tot bovenstaand opgelost probleem. De focus van de les kan dan liggen op het mathematiseren van het probleem, waarna de oplossing kan bepaald worden m.b.v. de computer.
</div>

**Doelgroep:** 2de graad, dubbele finaliteit of finaliteit doorstroom

**Vak**: Wiskunde

### Stap 1

**Voorkennis:** De leerlingen kennen de stelling van Pythagoras in formulevorm. Ze kunnen a.d.h.v. de stelling van Pythagoras de schuine zijde van een rechthoekige driehoek manueel berekenen. 

![ct-schema](@learning-object/m_ct_cases3a/nl/3)

### Stap 2

**Voorkennis:** De leerlingen weten hoe ze input kunnen vragen aan de gebruiker, of ze kunnen het hier aanleren. 

![ct-schema](@learning-object/m_ct_cases3a/nl/3)

### Stap 3: toepassen van patroonherkenning en abstractie

**Voorkennis:** De leerlingen hebben eventueel al geleerd om in Python een functie te definiëren, of dat kan hier worden aangebracht.

![ct-schema](@learning-object/m_ct_cases3b/nl/3)

### Toepassing: afstand in vogelvlucht

**Voorkennis:** De leerlingen gebruiken de zelfgedefinieerde functie in een oefening met context.

#### Uitdaging: "New York. Wat is de afstand in vogelvlucht van Times Square naar het Empire State Building, uitgedrukt in kilometer". 

*De leerlingen bedenken zelf dat ze een routeplanner en de stelling van Pythagoras kunnen gebruiken.*

![ct-schema](@learning-object/m_ct_cases3c/nl/3)

### Minimumdoelen (Bron: onderwijsdoelen.be)

<span style="color: yellowgreen">(06.06 Finaliteit doorstroom) De leerlingen passen de stelling van Pythagoras toe om meetkundige problemen op te lossen in het vlak en in de ruimte.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Memorie: <br>
&nbsp;&nbsp;&nbsp;&nbsp;‘In de ruimte’: bv. een ruimtediagonaal in een kubus of balk waarbij leerlingen het geschikte vlak tweemaal moeten kiezen.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Het is aangewezen om zowel met als zonder context te werken. Werken met contexten kan leerlingen immers motiveren. Wiskunde leren met en zonder contexten is belangrijk om kennis en vaardigheden te transfereren naar gelijkaardige en naar nieuwe situaties.

<span style="color: yellowgreen">(06.06 Dubbele finaliteit) De leerlingen passen de stelling van Pythagoras toe om meetkundige problemen op te lossen in het vlak.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Memorie: <br>
&nbsp;&nbsp;&nbsp;&nbsp;Het oplossen van meetkundige problemen in het vlak kan ook betrekking hebben op ruimtelijke situaties, met name die situaties waarin leerlingen eenmaal het geschikte vlak moeten kiezen. Bv. de ladder die tegen een muur wordt gezet, de IKEA-kast die in een ruimte moet passen. <br>
&nbsp;&nbsp;&nbsp;&nbsp;Het is aangewezen om zowel met als zonder context te werken. Werken met contexten kan leerlingen immers motiveren. Wiskunde leren met en zonder contexten is belangrijk om kennis en vaardigheden te transfereren naar gelijkaardige en naar nieuwe situaties.

<span style="color: yellowgreen">(06.52 Finaliteit doorstroom) De leerlingen ontwerpen een oplossing voor een probleem door wetenschappen, technologie of wiskunde geïntegreerd aan te wenden.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Memorie:<br>
&nbsp;&nbsp;&nbsp;&nbsp;STEM betekent per definitie dat je geïntegreerd denkt. De mate van integratie is afhankelijk van het probleem. <br>
&nbsp;&nbsp;&nbsp;&nbsp;Ook niet-STEM-disciplines kunnen aan bod komen.<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;Voetnoot: Rekening houdend met concepten van de tweede graad en de context waarin dit minimumdoel aan bod komt.

<span style="color: yellowgreen">(06.36 Dubbele finaliteit) De leerlingen ontwerpen een oplossing voor een probleem door wetenschappen, technologie of wiskunde geïntegreerd aan te wenden.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Memorie:<br>
&nbsp;&nbsp;&nbsp;&nbsp;STEM betekent per definitie dat je geïntegreerd denkt. De mate van integratie is afhankelijk van het probleem. <br>
&nbsp;&nbsp;&nbsp;&nbsp;Ook niet-STEM-disciplines kunnen aan bod komen.<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;Voetnoot: Rekening houdend met concepten van de tweede graad en de context waarin dit minimumdoel aan bod komt.

<span style="color: yellowgreen">(04.05 Finaliteit doorstroom; Dubbele finaliteit, Finaliteit arbeidsmarkt) De leerlingen analyseren de impact van digitale systemen op de maatschappij vanuit principes van computationeel denken.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Memorie:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Principes van computationeel denken zoals decompositie, patroonherkenning, abstractie en algoritmen.<br>
&nbsp;&nbsp;&nbsp;&nbsp;De impact van digitale systemen op de maatschappij vanuit principes van computationeel denken zoals algoritmes die digitale platformen gebruiken bij
het selecteren en presenteren van informatie aan gebruikers;
het verzamelen van persoonlijke informatie van gebruikers en die (mis)(ge)bruiken voor eigen doeleinden;
het beïnvloeden van de keuzes van gebruikers (vb. gepersonaliseerd aanbod, gepersonaliseerde reclame);
het beïnvloeden van de blik op de wereld/opinie van gebruikers ;
het nemen van beslissingen over gebruikers (vb. over kredietaanvragen, sollicitaties, verzekeringen);
het creëren van taalinteractie met behulp van artificiële intelligentie (chatbot);
het creëren van kunst (beelden, muziek, poëzie, andere kunstvormen) met behulp van artificiële intelligentie;
medische beeldvorming om op basis van een eerste scan eventuele afwijkingen te melden aan artsen.

### Vernietigde eindtermen (Bron: onderwijsdoelen.be)

<span style="color: yellowgreen">(4.5 Finaliteit doorstroom) De leerlingen ontwerpen algoritmen om problemen digitaal op te lossen.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau creëren

<span style="color: yellowgreen">(4.5 Dubbele finaliteit) De leerlingen lossen een afgebakend probleem digitaal op door een aangereikt algoritme aan te passen. </span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau creëren

<span style="color: yellowgreen">(Vernietigde eindterm 6.4 Finaliteit doorstroom, Dubbele finaliteit) De leerlingen passen geschikte meetkundige concepten en eigenschappen van vlakke figuren toe om vlakke en ruimtelijke problemen op te lossen:
* gelijkvormigheidskenmerken van driehoeken 
* de stelling van Thales
* de stelling van Pythagoras
* goniometrische getallen in een rechthoekige driehoek
* bijzondere lijnen in driehoeken
</span>

&nbsp;&nbsp;&nbsp;&nbsp; De eindterm wordt zowel met als zonder context gerealiseerd.

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau toepassen

<span style="color: yellowgreen">(6.4 Dubbele finaliteit) De leerlingen passen in betekenisvolle situaties geschikte meetkundige concepten en eigenschappen van vlakke figuren toe om vlakke en ruimtelijke problemen op te lossen:
* gelijkvormigheid van driehoeken
* de stelling van Pythagoras
* goniometrische getallen in een rechthoekige driehoek
</span>

&nbsp;&nbsp;&nbsp;&nbsp;De eindterm wordt zowel met als zonder context gerealiseerd.

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau toepassen

<span style="color: yellowgreen">(6.55 Finaliteit doorstroom; 6.31 Dubbele finaliteit) De leerlingen ontwerpen een oplossing voor een probleem door concepten en praktijken uit verschillende STEM-disciplines geïntegreerd aan te wenden.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Met inbegrip van context<br>
&nbsp;&nbsp;&nbsp;&nbsp;* Elke STEM-discipline komt ten minste één maal geïntegreerd aan bod.

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau creëren
