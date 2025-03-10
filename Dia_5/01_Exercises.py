#1
empty_list = list()
#2
lista1 = ['Pizza','Hanburgesa','Tacos','Carnitas','Flautas','Torta Cubana','Menudo']
print(lista1)
#3
print(len(lista1))
#4
print(lista1[0])
print(lista1[3])
print(lista1[6])
#5
mixed_data_types = ['Jose Sebastian Torres Reyes','18','1.87','Single','El Tule']
#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
#7
print(it_companies)
#8
Numero_de_Emrpesas = 7
print("Hay",Numero_de_Emrpesas,"Empresas")
#9
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2] if len(it_companies) % 2 != 0 else it_companies[len(it_companies) // 2 - 1]
last_company = it_companies[-1]
print("Primera empresa:", first_company)
print("Empresa del medio:", middle_company)
print("Última empresa:", last_company)
#10
it_companies1 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
#7
it_companies1[2] = "Truper"
print(  it_companies1)
#11
it_companies2 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
#7
it_companies2.append('Truper')
print(it_companies2)
#12
it_companies3 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
new_company = "Truper"
middle_index = len(it_companies3) // 2
it_companies3.insert(middle_index, new_company)
print(it_companies3)
#13
it_companies4 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
for i in range(len(it_companies4)):
    if it_companies4[i] != "IBM":
        it_companies4[i] = it_companies4[i].upper()
print(it_companies4)
#14
resultado = ';  '.join(it_companies)
print(resultado)
#15
Empresas = input("Ingresa el nombre de la empresa para verificar si existe: ")
if Empresas in it_companies:
    print(f"{Empresas} Existe en la lista de empresas.")
else:
    print(f"{Empresas} No existe en la lista de empresas")
#16
it_companies.sort()
print("Lista de empresas ordenada:", it_companies)
#17
it_companies1.sort(reverse=True)
it_companies1.reverse()
print("Lista de empresas en orden descendente:", it_companies1)
#18
primeras_companies = it_companies[3:]
print(primeras_companies)
#19
ultimas_companies = it_companies[:-3]
print(ultimas_companies)
#20
del it_companies [1]
print(it_companies)
#21
del it_companies[0]
print(it_companies)
#22
del it_companies[4]
print(it_companies)
#23
del it_companies[5]
#24
it_companies.clear()
print(it_companies)
#25
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end =['Node','Express', 'MongoDB']
print(front_end)
print(back_end)
#27
join_stack = front_end + back_end
print(join_stack)

full_stack = join_stack.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)
print("")