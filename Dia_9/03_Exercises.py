#1
person = {
    'first_name': 'Sebastian',
    'last_name': 'Torres',
    'age': 19,
    'country': 'Mexico',
    'is_marred':False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]  
    print(f"Middle skill: {middle_skill}")
    
    
    if 'Python' in skills:
        print("The person has Python skill.")

    
    if set(['JavaScript', 'React']) <= set(skills):
        print('He is a front end developer')
    elif set(['Node', 'Python', 'MongoDB']) <= set(skills):
        print('He is a backend developer')
    elif set(['React', 'Node', 'MongoDB']) <= set(skills):
        print('He is a fullstack developer')
    else:
        print('unknown title')


if person['is_marred'] and person['country'] == 'Mexico':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")