# MNIST Handwritten Digit Classifier
This project implements a feedforward neural network from scratch in NumPy to classify handwritten digits from the MNIST dataset. It avoids high-level machine learning libraries like TensorFlow or PyTorch to provide a deeper understanding of how neural networks work at the fundamental level.

# Dataset
Source: MNIST CSV from Kaggle

Each image: 28x28 grayscale pixels (flattened to 784 values)

Labels: Digits from 0 to 9

The dataset is split into:

Training set: 58,000 samples

Test set: 1,000 samples

Dev set: 1,000 samples

# Model Architecture
A simple 3-layer fully connected neural network:

Input Layer  (784 neurons)
Hidden Layer 1 (128 neurons) + ReLU
Hidden Layer 2 (64 neurons)  + ReLU
Output Layer  (10 neurons)   + Softmax

# Training Details
Loss Function: Cross-Entropy Loss

Optimization: Batch Gradient Descent

One-Hot Encoding for labels

Manual implementation of forward pass, backward pass (gradients), and parameter updates

# Evaluation
Accuracy: Printed on dev and test set

# Visuals: Sample predictions

# Confusion matrix: Misclassified digits with true vs predicted labels

# Project Structure
forward_pass(): Calculates activations through all layers.

backward_pass(): Computes gradients using chain rule.

update_params(): Updates weights and biases using gradients.

predict(): Returns class predictions for given input.

plot_confusion_matrix(): Displays model confusion matrix.

show_incorrect_predictions(): Displays examples the model got wrong.

# How to Run
pip install numpy pandas matplotlib scikit-learn kagglehub
Ensure you have your Kaggle API credentials set up (kaggle.json in the right location).

Run the notebook: MNIST_numpy_NN.ipynb

# Learning Objectives
Understand how neural networks work internally
Gain experience implementing backpropagation manually
Learn how to preprocess data, build evaluation metrics, and tune parameters
