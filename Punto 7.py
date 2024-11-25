print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Punto 7---------------")
nu = ()
for _ in range(10):#como son 10 edades solo se tenian que repetir 10 veces, por eso el for y range(10)
    n = int((input("ingresa un numero:")))
    nu += (n, )#Una tupla no funciona igual que una lista.

print("-Edades mayores a 20 años-")
for ed in nu:#aqui creamos usamos una varaible invetada, que se repetira 10 veses segun la tupla
    if ed > 20:#ahora cada elemento separado se impimira en pantalla si es mayor que 20
        print(ed)
print("-------------------------------------\n")
