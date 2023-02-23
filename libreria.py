"""
programa que permite al usuario ingresar titulos de libors por teclado 
finalizando el ingreso al leerse el string"*"(asterisco) 
y si usa el string de lingitug que contenga ("/") se termina la linea

"""
digitosEnLaLinea=0
cantLineas=0
titulo=input ("Título del libro: ")
while titulo!="*":
    if titulo == "/":
        cantLineas+=1
        print ("Línea completa. Aparecen", digitosEnLaLinea,"digitos")
        digitosEnLaLinea=0 
    else:
        for caracter in titulo:
            if caracter in "0123456789":
                digitosEnLaLinea+=1
    titulo=input ("Título del libro:")
print ("Fin. se leyeron", cantLineas,"lineas")
