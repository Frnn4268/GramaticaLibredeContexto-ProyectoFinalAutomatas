import random as rd #Import de random para obtener el valor random de nuestras funciones

#Reglas de la gramática
Reglas_Gramatica = {
    'S':[ 
        ['El', 'A', 'B']
    ], 

    'A':[ 
        ['Animal', 'gato'],
        ['Animal', 'perro'],
        ['Animal', 'pájaro'],
        ['Animal', 'elefante'],
        ['Animal', 'mono'],
        ['Animal', 'caballo'],
        ['Animal','cabra']
    ],

    'B':[ 
        ['mauya', 'C'],
        ['ladra', 'C'],
        ['canta', 'C'],
        ['gruñe', 'C'],
        ['relincha', 'C']
    ],

    'Animal': [
        ['pequeño'],
        ['gran'],
        ['bello'],
        ['feo'],
        ['feliz']
    ],

    'C': [
        ['y', 'el', 'A', 'D']
    ],

    'D': [
        ['toma leche'],
        ['come carne'],
        ['come semillas'],
        ['come pasto'],
        ['come frutas'],
        ['toma agua'],
        ['come verduras']
    ]
}

#Usar el parse para anlizar cualquier lista de strings e insertaros en un lugar de la lista
def generar_Palabra(palabra):
    for item in palabra:
        if isinstance(item, list):
            for subitem in generar_Palabra(item):
                yield subitem
        else:
            yield item       

#Nuestra funcion para añadir otra regla a la gramática
def añadir_Palabra(inicio):
    for elementos in inicio:
        if elementos in Reglas_Gramatica:
            loc = inicio.index(elementos)
            inicio[loc] = rd.choice(Reglas_Gramatica[elementos])
        result = [item for item in generar_Palabra(inicio)]

    for item in result:
        if not isinstance(item, list):
            if item in Reglas_Gramatica:
                result = añadir_Palabra(result)
                
    return result

def to_string(result):
    return ' '.join(result)

#Inicio de las impresiones
print('')
print('Gramática Libre de Contexto - Autómatas y Lenguajes Formales')
print('')
print('Estado incial: ')
result = ['S']
print(result) #Imprimimos nuestro inicio
result = añadir_Palabra(result) #Agregamos más datos a nuestra lista de inicio
Palabra_Completa = to_string(result)
print('')
print('Palabra generada: ' + Palabra_Completa) #Imprimimos el resultado final
print('')