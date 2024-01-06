---
hruid: pim_statistiek_inleiding
version: 3
language: nl
title: "Inleiding"
description: "Inleiding"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [15, 16, 17, 18]
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

# Inleiding

Voorkennis voor dit leerpad: het leerpad ['Werken met notebooks'](https://www.dwengo.org/learning-path.html?hruid=pn_werking&language=nl&te=true&source_page=%2Fmath_with_python%2F&source_title=%20Python%20in%20de%20Wiskundeles#pn_werkingnotebooks;nl;3).

Een aanvulling op dit leerpad is bivariate statistiek: het visualiseren van een puntenwolk en het eventueel bepalen van een de bijbehorende regressielijn. Zie daarvoor de leerpaden ['Spreidingsdiagram'](https://www.dwengo.org/learning-path.html?hruid=maths_spreidingsdiagrammen&language=nl&te=true&source_page=%2Fmath_with_python%2F&source_title=%20Python%20in%20de%20Wiskundeles#pn_inleiding_spreidingsdiagram;nl;3), ['Lineaire regressie'](https://www.dwengo.org/learning-path.html?hruid=maths_lineaireregressie&language=nl&te=true&source_page=%2Fmath_with_python%2F&source_title=%20Python%20in%20de%20Wiskundeles#pn_inleiding_lineaireregressie;nl;3), ['Regressielijnen'](https://www.dwengo.org/learning-path.html?hruid=pn_regressie&language=nl&te=true&source_page=%2Fmath_with_python%2F&source_title=%20Python%20in%20de%20Wiskundeles#pn_voorkennis_regressielijnen;nl;3).

Een inleiding tot het werken met NumPy-lijsten in het kader van lessen statistiek vind je in de tweede notebook van deze [reeks](https://dwengo.org/backend/api/learningObject/getWrapped?hruid=pn_nplijsten&version=3&language=nl).

De volgende drie onderdelen zijn te situeren binnen de beschrijvende statistiek. Het laatste onderdeel maakt een verbinding tussen de beschrijvende en de verklarende statistiek. 

------

### Minimumdoel grote datasets

**Dit leerpad sluit ook aan bij de nieuwe specifieke minimumdoelen over statistiek in de derde graad i.v.m. grote datasets.**

**Statistiek**<br>
*Deze specifieke eindtermen zijn geldig in de volgende studierichtingen: Freinetpedagogie, Humane wetenschappen* 

*06.01.05 De leerlingen analyseren grote datasets met behulp van statistische software in functie van een statistisch onderzoek.* <br>
*Memorie: De grote datasets zijn ofwel aangereikt of kwamen zelf tot stand (bijvoorbeeld in het kader van een project). De dataset is voldoende groot om een antwoord op de onderzoeksvraag te kunnen formuleren.*

### Andere minimumdoelen

#### Minimumdoelen wiskunde tweede graad - Finaliteit doorstroom

*06.18 De leerlingen analyseren statistische gegevens aan de hand van voorstellingswijzen en centrum- en spreidingsmaten.* <br>
*Onderliggende (kennis)elementen: Voorstellingswijzen: absolute en relatieve frequentietabel, staafdiagram, cirkeldiagram, lijndiagram, histogram en boxplot. Centrum- en spreidingsmaten: rekenkundig gemiddelde, mediaan, modus, variatiebreedte, interkwartielafstand en standaardafwijking. Misleidingen.*

*06.21 De leerlingen beschrijven fenomenen uit de realiteit aan de hand van wiskundige concepten uit de tweede graad.*

#### Minimumdoelen wiskunde tweede graad - Dubbele finaliteit

*06.16 De leerlingen analyseren statistische gegevens aan de hand van voorstellingswijzen en centrum- en spreidingsmaten.* <br>
*Onderliggende (kennis)elementen: Voorstellingswijzen: absolute en relatieve frequentietabel, staafdiagram, cirkeldiagram, lijndiagram, histogram en boxplot. Centrum- en spreidingsmaten: rekenkundig gemiddelde, mediaan, variatiebreedte, interkwartielafstand. Misleidingen.*

*06.17 De leerlingen beschrijven fenomenen uit de realiteit aan de hand van wiskundige concepten uit de tweede graad.*

#### Minimumdoelen wiskunde derde graad - Finaliteit doorstroom

*06.15 De leerlingen leggen in concrete situaties het verschil uit tussen samenhang en causaliteit.*

*06.16 De leerlingen gebruiken de normale verdeling als continu model bij gegeven data.* <br>
*Onderliggende (kennis)elementen: Grafische beoordeling van de toepasbaarheid van het model. Rekenkundig gemiddelde en de standaardafwijking van de gegeven data als schatting voor de parameters van het model. Grafische betekenis van gemiddelde en standaardafwijking van een normaal verdeelde kansvariabele in termen van de Gausskromme.* 

*06.19 De leerlingen beschrijven fenomenen uit de realiteit aan de hand van wiskundige concepten uit de derde graad.* 

*06.21 De leerlingen gebruiken ICT om berekeningen uit te voeren en grafische voorstellingen te maken.* <br>
*Voetnoot: Rekening houdend met concepten van de derde graad.*

#### Minimumdoelen wiskunde derde graad - Dubbele finaliteit

*06.08 De leerlingen leggen in concrete situaties het verschil uit tussen samenhang en causaliteit.*

*06.09 De leerlingen gebruiken de normale verdeling als continu model bij gegeven data.* <br>
*Onderliggende (kennis)elementen: Grafische beoordeling van de toepasbaarheid van het model. Rekenkundig gemiddelde en de standaardafwijking van de gegeven data als schatting voor de parameters van het model. Grafische betekenis van gemiddelde en standaardafwijking van een normaal verdeelde kansvariabele in termen van de Gausskromme.* 

*06.11 De leerlingen beschrijven fenomenen uit de realiteit aan de hand van wiskundige concepten uit de derde graad.* 

*06.13 De leerlingen gebruiken ICT om berekeningen uit te voeren en grafische voorstellingen te maken.* <br>
*Voetnoot: Rekening houdend met concepten van de derde graad.*
