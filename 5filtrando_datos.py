DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]



def run():

    # Agregar a una lista todos aquellos desarolladores en python
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    
    # Agregar a una lista tosos aquellos que estan en platzy
    all_platzy_worker = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']

    for dev in all_python_devs:
        print(f'dev ==> {dev}')

    for org in all_platzy_worker:
        print(f'org ==> {org}')

    # Utilizando las funciones de orden superior
    # Agregar aquellos que tengan edad mayor a 18 anos 
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults2 = list(map(lambda worker: worker["name"], adults))
    print(f'(workers > 18) ==> {adults2}')

    # Agregar al diccionario una nueva clave-valor
    # Si son mayores a 18 agregar true
    # Versiones de pythom < 3.9
    old_people = list(map(lambda worker: {**worker, **{'old': worker['age'] > 70}}, DATA))

    # En versiuones de python 3.9 utilizamos los pipes para unir diccionarios
    # old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    
    for people in old_people:
        print(f'New DATA dictionery ==> {people}')

if __name__ == '__main__':
    run()
