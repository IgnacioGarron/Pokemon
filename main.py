####### IGNACIO GARRON VEDIA ######
# Python 3.10.3

from collections import defaultdict
import collections
from pickle import TUPLE

def def_value():
    return "No es una opción"

## Definición funciones ##

def orden_segun(tipo, criterio):
    lista=[]
    orden=[]
    if tipo in tipos_de_pokemon:
        set1=set(pokemon_por_tipo[tipo][0])
        set2=set(pokemon_por_tipo[tipo][1])
        set3=set1.union(set2)
        for id in set3:
            lista.append(info_pokemon[id])
        if criterio=="HP":
            lista=sorted(lista,reverse = True, key=lambda lista: lista[1])
        elif criterio=="Ataque":
            lista=sorted(lista,reverse = True, key=lambda lista: lista[2])
        elif criterio=="Defensa":
            lista=sorted(lista,reverse = True, key=lambda lista: lista[3])
        elif criterio=="Generacion":
            lista=sorted(lista,reverse = True, key=lambda lista: lista[4])
        for i in lista:
            orden.append(i[0])
        return orden



def estadisticas(tipo, criterio):
    lista=[]
  #  datosF={'Máximo':[],'Mínimo':[],'Promedio':[]}
    if tipo in tipos_de_pokemon:
        set1=set(pokemon_por_tipo[tipo][0])
        set2=set(pokemon_por_tipo[tipo][1])
        set3=set1.union(set2)
        for id in set3:
            lista.append(info_pokemon[id])
        if criterio=="HP":
            lista=sorted(lista,reverse = True, key=lambda lista: lista[1])
            datos=list(zip(*lista))[1]
        elif criterio=="Ataque":
            lista=sorted(lista,reverse = True, key=lambda lista: lista[2])
            datos=list(zip(*lista))[2]
        elif criterio=="Defensa":
            lista=sorted(lista,reverse = True, key=lambda lista: lista[3])
            datos=list(zip(*lista))[3]
        elif criterio=="Gedneracion":
            lista=sorted(lista,reverse = True, key=lambda lista: lista[4])
            datos=list(zip(*lista))[4]
        datos=list(datos)
        sum=datos[0]
        max=datos[0]
        min=datos[0]
        for i in range(0,len(datos)-1):
            sum+=datos[i+1]
            if min>datos[i+1]:
                min=datos[i+1]
            if max<datos[i+1]:
                max=datos[i+1]
        mean=round(sum/len(datos),2)
        datosF=dict()
        datosF={'max':max,'min':min,'prom':mean}
        return datosF




def tipo_segun_nombre(nombre):
    archivo=open("pokemon.csv",'r')
    lineas=archivo.readlines()
    lineas.pop(0)
    archivo.close()
    lista=[]
    tipo_nombre=dict()
    for linea in lineas:
        linea=linea.split(sep=",")
        linea[6]=linea[6].rstrip('\n')
        linea[2]=linea[2].rsplit(sep=';')
        tipo_nombre[linea[1]]=(linea[2][0],linea[2][1])
    return tipo_nombre[nombre]

## Lectura archivo y definicion estructuras ##


# tipos_de_pokemon
archivo=open("pokemon.csv",'r')
lineas=archivo.readlines()
lineas.pop(0)
archivo.close()
tipo1=set()
tipo2=set()
for linea in lineas:
    linea=linea.split(sep=",")
    tipo1.add(linea[2].rsplit(sep=';')[0])
    tipo2.add(linea[2].rsplit(sep=';')[1])
tipos_de_pokemon=tipo1 | tipo2
tipos_de_pokemon.remove("")

# pokemon_por_tipo
archivo = open("pokemon.csv", 'r')
lineas = archivo.readlines()
lineas.pop(0)
archivo.close()
pokemon_por_tipo1=collections.defaultdict(list)
pokemon_por_tipo2=collections.defaultdict(list)
for linea in lineas:
    linea=linea.split(sep=",")
    linea[2]=(linea[2].split(';'))
    pokemon_por_tipo1[linea[2][0]].append(str(linea[0]))
    pokemon_por_tipo2[linea[2][1]].append(str(linea[0]))
pokemon_por_tipo={}
for k in pokemon_por_tipo1.keys():
    pokemon_por_tipo[k]=[pokemon_por_tipo1[k],pokemon_por_tipo2[k]]


# info_pokemon
archivo=open("pokemon.csv",'r')
lineas=archivo.readlines()
lineas.pop(0)
archivo.close()
info_pokemon=dict()
lista=[]
for linea in lineas:
    linea=linea.split(sep=",")
    linea[6]=linea[6].rstrip('\n')
    linea.pop(2)
    for i in range(2,len(linea)):
        linea[i]=float(linea[i])
    info_pokemon[linea[0]]=tuple(linea[1:6])


## Menu flujo principal ##

acciones = defaultdict(def_value)
acciones["1"] = "orden segun"
acciones["2"] = "estadisticas"
acciones["3"] = "encontrar tipo"
acciones["4"] = "revisar"
acciones["0"] = "salir"

continuar = True
while continuar:
    
    print('''
¿Que desea hacer?

1.- Ordenar segun criterio
2.- Obtener estadísticas
3.- Saber el tipo de un pokemon
4.- Revisar Estructuras
0.- Salir
    ''')

    accion = input()
    accion = acciones[accion]

    if accion == "orden segun":
        tipo = input()
        criterio = input()

        orden = orden_segun(tipo, criterio)

        print(f"Ordenando pokemon de tipo {tipo} segun {criterio}:")
        for elem in orden:
            print(f"  - {elem}")

    elif accion == "estadisticas":
        tipo = input()
        criterio = input()

        datos = estadisticas(tipo, criterio)

        print(f"Informacion de {criterio} en pokemon de tipo {tipo}")
        print(f"  - Máximo: {datos['max']}")
        print(f"  - Mínimo: {datos['min']}")
        print(f"  - Promedio: {round(datos['prom'],1)}")

    elif accion == "encontrar tipo":

        nombre = input()

        tipos = tipo_segun_nombre(nombre)
        print(f"El tipo principal de {nombre} es {tipos[0]}")

        if tipos[1] == "":
            print(f"{nombre} no tiene tipo secundario")
        else:
            print(f"El tipo secundario de {nombre} es {tipos[1]}")

    elif accion == "revisar":
        try:
            print("Tipos Encontrados:")
            for tipo in sorted(list(tipos_de_pokemon)):
                print(f"  - {tipo}")

            print("")

            p = pokemon_por_tipo["Electric"]
            print(f"Revisando Primarios: {'25' in p[0]}")
            print(f"Revisando Secundarios: {'170' in p[1]}")

            print("")

            print("Pokemon Ejemplo:")
            i = info_pokemon["25"]
            esta = "Electric" in i
            print(f"  - ID: 25")
            print(f"  - Nombre: {i[0]}")
            print(f"  - Esta Tipo: {esta}")
        except NameError:
            print("Esta parte no se puede ejecutar ya que aún no has definido todas las estructuras")
            

    elif accion == "salir":
        continuar = False

    else:
        print(accion)