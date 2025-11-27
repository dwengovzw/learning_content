---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Home assistant
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct04_04
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
title: Home assistant
version: 3
---
# Voice assistant and advertising

Will we all be using a voice assistant in the foreseeable future? Since the arrival of ChatGPT, more and more people are convinced of that. <br>
For several years now we have been able to rely on voice assistants, such as Siri, Alexa, or Google Assistant. Some make grateful use of them to call someone while driving, to turn on the heating at home, or to ask for the weather report. People who feel lonely find a conversation partner in a voice assistant. Such a *voice assistant* can therefore have an impact in multiple ways. <br>
Below is an example of that.

**What is the impact of using a voice assistant on the ads we see? Are we collectively being eavesdropped on?**

You often hear the following questions: Do voice assistants listen to everything we say all the time? And do they do anything with that? Is it a coincidence that I get ads about a particular product now that I talked about it with a friend?<br>
To give a clear answer to this, first look at some aspects of how such a *voice assistant* works, such as Siri, Alexa, or Google Assistant.   

## Principles of computational thinking

![ct-schema](@learning-object/m_ct04_04/en/3)


## Discussion of the impact

-  If a voice assistant were continuously listening actively, the **battery** of your smartphone or other device would always drain quickly.
-  If a voice assistant were continuously listening actively - **active listening means that everything the assistant hears is also stored** - to do something with it - which means that each audio fragment is converted to typed text - then that would amount to a **huge amount of data** in the cloud. It is impossible for the providers of such systems to keep everything from all users.
-  So you need to distinguish between **active and passive listening**. The voice assistant always listens passively, and upon 'hearing' a trigger word it switches to active listening. At that moment, what the assistant hears is also stored, and each audio fragment is converted to typed text. This text is then fed to an AI system that does something with it. All of that happens in an instant.
-  So if you get ads for a product you previously discussed with a friend, that is a coincidence.
-  However, if you have **asked something of the voice assistant**, and you later receive ads in that context, that is a different story.
-  You may get the impression you are being eavesdropped on if you suddenly receive ads for a product you discussed with a friend the day before. However, this can be explained
    -  by the *Baader-Meinhof phenomenon* or *frequency illusion* (because you talked about it the day before, the ad stands out more) (source: fact check);
    -  by *confirmation bias* (your suspicion that you're being eavesdropped on is confirmed by the ad);
    -  or you can attribute it to *lookalike audiences* (through **pattern recognition**, you are assigned the same interests as someone with a similar profile). 
-  This also deserves sufficient attention: How are the data that the systems collect stored, used, shared, and deleted?
    - A 2019 report from the Capgemini Research Institute indicates that good cooperation between the *in-car voice assistant*, the *home assistant*, and the digital assistant on users' smartphones is desirable. Then they could, for example, use the *in-car voice assistant* to open the garage door and turn on the heating at home. But such integration also brings privacy aspects:
after all, data are then shared between multiple applications (Walch, 2020). In theory, the digital assistant on the smartphone could thus find out where the user has been with the car.
    - Where will the data end up? Could that have consequences later when applying for a loan, for example?