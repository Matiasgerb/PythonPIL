#Str
from pickle import TRUE


a='Esto es una cadena'
b="Esto es una cadena"
print(a,type(a))
print(b,type(b))
c= str(123.44)
print(c,type(c))

#Contando caracteres
print(len(a))
print(a[0:5])
print(a[-1])

#Metodos
print(a.lower())
print(a.upper())
print(len(a.split()))

#List
Lista1=['Hola', 4, 2.5, TRUE, [1,2,3,4] ,('a','b')]
print(Lista1)
print(type(Lista1))
print(len(Lista1))
print(Lista1[2])

varUno=Lista1[4]
print(varUno)
print(type(varUno))

#Metodos
print(Lista1.append('Lista'))
print(Lista1)

print(Lista1.index(('a', 'b')))

print(Lista1.insert(1, 5))
print(Lista1)

#Diccionario
Usuario ={
        'nombre' : 'Matias',
        'apellido' : 'Gerbaldo',
        'edad' : 22,
        'hobbies' : ['Musica'],
        'mascotas' : True
}
print(Usuario)
print(['mascotas'])
print(len(Usuario))

#Metodos
print(Usuario.get('Puesto', 'No encontrado'))
print(Usuario.get('edad', 'Encontrado'))

keysUsuario = list(Usuario.keys())
print(type(keysUsuario))
print(Usuario.get(keysUsuario[0]))

print(Usuario.values())