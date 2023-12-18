---
hruid: org-dwengo-jommeke-definitie-ai-systeem-regels
version: 1
language: nl
title: "Definitie regelgebaseerd AI-systeem"
description: "Uitleg regelgebaseerd AI-systeem en definitie volgens de EU"
keywords: ["AI", "Regelgebaseerd", "AI-systeem", "artificiële intelligentie"]
content_type: "text/markdown"
estimated_time: 2
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-mediawijsheid',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-digitale-competenties-en-mediawijsheid',
    'http://ilearn.ilabt.imec.be/vocab/onddoel/sec-gr1-astroom-digitale-competenties-en-mediawijsheid-4.5',

]
copyright: "CC BY dwengo"
target_ages: [10, 11, 12, 13]
---


Een regelgebaseerd AI-systeem?
===============

Regelgebaseerde AI-systemen werken, zoals de naam al doet vermoeten, op basis van regels. Deze regels worden **verzonnen door experten** in een vakgebied en door een programmeur op de computer geprogrammeerd. Een voorbeeld van zo'n regelgebaseerd systeem is de toepassing ["Moet ik naar de dokter"](https://www.moetiknaardedokter.be/).

![Moet ik naar de dokter?](img/moet_ik_naar_dokter.png "Moet ik naar de dokter?")

Deze toepassing stelt een reeks vragen aan de gebruiker en beslist op basis van de antwoorden welke actie ondernomen moet worden. Moet de persoon niet naar de dokter, moet die onmiddellijk naar de dokter, kan die morgen naar de dokter gaan of moet die nu naar de spoeddienst.

Zo'n systeem werkt aan de hand van een beslissingsboom. Hieronder zie je een voorbeeld van zo'n boom. 

![Voorbeeld beslissingsboom](img/beslissingsboom.png "Voorbeeld beslissingsboom")

Om een beslissing te nemen doorlopen we de boom van boven naar beneden. In elk vakje staat een vraag. Als het antwoord op die vraag **ja** is, dan volg je de **linkse lijn** naar beneden. Als het antwoord op de vraag **nee** is dan volg je de **rechtse lijn** naar beneden. Wanneer je helemaal onderaan de boom komt, dan zie je daar staan welke actie de peroon moet ondernemen.