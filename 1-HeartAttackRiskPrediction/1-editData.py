import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler

# upload data
df = pd.read_csv('heart.csv')
# print(df.head())
# print(df.info())
# print(df.isnull().sum())

#categorical columns
categorical_columns = ['ChestPainType','Sex','RestingBP','ExerciseAngina','ST_Slope']

#labelEncoder
le = LabelEncoder()
for column in categorical_columns:
    df[column] = le.fit_transform(df[column])

#standardize the data
numeric_columns = ['Age','RestingBP','Cholesterol','FastingBS','MaxHR','Oldpeak']
scaler = StandardScaler()
df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
#all data became numerical data

#converting the new dataset to CSV
df.to_csv('heart_numeric.csv',index=False)


