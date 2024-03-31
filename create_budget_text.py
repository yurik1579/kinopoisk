import requests
import pandas as pd


df = pd.read_excel('TOP250.xlsx')
print(df.head())


list_id = []
for i in df['Ссылка']:
    id = i.split('/')[-2]
    list_id.append(id)

headers = {
        'accept': 'application/json',
        'X-API-KEY': 'af6b0652-b3f7-4ef4-9203-c8b50809625f',
    }

list_budget = []

k = 1
for id in list_id:
    link = 'https://kinopoiskapiunofficial.tech/api/v2.2/films/'+id+'/box_office'
    response = requests.get(link, headers=headers)
    print(response)
    list_budget.append(response.text)
    k += 1

print('Прошло', k, 'итераций')
MyFile = open('budget.txt', 'w', encoding='utf-8')
MyFile.writelines(list_budget)
MyFile.close()