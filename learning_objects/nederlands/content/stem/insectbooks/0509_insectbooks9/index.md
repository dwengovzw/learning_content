---
hruid: stem5_9
version: 3
language: nl
title: "De eindige differentiemethode"
description: "De eindige differentiemethode"
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
teacher_exclusive: false
---
# De eindige differentiemethode

In de vorige modules maakte je voor het eerst kennis met (groei)modellen. Realistisch of niet, deze werden gekarakteriseerd doordat ze discreet in de tijd waren: de tijd tikte generatie per generatie voorbij. In de praktijk ervaren we tijd echter als continu: tussen vandaag en morgen zitten een oneindig aantal individuele momenten. In deze module bespreken we daarom een belangrijk instrument om met continue functies en hun afgeleiden aan de slag te gaan: **de eindige differentiemethode**.

## Het gebruik van functies

Bij het modelleren gebruik je functies, die een gegeven input omzetten naar een output. Beschouw bijvoorbeeld de functie \\(f\\) met voorschrift \\(f(t) = t sin (t)\\). Deze functie zal een reële waarde \\(t\\) omzetten naar \\(t sin(t)\\), waarbij \\(t\\) een hoek (in radialen) is.

### Opdracht 1

Evalueer het functievoorschrift voor de waarden \\(t = \frac{\pi}{2}\\), \\(t = \pi\\), \\(t = \frac{3 \pi}{2}\\), \\(t = 2 \pi\\), \\(t = \frac{5 \pi}{2}\\), \\(t = 3 \pi\\), \\(t = \frac{7 \pi}{2}\\), \\(t = 4 \pi\\). Welke waarden bekom je? Kan je voorspellen hoe de functie zal evolueren voor grotere waarden van \\(t\\)?

\\(f(\frac{\pi}{2}) = 1.57\\)

\\(f(\pi) = 0\\)

\\(f(\frac{3 \pi}{2}) = -4.71\\)

\\(f(2 \pi) = 0\\)

\\(f(\frac{5 \pi}{2}) = 7.85\\)

\\(f(3 \pi) = 0\\)

\\(f(\frac{7 \pi}{2}) = -11.00\\)

\\(f(4 \pi) = 0\\)

## Het differentiequotiënt

Van een afleidbare functie kan je een afgeleide berekenen. Deze afgeleide kan benaderd worden door het differentiequotiënt:

\\(\\)f'(t) = \frac{\text{d}f(t)}{\text{d}t} \approx \frac{f(t + \Delta t) - f(t)}{\Delta t}\\(\\)

De formule die hier gebruikt wordt om de afgeleide te schatten wordt de **eindige differentiemethode** genoemd. Bij deze methode is \\(\Delta_t\\) bij voorkeur zo klein mogelijk.

### Opdracht 2

Bereken op basis van bovenstaande formule een schatting voor het differentiequotiënt van \\(f\\) in \\(t = 2\\), waarbij je \\(\Delta t = 0.1\\) stelt.

\\(f(2) = 2 sin(2) \approx 1.8186\\)

\\(f(t + \Delta t) = f(2.1) = 2.1 sin(2.1) \approx 1.8127\\)

\\(f(t + \Delta t) - f(t) \approx 1.8127 - 1.8186 = -0.0059\\)

\\(\frac{f(t + \Delta t) - f(t)}{\Delta t} \approx \frac{-0.0059}{0.1} = -0.059\\)

## De afgeleide van een functie

Wanneer je kleinere stapjes neemt, neemt de absolute waarde van het verschil \\(f(t + \Delta t) - f(t)\\) typisch af, maar deel je ook door een steeds kleiner getal. Wanneer je de limiet van \\(\Delta t\\) naar 0 beschouwt, convergeert de benadering naar de echte afgeleide \\(f'(t)\\):

\\[f'(t) = \lim\limits_{\Delta t \to 0} \frac{f(t + \Delta t) - f(t)}{\Delta t}\\]

In de notebook zullen we de impact van de parameter \\(\Delta t\\) onderzoeken.

## Interactieve notebook

In de notebook hieronder zal je Python gebruiken om de grafiek van de functie \\(f\\) te plotten, en om te onderzoeken of een kleinere waarde voor \\(\Delta t\\) tot betere schattingen van de afgeleide leidt.

[![Knop](embed/knop.png "https://colab.research.google.com/github/jvdrhoof/Insects/blob/main/hoofdstuk_5.ipynb")](https://colab.research.google.com/github/jvdrhoof/Insects/blob/main/hoofdstuk_5.ipynb)
