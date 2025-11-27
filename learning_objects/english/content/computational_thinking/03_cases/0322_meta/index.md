---

hruid: m_ct03_22
version: 3
language: en
title: "Locked-in"
description: "Locked-in"
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
**Problem Statement**<br>
Bauby wakes up completely paralyzed in the hospital. He can only blink one eye. He still finds a way to communicate and even succeeds in writing a book. Analyze, from the principles of computational thinking, how Bauby could communicate and write a book. Discuss his method and ways to improve it.
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>What is still possible? 
        <ul>
            <li>Bauby can blink one eye. 
	        <li>Bauby can read.
	        <li>The helper can speak, read, and write. 
        </ul>
    </li>
    <li>How could Bauby communicate?
        <ul>
            <li>Words consist of letters. Blinking with one eye must be converted into letters. For example, one blink means 'a', two blinks 'b' ... The helper only needs to count the blinks and write down the corresponding letter.</li>
        </ul>
    </li>	
    <li>How could Bauby write a book?
        <ul>
            <li>In the same way, but also adding spaces, punctuation, numbers, whitespace ... to the alphabet.</li>
        </ul>
    </li>
    <li>What to do if a mistake is made? How to approve or reject a guess by the helper?
        <ul>
            <li>There must be an agreed way to communicate in those cases.</li>
        </ul>
    </li>
    <li>How can it be faster? 
        <ul>
            <li>Use the timing of the blink instead of the number of blinks.</li>
            <li>First ask the most frequent letters by adjusting the order of letters in the alphabet.</li>
            <li>Binary search ensures each letter is found after at most 5 enumerations!</li>
            <li>The helper guesses a word if reasonably certain.</li>
            <li>Automate with technology.</li>
        </ul>
    </li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>Sometimes you can guess a word halfway. If you have 'a-n-t-i-l', the word 'antelope' could be a good guess. This is the same as 'word suggestion' on a smartphone. If the helper is reasonably certain, guessing saves time.
    <li>Some letters occur more frequently than others. Over the centuries, frequency analysis has been used to crack secret codes. Cracking codes and guessing letters are similar problems. Therefore, Bauby had the helper read letters in decreasing frequency (in French).
    <li>Binary search is a suitable divide-and-conquer strategy for searching among items with a certain order. You then ask halving questions (think of the game 'Guess Who?').</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>The number of blinks, a number, is an encoding of a letter, punctuation, ... (a different representation, the information is replaced by something else).
    <li>Thus, to know what the fastest algorithm is, you need to determine the number of letters the helper must go through. The duration itself is ignored (abstraction). You can estimate this by calculating the average number of letters enumerated per letter.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
<ul>
    <li>The algorithm Bauby used: the helper read the alphabet in order: 'e, s, a, r ... w'. When the letter Bauby thought of was spoken, he blinked. The helper wrote down the letter and started again, letter by letter.
    <li>Ways to speed up the process, e.g., binary search.</li>
</ul>
</algorithms>
<implementation>
**Program**<br>
Humans come first! We could apply binary search or use the computer to speed up the process. But would we still account for the correct aspects of the problem?
<ul>
    <li>What if blinking was very exhausting for Bauby? His solution required only one blink per letter. The divide-and-conquer algorithm would require five blinks. His solution is easy for everyone to understand. Ours is more complex, and who would explain it to visitors?
    <li>If we design a system with the computer, does automation do more harm than good? There would be no helpers providing human warmth.</li>
</ul>
</implementation>
