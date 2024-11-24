print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Punto 5---------------")
n = int(input("Allade un numero binario (SOLO 0 Y 1): "))
s = 0
i = 0
while n >= 1:#primero hasemos un bucle while, que se repita mientras n sea mayor o igual que 1
    d=n%10#ahora se hase un variable d, que es el residuo de n dividido entre 10
    n=int(n/10)#ahora se hace un n que es el cociente de n dividido entre 10
    s=s+d*(2**i)#despues se hace una suma de s y d multiplicando por 2 elevado a la i
    i=i+1#por ultimo se suma 1 a i
print("Binario:",n,"Traducion:",s)
#Nota: aaaaaaaaaaaaaaaaaaaaaaaaaaaa me duele la cabeza, muchas matematicas.
print("-------------------------------------")
