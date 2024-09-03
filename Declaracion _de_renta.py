print("Bienvenido")
ingreso=int(input("Ingrese sus ingresos anuales: "))
if ingreso<1000000:
    print("Su impositivo es de 5%")
elif ingreso>=1000000 and ingreso<2000000:
    print("Su impositivo es de 15%")
elif ingreso>=20000000 and ingreso<3500000:
    print("Su impositivo es de 20%")
elif ingreso>=3500000 and ingreso < 6000000:
    print("Su impositivo es de 30%")
elif ingreso>=6000000:
    print("Su impositivo es de 45%")                