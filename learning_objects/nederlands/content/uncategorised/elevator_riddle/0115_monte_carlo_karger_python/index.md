---
hruid: org-dwengo-elevator-riddle-monte-carlo-karger-python-2
version: 1
language: nl
title: "Karger in Python (de bogenmatrix)"
description: "Het algoritme van Karger gebruikt de Monte Carlo methode om tot een oplosing te komen."
keywords: ["grafen", "algoritme", "computationeel denken", "clustering", "datastructuur", "monte carlo", "python", "karger"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
]
teacher_exclusive: false
---

# Algoritme van Karger: de bogenmatrix

Een belangrijke observatie bij dit algoritme is dat we om de bogen van de samen te voegen knopen aan te passen we gebruik kunnen maken van de bogen matrix. Om dit te doen, nemen we eerst de kolommen voor de twee knopen en tellen die op. Daarna doen we hetzelfde voor de rijen. 


|  | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** |
| - | - | - | - | - | - |- | - |- |
| **4** | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| **5** | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 3 | 
| **6** | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 
| **7** | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 4 | 
| **8** | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 
| **9** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 
| **10** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **11** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |


<table>
  <tr>
    <th></th>
    <th>4</th>
    <th>5</th>
    <th>6</th>
    <th>7</th>
    <th style="background-color: orange;">8</th>
    <th>9</th>
    <th style="background-color: orange;">10</th>
    <th>11</th>
  </tr>
  <tr>
    <th>4</th>
    <td>0</td>
    <td>0</td>
    <td>2</td>
    <td>0</td>
    <td style="background-color: orange;">2</td>
    <td>0</td>
    <td style="background-color: orange;">2</td>
    <td>0</td>
  </tr>
  <tr>
    <th>5</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: orange;">3</td>
    <td>3</td>
    <td style="background-color: orange;">0</td>
    <td>3</td>
  </tr>
  <tr>
    <th>6</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: orange;">1</td>
    <td>0</td>
    <td style="background-color: orange;">2</td>
    <td>0</td>
  </tr>
  <tr>
    <th>7</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: orange;">0</td>
    <td>2</td>
    <td style="background-color: orange;">4</td>
    <td>4</td>
  </tr>
  <tr>
    <th>8</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: orange;">0</td>
    <td>0</td>
    <td style="background-color: orange;">2</td>
    <td>0</td>
  </tr>
  <tr>
    <th>9</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: orange;">0</td>
    <td>0</td>
    <td style="background-color: orange;">0</td>
    <td>3</td>
  </tr>
  <tr>
    <th>10</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: orange;">0</td>
    <td>0</td>
    <td style="background-color: orange;">0</td>
    <td>0</td>
  </tr>
  <tr>
    <th>11</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: orange;">0</td>
    <td>0</td>
    <td style="background-color: orange;">0</td>
    <td>0</td>
  </tr>
</table>