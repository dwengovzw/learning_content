---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Pythagoras - hypotenuse
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct03_36
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
title: Pythagoras - hypotenuse (2)
version: 3
---
# The Pythagorean theorem: calculating the hypotenuse

**Automating the calculation of the hypotenuse of a right triangle based on given legs.**

Do you want to program with your students in math class? This topic lends itself well to that.

Together with the students, you build an application step by step to automate the calculations for the Pythagorean theorem. You start from one type of exercise. You can have the students do a second type on their own; that immediately shows whether they have understood everything.

One strength of the Pythagorean theorem is that you can easily find real-world applications.

You can take the programming as far as you like. In this worked-out example, we cover variables, data types and operators, request input from the user, and use built-in and user-defined functions. We also use Python modules (libraries) and pay attention to writing comments. If desired, you can further improve the application and also work with selection and repetition structures.

This case is explained in this video.

![](@youtube/https://www.youtube.com/embed/ZUl27Ek9zHo "video case Pythagoras")

### Objective

**Automate calculating the hypotenuse when the legs are known.**

Once the students have the program, they can use it to solve complex problems that reduce to the solved problem above. The focus of the lesson can then be on mathematizing the problem, after which the solution can be determined using the computer.

**Target group:** second stage, double finality or transfer finality

**Subject**: Mathematics

### Step 1: automating the calculations.

**Prior knowledge:** The students know the Pythagorean theorem in formula form. Using the Pythagorean theorem, they can manually calculate the hypotenuse of a right triangle.

![ct-schema](@learning-object/m_ct03_36d/en/3)

In this video you see the programming part step by step.

![](@youtube/https://www.youtube.com/embed/oMFW-0mnAUU "demo case Pythagoras")

### Step 2: ask the user for input.

**Prior knowledge:** The students know how to ask the user for input, or they can learn it here.

![ct-schema](@learning-object/m_ct03_36a/en/3)

<div class="alert alert-box alert-success">
    <strong>Learning objective in function of MD 04.05:</strong><br>
    Students realize that it is important to make an application user-friendly if you want it to be used. More user-friendly digital applications will be able to achieve more impact.
</div>

### Step 3: applying pattern recognition and abstraction.

**Prior knowledge:** The students may already have learned how to define a function in Python, or that can be introduced here.

![ct-schema](@learning-object/m_ct03_36b/en/3)

### Application: distance as the crow flies

**Prior knowledge:** The students use the user-defined function in a context-based exercise.

**Challenge: "New York. What is the distance as the crow flies from Times Square to the Empire State Building, expressed in kilometers?"**

*The students themselves come up with the idea that they can use a route planner and the Pythagorean theorem.*

![ct-schema](@learning-object/m_ct03_36c/en/3)

<div class="alert alert-box alert-success">
<strong>Learning objective in function of MD 04.05:</strong><br> 
<ul>
    <li>One of the reasons that route planners are used so much and thus have so much impact is ease of use. That a route planner is so user-friendly is due to the high degree of abstraction in the route planner: the route is abstracted to number of kilometers and turning in time; if desired, you can simply follow the instructions of the road you must take (the step-by-step plan or algorithm). You don't have to bother looking up the way on a map, where you would have to take into account e.g. one-way traffic, the orientation of the map, etc.</li>
    <li>In addition, you get additional information such as traffic jams, road works, where you can refuel, etc.</li>  
    <li>Because so much is abstracted in route planners, you no longer have a complete view of the environment. That can also be a disadvantage compared to a paper map that gives many more details of the surroundings, and situates a certain place in a larger area. Route planners, as it were, hollow out the spatial awareness around a place. Being too dependent on digital route planners can therefore also be dangerous; people, for example, drive onto a railway track or onto a staircase.</li>
    <li>When using a route planner you must keep in mind that you can end up in an area without mobile coverage, or that your smartphone's battery can run out.</li>
    <li>You must also keep in mind that some areas may be insufficiently detailed or inaccurate. And that digital route planners may contain errors, such as an incorrect maximum speed allowed on a road or a one-way street indicated as two-way traffic.</li>
    <li>Route planners have an impact on society: The use of a route planner by so many people can have undesirable effects, such as extra traffic in residential areas when a route planner diverts car traffic through residential neighborhoods to avoid traffic jams. The question is how many aspects of the environment the algorithm in the route planner takes into account. In the input it may have been abstracted away that a certain area is a residential neighborhood, or in the program that variable is not taken into account. Route planners can contain advertising: How is it determined which shops, gas stations ... are shown in the route planner? Route planners have led to new applications in society, such as robots that deliver groceries to homes and medical drones; using route-planner techniques designed specifically for drones, they find their way. Using a route planner can also involve privacy aspects: If the user's locations are stored, the question arises what the provider of the route planner does with that data.</li>
</ul>
</div>

### Next step: applying pattern recognition and abstraction

Students in the second stage are introduced to the Pythagorean theorem in math class. Two types of exercises stand out:<br> 
- either the legs of a right triangle are given and the hypotenuse must be calculated;
- or the hypotenuse and one leg are given and the other leg must be calculated.

The students built an application to do the calculations for an exercise of the first type. The application uses a user-defined function `pythagoras1()`.<br>  
An extension of this case would be for the students to add a second function `pythagoras2()`, so that the application can do the calculations for both types.
From then on, a series of problems can be offered to the students, where they mainly have to do pattern recognition and use the application each time for the calculations.

<div class="alert alert-box alert-info">
<strong>Note on naming the user-defined functions:</strong><br>
It is better to adjust the names of the functions so that they immediately also tell what the functions do. Instead of <code>pythagoras1()</code> it is better to use <code>bereken_schuine_zijde_uit_rechthoekszijden()</code> as the function name. Analogously, change the name <code>pythagoras2()</code> to <code>bereken_rechthoekszijde_uit_schuine_zijde_en_rechthoekszijde()</code>.<br>
If you want the function to be usable also for those not familiar with the standard notations <em>a, b</em> and <em>c</em> from math class, then it is best to also adjust the parameters in the functions. So even better names for the functions are <code>bereken_schuine_zijde(rechthoekszijde_1, rechthoekszijde_2)</code> and <code>bereken_rechthoekszijde(schuine_zijde, rechthoekszijde)</code>.
</div>