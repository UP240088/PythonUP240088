# Create an empty tuple
empty_tuple = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
names_tuple = ("Rafa", "Jose", "Maria", "Juan")
print("Names: ", names_tuple)
print("Total names: ", len(names_tuple))

# Join brothers and sisters tuples and assign it to siblings
brothers = ("Rafa", "David", "Juan", "Adan")
sisters = ("Maria", "Sarai", "Jimena")
siblings = brothers + sisters
print("MY FAMILY")
print("")
print("Brothers: ", brothers)
print("Sisters: ", sisters)
print("Siblings: ", siblings)

# How many siblings do you have?
print("")
print("I have ",len(siblings), "siblings")

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Parents = ("Miles morales", "Maria Fenix")
Family_members = Parents + siblings
print("")
print("Siblings and Parents: ", Family_members)
print("")