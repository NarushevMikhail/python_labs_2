from collection import User, UserList


print('1. Вывод всей коллекции:')
try:
    user1 = User('Oleg Tinkhoff', 'sberbank228', 'oleggfgd', 'admin') # nickname, password, login, role
    user2 = User('Michael Jackson', 'jackson2007', 'jackson1234', 'user')
    list1 = UserList()
    list1.add(user1)
    list1.add(user2)
    print(list1)
except Exception as e:
    print(f'Возникла ошибка: {e}')

print('1.2 Ошибка при создании коллекции')
try: 
    list12 = UserList()
    user3 = (3348242)
    list12.add(user3)
    print(list12) 
except Exception as e: 
    print(f'Произошла ошибка: {e}')

print('1.3 Попытка добавить пользователя с таким же nickname')
try: 
    user4 = User('Oleg Tinkhoff', 'sberbank228', 'olegTink', 'admin')
    user11 = User('Oleg Tinkhoff', 'sfsdfsd222', 'olegCoffi', 'user')
    list13 = UserList()
    list13.add(user4)
    list13.add(user11)
    print(list13)
except Exception as e:
    print(f'Произошла ошибка: {e}')

print('1.4 Попытка добавить пользователя с таким же login')
try:
    user12 = User('Oleg Cobalt', 'nornikel234', 'olegbest', 'admin')
    user13 = User('Oleg Tinkhoff', 'sfsdfsd222', 'olegbest', 'user')
    list14 = UserList() 
    list14.add(user12)
    list14.add(user13)
    print(list14)
except Exception as e:
    print(f'Произошла ошибка: {e}')


print('-' * 50)
print('2. Удаление объекта из коллекции')
try: 
    user4 = User('Oleg Tinkhoff', 'sberbank228', 'olegTink', 'admin') # nickname, password, login, role
    user5 = User('Michael Jackson', 'jackson2007', 'jackson1234', 'user')
    list2 = UserList()
    list2.add(user4)
    list2.add(user5)
    print(f'Удаление...')
    list2.remove(user5)
    print(f'Удаление произошло успешно! Результат: \n{list2}')
except Exception as e:
    print(f'При удалении произошла ошибка: {e}') 

print('2.1 Ошибка при удалении User из коллекции.')
try:
    user6 = User('Test', 'test123', 'testLogin', 'user')
    user7 = User('Another', 'pass456', 'anotherLogin', 'user')
    list21 = UserList()
    list21.add(user6)
    list21.remove(user7)
except Exception as e:
    print(f'Произошла ошибка: {e}')

print('2.2 Ошбика при удалении не User - объекта')
try:
    user8 = User('Test2', 'pass789', 'test2', 'user')
    list22 = UserList()
    list22.add(user8)
    list22.remove('user8')
except Exception as e:
    print(f'Произошла ошибка: {e}')

print('-'*50)
print('3. Проверка метода get_all()')
try:
    user9 = User('Alice', 'alice123', 'alice', 'user')
    user10 = User('Bob', 'bob456', 'bob', 'admin')
    list3 = UserList()
    list3.add(user9)
    list3.add(user10)
    print(list3.get_all())
except Exception as e:
    print(f'Произошла ошибка: {e}')

print('-'*50)
print('4. Поиск пользователя по nickname')
try:
    user14 = User('Jhon', 'alice123', 'alice2', 'user')
    list14 = UserList()
    list14.add(user14)
    print(f'Найден пользователь: {list14.find_by_nickname('Jhon')}')
except Exception as e:
    print(f'Произошла ошибка: {e}')

print('4.1 Поиск пользователя по login')
try:
    user15 = User('Jhon', 'alice123', 'alice2', 'user')
    list15 = UserList()
    list15.add(user15)
    print(f"Найден пользователь: {list15.find_by_login('alice2')}")
except Exception as e:
    print(f'Произошла ошибка: {e}')

print('4.2 Поиск пользователя по role')
try:
    user16 = User('Bob', 'bob4ik', 'bob228', 'admin')
    list16 = UserList()
    list16.add(user16)
    print(f"Найден пользователь: {list16.find_by_role('Admin')}")
except Exception as e:
    print(f'Произошла ошибка: {e}')

print('4.3 Ошибка при поиске User')
try:
    user17 = User('Bob', 'bob4ik', 'bob228', 'admin')
    list17 = UserList()
    list17.add(user17)
    print(f"Найден пользователь: {list17.find_by_nickname(2131)}")
