---
hruid: sr1_maakeengezicht
version: 3
language: en
title: "Maak een gezicht"
description: "Maak een gezicht"
keywords: ["sociale robot", "activiteit"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
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
estimated_time: 20
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek'
]
teacher_exclusive: true
---
# Unplugged computational thinking
## Create a face

![face](embed/gezichtje.png "face")

Program facial expressions on a robot face and simulate emotions without using a computer. The face must meet the following conditions:

* The robot face must be able to respond to different sounds, such as annoying, sudden, and unexpected sounds.
* The robot face must be able to simulate different emotions, such as sadness, happiness, and surprise.
* You come up with a few other facial expressions that the robot should be able to display.
* You program rules to make the robot face respond to different sounds and emotions with the new facial expressions.

### Preparation

Be sure to watch the following video and prepare the face parts in advance using a piece of cardboard.

![](@youtube/https://www.youtube.com/embed/7S3_QkAMi3Y "preparation create a face")

### Procedure

**Preparation**

1. Prepare the face parts before the session. The eyes and eyebrows can be made from hard cardboard covered with self-adhesive plastic or glued to colored paper.

2. The mouth is made of 4 long tubes (e.g. wrapping paper or PVC). Tie them together in a loop by threading a wire or rope through them. They should be easy to bend into curved shapes and into a circle. Color it bright red with colored paper or self-adhesive plastic.

**Setting up the face**

1. Have six volunteers come forward. They will operate the different parts of the robot face by following the program's instructions. The rest of the group will make sounds to which the robot will respond. If you make the activity longer, you can have the volunteers who operate the robot face alternate with each other. You can even make 2 faces at the same time if you want to involve more participants.

2. Give the two tallest volunteers each an eyebrow and let them stand a few meters apart. They must hold the eyebrows quite high. Ideally, there should be a blank wall behind them as a background for the face. Then give two more volunteers an open and a squinted eye each. They kneel in front of the first two and hold the narrowed eyes under the eyebrows. The wide-open eyes are kept behind their backs until they are needed. Finally, the last two people kneel and hold the sides of the mouth.

**Controlling the Face**

1. Now you have a robot face. Point out that it will not do anything useful without following rules, without a program. You could write instructions for the entire face, but it is easier to think of it as different, smaller objects (two eyes, two eyebrows, and two sides of the mouth) each with their own, independent rules.

2. Give each person in the face the corresponding instructions for controlling their object. They are listed at the end of this activity. They are made up of IF-THEN rules:

![rules](embed/rules.png "rules")

3. Explain that they should listen to the sounds of the audience and then perform the corresponding action. The eyebrows can be held up as high as they want and lowered to just above the eyes. The eyes can be wide open or squinted. The mouth can point in the middle up or down, or the two tubes each person is holding can be opened. The rules tell them in which position to stand depending on the sounds they hear.

4. Then explain to the audience what they should do. When you tell them, they should either make a horrible sound (as horrible as possible), make a beautiful sound, or suddenly boo. You tell the audience what to do using flash cards so that the people controlling the face can only react to the sound and not to what you say. See Figures 2-4 for the types of faces you should get.

5. Hold a few practice rounds where you say what is on the card, so that the people controlling the face get the hang of it, while you check. Then do a real round, using the cards to show the audience what to do. Randomize these cards. You can do this with different students if you have time and want everyone to control the face.


**Programming the Face**

1. The next challenge is programming the face. Divide the children into groups of six and have each group come up with up to three new facial expressions of their choice (e.g., winking). They can also create new positions like slanted eyebrows or closed eyes. Have them take turns demonstrating their expression so that others get a better idea of the facial expression. Note that the left and right sides of the face can have different rules, so they can do different things.

2. Then, have them draw the different facial expressions of the face. This is important because exact positions and shapes of eyebrows, eyes, and mouth can be determined. Then, they need to come up with a sound (or something visible in the audience) that can cause those particular emotions or facial expressions to be displayed.

3. Finally, they need to choose one of these facial expressions to add to the face's program. They need to create a flash card for the facial expression that tells the audience what to do. They need to create an IF-THEN rule for the facial expression, based on the shape of the ones already on the cards. One rule is needed for each of the six objects. One possible example of such a rule is: "IF boring sound THEN closed" for the left eye. The additional rules are then added to the existing rules, and a copy of these instructions is given to each group.

4. Each group can then take turns controlling the face with their customized rules.

5. Wrap up by summarizing what they did: writing a program that resembles one that would be used to control a real face, object-oriented programming, and exploring the human-computer interaction of the future.

<div class="alert alert-box alert-success">
<strong>Variations and extensions</strong><br>
<ul>
<li>If you have more time, you can have the group design the different parts of the face themselves, using paper or other materials. </li>
<li>The group can also write rules to make the face react to things other than sound. For example, you could have two faces staring at each other, where one reacts to sound and the other mimics the first. If one smiles, the second one also smiles.</li>
</ul>
</div>