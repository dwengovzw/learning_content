---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: To describe an algorithm without coding, we can use pseudocode.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 5
hruid: org-dwengo-elevator-riddle-brute-force-3
keywords:
- grafen
- algoritme
- computationeel denken
- clustering
- datastructuur
- brute force
- pseudocode
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
- 16
- 17
- 18
teacher_exclusive: false
title: 'Step 1: Pseudocode'
version: 1
---
# Brute Force

## Pseudocode

In plain human language, it's often difficult to describe formal reasoning unambiguously. That's why computer scientists often use pseudocode to describe the logic of an algorithm. Below is the pseudocode for generating choices. The code uses two variables: k = the number of choices you are allowed to make, n = the number of items you can choose from.

```pseudocode
generate all possible choices of k items from a list of n items:
	if k = 0 then you may no longer choose from the rest of the n items:
		Return a list with n times the value 2
	if k = n then you must choose all remaining items:
		Return a list with n times the value 1
	if k > n then something is wrong, this case cannot occur:
		Return an empty list
	if k < n then we have to make a choice:
		choices = an empty list
		for all subchoices sa in (generate all possible choices of k - 1 items from a list of n items):
			make a list [1, sa] and add it to the choices list
		for all subchoices sb in (generate all possible choices of k - 1 items from a list of n-1 items):
			make a list [0, sb] and add it to the choices list
		return the choices list
```