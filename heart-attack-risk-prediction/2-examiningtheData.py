import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('heart.csv')
# print(df.describe())

# # histogram analizi
# df.hist(figsize=(18,12),bins=20,edgecolor='black')
# plt.suptitle('Data Distribution')
# plt.show()

# # yaş ve kolestrol arasındaki ilişki
# plt.figure(figsize=(10,6))
# sns.scatterplot(data=df,x='Age',y='Cholesterol',hue='HeartDisease')
# plt.title('The Relationship Between Age and Cholesterol')
# plt.show()

# # yeni korelasyon matrisini çizme ama önce ilk veriyi numeric yapma
# labelEncoder = LabelEncoder()
# df['Sex'] = labelEncoder.fit_transform(df['Sex'])
# df['ChestPainType'] = labelEncoder.fit_transform(df['ChestPainType'])
# df['RestingECG'] = labelEncoder.fit_transform(df['RestingECG'])
# df['ExerciseAngina'] = labelEncoder.fit_transform(df['ExerciseAngina'])
# df['ST_Slope'] = labelEncoder.fit_transform(df['ST_Slope'])

# # corelasyon ısı mapi
# plt.figure(figsize=(12,8))
# sns.heatmap(df.corr(),annot=True,cmap='coolwarm',fmt='.2f')
# plt.title('Correlation Heat Map')
# plt.show()

# # kalp krizi görülme olasılığı
# plt.figure(figsize=(6,6))
# sns.countplot(x='HeartDisease',data=df)
# plt.title('Heart Disease Incidence Rates')
# plt.show()
