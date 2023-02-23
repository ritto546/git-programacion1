"""
Se desea conocer el valor de un boleto, según el país de destino. introduzca 
el destino a donde desea ir. Son 3 destinos a saber: Francia, Uruguay y españa. 
Una vez seleccionado el país, deberá indicar con selección doble que tipo de vuelo desea,
si clase 1 o clase 2, donde el valor de la clase 1 PREFERENCIAL es de 1600  y 
la clase 2 sera ECONOMICA es de 1000, dependiendo de los días de estancia se le aplicara un descuento de 10% o 30%
"""

print("ingrece el pais al que viaja despues ingrese la clase del boleto si es (1) o (2) ")
descuento=0
Pais = input("ingrese el país a viajar: ")
match Pais:
    case "francia":
        clasevuelo = int(input("en que clase esta "))
        if clasevuelo == 1: 
            print ("el boleto es de clase preferencial ")
            dias_de_estancia = float (input ("Ingresa el valor de dias de estancia: "))
            subtotal=dias_de_estancia*1600
            if  dias_de_estancia > 7:
                descuento = subtotal*0.3
                precio_del_pasaje = subtotal-descuento
                print ("Valor de descuento: ",descuento)
                print ("Valor de precio del pasaje: ",precio_del_pasaje)
                print ("Valor de subtotal: ",subtotal)
            else:
                descuento = subtotal*0.1
                precio_del_pasaje = subtotal-descuento
                print ("Valor de descuento: ",descuento)
                print ("Valor de precio del pasaje: ",precio_del_pasaje)
                print ("Valor de subtotal: ",subtotal)

        else:
            print ("el boleto es de clase económica ")
            dias_de_estancia = float (input ("Ingresa el valor de dias de estancia: "))
            subtotal=dias_de_estancia*1000
            if  dias_de_estancia > 7:
                descuento = subtotal*0.3
                precio_del_pasaje = subtotal-descuento
                print ("Valor de descuento: ",descuento)
                print ("Valor de precio del pasaje: ",precio_del_pasaje)
                print ("Valor de subtotal: ",subtotal)
            else:
                descuento = subtotal*0.1
                precio_del_pasaje = subtotal-descuento
                print ("Valor de descuento: ",descuento)
                print ("Valor de precio del pasaje: ",precio_del_pasaje)
                print ("Valor de subtotal: ",subtotal)
    case "españa":
        clasevuelo = int(input("en que clase esta "))
        if clasevuelo == 1: 
            print ("el boleto es de clase preferencial ")
            dias_de_estancia = float (input ("Ingresa el valor de dias de estancia: "))
            subtotal=dias_de_estancia*1600
            if  dias_de_estancia > 7:
                descuento = subtotal*0.3
                precio_del_pasaje = subtotal-descuento
                print ("Valor de descuento: ",descuento)
                print ("Valor de precio del pasaje: ",precio_del_pasaje)
                print ("Valor de subtotal: ",subtotal)
            else:
                descuento = subtotal*0.1
                precio_del_pasaje = subtotal-descuento
                print ("Valor de descuento: ",descuento)
                print ("Valor de precio del pasaje: ",precio_del_pasaje)
                print ("Valor de subtotal: ",subtotal)

        else:
            print ("el boleto es de clase económica ")
            dias_de_estancia = float (input ("Ingresa el valor de dias de estancia: "))
            subtotal=dias_de_estancia*1000
            if  dias_de_estancia > 7:
                descuento = subtotal*0.3
                precio_del_pasaje = subtotal-descuento
                print ("Valor de descuento: ",descuento)
                print ("Valor de precio del pasaje: ",precio_del_pasaje)
                print ("Valor de subtotal: ",subtotal)
            else:
                descuento = subtotal*0.1
                precio_del_pasaje = subtotal-descuento
                print ("Valor de descuento: ",descuento)
                print ("Valor de precio del pasaje: ",precio_del_pasaje)
                print ("Valor de subtotal: ",subtotal)
    case "uruguai":
        clasevuelo = int(input("en que clase esta "))
        if clasevuelo == 1: 
            print ("el boleto es de clase preferencial ")
            dias_de_estancia = float (input ("Ingresa el valor de dias de estancia: "))
            subtotal=dias_de_estancia*1600
            if  dias_de_estancia > 7:
                descuento = subtotal*0.3
                precio_del_pasaje = subtotal-descuento
                print ("Valor de descuento: ",descuento)
                print ("Valor de precio del pasaje: ",precio_del_pasaje)
                print ("Valor de subtotal: ",subtotal)
            else:
                descuento = subtotal*0.1
                precio_del_pasaje = subtotal-descuento
                print ("Valor de descuento: ",descuento)
                print ("Valor de precio del pasaje: ",precio_del_pasaje)
                print ("Valor de subtotal: ",subtotal)

        else:
            print ("el boleto es de clase económica ")
            dias_de_estancia = float (input ("Ingresa el valor de dias de estancia: "))
            subtotal=dias_de_estancia*1000
            if  dias_de_estancia > 7:
                descuento = subtotal*0.3
                precio_del_pasaje = subtotal-descuento
                print ("Valor de descuento: ",descuento)
                print ("Valor de precio del pasaje: ",precio_del_pasaje)
                print ("Valor de subtotal: ",subtotal)
            else:
                descuento = subtotal*0.1
                precio_del_pasaje = subtotal-descuento
                print ("Valor de descuento: ",descuento)
                print ("Valor de precio del pasaje: ",precio_del_pasaje)
                print ("Valor de subtotal: ",subtotal)
    case _:
        print("no tenemos registro de su vuelo ")
