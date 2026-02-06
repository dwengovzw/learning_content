---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Processing in the project
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: aiz_etdigitalecompetentiezorg
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
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: true
title: Processing in the project
version: 3
---
# Digital competence and media literacy 
## Attainment targets for digital competence and media literacy, and the '*AI in de Zorg*' project 

*Attainment target 4.1 (second and third stage) - Self-confidence* 

You don't have to be a whiz at math and science, nor do you have to be great at programming to get started with the AI in de Zorg notebooks.<br>
By giving students positive experiences in a domain that is probably unfamiliar to them but socially relevant and connected to their world—everyone has to go to the doctor or hospital at some point—their self-confidence regarding computer science, in particular programming and artificial intelligence, can get a boost.<br>
Students from non-STEM tracks realize, by working with the notebooks of the ‘AI in de Zorg’ project, that some programming assignments are also within their reach.<br>
Students from STEM tracks also gain more self-confidence because they manage to apply familiar principles of programming and concepts of computational thinking to a new problem statement. 


*Attainment target 4.2 (second and third stage) - Compatibility between digital infrastructure and applications (second stage) - Standard functionalities/Functionalities* 

The notebooks of the ‘AI in de Zorg’ project work with datasets. The students process the data with Python to arrive at a decision tree. They can rely on existing Python modules for that, but they must ensure that the data used are compatible with the functionalities of the module employed. The data must be provided in the correct format to the rule-based AI system. To that end, the data sometimes have to be prepared first: e.g., remove patients whose data are missing from the dataset, and convert the values of categorical variables into numerical values. Fortunately, there are already simple functions for that which students can use. The data are then used to generate a decision tree by means of simple functions present in the module used.<br>
Students are introduced to files with the extension ‘ipynb’, which can only be opened with suitable software.<br>
You can tell students that, for example, in Natural Language Processing applications the text that an AI system has to work with must also be provided in the correct format. A chatbot or a digital assistant can be given as an example here. For example, a chatbot works with typed text that is first preprocessed before an AI system can get to work with it; a digital audio file must first be converted to text by means of speech recognition software (speech to text) before the assistant can analyze the question and then generate an appropriate answer.<br>
The same applies if one dictates the electronic patient record instead of typing the text. 


*Attainment target 4.3 (second and third stage) - Digital structure and applications to communicate digitally* 

<ul><li>The chatbot for the anamnesis interview is an example of digital communication.</li></ul>
<ul><li><em>Wearables</em> are also a form of digital communication, albeit between digital systems. The automated form of the EWS also falls under this.</li></ul>
<ul><li>If students use a <em>fitness tracker</em>, do they do so purposefully? Do they know what happens to the collected data?</li></ul>


*Attainment target 4.4 (second stage) - The bit as the basic unit of data* 

Data are given to the computer in a digital format. Specifically, this means that the data are converted into numbers, which in turn are represented by a string of zeros and ones. Such a zero or one is a bit. For example, the natural numbers from 0 up to and including 255 can be represented by a string of 8 zeros and ones; for example, 35 is 00100011 (a string of eight zeros and ones is a byte).<br>
For example, one hot encoding: with text (e.g., for an electronic patient record) the computer is given a list of words in a certain order. With a string of zeros and a one, for example 0000000000000001000000000...0, a particular word can then be given to the computer. In the example, the 1 is in the sixteenth position in the string, which means that the word is the sixteenth word in the word list. To make it known to the computer which of the words in the word list appear in a patient record, a string of zeros and ones, such as 0010111010000001000000100...0, can then be supplied.<br>
That means that the third, fifth, sixth, seventh, ninth, sixteenth, twenty-third ... word occurs in the dossier. Another example is medical imaging. For a computer, a photo is nothing more than a table of numbers. The computer can therefore very quickly, by calculating, discover the difference between two photos and even detect very subtle changes and signal them to the radiologist.<br>
For the EWS score, values of body parameters are given to the computer; these can naturally be integers (type int), or decimal numbers (type float), or also text (type string). 


