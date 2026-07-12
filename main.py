dicc = {}

balance_personal = 10000
Primer_pin = "1234"

while True:
    print("""
    Bienvendo a este gestionador de cajero automatico

     
    1.- Revisar balance
    2.- transferencia
    3.- Cambiar PIN
    4.- Retirar dinero
    5.- Depositar dinero    
    6- Salir del programa
    


""")
    
    opcion = input("seleccione el numero de la opcion que desea realizar: ")


    match opcion:
        case "1":
         print(f" su balance actual es: {balance_personal:.2f} ")

        case "2":
            deposito = float(input("ingrese la cantidad a transferir: ").strip())
            if deposito > balance_personal:
                print(f"no tu solo tienes {balance_personal} y tu intento de transferencia fue de {deposito}")

            else:
                balance_personal -= deposito
                print(f"deposito hecho correctamente, ese es su balance actual es su cuenta {balance_personal} ")

        
        case "3":
            print("Para cambiar el pin, usted debe ingreser su pin actual")
            Pin = input("ingrese su pin actual:")
            if  Pin == Primer_pin:
                print("Exelente, ahora ya usted puede cambiar su Pin") 
                nuevo_pin = input("ingrese su nuevo pin:")
                Primer_pin = nuevo_pin
                print("su pin ha sido cambiado correctamente")

            else:
                print("Debe ingrese su contraseña correctamente")
                continue
                    


        case "4":
            retiro = float(input("cual es la cantidad que usted desea retirar: "))
            if retiro > balance_personal:
                print("solo puedes depositar de acorde al balence de tu cuenta.")

            else:
                balance_personal -= retiro
                print("Bien, Retirando dinero correctamente.....")


        case "5":
            depositar = int(input("Ingrese el deposito: "))
            balance_personal += depositar
            
            print(f"su balence actual es de:  {balance_personal}")


        case "6":
         print("Gracias por utilizar nuestros servicios... ")
         break