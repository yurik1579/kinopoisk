from bs4 import BeautifulSoup
import pandas as pd


def all_ratings():
    names = soup.find_all('span', class_='styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg styles_top250Type__mPloU')
    list_names = []
    for name in names:
        list_names.append(name.text)
    #print(list_names)
    return list_names


full_list_ratings = []
for i in range(1, 6):
    file_name = str(i)+'.txt'
    text = open(file_name, 'r', encoding='utf-8').read()
    soup = BeautifulSoup(text, 'lxml')
    full_list_ratings += all_ratings()
print(full_list_ratings)
print(len(full_list_ratings))

df = pd.read_excel('TOP250.xlsx')
df['Рейтинг'] = full_list_ratings
df.to_excel('TOP250 с рейтингом2.xlsx', index=False)