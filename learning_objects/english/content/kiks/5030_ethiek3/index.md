---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Energy
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: kiks_ethiek3
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
- 16
- 17
- 18
teacher_exclusive: true
title: Energy
version: 3
---
# Energy

In these times of energy scarcity and climate change, we should consider the fact that AI systems **consume energy**. Such systems perform billions of calculations per second. Turning off the light through a command to Siri consumes more energy than leaving the light on for an hour.

<div class="alert alert-box alert-success">
    When you instruct <b>Siri</b> to turn off the light, more than one AI system is activated. The moment you say 'Hey Siri', Siri's behind-the-scenes system is powered up, and your spoken command is recorded. This recording is sent to a data center. Successively, your voice command is converted into typed text, the required action is determined, and the instruction needed is sent back to your smartphone. Your smartphone then issues an appropriate command to your lighting system, whereupon the light in your room turns off.
</div> 

Other examples of hidden (AI-based) energy consumers include:
- a smart thermostat;
- the driving assistance in your car that alerts you if you deviate from the lane;
- a GPS;
- word suggestion on your smartphone.

Is the use of a system necessary or even desirable? Do the benefits outweigh the drawbacks, particularly the energy costs and negative impact on the environment?

Every time you search the internet, have a text automatically translated, or get suggestions on a webshop, an AI system is at work consuming energy. A constant in the most energy-hungry applications is that they are **cloud-based**. To **execute** the AI application, data is sent to a data center consisting of many computers. There, the data is processed and returned.<br>
Such a data center, of course, consumes a lot of energy: electricity to power the servers, with the side effect of generating heat, and a system to cool the space.<br>
It is estimated that data centers worldwide are responsible for 0.3% to 2% of total greenhouse gas emissions. It was estimated that in 2018 they consumed 205 TWh of electricity, that is, 1% of global consumption.

![Data center](embed/datacenter.jpg "Data center")
<center>A picture of a 123Net Datacenter walkway in Southfield, MI (2011). 123net, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons. https://en.m.wikipedia.org/wiki/File:123Net_Data_Center_(DC2).jpg </center>
    
![Google data center Iowa](embed/googledatacenteriowa.jpg "Google data center Iowa")   
<center>Google Data Center, Council Bluffs Iowa. chaddavis.photography from United States, CC BY 2.0 <https://creativecommons.org/licenses/by/2.0>, via Wikimedia Commons https://commons.wikimedia.org/wiki/File:Google_Data_Center,_Council_Bluffs_Iowa_(49062863796).jpg </center>

<div class="alert alert-box alert-success">
    Every Google <b>search query</b> consumes a small amount of energy. But many small amounts add up to a large quantity and it goes without saying that an enormous number of queries occur, millions per minute and trillions per year. According to Google, each query results in CO<sub>2</sub> emissions of 0.2 g, which would correspond to the annual emissions of driving a car for a year.
</div> 

<div class="alert alert-box alert-success">
    When you ask a question to <b>ChatGPT</b>, your computer sends that question via the internet to ChatGPT's servers. Then, the AI system searches for the answer to your question. That answer is then sent back to your computer and appears on your screen.
</div>

**An even greater energy cost, however, goes into training these AI systems.** To develop these systems, that is before they can be used, they are trained on considerable amounts of data. Since the rise of deep learning, the amount of data used for training has grown year by year, and thus the amount of energy required has increased.

<div class="alert alert-box alert-success">
    The <b>training of GPT-3</b> was estimated to have consumed as much energy as needed to provide electricity to 367.5 Belgian families for a year (it is estimated that the training of GPT-3 consumed 936 MWh) and emitted as much CO<sub>2</sub> as 120 cars in a year. With its successor, GPT-4, which is coming soon, it will be much more.
</div>

But it's not all bad news.<br>
AI systems have already proven their **value**, for example in healthcare, with applications in medical imaging and the development of surgical robots.
Moreover, they can also help address the climate problem. Scientists are actively searching for new technological applications to reduce the amount of CO<sub>2</sub> in the atmosphere. They are also looking for ways to cope with the effects of climate change. For this, they gratefully use the power of AI systems, which can draw conclusions based on the values of a large number of parameters much faster than a human can handle.

Fortunately, there is significant investment in making data centers as energy-efficient as possible. And fortunately, the energy consumption of data centers does not increase to the same extent as the demand for data center services. For instance, there is the evolution from smaller, traditional data centers to larger, energy-efficient cloud data centers.<br>
In addition, there is an entire research domain focused on the development of **energy-saving computer chips**.

**In summary, energy consumption is an important societal factor that we should take into account when creating and using AI applications. This should give us pause the next time we ask a new question to ChatGPT or have an image generated by DALL·E 2.**

**Sources:**<br>
[https://www.nrdc.org/sites/default/files/gadget_report_r_19-07-b_13_locked.pdf](https://www.nrdc.org/sites/default/files/gadget_report_r_19-07-b_13_locked.pdf) <br>
[Data Centers on Wheels: Emissions From Computing Onboard Autonomous Vehicles](https://ieeexplore.ieee.org/document/9942310)<br>
Knack, Elisa Hulstaert 15/1/2023, Steven Latré (Imec): 'If AI does not become more sustainable, it is doomed to fail'<br>
Knack, The dangers of ChatGPT 'We risk becoming collectively dumber'<br>
[How Much Energy Do Data Centers Really Use?](https://energyinnovation.org/2020/03/17/how-much-energy-do-data-centers-really-use/)<br>
[Operating on 24/7 Carbon-Free Energy by 2030.](https://sustainability.google/progress/energy/)