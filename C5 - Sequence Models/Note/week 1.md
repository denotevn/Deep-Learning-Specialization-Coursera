# **Learning Objectives:**
  + Define notation for building sequence models
  + Describe the architecture of a basic RNN
  + Identify the main components of an LSTM
  + Implement backpropagation through time for a basic RNN and an LSTM
  + Give examples of several types of RNN
  + Build a character-level text generation model using an RNN
  + Store text data for processing using an RNN
  + Sample novel sequences in an RNN
  + Explain the vanishing/exploding gradient problem in RNNs
  + Apply gradient clipping as a solution for exploding gradients
  + Describe the architecture of a GRU
  + Use a bidirectional RNN to take information from two points of a sequence
  + Stack multiple RNNs on top of each other to create a deep RNN
  + Use the flexible Functional API to create complex models
  + Generate your own jazz music with deep learning
  + Apply an LSTM to a music generation task

## **RNN:**
  + ![RNN](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C5%20-%20Sequence%20Models/Week%201/images/RNN.png)
  + Recurrent Neural Networks (RNN) are very effective for Natural Language Processing and other sequence tasks because they have "memory.
  + They can read inputs $x^{\langle t \rangle}$ (such as words) one at a time, and remember some contextual information through the hidden layer activations that get passed from one time step to the next.
  + This allows a unidirectional (one-way) RNN to take information from the past to process later inputs. A bidirectional (two-way) RNN can take context from both the past and the future, much like Marty McFly.
  + ![Basic RNN](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C5%20-%20Sequence%20Models/Week%201/images/Basic%20RNN.png)
> **Forward RNN:**
  + ![Forward]()
  + The recurrent neural network, or RNN, is essentially the repeated use of a single cell.
  + A basic RNN reads inputs one at a time, and remembers information through the hidden layer activations (hidden states) that are passed from one time step to the next.
  + The time step dimension determines how many times to re-use the RNN cell (Tx)
  + Each cell takes two inputs at each time step:
     + The hidden state from the previous cell
     + The current time step's input data
  + Each cell has two outputs at each time step:
     + A hidden state
     + A prediction

## **Long Short-Term Memory (LSTM) Network:**
  + ![Basic LSTM](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C5%20-%20Sequence%20Models/Week%201/images/LSTM.png)
  + An LSTM is similar to an RNN in that they both use hidden states to pass along information, but an LSTM also uses a cell state, which is like a long-term memory, to help deal with the issue of vanishing gradients
  + An LSTM cell consists of a cell state, or long-term memory, a hidden state, or short-term memory, along with 3 gates that constantly update the relevancy of its inputs:
    + A forget gate, which decides which input units should be remembered and passed along. It's a tensor with values between 0 and 1
      + If a unit has a value close to 0, the LSTM will "forget" the stored state in the previous cell state
      + If it has a value close to 1, the LSTM will mostly remember the corresponding value.
    + An update gate, again a tensor containing values between 0 and 1. It decides on what information to throw away, and what new information to add.
      + When a unit in the update gate is close to 1, the value of its candidate is passed on to the hidden state
      + When a unit in the update gate is close to 0, it's prevented from being passed onto the hidden state.
    + And an output gate, which decides what gets sent as the output of the time step

