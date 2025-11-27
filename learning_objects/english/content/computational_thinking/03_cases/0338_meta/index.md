---

hruid: m_ct03_38
version: 3
language: en
title: "Quadratic Equation - Functions in Python"
description: "Calculate the real roots of a quadratic equation using functions"
keywords: ["quadratic equation", "roots", "Python", "discriminant"]
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
**Problem Statement**<br>
Automate the calculation of the real roots of a quadratic equation. Determine both the number of roots and their values.
</context>
<decomposition>
**Decomposition**<br>
<ol>
    <li>Ask the user for the coefficients.</li>
    <li>Calculate the discriminant and determine the number of roots and their multiplicity.</li>
    <li>Calculate the roots if discriminant ≥ 0.</li>
    <li>Display the number of roots and their values.</li>
</ol>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>Repeated calculations (discriminant, roots) are encapsulated in functions.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>Functions abstract sub-algorithms (e.g., discriminant, roots calculation).</li>
    <li>A quadratic equation is an abstraction of finding the intersection points of a parabola with the x-axis.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
<ol>
    <li>Request the coefficients from the user.</li>
    <li>Calculate the discriminant.</li>
    <li>Determine the number of roots and their multiplicity.</li>
    <li>Calculate the roots if the discriminant is non-negative.</li>
    <li>Display the number of roots and their values.</li>
</ol>
</algorithms>
<implementation>
**Program in Python**

```Python
import math

def discriminant(a, b, c):
    """Calculate discriminant of a quadratic equation."""
    return b**2 - 4 * a * c

def number_of_roots(d):
    """Determine the number of roots and their multiplicity."""
    if d > 0:
        return 2, 1
    elif d == 0:
        return 1, 2
    else:
        return 0, 0

def roots(a, b, c, d):
    """Calculate roots for non-negative discriminant."""
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return x1, x2

# input
a = float(input("Enter the coefficient of x² (≠ 0): "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

# processing
d = discriminant(a, b, c)
n, m = number_of_roots(d)

if n != 0:
    r1, r2 = roots(a, b, c, d)

# output
if n != 0:
    print(f"The roots are: {r1} and {r2}")
    print(f"Number of solutions: {n} with multiplicity {m}")
else:
    print("There are no real roots")
```

</implementation>
