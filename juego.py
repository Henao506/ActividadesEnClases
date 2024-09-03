import random
intentos=2
numA=random.randint(1,5)
print("¡Bienvenido!")
nombre=input("Ingrese su nombre: ")
print("Hola",nombre)
opcion=input("Elija una de las opciones de juego:  a.Numeros, b.Salir: ")
if opcion == "a":
    print("en este juego debes de adivinar un numero")
    numj=int(input("ingrese un numero entre el 1 y el 5: "))
    while intentos>=1 :
        intentos-=1
        if numj<numA:
            print("el numero ingresado es menor que el numero para adivinar: ")
            print(f"te quedan {intentos} intentos")
            numj=int(input("ingrese un numero entre el 1 y el 5: "))
        elif numj>numA:
            print("el numero ingresado es mayor que el numero para adivinar: ")
            print(f"te quedan {intentos} intentos")
            numj=int(input("ingrese un numero entre el 1 y el 5: "))
        elif numj==numA:
                print("has adivinado el numero")
                print("desea seguir jugando?")
                op1=input("b. continuar c. salir: ")
                if op1=="c":
                    print("gracias por jugar")
                    quit()

        if  intentos==0:   
            print("loser perdiste")
            print(f"el numero era{ numA} ")