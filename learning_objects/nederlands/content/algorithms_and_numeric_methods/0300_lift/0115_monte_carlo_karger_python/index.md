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
difficulty: 5
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
]
teacher_exclusive: false
---
# Monte Carlo

## Algoritme van Karger: de bogenmatrix

Een belangrijke observatie bij dit algoritme is dat we om de bogen van de samen te voegen knopen aan te passen, gebruik kunnen maken van de bogenmatrix. Om dit te doen, nemen we eerst de kolommen voor de twee knopen en tellen die op. Daarna doen we hetzelfde voor de rijen. 

<table>
  <tr>
    <th></th>
    <th>4</th>
    <th>5</th>
    <th>6</th>
    <th>7</th>
    <th style="background-color: #f9cb9c;">8</th>
    <th>9</th>
    <th style="background-color: #f9cb9c;">10</th>
    <th>11</th>
  </tr>
  <tr>
    <th>4</th>
    <td>0</td>
    <td>0</td>
    <td>2</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">2</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">2</td>
    <td>0</td>
  </tr>
  <tr>
    <th>5</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">3</td>
    <td>3</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td>3</td>
  </tr>
  <tr>
    <th>6</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">1</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">2</td>
    <td>0</td>
  </tr>
  <tr>
    <th>7</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td>2</td>
    <td style="background-color: #f9cb9c;">4</td>
    <td>4</td>
  </tr>
  <tr>
    <th>8</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">2</td>
    <td>0</td>
  </tr>
  <tr>
    <th>9</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td>3</td>
  </tr>
  <tr>
    <th>10</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td>0</td>
  </tr>
  <tr>
    <th>11</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td>0</td>
  </tr>
</table>

Zo bekomen we een matrix met 1 kolom minder:

<table>
  <tr>
    <th></th>
    <th>4</th>
    <th>5</th>
    <th>6</th>
    <th>7</th>
    <th style="background-color: #f9cb9c;">8, 10</th>
    <th>9</th>
    <th>11</th>
  </tr>
  <tr>
    <th>4</th>
    <td>0</td>
    <td>0</td>
    <td>2</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">4</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <th>5</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">3</td>
    <td>3</td>
    <td>3</td>
  </tr>
  <tr>
    <th>6</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">3</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <th>7</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">4</td>
    <td>2</td>
    <td>4</td>
  </tr>
  <tr>
    <th>8</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">2</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <th>9</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td>0</td>
    <td>3</td>
  </tr>
  <tr>
    <th>10</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <th>11</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td>0</td>
    <td>0</td>
  </tr>
</table>

Daarna doen we hetzelfde voor de rijen.

<table>
  <tr>
    <th></th>
    <th>4</th>
    <th>5</th>
    <th>6</th>
    <th>7</th>
    <th>8, 10</th>
    <th>9</th>
    <th>11</th>
  </tr>
  <tr>
    <th>4</th>
    <td>0</td>
    <td>0</td>
    <td>2</td>
    <td>0</td>
    <td>4</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <th>5</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>3</td>
    <td>3</td>
    <td>3</td>
  </tr>
  <tr>
    <th>6</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>3</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <th>7</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>4</td>
    <td>2</td>
    <td>4</td>
  </tr>
  <tr>
    <th style="background-color: #f9cb9c;">8</th>
    <td style="background-color: #f9cb9c;">0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td style="background-color: #f9cb9c;">2</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td style="background-color: #f9cb9c;">0</td>
  </tr>
  <tr>
    <th>9</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>3</td>
  </tr>
  <tr>
    <th style="background-color: #f9cb9c;">10</th>
    <td style="background-color: #f9cb9c;">0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td style="background-color: #f9cb9c;">0</td>
  </tr>
  <tr>
    <th>11</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
</table>

Dan krijgen we de volgende matrix.

<table>
  <tr>
    <th></th>
    <th>4</th>
    <th>5</th>
    <th>6</th>
    <th>7</th>
    <th>8, 10</th>
    <th>9</th>
    <th>11</th>
  </tr>
  <tr>
    <th>4</th>
    <td>0</td>
    <td>0</td>
    <td>2</td>
    <td>0</td>
    <td>4</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <th>5</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>3</td>
    <td>3</td>
    <td>3</td>
  </tr>
  <tr>
    <th>6</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>3</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <th>7</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>4</td>
    <td>2</td>
    <td>4</td>
  </tr>
  <tr>
    <th style="background-color: #f9cb9c;">8, 10</th>
    <td style="background-color: #f9cb9c;">2</td>
    <td style="background-color: #f9cb9c;">3</td>
    <td style="background-color: #f9cb9c;">5</td>
    <td style="background-color: #f9cb9c;">2</td>
    <td style="background-color: #f9cb9c;">4</td>
    <td style="background-color: #f9cb9c;">0</td>
    <td style="background-color: #f9cb9c;">0</td>
  </tr>
  <tr>
    <th>9</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>3</td>
  </tr>
  <tr>
    <th>11</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
</table>

We blijven dit herhalen tot de graaf slechts 2 knopen over heeft.