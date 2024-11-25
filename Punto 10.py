print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Punto 10---------------")
def añodis(año):
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:#esta formula fue sacada de la pagina original 
        #de microsoft, ya que la original tenia un margen de error, ya que cuando multiplicaba por 2012 no desia que era bisiesto.
        print("Es bisiesto")
        return True
    else:
        print("No es bisiesto")
        return False

a = int(input("Ingresa un año: "))
añodis(a)
#Nota: en este momento estoy emosionado, porque porque quiero descargar mas capitulos de undead unluck y majo taisen, 
#desde que llore al ver el final del racrarok y el inicio del nuevo bucle me emocione, y la pelea de majo taise, la numero 1 me emosiono, si me disculpan boy descargar capitulos.
#chaito
print("-------------------------------------\n")
