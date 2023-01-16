import random

numeroAleatorio = random.randint(0,10)

def intro():
    print("*"*40)
    print(" "*10, "ADVINA EL NUMERO", " "*10)
    print("*"*40)
    
def juego():
    intentos = 0
    while True:
        NumUsuario = int(input("Inserte un numero entre el 1 y el 10:"))
        if NumUsuario > numeroAleatorio:
            intentos += 1
            print("El numero a acertar es mas pequeño, intentalo de nuevo")
        elif NumUsuario < numeroAleatorio:
            intentos += 1
            print("El numero a acertar es mas grande, intentalo de nuevo")
        else:
            intentos +=1
            print(f"bingo acertaste el numero, era el numero {numeroAleatorio}, en el intento numero{intentos}")
            break

intro()
juego()
