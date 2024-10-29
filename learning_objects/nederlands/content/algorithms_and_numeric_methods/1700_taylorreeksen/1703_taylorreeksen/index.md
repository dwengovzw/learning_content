---
hruid: anm_1703
version: 3
language: nl
title: "Stellingen"
description: "Taylorreeksen"
keywords: [""]
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
# Stellingen

## MacLaurinontwikkeling

Als $f$ $n$ maal afleidbaar is in $0$ dan bestaat er juist één veeltermfunctie $f_n$ van de $n$-de graad zodat 
$$f_n(0) = f(0), f_{n}'(0) = f'(0), f_{n}''(0) = f''(0), ... , f_{n}^{(n)}(0) = f^{(n)}(0)$$<br>
namelijk
$f_n(x) = f(0)  + \frac{f'(0)}{1!} x +  \frac{f''(0)}{2!} x² + ... + \frac{f^{(n)}(0)}{n!} x^n$
## Taylorontwikkeling

Als $f$ $n$ maal afleidbaar is in $a$ dan bestaat er juist één veeltermfunctie $g_n$ van de $n$-de graad zodat 
$$g_n(a) = f(a), g_{n}'(a) = f'(a), g_{n}''(a) = f''(a), ... , g_{n}^{(n)}(a) = f^{(n)}(a)$$<br>
namelijk
$g_n(x) = f(a)  + \frac{f'(a)}{1!} (x - a) +  \frac{f''(a)}{2!} (x - a)² + ... + \frac{f^{(n)}(a)}{n!} (x - a)^n$
