---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: 'Flipping cards: Apply an algorithm and recognize a pattern'
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct05_04
keywords:
- ''
language: en
licence: dwengo
return_value:
  callback_schema:
    att: test
    att2: test2
  callback_url: callback-url-example
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
target_ages:
- 12
- 13
- 14
teacher_exclusive: true
title: 'Flipping cards: Applying an algorithm and recognizing a pattern'
version: 3
---
# Example 4: Applying an algorithm and recognizing patterns
Source: [the online platform of the Belgian Bebras competition](https://bebras.ugent.be/)<br>
Text: Kris Coolsaet, BE<br>
Images: Kris Coolsaet, BE
 
## Flipping cards (Bebras 2018-BE-01a)
We play the following 'little game.' In front of you lies a row of cards. A card is either face up or face down.

One step in the 'game' happens as follows:<br>
You look at the cards from right to left.<br>
If the current card is face down, you flip the card face up and stop.<br>
If the current card is face up, you flip it face down and continue with the card to its left.<br>
If you have passed all the cards, you stop.

The image below shows the effect of successive steps: you first flip the rightmost card, then the one to its left, and then the one to the left of that. And then you must stop, because the third card is now face up.

![Flipping cards](embed/bebrasalgoritmepatroon.png "Bebras algorithm and pattern recognition")

The game starts with 32 cards, all face down:

![Flipping cards](embed/bebrasalgoritmepatroonopgave.png "Bebras algorithm and pattern recognition")

*How many cards are **face up** after you have taken exactly 32 steps in the game? (Answer with a number.)*