import vk
import time


session = vk.AuthSession(app_id='5761059', user_login='89516252032', user_password='jglj2545hkjk')
api = vk.API(session)

friends = api.friends.get()

print(len(friends))
print(friends)

friends = api.friends.get()

friends_info = api.users.get(user_ids=friends)

for friend in friends_info:
    print('ID: %s Имя: %s %s' % (friend['uid'], friend['last_name'],friend['first_name']))

get_location = []

for id in friends:
    print('Получаем данные пользователя: %s' % id)
    albums = api.photos.getAlbums(owner_id=id)
    print('\t альбомов %s' % len(albums))

    for album in albums:
        try:
            photos = api.photos.get(owner_id=id, album_id=album['aid'])
            print('\t Обрабатывем файлы альбома')

            for photo in photos:
                if 'lat' in photo and 'long' in photo:
                    get_location.append((photo['lat'],photo['long']))
            print('\t\t найдено %s фото' % len(photos))
        except:
            pass
        time.sleep(0.5)
    time.sleep(0.5)

js_code = ""

for loc in get_location:
    js_code += 'new google.maps.Marker({ position: {lat: %s, lng: %s}, map: map });\n' % (loc[0], loc[1])

html = open('map.html').read()

html = html.replace('/* PLACEHOLDER */', js_code)

f = open('Vk.html', 'w')
f.write(html)
f.close()


