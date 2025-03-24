#1
def is_prime(n):
    if n <= 1:
        return False  
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  
    return True  

print(is_prime(2))  
print(is_prime(3))  
print(is_prime(4))  
print(is_prime(17)) 
print(is_prime(18)) 

#2
def are_all_items_unique(my_list):
    return len(my_list) == len(set(my_list))

print(are_all_items_unique([1, 2, 3, 4, 5]))  
print(are_all_items_unique([1, 2, 3, 4, 5, 2])) 
print(are_all_items_unique(['a', 'b', 'c', 'd']))  
print(are_all_items_unique(['apple', 'banana', 'apple']))  

#3
def are_all_items_same_type(my_list):
    return len(set(type(item) for item in my_list)) == 1

print(are_all_items_same_type([1, 2, 3, 4, 5])) 
print(are_all_items_same_type([1, 2, 3, '4', 5]))  
print(are_all_items_same_type([1.1, 2.2, 3.3]))  
print(are_all_items_same_type([True, False, True]))  
print(are_all_items_same_type([1, '2', 3]))  

#4
def is_valid_variable_name(variable_name):
    return variable_name.isidentifier()

print(is_valid_variable_name("validVar"))   
print(is_valid_variable_name("2invalid"))   
print(is_valid_variable_name("another_var"))  
print(is_valid_variable_name("invalid-var")) 
print(is_valid_variable_name("class")) 

#5
from countries_data import countries_data


def most_spoken_languages(countries_data, top_n=10):
    language_count = {}
    
   
    for country in countries_data:
        for language in country["languages"]:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1

   
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    
  
    return sorted_languages[:top_n]


def most_populated_countries(countries_data, top_n=10):
  
    sorted_countries = sorted(countries_data, key=lambda x: x["population"], reverse=True)
    
   
    return sorted_countries[:top_n]

top_10_languages = most_spoken_languages(countries_data, top_n=10)
top_10_countries = most_populated_countries(countries_data, top_n=10)

print("Top 10 idiomas más hablados:")
for language, count in top_10_languages:
    print(f"{language}: {count} países")

print("\nTop 10 países más poblados:")
for country in top_10_countries:
    print(f"{country['country']}: {country['population']} personas")