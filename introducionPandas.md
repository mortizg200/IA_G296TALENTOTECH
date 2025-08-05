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
