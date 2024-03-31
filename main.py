from bs4 import BeautifulSoup
import requests
import pandas as pd



file_name = '1.txt'
text = open(file_name, 'r', encoding='utf-8').read()
soup = BeautifulSoup(text, 'lxml')


def all_links():
    list_a = soup.find_all('a', class_='styles_poster__gJgwz styles_root__wgbNq')
    link_list = [link.get('href') for link in list_a]
    #print(link_list)
    return link_list


def all_names():
    names = soup.find_all('div', class_='base-movie-main-info_mainInfo__ZL_u3')
    list_names = []
    for name in names:
        list_names.append(name.text)
    #print(list_names)
    return list_names


def all_years_and_durations():
    years = soup.find_all('span', class_='desktop-list-main-info_secondaryText__M_aus')
    list_years = []
    list_durations = []
    for year in years:
        list_years.append(year.text.split(', ')[-2])
        list_durations.append(year.text.split(', ')[-1].split('\xa0')[0])
    #print(list_years)
    #print(list_durations)
    return [list_years, list_durations]


def all_years():
    years = soup.find_all('span', class_='desktop-list-main-info_secondaryText__M_aus')
    list_years = []
    for year in years:
        list_years.append(year.text.split(', ')[-2])
    #print(list_years)
    return list_years


def all_durations():
    years = soup.find_all('span', class_='desktop-list-main-info_secondaryText__M_aus')
    list_durations = []
    for year in years:
        list_durations.append(year.text.split(', ')[-1].split('\xa0')[0])
    #print(list_durations)
    return list_durations


def all_rating():
    ratings = soup.find_all('span', class_='styles_kinopoiskCount__2_VPQ')
    list_rating = []
    for rating in ratings:
        list_rating.append(rating.text.replace(' ', ''))
    #print(list_rating)
    return list_rating


def all_genre():
    genres = soup.find_all('div', class_='desktop-list-main-info_additionalInfo__Hqzof')
    list_genres = []
    k = 1
    for genre in genres:
        k += 1
        if k % 2 != 0:
            continue
        list_genres.append(genre.text.split('\xa0')[0].split(' ')[-1])
    #print(list_genres)
    return list_genres



def percent_male_actors():
    list_percent_male = []
    with open('female.txt', 'r', encoding='utf-8') as file:
        female = file.read()
    with open('male.txt', 'r', encoding='utf-8') as file:
        male = file.read()

    film_links = all_links()
    actors_id_list = []
    for link in film_links:
        #print(link)
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
        percent_male = 0
        for actor in list_actors:
            if actor in list_female:
                count_female += 1
                #print(actor, 'Женщина')
            elif actor in list_male:
                count_male += 1
                #print(actor, 'Мужчина')
        if count_male + count_female != 0:
            percent_male = count_male / (count_male + count_female) * 100
            percent_male = float('%.2f' % percent_male)
            #print(percent_male, 'Процент мужских ролей')
        else:
            #print('Не удалось определить')
            percent_male = 0
        list_percent_male.append(percent_male)
    return list_percent_male


df = pd.DataFrame()
df['Позиция в рейтинге'] = list(range(1, 51))
df['Название фильма'] = all_names()
df['Жанр'] = all_genre()
df['Год выпуска'] = all_years()
df['Количество оценок'] = all_rating()
df['Продолжительность'] = all_durations()
df['Ссылка'] = all_links()
df['Процент актеров мужчин'] = percent_male_actors()
print(df)
df.to_excel(r'ТОП-50 фильмов.xlsx', index=False)