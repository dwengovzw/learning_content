---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: The Karger algorithm uses the Monte Carlo method to arrive at a solution.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 5
hruid: org-dwengo-elevator-riddle-monte-carlo-karger-python-2
keywords:
- grafen
- algoritme
- computationeel denken
- clustering
- datastructuur
- monte carlo
- python
- karger
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
teacher_exclusive: false
title: Karger in Python (the adjacency matrix)
version: 1
---
# Monte Carlo

## Karger's Algorithm: The Adjacency Matrix

An important observation in this algorithm is that to modify the edges of the nodes being merged, we can make use of the adjacency matrix. To do this, we first add up the columns for the two nodes. Then we do the same for the rows.

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

This gives us a matrix with one fewer column:

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

Then we do the same for the rows.

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

This results in the following matrix.

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

We continue to repeat this process until the graph has only two nodes left.