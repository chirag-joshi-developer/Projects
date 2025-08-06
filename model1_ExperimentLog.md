🔬 Experiment #1: Test Run - Initial Model Sanity Check



Goal:

Check if the custom LeNet-style model is learning; verify model structure and training pipeline.



🧩 Configuration:



Model: Custom LeNet-style CNN

Epochs: 5

Batch Size: \[32]

Optimizer: \[ Adam ]

Learning Rate: \[lr=1e-3, betas=(0.9, 0.999)]

Loss Function: CrossEntropyLoss

Data Split: 80% Train / 10% Dev / 10% Test

Dropout Rate Conv Layer: 0.25

Dropout Rate Fully Connected Layer: 0.5

Augmentations: PreApplied

Pixel Normalization: Yes

Batch Normalization: Yes

weight initialization: He

Final layer weight initialization: Xavier

Activation Function: ReLU

Final Layer Acivation Function: Softmax



📈 Training Results (Train Set):

Epoch	Loss	Accuracy

1	1.8409	29.59%

2	1.5099	40.08%

3	1.3094	46.56%

4	1.1121	55.41%

5	0.9961	62.01%



✅ Verdict:

✔️ Model is functional and learning.

❌ Further tuning needed for higher accuracy.

🔜 Proceed to tuning learning rate and batch size next.



============================================================================================================================================================



🔬 Experiment #2: Deeper Training At Higher learning rate

🎯 Goal:

Improve model optimization and accuracy by increasing the number of epochs and learning rate



🧩 Configuration:

Model: Custom LeNet-style CNN

Epochs: 15

Batch Size: 64

Optimizer: Adam

lr=1e-2, betas=(0.9, 0.999)

Loss Function: CrossEntropyLoss

Data Split: 80% Train / 10% Dev / 10% Test

Dropout Rate (Conv Layers): 0.25

Dropout Rate (Fully Connected Layers): 0.5

Augmentations: PreApplied

Pixel Normalization: Yes

Batch Normalization: Yes

Weight Initialization:

Conv Layers: He

Final Layer: Xavier

Activation Function: ReLU

Final Layer Activation: Softmax



📈 Training Results (Train Set):

Epoch	Loss	Accuracy

1	1.7840	29.14%

4	1.0684	56.64%

7	0.6092	77.42%

11	0.3720	87.21%

15	0.2196	92.75%



🧪 Validation Results (Dev Set):

Loss: 0.2877

Accuracy: 91.78%

🧪 Generalization Results (Test Set):

Loss: 0.3359

Accuracy: 89.14%



✅ Verdict:

✔️ Significant accuracy improvement over Experiment #1.

✔️ Model successfully trained and generalized well on unseen data.



🔁 Potential Next Steps:

Experiment with different learning rates (e.g. 5e-3 or 1e-3 for fine-tuning)



============================================================================================================================================================



🔬 Experiment #3: Extended Training \& Broader Hyperparameter Tuning

🎯 Goal:

Push the model to achieve human-level performance on the training set by eliminating bias through extended training and broader hyperparameter adjustments.



🧩 Configuration:

Model: Custom LeNet-style CNN

Epochs: 18

Batch Size: 128

Optimizer: Adam (lr=5e-3, betas=(0.9, 0.999))

Loss Function: CrossEntropyLoss

Data Split: 80% Train / 10% Dev / 10% Test

Regularization \& Initialization:

Dropout: 0.2 (Conv layers), 0.4 (FC layers)

Augmentations: Pre-applied

Pixel Normalization: Yes

Batch Normalization: Yes

Weight Initialization:

He (Conv layers)

Xavier (Final layer)

Activation Function: ReLU

Final Layer Activation: Softmax



📈 Training Results (Train Set):

Epoch	Loss	Accuracy

1	1.6250	34.88%

4	0.6998	75.00%

7	0.3931	87.21%

11	0.3174	89.47%

15	0.1278	96.11%

18	0.0839	97.50%

Final Train Loss: 0.0072

Final Train Accuracy: 100.00%

🧪 Validation Results (Dev Set):

Loss: 0.2407

Accuracy: 93.42%

🧪 Generalization Results (Test Set):

Loss: 0.2283

Accuracy: 92.43%



📊 Classification Report:

✅ Train Set:

Precision: 1.0000

Recall: 1.0000

F1-Score: 1.0000

🧪 Dev Set:

Precision: 0.9322

Recall: 0.9369

F1-Score: 0.9336

🧪 Test Set:

Precision: 0.9220

Recall: 0.9236

F1-Score: 0.9226



✅ Verdict:

✔️ Model successfully fits the training data (bias eliminated).

⚠️ Mild variance observed — room for generalization improvement.



🔁 Potential Next Steps:

Apply L2 regularization to the model to reduce variance

Further tune hyperparameters (e.g. learning rate, dropout, batch size) to improve generalization



============================================================================================================================================================



🧪 Final Experiment Report – Experiment



🎯 Goal:

The primary goal of this experiment was to reduce overfitting and improve generalization by applying L2 regularization and tuning dropout rates across convolutional and fully connected layers.



⚙️ Configuration Summary

Model Architecture: Custom LeNet-style CNN

Epochs: 17

Batch Size: 64

Optimizer: Adam

Learning Rate: 1e-2

Weight Decay (L2 Regularization): 204e-6

Betas: (0.9, 0.999)

Loss Function: CrossEntropyLoss

Data Split: 80% Train / 10% Dev / 10% Test



Regularization \& Initialization

Dropout:

Convolutional Layers: 0.238

Fully Connected Layers: 0.447

Augmentations: Applied during preprocessing

Pixel Normalization: Enabled

Batch Normalization: Enabled

Weight Initialization:

He Initialization (Convolutional Layers)

Xavier Initialization (Final Layer)

Activation Function: ReLU

Output Activation: Softmax



📈 Training Metrics (Train Set)

Epoch	Loss	Accuracy (%)

1	1.8468	23.07

4	1.1871	53.73

7	0.8090	70.53

11	0.5029	82.91

14	0.4496	84.59

17	0.3960	86.43

Final Train Loss: 0.0979

Final Train Accuracy: 97.91%

Dev Loss: 0.2208 — Dev Accuracy: 93.09%

Test Loss: 0.2775 — Test Accuracy: 91.45%



📊 Classification Report

✅ Train Set

Precision: 0.9801

Recall: 0.9786

F1-Score: 0.9791

🧪 Dev Set

Precision: 0.9333

Recall: 0.9231

F1-Score: 0.9248

🧪 Test Set

Precision: 0.9249

Recall: 0.9149

F1-Score: 0.9162



✅ Conclusion

Introducing L2 regularization alongside dropout significantly reduced variance and improved generalization. The model achieved high performance across all splits, particularly showing strong consistency between the training, validation, and test sets.



Given that the dataset is self-curated and realistic in nature, expectations were kept practical throughout the process.



📌 Final Notes

After multiple rounds of experimentation and training, we have reached these values for the final experiment.



============================================================================================================================================================



🗒️ Side Note: K-Fold Cross Validation

In parallel, we conducted a separate experiment using k-fold cross validation to validate the robustness of our model.



K = 5, Epochs per fold = 15

Averaged Results Across Folds:



✅ Average Training Loss: 0.1064

✅ Average Training Accuracy: 96.52%

✅ Average Validation Loss: 0.2297

✅ Average Validation Accuracy: 93.26%

