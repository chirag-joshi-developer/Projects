# Project Development Process

# Problem Definition

- Identified the need for a computer vision model capable of classifying Indian satellite dish brands (e.g., Tata Sky, DishTV, Airtel Digital TV) by detecting logos on dish antennas.

- Chose this as a unique, real-world challenge with no publicly available dataset, and with added complexity due to worn-out or unclear branding on the dishes.

# Data Collection – Web Scraping

Developed a custom Google image scraping tool tailored to Google’s updated image search module, as existing scrapers were incompatible due to recent structural changes.

# Data Preprocessing – Image Resizing

Built an image preprocessing utility to resize all collected images to a consistent shape of 256×256×3, ensuring uniform input dimensions for model training.

# Dataset Expansion – Data Augmentation

Addressed the limited dataset size (400–500 images across 5 classes) by implementing a data augmentation pipeline.

# Applied the following 7 transformations to synthetically expand the dataset:

1. Brightness \& Contrast Adjustment

2. Color Jitter

3. Random Cropping

4. Horizontal Flipping

5. Gaussian Noise Injection

6. Rotation

7. Zooming

# Model Selection \& Feasibility Analysis

## Investigated multiple model architectures to determine their suitability given the dataset size and compute resources:

# LeNet-5 inspired ConvNet (built from scratch):

Lightweight and educational, ideal for baseline comparison.

# VGG-16 / VGG-19 (Transfer Learning):

Suitable for fine-tuning with limited data.

# InceptionV3:

Considered but deprioritized due to training complexity.

# Vision Transformers (ViT):

Deferred due to high computational requirements.

# Final Model Decision

## Based on time constraints and dataset size, selected the following dual-model approach:

1. Trained a LeNet-style custom CNN from scratch for baseline understanding.
2. Applied transfer learning using VGG-16, freezing convolutional layers and fine-tuning the final fully connected layers to improve performa

# Model Training

## Training procedures for both the custom LeNet-style CNN and the VGG-16 transfer learning model are documented in their respective experiment logs, detailing:
Loss curves
Accuracy trends

# Key observations and insights
These logs provide a comprehensive view of the models’ learning behavior across epochs.

Final Insight: Power of Selective Fine-Tuning
===

1. Our experiments demonstrate that fine-tuning a pre-existing large model like VGG-16, while freezing most of its layers and training only the classifier, offers superior performance with minimal training cost.
2. The best-performing model (Experiment 4) achieved over 98% test accuracy and high F1-scores across all sets, while only fine-tuning the final classifier layer with regularization.
3. Compared to training a custom CNN from scratch (Model 1), the fine-tuned VGG-16 (Model 2) showed:
4. Higher accuracy
5. Lower variance across train/dev/test sets
6. Greater generalization
7. Less bias and better convergence with fewer epochs

# ✅ Conclusion

Selective fine-tuning of larger pretrained models is not only more computationally efficient, but also leads to more stable and robust performance than training smaller models from scratch.

