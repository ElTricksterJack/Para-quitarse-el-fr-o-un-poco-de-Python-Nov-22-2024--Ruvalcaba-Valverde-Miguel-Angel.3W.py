print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Punto 4-MODE---------------")
p = input("Inserte una palabra o texto: ")
mai = sum(1 for c in p if c.islower())
may = sum(1 for c in p if c.isupper())
print("Tu frase o texto tiene",may,"mayusculas.")
print("Tu frase o texto tiene",mai,"Minusculas")
e = p.casefold()#como tal ete trasforma todas a minusculas
o = p.capitalize()#limita
inv = p.swapcase()#este ivierte
print(e)
print("/-----------------c------------/")
print(o)
print("/-----------------------------/")
print(inv)
print("-------------------------------------")
#Nota: .casefold() los combierte a minuscula como el ejemplo extra que puse
