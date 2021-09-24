# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




clave = input("Digite su clave:")
tipo = input("Tipo de cuenta 1-Corriente 2-Ahorros:")




def montox():
    monto = int(input("Digite el monto a retirar"))


    if monto < 100000:

        print("Su disponible es 200,000")

    else:

        print("El monto es superior a 100,000 diarios : ")
        return montox()
montox()

















