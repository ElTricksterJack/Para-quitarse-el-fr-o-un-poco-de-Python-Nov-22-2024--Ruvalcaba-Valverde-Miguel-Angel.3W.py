print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Punto 3---------------")
c = 0
nu = []
while c < 1:#este while te permite ingresar un numero de veces que quieras.
    n = input("ingresa una palabra:")
    nu.append(n)#se podria desir que eso permite agregar un elemento a la lista como nuevos valores sin coregir los otros.
    c = int(input("deseas alladir otro numero? 1 si 0 no:"))
print("--Se fitraran las palabras con una menor cantidad de carapteres que tu eligas--")
e=int(input("numero de carapteres mini para filtrar las palabras:"))

def fipal(lp, n):#abrir funcion
    return [pa for pa in lp if len(pa) > n]#esta parte hase una lista con los elementos que cumplan la condicion de la funcion, como ejemplo
print(fipal(nu,e))#mostrar el resultado de la funcion
print("-------------------------------------")
print("Resultado: se puede crear un histograma fasilente.\n")
