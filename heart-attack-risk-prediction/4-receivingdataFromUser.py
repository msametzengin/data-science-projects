import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
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

# Receiving data from the user and training the model.

while True:
    user_input_1 = float(input('Enter your age: '))
    user_input_2 = input('Enter your gender: ')
    user_input_3 = input('Enter your type of chest pain (ATA, NAP, ASY, TA): ')
    user_input_4 = float(input('Enter your resting blood pressure: '))
    user_input_5 = float(input('Enter your cholesterol level: '))

    try:
        # Let's convert user data into numerical data.
        user_data = pd.DataFrame({
            'Age':[user_input_1],
            'Sex':[label_encoder_sex.transform([user_input_2])[0]],
            'ChestPainType':[label_encoder_cp.transform([user_input_3])[0]],
            'RestingBP':[user_input_4],
            'Cholesterol':[user_input_5],

            # The following values ​​are the 6 values ​​remaining from the 11 data points, which were not received from the user.
            'FastingBS':[0],
            'RestingECG':[0],
            'MaxHR':[150],
            'ExerciseAngina':[0],
            'Oldpeak':[0.0],
            'ST_Slope':[1]
        })


        # Scaling the acquired data.
        user_data_scaled=scaler.transform(user_data)
        
        # Make a prediction
        prediction=model.predict(user_data_scaled)
        print(f'Your estimated risk of heart disease is: {prediction[0][0]:.4f}')
    except ValueError as e:
        print(f'An error occurred: {e}. Please check the information!')
    
    # Ask the user a question for a new prediction.
    againPred = input('Would you like to make another prediction? (Y/N)')
    if againPred.lower() != 'e':
        break
    
