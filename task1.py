# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KyAc0K6-QSIKl4oLdwi95MoBwn8cYYDD
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
data = pd.read_csv('/content/sample_data/task1.csv')  # Replace with your dataset path

# Select relevant columns
features = ['Release Year', 'Duration', 'IMDB Rating', 'Metascore', 'Votes', 'Gross']
target = 'Genre'

# Ensure required columns are present
assert all(col in data.columns for col in features + [target]), "Dataset must have required columns."

# Handle missing values (e.g., fill with mean for numerical features)
data = data.fillna(data.mean())

# Encode categorical target (Genre)
label_encoder = LabelEncoder()
data[target] = label_encoder.fit_transform(data[target])

# Split the data into features (X) and target (y)
X = data[features]
y = data[target]

# Standardize numerical features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
data = pd.read_csv('/content/sample_data/task1.csv')  # Replace with your dataset path

# Select relevant columns
features = ['Release Year', 'Duration', 'IMDB Rating', 'Metascore', 'Votes', 'Gross']
target = 'Genre'

# Ensure required columns are present
assert all(col in data.columns for col in features + [target]), "Dataset must have required columns."

# Handle missing values (e.g., fill with mean for numerical features)
# Select only numerical features for calculating the mean
numerical_features = data.select_dtypes(include=['number']).columns
data[numerical_features] = data[numerical_features].fillna(data[numerical_features].mean())

# Encode categorical target (Genre)
label_encoder = LabelEncoder()
data[target] = label_encoder.fit_transform(data[target])

# Split the data into features (X) and target (y)
X = data[features]
y = data[target]

# Standardize numerical features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import numpy as np

# Load the dataset
data = pd.read_csv('/content/sample_data/task1.csv')  # Replace with your dataset path

# Select relevant columns
features = ['Release Year', 'Duration', 'IMDB Rating', 'Metascore', 'Votes', 'Gross']
target = 'Genre'

# Ensure required columns are present
assert all(col in data.columns for col in features + [target]), "Dataset must have required columns."

# Clean and preprocess data
# Handle 'Release Year': Extract the first year if it's a range
data['Release Year'] = data['Release Year'].astype(str).str.extract(r'(\d{4})').astype(float)

# Handle 'Gross': Remove commas or symbols and convert to float
data['Gross'] = data['Gross'].replace('[^\d.]', '', regex=True).astype(float)

# Handle missing values (e.g., fill with mean for numerical features)
numerical_features = data.select_dtypes(include=['number']).columns
data[numerical_features] = data[numerical_features].fillna(data[numerical_features].mean())

# Encode categorical target (Genre)
label_encoder = LabelEncoder()
data[target] = label_encoder.fit_transform(data[target])

# Split the data into features (X) and target (y)
X = data[features]
y = data[target]

# Standardize numerical features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