*Attainment target 4.4 (second and third stage) - Sending, receiving, processing, storing, agreements between digital systems* 

To get started with a notebook, the URL is entered into the web browser. This URL contains a protocol (HTTPS, which indicates a secure connection) and a domain name (kiks.ilabt.imec.be/jupyter).<br>
The web browser contacts a DNS server via the internet to look up the IP address (a numeric internet address) of the AI Op School server. The user's message (the client, here the web browser of the student's or teacher's computer) is then passed on to the AI Op School web server. This server is asked to grant access to the AI Op School notebooks.<br>
The *Hypertext Transfer Protocol* (HTTP) is a computer protocol in which agreements are laid down so that one computer (in this case the student's or teacher's computer) and another computer (here the AI Op School web server) can communicate with each other.<br>
*HyperText Transfer Protocol* Secure (HTTPS) is nothing more than an extension of the HTTP protocol to allow the exchange of data to take place securely as well. The HTTPS protocol encrypts the data.<br>
The server then grants access to the notebook of the ‘AI in de Zorg’ project. The desired project can be selected and afterwards the desired notebook as well. While going through the notebook, the web browser continually communicates with the server, e.g., when executing a Python script. In doing so, the notebook, for example, uses the CPU (computational unit) or the GPU (even more computing power) of the server. 

The student can download a notebook and save it on their own computer. To be able to open the notebook again on their own computer, suitable software will have to be installed on that computer.<br>
If a student wants to print a notebook, then the student's computer must be able to communicate with the printer. A protocol is also needed for this. 


*Attainment target 4.4 (second stage) - Algorithm* 

The Python scripts in the notebooks contain algorithms that were developed to obtain a decision tree.<br>
In particular, for the manual construction of a decision tree, a ‘divide and conquer’ algorithm is used. In this unplugged activity, students experience firsthand the iterative process that the computer can also perform—and much faster. The students manually construct a decision tree by means of the Gini index and starting from labeled data. Afterwards they give the same data to the computer, with which they generate the same decision tree using Python. Python also works with the Gini index in the notebook; the students are confronted with the fact that the computer can do it much faster.<br> 
Examples: 

<ul><li>Some notebooks contain only an algorithm that reads in the data and, based on that, generates a decision tree.</li></ul> 
<ul><li>In other notebooks, that same algorithm is expanded with a few instructions to prepare the data.</li></ul>
<ul><li>In the chatbot notebook, an algorithm checks whether the question asked occurs in the dataset, upon which it returns a corresponding answer.</li></ul> 

There are also a few notebooks that prepare for the notebooks on decision trees and on chatbots. In these notebooks, students adapt a given algorithm or devise one themselves. 


*Attainment target 4.4 (second stage) - Input, processing, output* 

Examples: 

<ul><li>In the notebooks one starts from data (the input); in AI in de Zorg these are usually patient data. These data are processed: the data are preprocessed after which they can be offered in the correct format to the AI system. The AI system then gets to work with the data. This ultimately leads to an output: the decision tree.</li></ul> 
<ul><li>Once you have a decision tree, you use it to make a prediction about a new, previously unseen patient, for example: Is this patient at risk of a heart attack? Will a particular patient be able to go home the day after the operation? The data of the new patient are the input; these data are entered into the decision tree and then follow a path, depending on the answers to the successive questions, until a leaf is reached; that is the processing. The information that the leaf provides is the output.</li></ul> 
<ul><li>In the notebook about the chatbot, the user enters a question; that is the input. The AI system then searches the database for that question or one that does not differ too much from it; that is the processing. Finally, the chatbot gives an answer to the user; that answer is the output.</li></ul> 


*Attainment target 4.4 (second stage) - Error messages* 

If the students use data in their Python script that do not conform to the format required by the functions used, they will see an error message in the notebook as a result of the compatibility problem. 


*Attainment target 4.4 (third stage) - Databases, digital systems - Assessing building blocks* 

