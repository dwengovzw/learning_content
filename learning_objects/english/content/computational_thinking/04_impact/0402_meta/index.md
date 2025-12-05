---

hruid: m_ct04_02
version: 3
language: en
title: "Impact route planner"
description: "Impact route planner"
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
    '[http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen](http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen)'
]
teacher_exclusive: true
-----------------------

<context>
**Problem statement**<br>
Developing a route planner.
</div>
</context>
<decomposition>
**Decomposition**<br>
1. The position of the user
2. A representation of the road network, which includes:
    - which roads are connected to each other;
    - the value of the parameters of the roads.
3. It must be decided which parameters the route planner will take into account and which it will ignore, such as:
    - allowed speed;
    - traffic density;
    - distance;
    - weather;
    - character.
      - Suitability of roads for trucks.
      - Local character, such as residential area or industrial park. 
    - Which databases the route planner has access to? 
       - A database from commercial partners, such as certain stores, gas stations, ...
       - Road works
    ...
3. An algorithm to determine the shortest, fastest, or most optimal route    
4. Determine whether and how the route planner can make real-time adjustments to the route.
    - A mobile internet connection
    - Real-time position of the user 
      - Global positioning system (GPS)
    - Real-time traffic information
      - Is it chosen to communicate real-time information about users’ routes?
</decomposition>
<patternRecognition>
**Pattern recognition**<br>
1. Users driving slower on a certain section of road can be recognized by the system as traffic jams or delayed traffic.
2. The system could detect a pattern of recurring traffic jams at a certain location and mark it as a place to avoid.
3. A route typically known only by local residents could be stored in the system as a possible trajectory after being driven.
</patternRecognition>
<abstraction>
**Abstraction**<br>
Abstraction plays a prominent role both in the design and operation of a route planner. 
1. Superfluous information about the surroundings is removed in the design. You only see the road, without much information about the surrounding environment.
    - Nevertheless, certain stores, gas stations, etc., are still displayed.  
2. The route planner only considers certain parameters, such as distance, when determining the route. Other parameters, such as the fact that a street is in a residential area, are ignored.       
</abstraction>
<algorithms>
**Algorithmic thinking**<br>
Route planners use algorithms to calculate the route. 
1. Depending on the user’s preference, they search for the shortest, fastest, or most optimal route.
2. There may be an algorithm that processes real-time information.
3. There may also be an algorithm that links the route to the presence of commercial partners. 
</algorithms>
