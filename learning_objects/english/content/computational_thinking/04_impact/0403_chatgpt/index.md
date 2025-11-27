---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: ChatGPT
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct04_03
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
- 15
- 16
- 17
- 18
teacher_exclusive: true
title: ChatGPT
version: 3
---
# ChatGPT 3.5

In November 2022, OpenAI launched ChatGPT. And although GPT has existed since 2018 and applications based on large language models have been present on the World Wide Web for some time, many realized that artificial intelligence is not science fiction after all. <br>
Since then, the newspapers have been full of it, and one (commercial) application after another is being developed. ChatGPT already has applications in various domains, such as recruiting new staff and automatically generating news websites. At the same time, ChatGPT also brings concerns, such as the spread of disinformation.<br>
The arrival of ChatGPT has a major impact, for example on education. For instance, teachers are on their guard for the possible cheating of students. They are, for example, more suspicious when students submit a fluent text; many teachers are therefore rethinking the assignments for their students. On the other hand, they themselves use ChatGPT to create exercises. 

In this learning path you will delve deeper into one of the aspects of ChatGPT: an aspect that fundamentally contributes to the impact of the AI system. 

**Impact: Because ChatGPT's answers sound fluent and confident, these answers are often wrongly assumed to be correct.**<br>

<div class="alert alert-box alert-info">
    Murray Shanahan says that we must clearly understand what a large language model does. "Suppose we give the following prompt to an LLM: “The first person to walk on the Moon was”, and suppose it answers with “Neil Armstrong”. What are we actually asking here? It is important to realize that we are not really asking who the first person to walk on the Moon was. The question we are really asking the model is the following: Given the statistical distribution of the words in the extensive public corpus of (English) text, which words are most likely to follow the sequence “The first person to walk on the Moon was ”? A good answer to this question is “Neil Armstrong” (Source: Talking About Large Language Models, Murray Shanahan, 2022).
</div>

## Principles of computational thinking

![ct-schema](@learning-object/m_ct04_03/en/3)

## Discussion of the impact

- ChatGPT 3.5 involves several aspects: the language model it is based on, the training data, and the interface people use to communicate with the model.
- Training a language model requires a lot of energy; that too is an aspect to consider. Using ChatGPT also consumes energy.
- Because ChatGPT 3.5 operates in a dialogue format, the system is very accessible. Due to the similarities with an app such as WhatsApp, ChatGPT feels very familiar. That accessibility is one of the reasons ChatGPT is used so much.
- ChatGPT 3.5 is essentially intended to generate text. Because it is based on a large language model, ChatGPT is also suitable for, for example, summarizing texts, converting text into a different style, rewriting for a different audience, and translating.
- However, people also use ChatGPT 3.5 for things the system was not designed for:
    - using ChatGPT as a search engine;
    - solving math problems;
    - to unburden themselves emotionally (research showed that students who did not have a tendency to cheat before ChatGPT existed generally still do not, but that young people do turn to ChatGPT for emotional problems).
- ChatGPT is very fast, allowing someone with bad intentions to generate a lot of fake news in a short time and then spread it.
- So ChatGPT does not understand text in the way a human understands text. ChatGPT uses pattern recognition to understand and generate natural language. The model learns patterns in text data and uses these to form sentences that are coherent and relevant. To do that, the system performs computations. ChatGPT 3.5 does not (as yet) have access to the World Wide Web and therefore does not have the latest information. ChatGPT 3.5 will therefore also be unable to substantiate its claims with sources. It thus happens that ChatGPT 'hallucinates', in other words, produces nonsense. (*If you ask ChatGPT for sources, it will make them up.*)
- ChatGPT answers in a 'human' manner and comes across as friendly and courteous. The step toward 'humanization', i.e., treating the system as a person, is therefore not large.  - A 2020 study by Følstad & Brandtzaeg shows that a chatbot conversation can also be about small talk, or about someone's feelings and life. Some users take up the challenge of testing the chatbot: to what extent is the chatbot able to respond like a human. But for others, the chatbot is a way to get through the day; although
they are aware that they are conversing with a machine, the chat is regarded as a valuable social interaction.
- Although the system answers confidently, you can often easily convince it - due to its courteous and *pleasing* nature - that it is wrong (even when it is not).
  
> Most customer service chatbots that already existed were rule-based systems. In such chatbots, various scenarios are explicitly
programmed. This automatically leads to limitations that force users to adapt to the limits of the system. For example, if one formulates a question to the chatbot differently than programmed, the chatbot will not recognize the question. Such chatbots are often unpopular.
> The same question can, for example, be asked in different ways. For instance: “Will it rain all day today?” or “Will today be a drizzly day?”.
> To understand a question, world knowledge, knowledge of the physical world, may be required. For example: “Will it be bikini weather tomorrow?”.
> A message may contain humor, irony, or sarcasm. For example: “Hooray, my train is right on time again”.  
- Satisfaction with a chatbot conversation can contribute to customer satisfaction or partially nullify it. People expect a chatbot to be efficient, to have a friendly, polite personality, and to provide quick and solid answers. Because ChatGPT meets these criteria, some companies are considering deploying ChatGPT as a customer service chatbot. When the chatbot then hallucinates, the customer does not benefit. Moreover, users want it to be clearly stated that they are chatting with a bot and not a human; they expect that to be indicated. Companies that deploy ChatGPT as a chatbot could easily conceal that, especially if the systems become even better in the future.

  
**Consideration:** texts generated by generative AI also end up online; it is realistic that these texts will serve as training data for new systems. Will misinformation and disinformation not be amplified as a result?