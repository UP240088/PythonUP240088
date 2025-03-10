# Unpack siblings and parents from family_members
brothers = ("Rafa", "David", "Juan", "Adan")
sisters = ("Maria", "Sarai", "Jimena")
Parents = ("Miles morales", "Maria Fenix")
siblings = brothers + sisters
Family_members = Parents + siblings
unpack_siblings_parents = siblings
unpack_parents_siblings = Parents
print("")
print("Pack siblings: ", unpack_siblings_parents)
print("Pack parents: ", unpack_parents_siblings)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Manzana", "Piña", "Sandia", "Platano", "Kiwi")
vejetables = ("Espinacas", "Jitomate", "Aguacate", "Lechuga", "Cebolla")
animal_products = ("Croquetas", "Shampoo para perros", "Pelotas", "Rascador", "Collar")
food_stuff_tp = fruits + vejetables + animal_products
print("")
print("Fruits: ", fruits)
print("Vegetables: ", vejetables)
print("Animal products. ", animal_products)
print("Food stuff: ", food_stuff_tp)


# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_list = list(food_stuff_tp)
print("")
print("Change tp: ", food_stuff_list)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = food_stuff_list[7]
print("")
print(middle_item)

# Slice out the first three items and the last three items from food_staff_lt list
first_three_item = food_stuff_list[0:3]
print("")
print(first_three_item)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple: -Check if 'Estonia' is a nordic country  -Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
does_exist = "Estonia" in nordic_countries
print("")
print(does_exist)
does_exist_2 = "Iceland" in nordic_countries
print("")
print(does_exist_2)
print("")