In the notebooks, a rule-based system generates a decision tree based on large datasets that are difficult to process manually. The data are stored in a csv file.<br>
The ‘AI in de Zorg’ project covers digital systems such as wearables and monitoring systems in hospitals.<br>
By going through the chatbot notebook and doing the activities around chatbots, students realize that many of today's chatbots still work by means of a large data file with questions and answers in it. 


*Attainment target 4.4 (third stage) - Analog and digital representations* 

As mentioned earlier, with digital assistants a digital audio file is first converted to text by means of speech recognition software (speech to text) before the assistant can analyze the question and then generate an appropriate answer. That digital audio file is itself already a conversion of a recording of a particular voice sound (an analog audio file). Information is always lost in the conversion from analog to digital.<br?>
Speech recognition software is also used when, for example, one dictates an electronic patient record or addresses a robot. The voice sound (an analog audio file) is converted to typed text or to a format that the robot can understand. 


*Attainment target 4.5 (second and third stage) - Concepts of computational thinking* 

In the notebooks: decomposition (different matters must be addressed when preparing the data) - algorithm - abstraction (use of functions).<br>
Pattern recognition: problems from very different contexts can be tackled with a similar AI system, here a decision tree. 


*Attainment target 4.5 (third stage - General and dual finality) - Digital representation of information* 

Data and information are not the same. A computer works with data, which must be represented in the right way. The information is derived by humans from the data by interpreting the data. 


*Attainment target 4.5 (second and third stage - General and dual finality) - Programming language, program, principles of programming, debugging* 

Students take simple steps in Python. They acquire insights by means of an example program and adapt that program to new contexts. It may also be that they need to expand the program with extra instructions to preprocess the data.<br>
Sequence is covered in the notebooks, as are debugging and working with built-in functions.<br>
Students run the code continuously while going through the notebooks. When error messages occur, they must immediately track down the error and then adjust the code or the data. 


*Attainment target 4.5 (second and third stage - General and dual finality) - Elements of programming languages* 

Concepts such as types (e.g., *string*, *int*, *float* and *NumPy array*), variables (e.g., variables that refer to the data or to the generated decision tree), and functions (e.g., the built-in functions that are used) are covered in the notebooks. Operators may also be covered.<br>
To look up a given item in a *NumPy array*, a comparison operator or a logical operator is used, for example. Displaying something on the screen is done with the function print(). 


*Attainment target 4.6/4.7 (second and third stage) - Mutual influences between individuals and media and society on learning, work and leisure* 

These mutual influences are amply addressed in the content of the ‘AI in de Zorg’ project. The interplay between technological developments and society can be nicely illustrated through the causes of the AI winters and summers. The needs that arise in society, e.g., the staff shortage in the healthcare sector, also influence the presence and development of new technology. Ethical aspects, e.g., the importance of social contact, certainly also have their influence. Quite a few examples are described in the contents of the project. 


*Attainment target 4.6/4.7 (second and third stage) - Data literacy, e-inclusion* 

Through the project contents, students realize how personal data can be used by different parties and linked to each other.<br>
They realize that collecting and processing data from many patients can lead to new insights that may be important for better healthcare. On the other hand, they also reflect on the privacy aspects involved.<br>
They can deal more consciously with wearables, fitness trackers, and with who they grant access to their electronic patient record and why.<br>
COVID-19 also showed that patient data are important for controlling the pandemic. E-inclusion is also related to this: not everyone has a smartphone to use the ‘Coronalert’ app. 


*Attainment target 4.7/4.8 (second and third stage) - Ethics* 

Students are aware that new technologies can also raise ethical issues. Because people are involved in the healthcare sector, ethical questions are prominently present there. In the ‘AI in de Zorg’ project, examples of ethical aspects are provided that can be used as topics for a class discussion. 


*Attainment target 4.7/4.8 (second and third stage) - Risks of media behavior* 

Students realize that when collecting and processing patient data one must think about privacy issues and handle them consciously.<br>
In the context of the COVID-19 pandemic, it has already become clear several times that views on privacy can change when the situation changes; think, for example, of the ‘Coronalert’ app and the ‘Covid Safe Ticket’. That is not wrong in itself, but students should be aware of it.