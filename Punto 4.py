print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Punto 4---------------")
p = input("Inserte una palabra o texto: ")
may = sum(1 for c in p if c.isupper())
#el esta parte hase un buclie for que lee cada caracter y si se topa con una mayuscula la suma.
print("Tu frase o texto tiene",may,"mayusculas.")
print("-------------------------------------")
