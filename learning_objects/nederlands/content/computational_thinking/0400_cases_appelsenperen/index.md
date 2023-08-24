---
hruid: ct_cases0
version: 3
language: nl
title: "Appels en peren"
description: "Appels en peren"
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
teacher_exclusive: true
---
# Appels onderscheiden van peren
Objectherkenning is een toepassing van artificiële intelligentie die de dag van vandaag veelvuldig voorkomt. Met technieken van machinaal leren kan een computer bv. dier- en plantsoorten of gezichten van mensen herkennen. 

In de klas kan je samen met de leerlingen bespreken hoe een computer naar foto's kijkt en hoe men een computer zou kunnen programmeren om a.d.h.v. regels appels en peren van elkaar te onderscheiden.

**Doelgroep:** alle graden - alle finaliteiten

**Vak:** Wiskunde -  STEM - Computerwetenschappen - Mediawijsheid

**Voorkennis:** De leerlingen weten dat getallen kunnen geordend worden.

<div class="alert alert-box alert-warning">
    <strong>Appels en peren onderscheiden - klasgesprek</strong><br>
<ul><li>Hoe onderscheiden wij appels en een peren? Welke kenmerken nemen wij daarin mee?</li></ul>
<ul><li>Zou een computer dat op dezelfde manier doen?</li></ul>
<ul><li>Een computer kan doorgaans niet voelen of kijken. Hoe zou een computer wel kunnen kijken? (Als hij over een camera beschikt, kan hij wel kijken.) <em>Computer vision</em> zal een rol spelen.</em></li></ul>
<ul><li>Hoe kunnen we die appels en peren aan de computer geven?</li></ul>
<ul><li>Hoe kijkt een computer naar een afbeelding?</li></ul>
<ul><li>Welke kenmerken van appels en peren zijn voor een computer wel zinvol?</li></ul>
</div>

De bedenkingen en conclusies uit het klasgesprek kunnen worden samengevat in een schema.

![ct-schema](@learning-object/m_ct_cases0/nl/3)

Het spreekt voor zich dat de oplossing van het probleem in realiteit veel complexer is. De vorm van sommige peren gelijkt bv. sterk op die van een appel; andere kenmerken zoals de textuur van de schil kunnen dan uitsluitsel geven. Het gebruik van een diep neuraal netwerk kan betere resultaten geven, dan progammeren aan de hand van regels. 

![CNN zoekt naar kenmerken van objecten om ze te kunnen herkennen.](embed/kenmerkenappelpeer.png)

---------------------------
Het leerpad 'Digitale beelden' legt uit hoe een computer naar afbeeldingen kijkt. In de notebooks kan je er ook actief mee aan de slag gaan.<br> Het leerpad 'Artificiele intelligentie' gaat o.a. in op AI voor beeldherkenning. <br>
In de projecten 'KIKS' en 'AI in de Landbouw' wordt hier dieper op ingegaan. 
