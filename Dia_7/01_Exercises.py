#1
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
Numero_de_elementos = len(it_companies)
print('El numero de elementos de it_companies es:',Numero_de_elementos)
#2
it_companies1 =  {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon'}
it_companies1.add("Twitter")
print("El conjunto actualizado es:", it_companies1)
#3
it_companies2 = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon'}
it_companies2.update({"Twitter", "LinkedIn", "Netflix", "Tesla"})
print("El conjunto actualizado es:",it_companies2)
#4
it_companies3 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
it_companies3.remove("Google")
print("El conjunto actualizado es:",it_companies3)
#5 What is the difference between remove and discard
#remove(): Genera un KeyError si el elemento no se encuentra en el conjunto.
#discard(): No genera error si el elemento no se encuentra en el conjunto.



