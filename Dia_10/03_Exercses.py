#1
from countries import countries
for country in countries:
    if "land" in country.lower():  
        print(country)

#2
frutas = ['banana', 'orange', 'mango', 'lemon']
frutas_invertidas = []

for i in range(len(frutas) - 1, -1, -1):
    frutas_invertidas.append(frutas[i])
print(frutas_invertidas)

#3
from collections import Counter
from countries_data import countries_d 
#i.
language_counter = Counter()
unique_languages = set()

for country in countries_d:
    for language in country["languages"]:
        language_counter[language] += 1
        unique_languages.add(language)


total_languages = len(unique_languages)

# ii.
most_spoken_languages = language_counter.most_common(10)

most_populated_countries = sorted(
    countries_d, key=lambda x: x["population"], reverse=True
)[:10]

# iii.
top_10_populated = [(country["name"], country["population"]) for country in most_populated_countries]
print(f"Total number of unique languages: {total_languages}")
print("\nTen most spoken languages:")
for lang, count in most_spoken_languages:
    print(f"{lang}: {count} countries")

print("\nTen most populated countries:")
for country, population in top_10_populated:
    print(f"{country}: {population}")
