#1
age = int(input("Ingresa tu edad: "))
if age >= 18:
    print("Tienes la edad necesaria para aprender a conducir.")
else:
    years_left = 18 - age
    print(f"Necesitas {years_left} mas para aprender a conducir.")
#2
mi_edad = int(input("Ingresar mi edad: "))
tu_edad = int(input("Ingresa tu edad: "))
if mi_edad > tu_edad:
    edad_diff = mi_edad - tu_edad
    if edad_diff == 1:
        print(f"Yo soy mayor por {edad_diff} años.")
    else:
        print(f"Yo soy mayor por {edad_diff} años.")
elif mi_edad < tu_edad:
    edad_diff = tu_edad - mi_edad
    if edad_diff == 1:
        print(f"Tu eres mayor por {edad_diff} años.")
    else:
        print(f"Tu eres mayor por {edad_diff} años.")
else:
    print("Somos de la misma edad")

#3
A= input("Ingresa el primer numero(A):")  
B= input("Ingresa el segundo numero(B:)") 

if A>B :
   print(f"{A} es mayor que {B}")
elif A<B:
    print(f"{A} es menor que {B}")
else:
    print(f"{A} y {B} son iguales")    

