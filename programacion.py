import random

numeroAleatorio = random.randint(0,10)

def intro():
    print("*"*40)
    print(" "*10, "ADVINA EL NUMERO", " "*10)
    print("*"*40)
    
def juego():
    intentos = 0
    while True:
        NumUsuario = int(input("Inserta un numero entre el 1 y el 10:"))
        if NumUsuario > numeroAleatorio:
            intentos += 1
            print("El nùmero a acertar es màs pequeño, intentalo de nuevo.")
        elif NumUsuario < numeroAleatorio:
            intentos += 1
            print("El nùmero a acertar es màs grande, intentalo de nuevo.")
        else:
            intentos += 1
            print(f"bingo acertaste el numero, era el {numeroAleatorio}, en el intento numero{intentos}")
            input("presiona intro para salir....")
            break
        
intro()
juego()

