print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Punto 8---------------")
c = 0
no = []
while c < 1:#este while te permite ingresar un numero de veces que quieras.
    n = input("ingresa un nombre:")
    no.append(n)#se podria desir que eso permite agregar un elemento a la lista como nuevos valores sin coregir los otros.
    c = int(input("deseas alladir otro numero? 1 si 0 no:"))
print("--De esa lista bamos a buscar los que inisien con la letra de tu elecion--")
l = input("Ingresa una letra:")#Nota: esta parte me carcomio un buen rato la cabesa, porque? simple porque pense que el problema estaba en el ster pero estaba qui abia puesto print ebes de input, hay que divertido.

print(f"-Edades con letra{l}-")
for nom in no:
    if nom.lower().startswith(l):#aqui tambien batalle un poco, yo no sabia que se podian alladir funciones en bucles, pero ahora tengo mas ideas, ademas aprendi que es el startswith lo cual me sera mas util que un tipli x = "un" in union
        print(nom)#en si se repite la forma de imprimir de la anterior.

print("-------------------------------------\n")
#.startswith: esta funcion comprueba si una texto empiesa con un valor especificado. 
# algo hasi como si naso, si Hola amigo, estada cadena comprobaria si inicia con Hola o con H.
