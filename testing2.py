import requests


actors_id_list = ['9144', '12759', '22527', '677', '20664', '8989', '1130', '12761', '21496', '7370', '24264', '3420',
                  '22209', '24265', '24266', '24267', '24268', '24269', '24270', '10082', '24271', '24272', '24273',
                  '24274', '13487', '24275', '3100', '24276', '24277', '24278', '15235', '24279', '660035', '24280',
                  '20718', '24281', '154895', '724791', '1967572', '1586213', '1451292', '967709', '356', '25974',
                  '1451', '736956', '379898', '751695', '4321465', '154905', '152828', '677263', '591747', '3889715',
                  '1670063', '1670066', '3483', '24282']

headers = {
    'accept': 'application/json',
    'X-API-KEY': 'ef5f58f5-b4cc-4def-8534-53ad6939c82f',
}

count_male = 0
count = 0
for actor in actors_id_list:
    count += 1
    url = 'https://kinopoiskapiunofficial.tech/api/v1/staff/'+actor
    response = requests.get(url, headers=headers)
    print(response)
    person = response.text.split(',')
    sex = person[4].split(':')[1]
    if sex == '"MALE"':
        count_male += 1
percent_actors_male = count_male / count * 100
print('%.2f' % percent_actors_male)