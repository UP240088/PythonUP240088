#1
dog={}

#2
dog['name'] = 'Gordo'  
dog['color'] = 'Brown'  
dog['breed'] = 'Boxer' 
dog['legs'] = 4  
dog['age'] = 5  
print(dog)

#3
student = {}

student['first_name'] = 'Jose'  
student['last_name'] = 'Torres'  
student['gender'] = 'Male'  
student['age'] = 18  
student['marital_status'] = 'Single'  
student['skills'] = ['Python', 'Farmer', 'Machine Learning']  
student['city'] = 'Aguascalientes'
student['address'] = 'El Tule ,Asientos,Aguascalientes'  

print(student)

#4
length_of_student = len(student)
print(f"La longitud de diccionario es: {length_of_student}")

#5
skills_value = student['skills']
skills_type = type(skills_value)
print(f"Skills: {skills_value}")
print(f"Data type of 'skills': {skills_type}")

#6
student['skills'].append('Manualidades') 
student['skills'].append('Mecanica') 
print("Updated skills:", student['skills'])

#7
keys_list = list(student.keys())
print(keys_list)

#8
values_list = list(student.values())
print(values_list)

#9
student_tuples = list(student.items())
print(student_tuples)

#10
del student['last_name']
print(student)
#11
del dog
print(dog)