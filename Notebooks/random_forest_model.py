import os
import kagglehub
import numpy as np
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("ayeshaimran123/social-media-and-mental-health-balance")

print("Path to dataset files:", path)

# Load dataset
file_path = os.path.join(path, 'Mental_Health_and_Social_Media_Balance_Dataset.csv')
df = pd.read_csv(file_path)

df.head()