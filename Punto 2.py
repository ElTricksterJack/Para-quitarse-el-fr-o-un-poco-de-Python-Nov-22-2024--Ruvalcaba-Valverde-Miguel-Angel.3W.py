print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Punto 2---------------")
c = 0
nu = []
while c < 1:#este while te permite ingresar un numero de veces que quieras.
    n = input("ingresa una palabra:")
    nu.append(n)#se podria desir que eso permite agregar un elemento a la lista como nuevos valores sin coregir los otros.
    c = int(input("deseas alladir otro numero? 1 si 0 no:"))
print("Lista:",nu)#mostramos la lista
def may(n):
    may=max(n, key=len)#ahora la palabra mas larga buscando entre la lista ya que el len cuenta los elementos 1 por uno y el max saca el maximo
    print("la palabra mas larga es:",may)
may(nu)
print("-------------------------------------")
print("Resultado: se puede crear un histograma fasilente.\n")
