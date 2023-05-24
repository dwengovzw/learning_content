---
hruid: un_biomimicry8
version: 3
language: nl
title: "Radardiagrammen"
description: "Biomimicry"
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
estimated_time: 
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Vergelijken van de enkel-voet-ortheses
We willen de verschillende enkel-voet-ortheses vergelijken met elkaar. We kunnen dit doen met behulp van een radardiagram. Een radardiagram, ook wel spindiagram genoemd, combineert verschillende parameters. We maken nu voor iedere enkel-voet-orthese een radardiagram.
De leerlingen maken zelf de radardiagrammen op uit onderstaande dataset. Hier wordt stap voor stap uitgelegd hoe ze tot die radardiagrammen komen.


## Stap 1: dataset aanvullen: 'op maat van de patiënt' 

Van de bestaande ortheses vind je hieronder een tabel met de verschillende eigenschappen. Dit is ook de dataset die de leerlingen krijgen.
|                 | **Malleloc-L** | **ROM Walker** | **M-step** | **Stabili-tri** | **EXO-L** | **B2-foot** | **Zeepaardje orthese** |
|-----------------|----------------|----------------|------------|-----------------|-----------|-------------|------------------------|
| Compatibiliteit | 3              | 4              | 3          | 3               | 3         | 1           | 5 |
| Prijs           | 70             | 253.8          | 85         | 175          | 172     | 115       | 127.5 |
| Stabiliteit     | 2              | 5              | 4          | 4               | 2         | 5           | 4 | 
| Hygiëne         | 2              | 1              | 2          | 3               | 3         | 5           | 3 |

**Vanaf hier** moeten de leerlingen zelf de verschillende stappen doorlopen, maar ze krijgen niet aangereikd hoe ze die stappen moeten doorlopen. 

We kunnen daarvoor gebruikmaken van bovenstaande eigenschappen. Wetenschappers hebben die ‘gekwantificeerd’. 
Er ontbreekt nog één parameter: namelijk ‘op maat van de patiënt’. Die staat nog niet in de tabel maar is wel opgenomen als belangrijke eigenschap. We moeten eerst ook nog iedere enkel-voet-orthese een cijfer geven voor ‘op maat van de patiënt’. We zouden ervoor kunnen kiezen de orthese die volledig op maat van de patiënt is, de hoogste score te geven en dan af te tellen. Maar dan verkrijg je niet zo’n optimale weergave. Beter is om eerst scores te bepalen en met wat die score overeenkomt. We doen dit eerst in onderstaande tabel:

| **Score:** | **Betekenis:**                  |
|------------|---------------------------------|
| 5          | Volledig op maat van de patiënt |
| 4          | 5 vormen of meer                |
| 3          | 4-5 vormen of meer              |
| 2          | 2-3 vormen of meer              |
| 1          | Slechts één universele vorm     |

Nu we dit hebben kunnen we de score toekennen aan de orthese. We bekomen het volgende:
|                 | **Malleloc-L** | **ROM Walker** | **M-step** | **Stabili-tri** | **EXO-L** | **B2-foot** | **Zeepaardje orthese** |
|-----------------|----------------|----------------|------------|-----------------|-----------|-------------|------------------------|
| Compatibiliteit | 3              | 4              | 3          | 3               | 3         | 1           | 5 | 
| Prijs           | 70             | 253.8          | 85         | 175          | 172     | 115       | 127.5 |
| Stabiliteit     | 2              | 5              | 4          | 4               | 2         | 5           | 4 |
| Hygiëne         | 2              | 1              | 2          | 3               | 3         | 5           | 3 |
| Op maat van de patiënt | 1 | 2 | 2 | 3 | 5 | 5 | 5 |

## Stap 2: Omgekeerde prijs gebruiken en normaliseren

Nu kunnen we radardiagrammen maken. Alleen zal deze nog geen volledig beeld geven. Alle scores werken namelijk als volgt: een lage score is slecht, een hoge score is goed. Voor ‘prijs’ werkt dit net omgekeerd, we willen een zo laag mogelijke prijs. Daarom moeten we de waarde van de prijs anders gaan bekijken. We doen dit door het **omgekeerde** te nemen van de prijs: 1/prijs. Daardoor krijgen we hoge waarden die een lage prijs weerspiegelen en omgekeerd. 

