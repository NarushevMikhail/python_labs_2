from model import User

def main():
    print('=' * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССА USER")

    print('\n-- 1. Создание объекта. --')
    try:
        user1 = User('Oleg Tinkhoff', 'sberbank228', 'olegTink', 'admin') # nickname, password, login, role
        user2 = User('Michael Jackson', 'jackson2007', 'jackson1234', 'user')
        print(f'Пользователь(ы) успешно создан(ы).')
    except Exception as e:
        print(f'Ошибка при создании объекта: {e}')

    print('\n- 1.1 Пусто имя пользователя')
    try: 
        user11 = User('', 'sjdjdoj33', 'OlegCobalt', 'admin')
        print(f'Пользователь успешно создан')
    except Exception as e:
        print(f'Ошибка при создании пользователя: {e}')

    print('\n-- 2. Вывод через print, __str__')
    print('user1.', user1)
    print('user2.', user2)

    print('\n-- 3. Вывод через print, __repr__')
    print('user1.', repr(user1))
    print('user2.', repr(user2))

    print('\n-- 4. Сравнение двух пользователей через __eq__ ')
    print('\n- 4.1 Логины совпалают')
    user3 = User('Olegs son', 'qerty12345', 'olegTink', 'superadmin')
    print(f'Логин user1: {user1.login}')
    print(f'Логин user3: {user3.login}')
    print(f'Логины пользоватей совпадают: {user1 == user3}')

    print('\n- 4.2 Логины различаются')
    print(f'Логин user2: {user2.login}')
    print(f'Логин user3: {user3.login}')
    print(f'Логины пользователей совпадают: {user2 == user3}')

    print('\n- 5. Логин только из цифр')
    try: 
        user5 = User('Max Verstappen', 'maxon4ik', '83627490282', 'user')
    except Exception as e: 
        print(f'Ошибка: {e}')

    print('\n-- 5.1 Логин состоит из недопустимых символов')
    try: 
        user51 = User('Charles Lecler', '2ferrari2', '!!!&&&&!&!&!&!&', 'user')
        print('Пользователь успешно создан')
    except Exception as e:
        print(f'Ошибка: {e}')
    

    print('\n- 6. Пароль без фицр')
    try: 
        user6 = User('Michael Jorddanio', 'kkkkk', 'jordan2000', 'user') 
        print(f'Пользователь успешно создан.')
    except Exception as e:
        print(f'Ошибка: {e}')

    print('\n-- 6.1 Пустой пароль.')
    try:
        user61 = User('Michael Jhonson', '', 'olegkrut', 'admin')
        print(f'Пользователь успешно создан.')
    except Exception as e:
        print(f'Ошибка: {e}')

    print('\n-- 7. Изменение свойств через setter --')
    try:
        user7 = User('Rebeka Wecksler', 'lolsjc23', 'weckslerqwerty12345', 'user')
        print(f'Роль пользователя "{user7.nickname}": {user7.role}') 
        print(f'Старая роль user1: {user7.role}') 
        user7.role = 'moderator'
        print(f'Новая роль user1: {user7.role}')
        print(f'Роль пользователя "{user7.nickname}": {user7.role}') 
    except Exception as e:
        print(f'Ошибка: {e}')

    print('\n-- 7.1 Проверка ограничений setter --')
    try:
        user1.role = 'god'  # недопустимая роль
    except Exception as e:
        print(f'Ошибка (ожидаемо): {e}')    


    print('\n-- 8. Доступ к атрибуту класса --')
    print(f"Атрибут класса через класс: {User.total_users}")
    print(f"Атрибут класса через экземпляр: {user1.total_users}")

    # Если добавили метод:
    print(f"\nВызов метода класса:")
    print(User.get_total_users())
    print(user1.get_total_users())
    
    
    print('')
    print('-'*50)
    print('\n-- Отработка бизнес методов.')
    print('\n-- 1. Обновление профиля.')
    user1.update_profile(bio='Программист', age=30, city='Москва')
    print(user1.view_profile())
    
    print('\n-- 2.Отрицательный возраст')
    try:
        user1.update_profile(age=-5)
    except Exception as e:
        print(f'Ошибка: {e}')

    print('\n-- 3.Возраст не число')
    try:
        user1.update_profile(age='тридцать')
    except Exception as e:
        print(f'Ошибка: {e}')

    print('\n-- 4. Просмотр профиля')
    user1.update_profile(bio='Фронтендер', age=28)
    print(user1.view_profile())


if __name__ == '__main__': #запущен ли файл напрямую или импортирован
    main()