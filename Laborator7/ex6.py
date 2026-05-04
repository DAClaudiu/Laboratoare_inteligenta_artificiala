import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
import pandas as pd

# Load dataset
diabetes = load_diabetes()

# Convert to DataFrame
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target

# Create figure with 2 subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Subplot 1: BMI vs target
axs[0].scatter(df['bmi'], df['target'])
axs[0].set_title('BMI vs Target')
axs[0].set_xlabel('BMI')
axs[0].set_ylabel('Target')

# Subplot 2: Age vs target
axs[1].scatter(df['age'], df['target'])
axs[1].set_title('Age vs Target')
axs[1].set_xlabel('Age')
axs[1].set_ylabel('Target')

plt.tight_layout()
plt.show()