🧪 Experiment #1: Test Run – Sanity Check

🎯 Goal

Verify whether the custom VGG-16 model is learning properly and validate the model structure and training pipeline.



🧩 Configuration

Model: VGG-16 (pretrained, partial fine-tuning)

Epochs: 10

Batch Size: 64

Optimizer: Adam (lr = 1e-3, betas = (0.9, 0.999))

Loss Function: CrossEntropyLoss

Data Split: 80% Train / 10% Dev / 10% Test

Augmentations: Pre-applied (flip, rotate, etc.)

Pixel Normalization: Yes (using ImageNet stats)

Trainable Layers:



Conv Block 5 (last convolutional block)

Final Linear Layer of Classifier only

📊 Observations

Training started normally with decreasing loss and increasing accuracy during early epochs.

Around Epoch 6, both training loss and accuracy began oscillating.

Final training accuracy capped at ~60%.

Indicates instability in learning.

🔎 Possible Reasons

Learning rate may be too high for the small number of trainable parameters.

Model may be overfitting or failing to generalize due to limited training signal from only a few unfrozen layers.

🧾 Verdict

✔️ Pipeline and model setup are functional.

⚠️ Training dynamics show instability after ~6 epochs.



🔄 Next Steps

Up the learning rate (e.g., to 1e-2)

Consider unfreezing entire conv block 5 and entire classifier block

==================================================================



🧪 Experiment #2: Expanded Fine-Tuning – Deeper Training, Higher LR

🎯 Goal

Increase model optimization by training a larger portion of the VGG-16 network and experimenting with a higher learning rate.



🧩 Configuration

Model: VGG-16 (pretrained, partial fine-tuning)

Epochs: 10

Batch Size: 64

Optimizer: Adam (lr = 1e-2, betas = (0.9, 0.999))

Loss Function: CrossEntropyLoss

Data Split: 80% Train / 10% Dev / 10% Test

Augmentations: Pre-applied

Pixel Normalization: Yes (ImageNet stats)

Trainable Layers:



Entire Conv Block 5

Entire Classifier

📊 Observations

Training was unstable across all 10 epochs.

Loss did not consistently decrease, and accuracy remained low throughout training.

Final training accuracy capped at ~25%.

🔎 Possible Reasons

Learning rate too high for the given training setup.

Too many parameters being updated without sufficient regularization or tuning.

Likely overfitting or poor convergence due to rapid weight updates.

🧾 Verdict

⚠️ Increasing the number of trainable layers and learning rate led to poor performance.

❌ No noticeable learning; model failed to generalize.



🔄 Next Steps

Reduce the number of trainable layers

==================================================================



🧪 Experiment #3: Classifier-Only Training – Reduced Fine-Tuning, Larger Batch

🎯 Goal

Assess the performance of VGG-16 when only the final classifier block is trained, freezing all convolutional layers. Also evaluate impact of increasing batch size.



🧩 Configuration

Model: VGG-16 (pretrained, partial fine-tuning)

Epochs: 10

Batch Size: 128

Optimizer: Adam (lr = 1e-3, betas = (0.9, 0.999))

Loss Function: CrossEntropyLoss

Data Split: 80% Train / 10% Dev / 10% Test

Augmentations: Pre-applied

Pixel Normalization: Yes (ImageNet stats)

Trainable Layers:



Only Classifier (All Conv Blocks frozen)

📊 Observations

Training was more stable compared to earlier experiments.

Loss decreased steadily across epochs.

Final accuracy peaked around 45% by epoch 10.

🔎 Interpretation

Freezing convolutional layers helped.

Larger batch size improved training stability.

The classifier alone was able to learn meaningful features from pretrained convolutional representations.

🧾 Verdict

✔️ Reducing the number of trainable layers improved performance significantly.

🎯 Training only the classifier is currently the best-performing setup.



🔄 Next Steps

Only Unfreezing last layer of classifier

==================================================================



🧪 Final Experiment: Minimal Fine-Tuning with L2 Regularization – Precision Boost

🎯 Goal

Test the impact of fine-tuning only the last layer of the classifier with L2 regularization to prevent overfitting. Focused on stabilizing high performance while keeping the model light.



🧩 Configuration

Model: VGG-16 (pretrained, minimal fine-tuning)

Epochs: 8

Batch Size: 128

Optimizer: Adam (lr = 5e-3, betas = (0.9, 0.999), weight\_decay = 1e-4)

Loss Function: CrossEntropyLoss

Data Split: 80% Train / 10% Dev / 10% Test

Augmentations: Pre-applied

Pixel Normalization: Yes (ImageNet stats)

Trainable Layers:



Only the last layer of the Classifier

📊 Final Epoch Performance (Epoch 8/8)

Loss: 0.1506

Overall Accuracy: 94.59%

🔍 Breakdown

Train Set



Loss: 0.0343

Accuracy: 99.59%

Precision: 0.9960

Recall: 0.9960

F1-Score: 0.9960

Dev Set



Loss: 0.0689

Accuracy: 99.01%

Precision: 0.9899

Recall: 0.9903

F1-Score: 0.9900

Test Set



Loss: 0.0922ss

Accuracy: 98.03%

Precision: 0.9823

Recall: 0.9810

F1-Score: 0.9814

🔎 Interpretation

L2 regularization (weight decay) was crucial in preventing overfitting.

Minimal fine-tuning allowed pretrained features to be preserved.

Classifier effectively adapted to new task using only shallow updates.

High generalization achieved with just the final layer being trained.

🧾 Verdict

✅ Best performance so far – nearly perfect generalization on unseen data

⚡ Minimal fine-tuning with proper regularization is extremely effective

🚀 Excellent baseline for future expansion or deployments

