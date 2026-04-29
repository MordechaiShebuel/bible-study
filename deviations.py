import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Data matrix (excluding diagonal "-")
data = np.array([
    [0, 0.8, 0.7, 0.6, 0.5, 0.3, 0.2],
    [0.8, 0, 0.5, 0.6, 0.4, 0.3, 0.2],
    [0.7, 0.6, 0, 0.6, 0.7, 0.5, 0.4],
    [0.6, 0.5, 0.6, 0, 0.4, 0.4, 0.3],
    [0.5, 0.4, 0.7, 0.4, 0, 0.6, 0.5],
    [0.3, 0.4, 0.3, 0.5, 0.6, 0, 0.8],
    [0.2, 0.3, 0.2, 0.4, 0.5, 0.8, 0]
])

# Groupings
groupings = ["Pauline Epistles", "Johannine Epistles", "Practical Faith & Works",
             "Synoptic Narrative", "Eschatological & Diverse", "Torah", "Nevi'im/Ketuvim"]

# Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data, annot=True, cmap="YlOrRd", xticklabels=groupings, yticklabels=groupings,
            vmin=0, vmax=1, center=0.5, square=True, fmt=".1f")
plt.title("Likelihood of Connection Between Biblical Groupings", pad=20)
plt.xlabel("To")
plt.ylabel("From")
plt.tight_layout()
plt.show()