except Exception as e:
    print(f'Произошла ошибка: {e}')

print('-'*50)
print('5. Длина коллекции')
try:
    user_a = User('Иван Петров', 'pass123', 'ivanp', 'user')
    user_b = User('Мария Сидорова', 'maria2024', 'mashas', 'admin')
    user_c = User('Алексей Смирнов', 'alex777', 'smirnova', 'moderator')
    listabc = UserList()
    listabc.add(user_a)
    listabc.add(user_b)
    listabc.add(user_c)
    print(f'Длина коллекции: {len(listabc)}')
except Exception as e:
    print(f'Произошла ошибка: {e}')

print('5.1 Длина пустой коллекции')
try:
    empty_list = UserList()
    print(f'Длина пустой коллекции: {len(empty_list)}')
except Exception as e:
    print(f'Произошла ошибка: {e}')   

print('-'*50)
print('6. Итерация по коллекции (for)')
try:
    print("Перебор всех пользователей:")
    for user in listabc:
        print(f"  - {user.nickname} ({user.role})")
except Exception as e:
    print(f'Произошла ошибка: {e}')

print('-'*50)
print('7. Индексация коллекции (__getitem__)')
try:
    print(f"Элемент с индексом 0: {listabc[0].nickname}")
    print(f"Элемент с индексом 1: {listabc[1].nickname}")
    print(f"Элемент с индексом 2: {listabc[2].nickname}")
    print(f"Элемент с индексом -1 (последний): {listabc[-1].nickname}")
except Exception as e:
    print(f'Произошла ошибка: {e}')

# ДОБАВЛЕНО: ошибка при неверном индексе
print('7.1 Ошибка при неверном индексе')
try:
    print(listabc[10])
except Exception as e:
    print(f'Произошла ошибка: {e}')

print('-'*50)
print('8. Сортировка коллекции')
try:
    # Создаем коллекцию для сортировки
    sort_list = UserList()
    sort_list.add(User('Зоя Лебедева', 'pass1', 'zoya', 'user'))
    sort_list.add(User('Анна Воронова', 'pass2', 'anna', 'admin'))
    sort_list.add(User('Борис Громов', 'pass3', 'boris', 'moderator'))
    sort_list.add(User('Денис Козлов', 'pass4', 'denis', 'user'))
    
    print('Исходный порядок:')
    for user in sort_list:
        print(f'  - {user.nickname}')
    
    print('\nСортировка по nickname (по возрастанию):')
    sort_list.sort_by_nickname()
    for user in sort_list:
        print(f'  - {user.nickname}')
    
    print('\nСортировка по nickname (по убыванию):')
    sort_list.sort_by_nickname(reverse=True)
    for user in sort_list:
        print(f'  - {user.nickname}')

    print('\nСортировка по login:')
    sort_list.sort_by_login()
    for user in sort_list:
        print(f'  - {user.login} -> {user.nickname}')
    
    print('\nСортировка по role:')
    sort_list.sort_by_role()
    for user in sort_list:
        print(f'  - {user.role} -> {user.nickname}')
        
except Exception as e:
    print(f'Произошла ошибка: {e}')

print('-'*50)
print('9. Фильтрация коллекции (логические операции)')
try:
    # Создаем коллекцию с разными пользователями
    filter_list = UserList()
    
    user_admin1 = User('Admin Иванов', 'admin123', 'ivanov', 'admin')
    user_admin2 = User('Admin Петров', 'admin456', 'petrov', 'admin')
    user_user1 = User('User Сидоров', 'user123', 'sidorov', 'user')
    user_user2 = User('User Кузнецова', 'user456', 'kuznetsova', 'user')
    user_moder = User('Moder Смирнов', 'moder123', 'smirnov', 'moderator')
    
    # Заполняем профили для некоторых
    user_user1.update_profile(age=25, city='Москва', bio='Люблю программирование')
    user_admin1.update_profile(age=35, city='СПб', bio='Менеджер проектов')
    
    filter_list.add(user_admin1)
    filter_list.add(user_admin2)
    filter_list.add(user_user1)
    filter_list.add(user_user2)
    filter_list.add(user_moder)

    print(f'Всего пользователей: {len(filter_list)}')
    
    print('\n9.1 get_admins() - все администраторы:')
    admins = filter_list.get_admins()
    for admin in admins:
        print(f'  - {admin.nickname} (роль: {admin.role})')
    
    print('\n9.2 get_users() - все обычные пользователи:')
    users = filter_list.get_users()
    for user in users:
        print(f'  - {user.nickname} (роль: {user.role})')
    
    print('\n9.3 get_moderators() - все модераторы:')
    moders = filter_list.get_moderators()
    for moder in moders:
        print(f'  - {moder.nickname} (роль: {moder.role})')
    
    print('\n9.4 get_with_profile() - пользователи с заполненным профилем:')
    with_profile = filter_list.get_with_profile()
    for user in with_profile:
        print(f'  - {user.nickname}')

