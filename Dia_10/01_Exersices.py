#1
for i in  range(11):
    print(i)
i=0

while i <= 10:
    print(i)
    i+=1

#2
for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1

#3
for i in range(1, 8):
    print('#' * i)

#4
for i in range(8): 
    for j in range(8):  
        print('#', end=' ')  
    print()  

#5
for i in range(11):  
    print(f"{i} x {i} = {i * i}")  

#6
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in lista:
    print(item)

#7
for i in range(101):  
    if i % 2 == 0:  
        print(i)

#8
for i in range(101): 
    if i % 2 != 0: 
        print(i)
        