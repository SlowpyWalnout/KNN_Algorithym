# KNN_Algorithym
Este es el repositorio para la tarea de bigdata donde tenemos que hacer el algoritmo visto en clase en python.
## Pasos del algoritmo KNN
1. Conseguir las distancias euclidianas entre los valores ingresados y los valores de cada elemento comparado.
2. Ordenar de menor a menor las distancias obtenidas.
3. Estimación según el número de vecinos en el ordenamiento.
## Datos importantes sobre el código
- Los datos que querramos clasificar los tenemos que ingresar manualmente en la lista "Input" en el orden de las columnas del dataset.
- está por default el algoritmo para leer y clasificar de acuerdo a las primeras dos columnas del dataset "SepalLenght" y "SepalWidth", si queremos clasificar con los demás datos del dataset, es decir por ejemplo utilizando las primeras tres columnas ("SepalLenght", "SepalWidth" y el "PetalLenght") o las 4 columnas ("SepalLenght", "SepalWidth", "PetalLenght" y el "PetalWidth") ocupamos ingresar los datos faltantes a la lista de entrada "Input" y elegir bien la función de acuerdo a la dimensión de datos que estamos usando.
- Hay un problema con el código y es que cuando se llega a la misma cantidad de especies en la lista "knn" es decir por ejemplo que hay 10 de una especie y 10 de otra especie, el programa reconoce como la especie más repetida a la primera especie en llegar al valor de 10.
