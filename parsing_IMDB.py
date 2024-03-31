import requests
from bs4 import BeautifulSoup


list_name_actress = []
for i in range(1, 4):
    link = 'https://www.imdb.com/list/ls500208707/?sort=list_order,asc&mode=detail&page='+str(i)
    print(link)
    response = requests.get(link)
    print(response)

    soup = BeautifulSoup(response.text, 'lxml')
    soup_actors = soup.find_all('h3', class_='lister-item-header')
    for name_actor in soup_actors:
        list_name_actress.append(name_actor.find('a').text.strip().strip())
    print(list_name_actress)
print(len(list_name_actress))
with open('female.txt', 'w', encoding='utf-8') as file:
    file.write(str(list_name_actress))
print('файл записан')


list_name_actors = []
for i in range(1, 6):
    link = 'https://www.imdb.com/list/ls002984722/?sort=list_order,asc&mode=detail&page='+str(i)
    print(link)
    response = requests.get(link)
    print(response)

    soup = BeautifulSoup(response.text, 'lxml')
    soup_actors = soup.find_all('h3', class_='lister-item-header')
    for name_actor in soup_actors:
        list_name_actors.append(name_actor.find('a').text.strip().strip())
    print(list_name_actors)
print(len(list_name_actors))
with open('male.txt', 'w', encoding='utf-8') as file:
    file.write(str(list_name_actors))
print('файл записан')