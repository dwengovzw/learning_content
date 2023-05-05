---
hruid: g_sound2
version: 3
language: en
title: "Afstellen Geluidssensor"
description: "Uitleg Geluidssensor"
keywords: ["oefeningen", "geluidssensor"]
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
# dwenguinoBlockly
## Sound Sensor

When you connect the sound sensor (and provide it with power), you can distinguish 2 LEDs. One LED lets you know that the sound sensor is on, the other LED that your sound sensor is detecting sound. When the sound sensor detects sound, the LED is on, otherwise it is off.

The sound sensor can be adjusted (made more or less sensitive) with the small screw on top of the sensor.

- Clockwise: The sound sensor becomes more sensitive to sound.
- Counterclockwise: The sound sensor becomes less sensitive to sound.

When using a sound sensor for the first time, it is very sensitive to sound. To adjust the sensor, proceed as follows:
*Make sure that the current sound level is the level at which the sensor will operate. If it is now completely silent, but this will not be the case when the sensor is in use, you will have to readjust it.*

1. Turn the screw **counterclockwise** until one LED goes out.
2. Now *carefully* turn the screw *clockwise* until the LED comes back on.
3. *Carefully* turn the screw back *counterclockwise* and stop when the LED goes out again.
4. Now tap the sensor with your finger. If the LED lights up during the tap, your sensor is properly adjusted. Otherwise, go back to step 2.