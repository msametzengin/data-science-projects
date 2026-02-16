import pandas as pd
from sklearn.cluster import KMeans #to cluster
import numpy as np

def bloodPressureRelief(bloodPressure):
    try:
        systolic,diastolic = bloodPressure.split('/')
        return int(systolic),int(diastolic)
    except Exception as error:
        return np.nan,np.nan

def main():
    # get excel data
    data = pd.read_excel('tansiyon.xlsx')

    data[['morning_systolic','morning_diastolic']] = data['Morning Blood Pressure'].apply(lambda x: pd.Series(bloodPressureRelief(x)))
    data[['evening_systolic','evening_diastolic']] = data['Evening Blood Pressure'].apply(lambda x: pd.Series(bloodPressureRelief(x)))

    features = data[['morning_systolic','morning_diastolic','evening_systolic','evening_diastolic']].dropna()
    kmeans = KMeans(n_clusters=2,random_state=42)
    clusters = kmeans.fit_predict(features)
    features['cluster'] = clusters # We are adding the data we trained with.

    clustersAverage = features.groupby('cluster').mean()[['morning_systolic','evening_systolic']]
    riskyCluster = clustersAverage.mean(axis=1).idxmax()

    features['risky'] = features['cluster'].apply(lambda x:'Risky' if x == riskyCluster else 'Normal')

    # Embed the data into the original data.
    data = data.join(features['risky'])
    numberofRisky = data['risky'].value_counts().get('Risky',0)
    total = data['risky'].count()
    generalRisk = 'High blood pressure / Heart risk' if numberofRisky >= 0.5 else 'Normal'

    data.to_excel('tansiyon_sonuc.xlsx', index=False)
    
    print('Daily Risk Situation')
    print(data[['Date','risky']])
    print('\nGeneral Assesment: ',generalRisk)

if __name__ == '__main__':
        main()