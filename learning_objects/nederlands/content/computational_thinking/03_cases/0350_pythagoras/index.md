---
hruid: ct03_50
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

**De berekening van de schuine zijde van een rechthoekige driehoek op basis van gegeven rechthoekszijden automatiseren.**

Wil je met je leerlingen programmeren in de wiskundeles? Dit onderwerp leent er zich toe.

Samen met de leerlingen bouw je stap voor stap een applicatie om het rekenwerk bij de stelling van Pythagoras te automatiseren. Je vertrekt daarbij van één type oefening. Een tweede type kan je door de leerlingen alleen laten doen; dan is het ineens duidelijk of ze alles begrepen hebben. 

Een troef van de stelling van Pythagoras is dat je gemakkelijk *real-world* toepassingen vindt.

Met het programmeren ga je zo ver als je zelf wilt. In dit uitgewerkt voorbeeld komen variabelen, datatypes en operatoren aan bod, vragen we input aan de gebruiker, en gebruiken we ingebouwde en zelfgedefinieerde functies. We maken ook gebruik van Python-modules (bibliotheken) en besteden aandacht aan het schrijven van commentaar. Indien gewenst, dan kan je de applicatie nog verder verbeteren en ook aan de slag gaan met keuze- en herhalingsstructuren. 

Deze case wordt toegelicht in dit filmpje. 