|                 | **Malleloc-L** | **ROM Walker** | **M-step** | **Stabili-tri** | **EXO-L** | **B2-foot** | **Zeepaardje orthese** |
|-----------------|----------------|----------------|------------|-----------------|-----------|-------------|------------------------|
| Compatibiliteit | 3              | 4              | 3          | 3               | 3         | 1           | 5 |
| Prijs           | 85             | 253.8          | 80         | 184.95          | 169       | 100         | 127.5 |
| 1/Prijs         | 0.01429    | 0.00394        | 0.01176     | 0.00571        | 0.005817  | 0.0087 | 0.00784 |
| Stabiliteit     | 2              | 5              | 4          | 4               | 2         | 5           | 4 | 
| Hygiëne         | 2              | 1              | 2          | 3               | 3         | 5           |3 |
| Maat| 1 | 2 | 2 | 3 | 5 | 5 | 5 |

Een radardiagram kunnen we opstellen, maar daarvoor moeten we zorgen dat alle assen **dezelfde schaal** hanteren. Anders kunnen we ze niet t.o.v. elkaar vergelijken. We hebben geluk: alle eigenschappen buiten ‘1/Prijs’ staan al op éénzelfde schaal: namelijk een getal tussen 1 en 5. Enkel de omgekeerde prijs wordt nu uitgedrukt in veel te kleine getallen. We moeten deze eigenschap dus hetzelfde interpreteren als de anderen; de prijs moet namelijk een ‘score’ krijgen. Dit doen we door ieder getal te delen door de maximumwaarde van de volledige rij. De goedkoopste enkel-voet-orthese krijgt dan de score ‘1’, alle anderen krijgen een score tussen 0 en 1.

|                 | **Malleloc-L** | **ROM Walker** | **M-step** | **Stabili-tri** | **EXO-L** | **B2-foot** | **Zeepaardje orthese** |
|-----------------|----------------|----------------|------------|-----------------|-----------|-------------|------------------------|
| Compatibiliteit | 3              | 4              | 3          | 3               | 3         | 1           | 5 |
| 1/Prijs         | 1       | 0.27581        | 0.82353     | 0.4       | 0.40698  | 0.6087 | 0.54902 |
| Stabiliteit     | 2              | 5              | 4          | 4               | 2         | 5           | 4 | 
| Hygiëne         | 2              | 1              | 2          | 3               | 3         | 5           |3 |
| Maat| 1 | 2 | 2 | 3 | 5 | 5 | 5 |

Tot slot moeten we de omgekeerde prijs alleen nog vermenigvuldigen met 5, we doen dit om de waarden te **normaliseren**. Op deze manier bekomen we een score tussen 0 en 5 en niet tussen 0 en 1. We bekomen het volgende:

|                 | **Malleloc-L** | **ROM Walker** | **M-step** | **Stabili-tri** | **EXO-L** | **B2-foot** | **Zeepaardje orthese** |
|-----------------|----------------|----------------|------------|-----------------|-----------|-------------|------------------------|
| Compatibiliteit | 3              | 4              | 3          | 3               | 3         | 1           | 5 |
| 1/Prijs         | 5       | 1.37904       | 4.11765          | 2        | 2.03488  | 3.04348           | 2.7451 |
| Stabiliteit     | 2              | 5              | 4          | 4               | 2         | 5           | 4 | 
| Hygiëne         | 2              | 1              | 2          | 3               | 3         | 5           |3 |
| Maat| 1 | 2 | 2 | 3 | 5 | 5 | 5 |


Eens dit alles is opgelost, kunnen de leerlingen de radardiagrammen opmaken.

Een radardiagram opmaken doe je zo:
* [Bekijk](embed/Radardiagram_Excel.pdf "pdf") het stappenplan voor Microsoft Excel
* [Bekijk](embed/Radardiagram_Spreadsheets.pdf "pdf") het stappenplan voor Google Spreadsheets 

[Hier](embed/Radardiagram_orthese.pdf "pdf") kan je de verschillende radardiagrammen bekijken
