#Programa que dependiendo de la cantidad de preoducto que ingrese un usuario realice un descuento 
#si la venta supera los 100 descuento del 10%
#si la venta supera los 200 descuento del 20%
#si la venta supera los 600 descuento del 40%
#el programa se detendra cuando el usuario ingrese un 0

total=0
print("Para saber el monto total a pagar ingrece un 0")
monto=float (input ("Monto de una venta: "))
while monto!=0:
    if monto<0:
        print ("Monto no válido")
    else:
        total+=monto
    monto=float (input ("Monto de una venta: "))

if total > 100:
    total-=total*0.1 #total=total-(total*0.1)
elif total > 200:
    total-=total*0.2 #total=total-(total*0.2)
elif total > 600:
    total-=total*0.4 #total=total-(total*0.4)
print ("Monto total a pagar: " ,total)
