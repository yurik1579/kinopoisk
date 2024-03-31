import requests
from bs4 import BeautifulSoup


with open('female.txt', 'r', encoding='utf-8') as file:
    female = file.read()
with open('male.txt', 'r', encoding='utf-8') as file:
    male = file.read()


file_name = 'kino.txt'
text = open(file_name, 'r', encoding='utf-8').read()
soup = BeautifulSoup(text, 'lxml')


def all_links():
    list_a = soup.find_all('a', class_='styles_poster__gJgwz styles_root__wgbNq')
    link_list = [link.get('href') for link in list_a]
    return link_list


film_links = all_links()
actors_id_list = []
k = 0
for link in film_links:
    print(link)
    film_id = link.split('/')[-2]
    headers = {
        'accept': 'application/json',
        'X-API-KEY': 'af6b0652-b3f7-4ef4-9203-c8b50809625f',
    }
    params = {
        'filmId': film_id,
    }
    response = requests.get('https://kinopoiskapiunofficial.tech/api/v1/staff', params=params, headers=headers)
    print(response)
    actors = response.text.split('},{')
    actors_id_list = []
    actors_names_list = []
    for i in actors:
        actor = i.split(',')
        id_actors = actor[0].split('":')[1]
        actor_name = actor[2].split('":')[1]
        profession = actor[-1].split('":')[1]
        if profession == '"ACTOR"':
            actors_id_list.append(id_actors)
            actors_names_list.append(actor_name)

    MyFile = open('actors.txt', 'w', encoding='utf-8')
    MyFile.writelines(actors_names_list)
    MyFile.close()

    with open('actors.txt', 'r', encoding='utf-8') as file:
        actors = file.read()



    list_actors = actors.split('""')
    list_female = female.replace('[', '').replace(']', '').replace("'", "").split(', ')
    list_male = male.replace('[', '').replace(']', '').replace("'", "").split(', ')
    count_male = 0
    count_female = 0
    for actor in list_actors:
        if actor in list_female:
            count_female += 1
            print(actor, 'Женщина')
        elif actor in list_male:
            count_male += 1
            print(actor, 'Мужчина')
    if count_male+count_female != 0:
        percent_male = count_male/(count_male+count_female)*100
        percent_male = '%.2f' % percent_male
        print(percent_male, 'Процент мужских ролей')
    else:
        print('Не удалось определить')
    k += 1
    if k == 5:
        break