# Introducción Pandas
python 3.13.3
## librerias

# Creación de objetos series
```
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

```
# Creación de onjetos serie
s= pd.Series([2,3,4,6,8,10])
print(s)
```
```
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

```