---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: The finite difference method
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: stem5_10
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
teacher_exclusive: false
title: The finite difference method
version: 3
---
# The finite difference method

In the previous modules you were first introduced to (growth) models. Realistic or not, these were characterized by being discrete in time: time ticked by generation after generation. In practice, however, we experience time as continuous: between today and tomorrow there are an infinite number of individual moments. In this module we therefore discuss an important tool for working with continuous functions and their derivatives: the finite difference method.

## The use of functions

When modeling you use functions that convert a given input into an output. Consider, for example, the function \\(f\\) with definition \\(f(t) = t sin (t)\\). This function will convert a real value \\(t\\) into \\(t sin(t)\\), where \\(t\\) is an angle (in radians).

### Exercise 1

Evaluate the function definition for the values \\(t = \frac{\pi}{2}\\), \\(t = \pi\\), \\(t = \frac{3 \pi}{2}\\), \\(t = 2 \pi\\), \\(t = \frac{5 \pi}{2}\\), \\(t = 3 \pi\\), \\(t = \frac{7 \pi}{2}\\), \\(t = 4 \pi\\). Which values do you obtain? Can you predict how the function will evolve for larger values of \\(t\\)?

\\(f(\frac{\pi}{2}) = 1.57\\)

\\(f(\pi) = 0\\)

\\(f(\frac{3 \pi}{2}) = -4.71\\)

\\(f(2 \pi) = 0\\)

\\(f(\frac{5 \pi}{2}) = 7.85\\)

\\(f(3 \pi) = 0\\)

\\(f(\frac{7 \pi}{2}) = -11.00\\)

\\(f(4 \pi) = 0\\)

## The difference quotient

For a differentiable function you can compute a derivative. This derivative can be approximated by the difference quotient:

\\(f'(t) = \frac{\text{d}f(t)}{\text{d}t} \approx \frac{f(t + \Delta t) - f(t)}{\Delta t}\\)

The formula used here to estimate the derivative is called the finite difference method. In this method, \\(\Delta_t\\) is preferably as small as possible.

### Exercise 2

Compute, based on the above formula, an estimate for the difference quotient of \\(f\\) at \\(t = 2\\), taking \\(\Delta t = 0.1\\).

\\(f(2) = 2 sin(2) \approx 1.8186\\)

\\(f(t + \Delta t) = f(2.1) = 2.1 sin(2.1) \approx 1.8127\\)

\\(f(t + \Delta t) - f(t) \approx 1.8127 - 1.8186 = -0.0059\\)

\\(\frac{f(t + \Delta t) - f(t)}{\Delta t} \approx \frac{-0.0059}{0.1} = -0.059\\)

## The derivative of a function

When you take smaller steps, the absolute value of the difference \\(f(t + \Delta t) - f(t)\\) typically decreases, but you also divide by an ever smaller number. When you consider the limit of \\(\Delta t\\) to 0, the approximation converges to the true derivative \\(f'(t)\\):

\\[f'(t) = \lim\limits_{\Delta t \to 0} \frac{f(t + \Delta t) - f(t)}{\Delta t}\\]

In the notebook we will investigate the impact of the parameter \\(\Delta t\\).

## Interactive notebook

In the notebook below you will use Python to plot the graph of the function \\(f\\), and to investigate whether a smaller value for \\(\Delta t\\) leads to better estimates of the derivative.

[![](embed/knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=6060_en "Finite difference method")