except Exception as e:
    print(f'Произошла ошибка: {e}')

print('-'*50)
print('10. Управление пользователями (добавление, поиск, удаление)')
try:
    management_list = UserList()
    
    management_list.add(User('Сергей Иванов', 'sergey123', 'sivanov', 'admin'))
    management_list.add(User('Ольга Петрова', 'olga456', 'opetrova', 'user'))
    management_list.add(User('Дмитрий Сидоров', 'dima789', 'dsidorov', 'user'))
    print(f'Всего добавлено: {len(management_list)} пользователей')
    
    print('\nПоиск пользователя по nickname "Ольга Петрова":')
    found = management_list.find_by_nickname('Ольга Петрова')
    print(f'Найден: {found[0].nickname}, роль: {found[0].role}')
    
    print('\nУдаляем пользователя "Дмитрий Сидоров"...')
    user_to_remove = management_list.find_by_nickname('Дмитрий Сидоров')[0]
    management_list.remove(user_to_remove)
    print(f'После удаления осталось: {len(management_list)} пользователей')
    
except Exception as e:
    print(f'Произошла ошибка: {e}')

print('-'*50)
print('11. Сортировка и анализ пользователей')
try:
    analytics_list = UserList()
    
    # Добавляем пользователей с разными именами
    analytics_list.add(User('Анна', 'pass1', 'anna', 'user'))
    analytics_list.add(User('Виктор', 'pass2', 'victor', 'admin'))
    analytics_list.add(User('Борис', 'pass3', 'boris', 'user'))
    analytics_list.add(User('Елена', 'pass4', 'elena', 'moderator'))
    analytics_list.add(User('Григорий', 'pass5', 'gregory', 'user'))
    
    print('Исходный список:')
    for user in analytics_list:
        print(f'  - {user.nickname}')
    
    print('\nСортировка по nickname (алфавитный порядок):')
    analytics_list.sort_by_nickname()
    for user in analytics_list:
        print(f'  - {user.nickname}')
    
    print(f'\nСтатистика:')
    print(f'  - Всего: {len(analytics_list)} пользователей')
    print(f'  - Администраторов: {len(analytics_list.get_admins())}')
    print(f'  - Модераторов: {len(analytics_list.get_moderators())}')
    print(f'  - Обычных пользователей: {len(analytics_list.get_users())}')
    
except Exception as e:
    print(f'Произошла ошибка: {e}')

    print('-'*50)
print('12. Индексация и фильтрация')
try:
    index_list = UserList()
    
    # Добавляем пользователей
    index_list.add(User('Пользователь 1', 'pass1', 'user1', 'user'))
    index_list.add(User('Пользователь 2', 'pass2', 'user2', 'user'))
    index_list.add(User('Администратор 1', 'pass3', 'admin1', 'admin'))
    index_list.add(User('Пользователь 3', 'pass4', 'user3', 'user'))
    index_list.add(User('Модератор 1', 'pass5', 'moder1', 'moderator'))
    
    print('Доступ к элементам по индексу:')
    print(f'  - Первый пользователь: {index_list[0].nickname}')
    print(f'  - Последний пользователь: {index_list[-1].nickname}')
    print(f'  - Третий пользователь: {index_list[2].nickname}')
    
    print('\nФильтрация:')
    only_users = index_list.get_users()
    print(f'  - Только обычные пользователи: {len(only_users)}')
    for user in only_users:
        print(f'    * {user.nickname}')
    
    only_admins = index_list.get_admins()
    print(f'  - Только администраторы: {len(only_admins)}')
    for admin in only_admins:
        print(f'    * {admin.nickname}')
    
    print('\nУдаление по индексу (удаляем первого пользователя):')
    print(f'  - Удалён: {index_list.remove_at(0).nickname}')
    print(f'  - Осталось: {len(index_list)} пользователей')

except Exception as e:
    print(f'Произошла ошибка: {e}')