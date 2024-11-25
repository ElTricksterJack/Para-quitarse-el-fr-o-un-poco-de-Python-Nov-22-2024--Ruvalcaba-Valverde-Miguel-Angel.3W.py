print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Punto 9---------------")
#han escuchado ese cuento griego del que cada ves que intetaba tomar agua el agua baja y cuando tenia hambre intentaba tomar un fruta pero no podia, tan sercas y tan lejos
#hasi me siento.
fra = input("Escribe una frase o un texto: ")
def convol(pa):#creamos una funcion
	pal = pa.lower()#ahora hasemos una variable de rellno que es pa pero que se puede leer en cualquier minuscula o mayuscula
	a = 0
	e = 0
	i = 0
	o = 0
	u = 0
	#lo de arida es para rellenar
	for l in pal:#hasemos un bucle con una variable de relleno
		if l == "a":#aqui si en l esta a se suma un 1 a la variable a 
			a = a + 1
		elif l == "e":
			e = e + 1
		elif l == "i":
			i = i + 1
		elif l== "o":
			o = o + 1
		elif l == "u":
			u = u + 1
	print(f"a: {a}\ne: {e}\ni: {i}\no: {o} \nu: {u}")
convol(fra)	
print("-------------------------------------\n")
