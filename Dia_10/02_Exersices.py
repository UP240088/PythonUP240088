#1
sumatoria = 0  
for i in range(101): 
    sumatoria += i  
print("La suma de todos los números es:", sumatoria)
#2
suma_pares = 0  
suma_impares = 0  

for i in range(101):  
    if i % 2 == 0:  
        suma_pares += i  
    else:  
        suma_impares += i  

print("La suma de todos los números pares es:", suma_pares)
print("La suma de todos los números impares es:", suma_impares)