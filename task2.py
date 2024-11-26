import requests 
import csv


api_url = "https://ru.wikipedia.org/w/api.php" 

def get_all_animals(): 
    animals = [] 
    params = {"action": "query", 
              "format": "json", 
              "list": "categorymembers", 
              "cmtitle": "Категория:Животные_по_алфавиту", 
              "cmlimit": "max"}
    
    while True: 
        response = requests.get(api_url, params=params) 
        data = response.json()  
        
        animals.extend(member['title'] for member in data['query']['categorymembers'])
        
        if 'continue' in data: 
            params.update(data['continue']) 
        else: 
            break

    return animals

all_animals = get_all_animals()

russian_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' 
sorted_animals = {letter: 0 for letter in russian_alphabet}

for animal in all_animals: 
    first_letter = animal[0].upper() 
    if first_letter in sorted_animals: 
        sorted_animals[first_letter] += 1 


with open('beasts.csv', 'w', newline='', encoding='utf-8') as csvfile: 
    writer = csv.writer(csvfile) 
    for letter, count in sorted_animals.items(): 
        writer.writerow([letter, count]) 
print("Данные успешно записаны в файл beasts.csv")