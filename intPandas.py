import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
# Creación de onjetos serie
s= pd.Series([2,3,4,6,8,10])
print(s)

# Creación de un objeto Serie inicializando con un diccionario de python
altura={"Santiago":180,"marcelo":172,"Luis":174,"Alejandra":160}
s=pd.Series(altura)
print(s)
"""
Creación de un objeto series inicializandolo con algunos
de los elementos de un diccionario de python 
"""
altura={"Santiago":180,"marcelo":172,"Luis":174,"Alejandra":160}
s=pd.Series(altura,index=["marcelo","Luis"])
print(s)

#Creación de un objeto Series inicializandnlo con un escalar
s=pd.Series(34,["test1","test2","test3"])
print(s)

# Acceso a los Elementos de un objeto Series
#cada elelmento de objeto series tiene un identificador unico
s=pd.Series([2,4,6,8],index=["num2","num3","num4","num5"])
print(s)
# Accediendo al tercer elemento del objeto
print(s["num3"])
# aceder por la posición 
print(s.iloc[2])
print(s.loc["num3"])
#accediendo al segundo y tercer elemento por posición
print(s.iloc[2:4])

# Operaciones aritméticas con series
#sumar
print(f"suma {np.sum(s)}")
print("suma", np.sum(s))

# creación de un objeto series denominado temperaturas
temperaturas=pd.Series([4.4,5.1,6.1,6.2,6.1,6.1,5.2,4.7,4.1,3.9])
s=pd.Series(temperaturas,name="Temperaturas")
print(s)
s.plot()
#plt.show()

#Creación de un DataFrame
personas={ "peso":pd.Series([90,80,70,60],["Santiago","marcelo","Luis","Alejandra"]),
          "altura":pd.Series({"Santiago":180,"marcelo":172,"Luis":174,"Alejandra":160}),
          "hijos":pd.Series([2,3],["Luis","marcelo"])
          }
df =pd.DataFrame(personas)
print(df)
df=pd.DataFrame(
    personas,
    columns=["altura","peso"],
    index=["Santiago","Luis","marcelo"] )
print(df)
#Acceso a los elementos
print(df["peso"])
#combinar metodos
print((df["peso"]>=60) & (df["peso"]<80))
print(df.iloc[1:3])
#consultas avanzadas
df4=df.query("altura >= 170 and peso >70")
print(df)
#copiar un dataframe
df_copy = df.copy()
#añadir una nueva columna
df_copy["Cumpleaños"]=[1990,1978,1989]
print(df_copy)
#añadir una columna calculada
df_copy["años"]=2025- df_copy["Cumpleaños"]
print(df_copy)
#añadir una nueca columna creando una Dataframe nuevo 
df_mod=df_copy.assign(mascotas=[1,3,0])
print(df_mod)
#Eliminar una columna
del df_mod["peso"]
print(df_mod)