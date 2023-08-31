---
hruid: m_ct_cases12
version: 3
language: nl
title: "Locked-in"
description: "Locked-in"
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
Locked-in syndroom: Een man, Bauby,  wordt volledig verlamd wakker in het ziekenhuis. Hij kan enkel nog knipperen met één oog. Hij vindt toch een manier om te communiceren en slaagt er zo zelfs in om een boek te schrijven. 
</context>
<decomposition>
**Decompositie:**<br>
1. Wat is er nog mogelijk? 
    - Bauby kan knipperen met één oog. 
	- Bauby kan lezen en horen. Hij kan niet praten.
	- Helper kan praten, lezen en schrijven. 
2. Hoe zou Bauby kunnen communiceren?
    - Woorden bestaan uit letters. Het knipperen met een oog zal moeten omgezet worden naar letters. Bv. één keer knipperen betekent ‘A’, 2 keer knipperen ‘B’, enz. De helper hoeft alleen maar het aantal keer dat geknipperd wordt te tellen en de bijbehorende letter op te schrijven. 	
3. Hoe zou Bauby een boek kunnen schrijven?
    Op dezelfde manier, maar ook spaties, leestekens, cijfers, witruimtes ... toevoegen aan het alfabet.
4. Er moeten worden afgesproken hoe te communiceren als er per ongeluk een fout wordt gemaakt, of om een gok van de helper goed of af te keuren.
5. Hoe kan het sneller? 
    - Moment van knipperen gebruiken i.p.v. het aantal keer.
    - Eerst de courante letters vragen door de volgorde van de letters in het alfabet aan te passen.
    - 'Binair zoeken' garandeert dat elke letter gevonden wordt na hoogstens 5 letters op te sommen!
6. Kunnen we het automatiseren met technologie?
</decomposition>
<patternRecognition>
Soms kan je halverwege een woord al raden wat het is. Als je ‘a-n-t-i-l’ hebt, zou het woord ‘antiloop’ een goede gok zijn. Dat is hetzelfde als de ‘woordsuggestie’ op een smartphone. (**patroonherkenning**)<br>
Sommige letters komen meer voor dan andere. Door de eeuwen heen werd frequentieanalyse gebruikt om geheime codes te kraken. Het kraken van codes en het raden van letters zijn vergelijkbare problemen (patroonherkenning). Bauby liet daarom de helper de letters voorlezen in volgorde van dalende frequentie (in de Franse taal).<br> 
Een geschikte ‘verdeel-en-heers’ zoekstrategie om te zoeken tussen dingen met een bepaalde volgorde is binair zoeken. Je stelt dan halveringsvragen (denk aan het spel 'Wie is het?'). (**patroonherkenning**)
</patternRecognition>
<abstraction>
Het aantal keer knipperen, een getal dus, is een abstractie van een letter, leesteken ... <br>
Dus om te weten wat het snelste algoritme is, moet je de hoeveelheid letters die de helper moet overlopen, bepalen. (**abstractie**) Je kan dit inschatten door het gemiddeld aantal opgesomde letters per letter te schatten.
</abstraction>
<algorithms>
**Algoritme** dat Bauby gebruikte:<br>
De helper las telkens weer het alfabet hardop voor in de volgorde: “E, S, A, R, ..., W”. <br>
Als de letter waar Bauby aan dacht, werd uitgesproken, dan knipperde hij met zijn ogen. De helper schreef die letter op en begon toen opnieuw, letter voor letter. 
    
**Verbeterd algoritme:**<br>
    via verdeel-en-heers (binair zoeken).
</algorithms>
<implementation>
Bij het zoeken naar een oplossing voor een probleem en bij de implementatie ervan gaat men best uit van het principe 'de mens komt eerst'! Hebben we wel met de juiste aspecten van het probleem rekening gehouden? <br>
Wat als knipperen een grote inspanning was voor Bauby? Zijn oplossing hield in dat hij slechts één keer per letter knipperde. Ons verdeel-en-heersalgoritme vereist dat hij 5 keer knippert. Zijn oplossing is gemakkelijk te begrijpen voor iedereen, de onze is complexer. Wie zal het uitleggen aan bezoekers? <br>
Kan automatiseren niet meer kwaad dan goed doen? Er zouden dan geen helpers meer zijn die zorgen voor menselijke warmte. 
	
	Bij dit voorbeeld moet niet geprogrammeerd worden.
</implementation>

