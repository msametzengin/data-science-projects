import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('heart.csv')
# print(df.describe())

# # Histogram Analysis
# df.hist(figsize=(18,12),bins=20,edgecolor='black')
# plt.suptitle('Data Distribution')
# plt.show()

# # The Relationship Between Age and Cholesterol
# plt.figure(figsize=(10,6))
# sns.scatterplot(data=df,x='Age',y='Cholesterol',hue='HeartDisease')
# plt.title('The Relationship Between Age and Cholesterol')
# plt.show()

# # Let's plot the correlation matrix, but first, let's convert the data into numerical data.
# labelEncoder = LabelEncoder()
# df['Sex'] = labelEncoder.fit_transform(df['Sex'])
# df['ChestPainType'] = labelEncoder.fit_transform(df['ChestPainType'])
# df['RestingECG'] = labelEncoder.fit_transform(df['RestingECG'])
# df['ExerciseAngina'] = labelEncoder.fit_transform(df['ExerciseAngina'])
# df['ST_Slope'] = labelEncoder.fit_transform(df['ST_Slope'])

# plt.figure(figsize=(12,8))
# sns.heatmap(df.corr(),annot=True,cmap='coolwarm',fmt='.2f')
# plt.title('Correlation Heat Map')
# plt.show()

# # Heart Disease Incidence Rates
# plt.figure(figsize=(6,6))
# sns.countplot(x='HeartDisease',data=df)
# plt.title('Heart Disease Incidence Rates')
# plt.show()
