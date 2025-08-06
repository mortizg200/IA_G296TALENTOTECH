import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset ficticio
datos_estudiantes = {
    "peso": pd.Series([55, 68, 74, 60, 72], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "altura": pd.Series([162, 175, 168, 180, 170], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "promedio": pd.Series([4.5, 3.8, 4.2, 2.9, 3.5], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "edad": pd.Series([17, 18, 17, 19, 18], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"])
}

df = pd.DataFrame(datos_estudiantes)
print(df)

# Crear una Serie con los nombres y alturas de los estudiantes
df =pd.DataFrame(datos_estudiantes)

df4=pd.DataFrame(
    datos_estudiantes,
    columns=["altura"],
    index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"] )
print(df4)

# ¿Cuál es la altura de Daniela?
df5=pd.DataFrame(
    datos_estudiantes,
    columns=["altura"],
    index=["Daniela"] )
print(df5)

#Accede al promedio de calificación de Carlos de 3 formas diferentes:
df6=pd.DataFrame(
    datos_estudiantes,
    columns=["promedio"],
    index=["Carlos"] )
print(df6)

print((df6["promedio"]>=3.8))
#usando loc
promedio_carlos=df.loc['Carlos']['promedio']
print(promedio_carlos)
#usando iloc
#promedio_carlos=df.iloc[1]["promedio"]
#print(promedio_carlos)
promedio_carlos = df.query("index == 'Carlos'")["promedio"]
print(promedio_carlos)

#Filtra a los estudiantes con promedio mayor o igual a 4.0
df7 =pd.DataFrame(datos_estudiantes)
print(df7)
df7=pd.DataFrame(
    datos_estudiantes,
    columns=["promedio"],
    index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"] )
#print(df)
print(df7["promedio"]>=4.0)

#otra forma
estudiantes_mayor4=df.query("promedio >= 4.0")
print(estudiantes_mayor4)
#con loc
estudiantes_mayor4=df.loc[df["promedio"]>=4]
print(estudiantes_mayor4)

#¿Cuántos estudiantes tienen un buen promedio?
promedio_bueno = df.query("promedio >= 4.0")
promedio_bueno = len(promedio_bueno)
print(promedio_bueno)

# Calcular operaciones estadisticas:
estaidisticas=df.describe()
print(estaidisticas)

#agrega una nueva columna que indique si el estudiante es mayor de edad
df["mayor"]=df["edad"]>= 18
print("\n Añadiendo columna de mayor de edad \n", df)

#agregar una columna con el año de nacimiento
df["año_nacimiento"]= 2025-df["edad"]
print("\n Añadiendo columna de cumpleaños \n", df)

# visualiza los promedios de los estudiantes en un grafico
#df["promedio"].plot(kind="bar", title="Promedio de estudiantes")
#plt.xlabel("Estudiante")
#plt.ylabel("Nota promedio")
#plt.show()

#filtra a los estudiantes con una altura entre 165 y 175
alturamay=df.query("altura >= 165 and altura <= 175")
print(alturamay)

#Copia el DataFrame y elimina la columna "peso"
df_copy = df.copy()
del df_copy["peso"]

#Crea un nuevo DataFrame con solo 3 columnas: nombre, edad y año de nacimiento
df2=pd.DataFrame(df,
                 columns=["altura","peso"],
                )
print(df2)