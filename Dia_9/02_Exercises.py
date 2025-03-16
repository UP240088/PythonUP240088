#1
Calificacion= int(input("Ingresa el puntaje:"))
if  80<=  Calificacion <=100:
    puntaje= 'A'
elif 70 <= Calificacion <= 79:
    puntaje='B'
elif 60 <= Calificacion <= 69:
    puntaje='C'
elif 50 <= Calificacion <= 59:
    puntaje='D'
elif 0 <= Calificacion <= 49:
    puntaje='F'                    
else:
    puntaje='Puntaje Invalido'

print(f'Tu grado es',puntaje)  
#2
month = input("Ingresa el mes: ").capitalize()

if month in ['Septiembre', 'Octubre', 'Noviembre']:
    season = 'Otoño'
elif month in ['Diciembre', 'Enero', 'Febrero']:
    season = 'Invierno'
elif month in ['Marzo', 'Abril', 'Mayo']:
    season = 'Primavera'
elif month in ['Junio', 'Julio', 'Agosto']:
    season = 'Verano'
else:
    season = 'Mes Invalido'

print(f"La temporada es {month} es: {season}")
#3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_to_check = input("Ingresa el nombre de la fruta: ").lower()
if fruit_to_check in fruits:
    print("Esa fruta ya existe en la lista")
else:
   
    fruits.append(fruit_to_check)
    print(f"Lista modificada: {fruits}")

     


