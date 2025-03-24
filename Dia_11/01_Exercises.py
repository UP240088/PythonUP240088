#1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b
result = add_two_numbers(4, 7)
print(result) 

#2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
import math

def area_of_circle(r):
    return math.pi * r * r

radius = 5
area = area_of_circle(radius)
print(area)

#3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    
    for arg in args:
        if not isinstance(arg, (int, float)):
            return 
    
   
    return sum(args)


resultado = add_all_nums(1, 2, 3, 4)
print(resultado)  # El resultado será 10

resultado = add_all_nums(1, 2, "tres", 4)
print(resultado)

#4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = 20
fahrenheit = convert_celsius_to_fahrenheit(celsius)
print(f"{celsius}°C es igual a {fahrenheit}°F")

#5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer. 
def check_season(month):
   
    if month in [12, 1, 2]:
        return "Winter"  
    elif month in [3, 4, 5]:
        return "Spring"  
    elif month in [6, 7, 8]:
        return "Summer"  
    elif month in [9, 10, 11]:
        return "Autumn"  
    else:
        return "Invalid month"  
    
month = 11 
season = check_season(month)
print(f"El mes {month} corresponde a la estación: {season}")

#6 Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return 
    else:
        return (y2 - y1) / (x2 - x1)


x1, y1 = 1, 2  
x2, y2 = 3, 6 

pendiente = calculate_slope(x1, y1, x2, y2)
print(f"La pendiente de la recta es: {pendiente}")

#7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

import cmath  
def solve_quadratic_eqn(a, b, c):
   
    discriminant = b**2 - 4*a*c
    
    solution1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    solution2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    return solution1, solution2

a = 1
b = -3
c = 2

sol1, sol2 = solve_quadratic_eqn(a, b, c)
print(f"Las soluciones de la ecuación son: {sol1} y {sol2}")

#8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(my_list):
    for item in my_list:
        print(item)

example_list = [1, 2, 3, 4, 5]
print_list(example_list)

#9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_list([1, 2, 3, 4, 5]))  
print(reverse_list(["A", "B", "C"]))  

#10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(my_list):
    return [item.capitalize() for item in my_list]

example_list = ["apple", "banana", "cherry"]
capitalized_list = capitalize_list_items(example_list)
print(capitalized_list)  # ['Apple', 'Banana', 'Cherry']

#11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(my_list, item):
    my_list.append(item)
    return my_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))  # [2, 3, 7, 9, 5]

#12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.


def remove_item(my_list, item):
    if item in my_list:
        my_list.remove(item)
    return my_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

#13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(n):
    return sum(range(1, n + 1))

print(sum_of_numbers(5))  
print(sum_of_numbers(10)) 
print(sum_of_numbers(100)) 

#14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(n):
    return sum(range(1, n + 1, 2))

print(sum_of_odds(5))   
print(sum_of_odds(10))  
print(sum_of_odds(100)) 

#15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(n):
    return sum(range(2, n + 1, 2))


print(sum_of_even(5))   
print(sum_of_even(10))  
print(sum_of_even(100))



