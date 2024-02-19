import pandas as pd

def DistanciaEuclidiana(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

df = pd.read_csv('iris.csv')
Input = [5.2, 3.1]
distances = []
for index, row in df.iterrows():
    row_data = row.iloc[1:].values
    distance = DistanciaEuclidiana(Input[0], Input[1], row_data[0], row_data[1])
    #print(distance)
    distanceItem = {
        'distance': distance,
        'species': row_data[-1]
    }
    distances.append(distanceItem) 

distances.sort(key=lambda x: x['distance'])

species = []
knn = []
for i in range(len(distances)):
    specie = distances[i]['species']
    species.append(specie)
    count = species.count(specie)
    mostCommonSpecie = max(set(species), key = species.count)
    #print(mostCommonSpecie)
    knn.append(mostCommonSpecie)

#print(knn)
#print(len(knn))
mostCommonSpecie = max(set(knn), key = knn.count)
print(f'los datos que ingresaste son de la especie: {mostCommonSpecie}')
