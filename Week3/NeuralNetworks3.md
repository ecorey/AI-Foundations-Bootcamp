# Neural Networks

---

- **Standard Neural Networks (SNNs):**

Also known as Feedforward Neural Networks (FNNs).
They consist of a series of layers: an input layer, hidden layers, and an output layer.
Each neuron in one layer is connected to every neuron in the next layer, forming a "feedforward" structure with no loops.

They are typically used for static pattern recognition, where the input is fixed, like classifying images or predicting the next word in a sentence.

---

- **Recurrent Neural Networks (RNNs):**

Designed to recognize patterns in sequences of data, such as text, genomes, handwriting, the spoken word, numerical time series data, and more.

They have "memory" which captures information about what has been calculated so far, essentially allowing them to make decisions based on previously seen data.
The output from the neurons can be directed back into the network, creating a loop, or "recurrence".

A major issue with RNNs is the difficulty in learning long-range dependencies (long-term memory) due to problems like vanishing or exploding gradients during training.

---

- **Convolutional Neural Networks (CNNs):**

Primarily used in image processing but also applicable to other types of data that can be represented in a grid (like audio).

They use a special operation called "convolution" which applies filters to an input to create feature maps that summarize the presence of detected features in the input.
They typically include layers that perform pooling operations which reduce the dimensionality of the feature maps, thus reducing the number of parameters and computation in the network.

CNNs are excellent for recognizing visual patterns directly from pixel images with minimal preprocessing.

---

-**Generative Adversarial Networks (GANs):**

Composed of two neural networks, a generator and a discriminator, which are trained simultaneously by an adversarial process.

The generator creates samples that are intended to come from the same distribution as the training data, while the discriminator tries to distinguish between real and fake samples.

The training procedure for GANs is a mini-max game where the generator is trying to maximize the probability of the discriminator making a mistake, and the discriminator is trying to minimize that same probability.

GANs are widely used for generating realistic images, 3D-models, and can even be used for super-resolution, style transfer, and more.

---

- **Transformer Neural Networks:**

Introduced in the paper "Attention is All You Need", transformers revolutionized natural language processing tasks.

They rely entirely on an attention mechanism to draw global dependencies between input and output, without using sequence-aligned RNNs or convolution.

The key innovation of transformers is the self-attention mechanism, which computes a representation of a sequence by relating different positions of the sequence to each other.

Transformers are the architecture behind models like GPT (Generative Pretrained Transformer) and BERT (Bidirectional Encoder Representations from Transformers), which achieve state-of-the-art results on various NLP tasks.
