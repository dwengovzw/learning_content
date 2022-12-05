---
hruid: m_cd_cases3
version: 3
language: nl
title: "Pythagoras - schuine zijde"
description: "Pythagoras - schuine zijde"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/ct-schema
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

<context>
![Face](ct_face.png)
<div style="position:absolute;right:0px;width:40%;height:100px;margin-top:-100px;margin-right:20px">
Tekst
</div>
</context>
<decomposition>
Subtaken (**decompositie**):<br>
1. Inzetten van de computer om de schuine zijde te berekenen. 
2. Formule? Gekend uit de stelling van Pythagoras.
3. Gebruiker moet in staat zijn om de lengte van de  gegeven rechthoekszijden in te geven.
4. Welk datatype is het meest geschikt voor die zijden? Int of float?
5. Na de verwerking van de gegevens via de formule, is er een output. Hoe laat je de output proper verschijnen?
![image](https://user-images.githubusercontent.com/48352335/205660318-60481c86-7bd1-4091-9d11-1a60ef64412c.png)

</decomposition>
<patternRecognition>
Als eenzelfde berekening vaak moet herhaald worden, dan is het handig deze te vatten in een functie. (**patroonherkenning**)
    
De formule zal daarom opgenomen worden in een zelfgedefinieerde functie. 
![image](https://user-images.githubusercontent.com/48352335/205660596-8b542e87-84e0-42b3-89ca-9e16c70bba8f.png)

</patternRecognition>
<abstraction>
Een functie is een abstractie van een subalgoritme.
![image](https://user-images.githubusercontent.com/48352335/205660711-935976bd-feeb-4362-aba6-1c4a30385d41.png)

</abstraction>
<algorithms>
Het algoritme bevat (in deze volgorde) instructies om:
1. de gegevens op te vragen aan de gebruiker;
2. die gegevens te verwerken met als doel het bekomen van de lengte van de schuine zijde;
3. de lengte van de schuine zijde te laten zien op het scherm. 
![image](https://user-images.githubusercontent.com/48352335/205660774-ca1876c9-1d01-42a8-b153-d636d893ae68.png)

</algorithms>
<implementation>
** Programma in Python**
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
def pythagoras(a, b):<br>
    c = math.sqrt(a**2 + b**2)<br>
    return c<br>
    
# invoer<br>
rhz1 = float(input("Lengte van de eerste rechthoekszijde: "))<br>
rhz2 = float(input(“Geef de lengte van de tweede rechthoekszijde: "))<br>

# verwerking<br>
schz = pythagoras(rhz1, rhz2)<br>

# uitvoer<br>
print("De lengte van de schuine zijde is: ", schz)

    </p></div>
![image](https://user-images.githubusercontent.com/48352335/205660996-b001e1c6-d6bf-4b0f-848c-276739eb12fe.png)

![image](https://user-images.githubusercontent.com/48352335/205660946-77e477fc-9aa0-49bf-94d5-9f4fd9950279.png)


</implementation>

