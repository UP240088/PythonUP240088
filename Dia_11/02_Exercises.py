#1

def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {evens}.")

evens_and_odds(100)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(factorial(5))  


def is_empty(param):
    if not param:
        return True
    else:
        return False

print(is_empty([]))  
print(is_empty([1, 2, 3]))  
print(is_empty(""))  



import statistics

def calculate_mean(my_list):
    return sum(my_list) / len(my_list)

def calculate_median(my_list):
    return statistics.median(my_list)

def calculate_mode(my_list):
    try:
        return statistics.mode(my_list)
    except statistics.StatisticsError:
        return "No unique mode"

def calculate_range(my_list):
    return max(my_list) - min(my_list)

def calculate_variance(my_list):
    return statistics.variance(my_list)

def calculate_std(my_list):
    return statistics.stdev(my_list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Mean:", calculate_mean(my_list))           
print("Median:", calculate_median(my_list))       
print("Mode:", calculate_mode(my_list))           
print("Range:", calculate_range(my_list))         
print("Variance:", calculate_variance(my_list))   
print("Standard Deviation:", calculate_std(my_list))  