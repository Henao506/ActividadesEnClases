print("Bienvenido")
pizza=input("Ingrese la opcion de la pizza que desea, v. Vegetariana n.Normal. ")
if pizza== "v":
    print("Acontinuacion ingrese sus ingrediente")
    print("p.Pimiento")
    print("t.Tofu")
    ingre=input()
    if ingre== "p":
        print("Su pizza es vegetariana con pimiento")
        print("Desea ponerle mozzarella y tomate")
        print("A.Si ambas")
        print("N. No ninguna")
        normal=input()
        if normal== "A":
            print("Su pizza es vegetariana con pimiento y tomate y mozarella")
    elif ingre== "t":
        print("Su pizza es vegetariana con tofu")
        print("Desea ponerle mozzarella y tomate")
        print("A.Si ambas")
        print("N. No ninguna")
        normal=input()
        if normal== "A":
            print("Su pizza es vegetariana con tofu y tomate y mozarella")
elif pizza=="n":
    print("Acontinuacion ingrese sus ingrediente")
    print("p.Peperoni")
    print("j.Jamo")
    print("s.Salmon")
    ingri=input()
    if ingri== "p":
         print("Su pizza es normal con Peperoni")
         print("Desea ponerle mozzarella y tomate")
         print("A.Si ambas")
         print("N. No ninguna")
         normal=input()
         if normal== "A":
            print("Su pizza es normal con peperoni y tomate y mozarella")
elif pizza=="n":
     print("Acontinuacion ingrese sus ingrediente")
     print("p.Peperoni")
     print("j.Jamo")
     print("s.Salmon")
     ingri=input()
     if ingri== "j":
         print("Su pizza es normal con Jamon")
         print("Desea ponerle mozzarella y tomate")
         print("A.Si ambas")
         print("N. No ninguna")
         normal=input()
         if normal== "A":
            print("Su pizza es normal con jamon y tomate y mozarella")

     if ingri== "s":
         print("Su pizza es normal con Salmon")
         print("Desea ponerle mozzarella y tomate")
         print("A.Si ambas")
         print("N. No ninguna")
         normal=input()
         if normal== "A":
            print("Su pizza es normal con Salmon y tomate y mozarella")    
           

