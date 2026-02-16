"""
---------- RESAULT --------
Artificial Neural Network Accuracy Rate: 89.49%
Random Forest Accuracy Rate: 70.65%
Decision Trees Accuracy Rate: 31.16%
Logistics Accuracy Rate: 85.51%
---------- RESAULT --------

According to the results: an artificial neural network model should be used.
The codes are below.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.layers import Dense  # type: ignore
from tensorflow.keras.optimizers import Adam  # type: ignore

df = pd.read_csv('heart.csv')

# Let's convert categorical data into numerical values.
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
label_encoder_sex = LabelEncoder()
label_encoder_cp = LabelEncoder()
df['Sex'] = label_encoder_sex.fit_transform(df['Sex'])
df['ChestPainType'] = label_encoder_cp.fit_transform(df['ChestPainType'])
df['RestingECG'] = label_encoder.fit_transform(df['RestingECG'])
df['ExerciseAngina'] = label_encoder.fit_transform(df['ExerciseAngina'])
df['ST_Slope'] = label_encoder.fit_transform(df['ST_Slope'])

# Define the input and output.
X = df.drop('HeartDisease' , axis=1)
y = df['HeartDisease']

# Let's separate the data into training and testing categories.
X_train, X_test , y_train, y_test = train_test_split(X,y, test_size=0.3 , random_state=42)

# Correct data imbalance
smote = SMOTE(random_state=42)
X_train_smote , y_train_smote = smote.fit_resample(X_train, y_train)

# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_smote)
X_test_scaled = scaler.transform(X_test)

# ------------- MODELS -------------

#1. Artificial neural networks (ANN)
print('Model 1: Artificial Neural Networks')
model = Sequential()
model.add(Dense(16, input_dim=X_train_scaled.shape[1] ,activation = 'relu'))
model.add(Dense(1, activation='sigmoid'))

# Let's compile and train the model.
optimizer = Adam(learning_rate=0.001)
model.compile(loss='binary_crossentropy' , optimizer = optimizer , metrics=['accuracy'])

model.fit(X_train_scaled, y_train_smote, epochs=100 , verbose=1 , validation_data=(X_test_scaled, y_test) )
loss, accuracy = model.evaluate(X_test_scaled, y_test)

#2. Random Forest model (RF)
print('Model 2: Random Forest Model')
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train_smote,y_train_smote)
y_pred_rf=rf_model.predict(X_test_scaled)
rf_accuracy = accuracy_score(y_test,y_pred_rf)

#3. Decision Tree model (DT)
print('Model 3: Decision Tree Model')
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train_smote,y_train_smote)
y_pred_dt = dt_model.predict(X_test_scaled)
dt_accuracy = accuracy_score(y_test,y_pred_dt)

#4. Logistic Regression model (LR)
print('Model 4: Logistic Regression Model')
lr_model = LogisticRegression(random_state=42)
lr_model.fit(X_train_smote,y_train_smote)
y_pred_lr = lr_model.predict(X_test_scaled)
lr_accuracy = accuracy_score(y_test,y_pred_lr)

# ------------- MODELS -------------
# ------------- PRINTS -------------

print(f"Artificial Neural Network Accuracy Rate: {accuracy*100:.2f}%")
print(f"Random Forest Accuracy Rate: {rf_accuracy*100:.2f}%")
print(f"Decision Trees Accuracy Rate: {dt_accuracy*100:.2f}%")
print(f"Logistics Accuracy Rate: {lr_accuracy*100:.2f}%")

# ------------- PRINTS -------------