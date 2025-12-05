---
content_type: text/markdown
copyright: CC BY dwengo
description: Learn which layers a neural network consists of and what these layers
  are for.
estimated_time: 10
hruid: org-dwengo-waisda-beelden-emoties-deel2-het-netwerk
keywords:
- lagen
- AI
- neurale netwerken
language: en
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
- http://ilearn.ilabt.imec.be/vocab/tref1/ict
target_ages:
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: false
title: The layers of the neural network
version: 1
---
# The neural network that can learn to recognize emotions

In part 1 of the activity on recognizing emotions, you trained the following neural network.

![Figure neural network emotions](img/neural_network_visualized.png)

You saw that this network consisted of different layers.
- An input layer (InputLayer)
- Convolutional layers (Conv2d)
- Normalization layers (BatchNormalization)
- Pooling layers (MaxPooling2D)
- Dropout layers (Dropout)
- Fully connected layers (Dense)

We used the following Python code to add the layers to our model.

```Python

    model = Sequential()
    
    model.add(InputLayer(input_shape=(hoogte_afbeelding, breedte_afbeelding, 1)))
    
    model.add(Conv2D(1, (3, 3), activation="relu"))
    model.add(BatchNormalization())
    model.add(MaxPooling2D((2, 2)))
    model.add(Dropout(0.1))
    
    model.add(Conv2D(2, (3, 3), activation="relu"))
    model.add(BatchNormalization())
    model.add(MaxPooling2D((2, 2)))
    model.add(Dropout(0.1))
    
    model.add(Conv2D(4, (3, 3), activation="relu"))
    model.add(BatchNormalization())
    model.add(MaxPooling2D((2, 2)))
    model.add(Dropout(0.1))
    
    model.add(Conv2D(8, (3, 3), activation="relu"))
    model.add(BatchNormalization())
    model.add(MaxPooling2D((2, 2)))
    model.add(Dropout(0.1))
    
    model.add(Conv2D(16, (3, 3), activation="relu"))
    model.add(BatchNormalization())
    model.add(MaxPooling2D((2, 2)))
    model.add(Dropout(0.1))
    
    model.add(Flatten())
    model.add(Dense(16, activation="relu"))   
    model.add(Dropout(0.1)) 
    model.add(Dense(2, activation="softmax"))
    
    model.compile(optimizer="adam", 
        loss="categorical_crossentropy", 
        metrics=["accuracy"])

```

You trained this model to recognize the emotions of smileys. In this learning path you will see what the different layers are used for. Then you will try to "break" the model. That means you will remove or modify layers until you can no longer train it reliably to recognize emotions.