![](@youtube/https://www.youtube.com/embed/ZUl27Ek9zHo "filmpje case pythagoras") 

### Doel

**Het berekenen van de schuine zijde bij gekende rechthoekszijden automatiseren.** 

Eens de leerlingen over het programma beschikken, kunnen ze het gebruiken om complexe problemen op te lossen die zich herleiden tot bovenstaand opgelost probleem. De focus van de les kan dan liggen op het mathematiseren van het probleem, waarna de oplossing bepaald kan worden m.b.v. de computer.

**Doelgroep:** 2de graad, dubbele finaliteit of finaliteit doorstroom

**Vak**: Wiskunde

### Stap 1: automatiseren van het rekenwerk.

**Voorkennis:** De leerlingen kennen de stelling van Pythagoras in formulevorm. Ze kunnen a.d.h.v. de stelling van Pythagoras de schuine zijde van een rechthoekige driehoek manueel berekenen. 

![ct-schema](@learning-object/m_ct03_50d/nl/3)

In dit filmpje krijg je stap voor stap het programmeergedeelte te zien. 

![](@youtube/https://www.youtube.com/embed/oMFW-0mnAUU "demo case pythagoras") 

### Stap 2: input vragen aan de gebruiker.

**Voorkennis:** De leerlingen weten hoe ze input kunnen vragen aan de gebruiker, of ze kunnen het hier aanleren. 

![ct-schema](@learning-object/m_ct03_50a/nl/3)

<div class="alert alert-box alert-success">
    <strong>Leerdoel in functie van MD 04.05:</strong><br>
    De leerlingen zien in dat het belangrijk is dat je een applicatie gebruiksvriendelijk maakt, als je wil dat die applicatie wordt gebruikt. Gebruiksvriendelijkere digitale toepassingen zullen meer impact kunnen verwezenlijken.
</div>

### Stap 3: toepassen van patroonherkenning en abstractie.

**Voorkennis:** De leerlingen hebben eventueel al geleerd om in Python een functie te definiëren, of dat kan hier worden aangebracht.

![ct-schema](@learning-object/m_ct03_50b/nl/3)

### Toepassing: afstand in vogelvlucht

**Voorkennis:** De leerlingen gebruiken de zelfgedefinieerde functie in een oefening met context.

**Uitdaging: "New York. Wat is de afstand in vogelvlucht van Times Square naar het Empire State Building, uitgedrukt in kilometer?"**

*De leerlingen bedenken zelf dat ze een routeplanner en de stelling van Pythagoras kunnen gebruiken.*

![ct-schema](@learning-object/m_ct03_50c/nl/3)

<div class="alert alert-box alert-success">
<strong>Leerdoel in functie van MD 04.05:</strong><br> 
<ul>
    <li>Een van de redenen dat routeplanners zoveel gebruikt worden en dus zoveel impact hebben, is het gebruiksgemak. Dat een routeplanner zo gebruiksvriendelijk is, komt door de hoge graad van abstractie in de routplanner: de route is geabstraheerd tot aantal kilometers en tijdig afslaan; indien gewenst, kan je enkel de instructies opvolgen van de weg die je moet volgen (het stappenplan of algoritme). Je moet je niet bezighouden met het opzoeken van de weg op een kaart, waarbij je rekening zou moeten houden met bv. eenrichtingsverkeer, de oriëntatie van de kaart, enz. </li>
    <li>Bovendien krijg je er bijkomende informatie over bv. files, wegwerkzaamheden, waar je kan tanken, enz. </li>  
    <li>Omdat er in routeplanners zoveel geabstraheerd wordt, heb je geen volledig zicht meer op de omgeving. Dat kan ook een nadeel zijn t.o.v. een papieren kaart die veel meer details geeft van de omgeving, en een bepaalde plaats bovendien situeert in een groter gebied. Routeplanners hollen als het ware het ruimtelijk bewustzijn rond een plaats uit. Te veel afhankelijk zijn van digitale routeplanners kan daarom ook gevaarlijk zijn, mensen rijden bv. een treinspoor op of op een trap. </li>
    <li>Bij gebruik van een routeplanner moet je er rekening mee houden dat je in een gebied kunt terechtkomen waar er geen mobiel bereik is, of dat de batterij van je smartphone leeg kan lopen. </li>
    <li>Je moet er ook rekening mee houden dat sommige gebieden onvoldoende gedetailleerd of onnauwkeurig aanwezig kunnen zijn. En dat digitale routeplanners fouten kunnen bevatten, zoals een foute maximale snelheid die op een bepaalde weg is toegelaten of een straat met eenrichtingsverkeer die als tweerichtingsverkeer is aangegeven. </li>
    <li>Routeplanners hebben een impact op de maatschappij: Het gebruik van een routeplanner door zoveel mensen kan ongewenste effecten hebben, zoals extra verkeer in woonwijken, wanneer een routeplanner het autoverkeer langs woonwijken omleidt om files te vermijden. De vraag is met hoeveel aspecten van de omgeving het algoritme in de routeplanner rekening houdt. In de invoer is het misschien weggeabstraheerd dat een bepaalde omgeving een woonwijk is, of in het programma wordt er met die variabele geen rekening gehouden. Routeplanners kunnen reclame bevatten: Hoe wordt immers bepaald welke winkels, tankstations ... getoond worden in de routeplanner? Routeplanners hebben geleid tot nieuwe toepassingen in de maatschappij: ze worden bv. gebruikt door robots die boodschappen naar huis brengen of door medische drones; a.d.h.v. de routeplanner vinden ze de weg. Met het gebruik van een routeplanner kunnen ook privacyaspecten gemoeid zijn: Als de locaties van de gebruiker worden opgeslagen, dan rijst de vraag wat de verstrekker van de routeplanner aanvangt met die gegevens. </li>
</ul>
</div>

### Volgende stap: toepassen van patroonherkenning en abstractie

De leerlingen van de tweede graad worden in de wiskundeles ingewijd in de stelling van Pythagoras. Twee types van oefeningen vallen daarbij op:<br> 
-  ofwel zijn de rechthoekszijden van een rechthoekige driehoek gegeven en moet de schuine zijde berekend worden;
-  ofwel is de schuine zijde en een rechthoekszijde gegeven en moet de andere rechthoekszijde berekend worden.

De leerlingen bouwden een applicatie om het rekenwerk te doen bij een oefening van het eerste type. In de applicatie wordt een zelfgedefinieerde functie `pythagoras1()` gebruikt.<br>  
Een aanvulling bij deze case zou zijn dat de leerlingen een tweede functie toevoegen `pythagoras2()`, zodat met de applicatie het rekenwerk van beide types gedaan kan worden.
Vanaf dan kunnen een reeks vraagstukken aan de leerlingen aangeboden worden, waarbij de leerlingen vooral aan patroonherkenning moeten doen en telkens de applicatie gebruiken voor het rekenwerk.

<div class="alert alert-box alert-info">
<strong>Opmerking bij de naamgeving van de zelfgedefinieerde functies:</strong><br>
Het is beter de namen van de functies aan te passen zodat ze ineens ook vertellen wat de functies doen. In plaats van <code>pythagoras1()</code> gebruik je beter <code>bereken_schuine_zijde_uit_rechthoekszijden()</code> als naam van de functie. Analoog pas je de naam <code>pythagoras2()</code> aan naar <code>bereken_rechthoekszijde_uit_schuine_zijde_en_rechthoekszijde()</code>.<br>
Als je wilt bereiken dat de functie ook bruikbaar is voor wie niet vertrouwd is met de standaardnotaties <em>a, b</em> en <em>c</em> uit de wiskundeles, dan pas je best ook de parameters in de functies aan. Dus nog betere namen voor de functies zijn <code>bereken_schuine_zijde(rechthoekszijde_1, rechthoekszijde_2)</code> en <code>bereken_rechthoekszijde(schuine_zijde, rechthoekszijde)</code>.
</div>

----------------------------------------------------
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
* gelijkvormigheidskenmerken van driehoeken;
* de stelling van Thales;
* de stelling van Pythagoras;
* goniometrische getallen in een rechthoekige driehoek;
* bijzondere lijnen in driehoeken.
</span>

&nbsp;&nbsp;&nbsp;&nbsp; De eindterm wordt zowel met als zonder context gerealiseerd.

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau toepassen

<span style="color: yellowgreen">(6.4 Dubbele finaliteit) De leerlingen passen in betekenisvolle situaties geschikte meetkundige concepten en eigenschappen van vlakke figuren toe om vlakke en ruimtelijke problemen op te lossen:
* gelijkvormigheid van driehoeken;
* de stelling van Pythagoras;
* goniometrische getallen in een rechthoekige driehoek.
</span>

&nbsp;&nbsp;&nbsp;&nbsp;De eindterm wordt zowel met als zonder context gerealiseerd.

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau toepassen

<span style="color: yellowgreen">(6.55 Finaliteit doorstroom; 6.31 Dubbele finaliteit) De leerlingen ontwerpen een oplossing voor een probleem door concepten en praktijken uit verschillende STEM-disciplines geïntegreerd aan te wenden.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Met inbegrip van context<br>
&nbsp;&nbsp;&nbsp;&nbsp;* Elke STEM-discipline komt ten minste eenmaal geïntegreerd aan bod.

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau creëren
