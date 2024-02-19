import pandas as pd #importamos pandas para leer el dataset

#funcion para calcular la distancia euclidiana
def DistanciaEuclidiana(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

#leemos el dataset
df = pd.read_csv('iris.csv')

#ingresamos los datos que queremos clasificar
Input = [5.2, 3.1]

#calculamos la distancia euclidiana de los datos ingresados con los datos del dataset
distances = [] #en esta lista guardamos las distancias y la especie en forma de diccionario

#comenzamos a recorrer el dataset de fila en fila 
for index, row in df.iterrows():
    #recolectamos la informacion de la fila
    row_data = row.iloc[1:].values
    #calculamos la distancia euclidiana, en este caso trabajamos sobre la informacion de las columnas 1 y 2 agregadas en row_data
    distance = DistanciaEuclidiana(Input[0], Input[1], row_data[0], row_data[1])
    #guardamos la distancia y la especie en un diccionario
    distanceItem = {
        'distance': distance,
        'species': row_data[-1]
    }
    #agregamos el diccionario a la lista
    distances.append(distanceItem) 
#ordenamos(rankeamos las distancias de menor a mayor)
distances.sort(key=lambda x: x['distance'])

#obtenemos las especies de los k vecinos mas cercanos
species = [] #esta lista es para guardar las especies que han salido hasta el momento en el ciclo
knn = []#en esta lista guardamos la especie que mas se repite en la lista species

#recorremos la lista de distancias
for i in range(len(distances)): 
    #asignamos la especie a una variable
    specie = distances[i]['species']
    #agregamos la especie a la lista species
    species.append(specie)
    #contamos cuantas veces se repite la especie en la lista species (esto era para depurar)
        #count = species.count(specie)
        #print(f'{specie} aparece {count} veces')
    #obtenemos la especie que mas se repite en la lista species
    mostCommonSpecie = max(set(species), key = species.count)
    #agregamos la especie mas repetida a la lista knn
    knn.append(mostCommonSpecie)

#obtenemos la especie que mas se repite en la lista knn    
mostCommonSpecie = max(set(knn), key = knn.count)
#imprimimos la especie mas repetida en la lista knn
print(f'los datos que ingresaste son de la especie: {mostCommonSpecie}')
