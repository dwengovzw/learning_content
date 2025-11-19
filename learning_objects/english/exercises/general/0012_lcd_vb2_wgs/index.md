---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Example LCD 2
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 5
hruid: g_lcd_vb2_wgs
keywords:
- oefeningen
- lcd
- lcd-scherm
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
- 10
- 11
- 12
teacher_exclusive: false
title: Example Lcd 2
version: 3
---
## LCD screen

EXERCISE 2

Make sure that 'Welcome' and 'robot' appear on separate lines.

Solution:

![blockly](@learning-object/lcd_m2/nl/3)

<div class="alert alert-box alert-success">
To split the text over two lines, you need a second <em>'LCD screen' block</em>.<br>
If you change 'on row:' from 0 to 1, the text will appear on the second line.
</div>

<div class="alert alert-box alert-warning">
<em>Test these examples yourself in the simulator as well! Once you get the hang of how it works, you can get started on your own.</em>
</div>