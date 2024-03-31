with open('actors.txt', 'r', encoding='utf-8') as file:
    actors = file.read()
with open('female.txt', 'r', encoding='utf-8') as file:
    female = file.read()
with open('male.txt', 'r', encoding='utf-8') as file:
    male = file.read()


list_actors = actors.split('""')
list_female = female.replace('[', '').replace(']', '').replace("'", "").split(', ')
list_male = male.replace('[', '').replace(']', '').replace("'", "").split(', ')
count_male = 0
count_female = 0
for actor in list_actors:
    if actor in list_female:
        print(actor, 'Женщина')
        count_female += 1
    elif actor in list_male:
        print(actor, 'Мужчина')
        count_male += 1
percent_male = count_male/(count_male+count_female)*100
percent_male = '%.2f' % percent_male
print(percent_male, 'Процент мужских ролей')