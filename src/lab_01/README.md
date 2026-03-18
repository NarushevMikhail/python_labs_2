# Лабораторная работа №1, вариант 8
## 1.CLass User
### атрибут класса и закрытые экземпляры
<img width="955" height="462" alt="image" src="https://github.com/user-attachments/assets/812b6eb7-d1ad-4ee0-a3fa-2d18da2b4760" />


## 2.Декоратор @Property с валидацией и метод - setter, а также две функция вне класса для проверки данных.
- Проверка, что имя пользователя не пустое, и что оно является строкой.
- Проверка пароля, что он является строкой, его длина находиться в диапазоне от 1 до 64, и что в пароле есть цифры.
- Проверка логина, что он является строкой, что он состоит не только из чисел, не начинается с @.
- ПРоверка роли, роль может быть только из списка allowed_roles, и что она являеться строкой 
 <img width="1651" height="1437" alt="image" src="https://github.com/user-attachments/assets/50d7f0a0-02e6-4eda-9d60-bd9fb899c642" />
 <img width="1158" height="504" alt="image" src="https://github.com/user-attachments/assets/85fbf80c-2364-47a5-abab-7ebcdc22b0a2" />

## 3.Бизнес - методы
- Обновление профиля
- Просмотр профиля
 <img width="1052" height="960" alt="image" src="https://github.com/user-attachments/assets/f0d1f9bc-55d0-4a60-8d37-76eb0157c0f6" />


## 4.Магические методы 
### ```__str__``` - неформальное строковое представление объекта для пользователей (например, для print())
### ```__repr__``` - официальное строковое представление для разработчиков (отладочная инфомрация)
### ```__eq__``` - переопределяет оператор равенства ```==```, задает логику сравнения объектов
<img width="1408" height="440" alt="image" src="https://github.com/user-attachments/assets/d274ca4d-d2a8-43ba-b16c-323d1e7c15e0" />


## 5. Вывод в файле ```Demo.py```
<img width="1130" height="1339" alt="image" src="https://github.com/user-attachments/assets/037026d0-9048-4abb-b2f1-a34d66b5bb41" />
<img width="1677" height="944" alt="image" src="https://github.com/user-attachments/assets/288692ef-0982-4a6b-a208-ae2bdea62891" />

## 6. ```model.py```
```
import re 

def password_check(password: str):
    if len(password) > 0 and len(password) < 64:
        if any(x in '0123456789' for x in password): 
            return True
        else: 
            return False
    else:
        return False
    
def login_check(login: str):
    if login.isdigit() or login[0] == '@': #проверка что логин состоит только из цифр
        return False 
    else: 
        pattern = r'^[A-Za-z0-9@]+$'
        return bool(re.match(pattern, login))
    

class User:
    total_users = 0
    def __init__(self, nickname, password, login, role):
        User.total_users += 1
        self.nickname = nickname
        self.password = password
        self.login = login
        self.role = role
        self._bio = ''
        self._age = 0
        self._city = ''
        

    @property #из метода в свойство 
    def nickname(self):
        return self._nickname
    @nickname.setter
    def nickname(self, value):
        if isinstance(value, str) and value != '':
            self._nickname = value
        else:
            raise TypeError('Неверный формат имени')
        
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        if isinstance(value, str) and password_check(value):
            self.__password = value
        elif any(x not in '0987654321' for x in value):
            raise TypeError('В пароле должны быть цифры')
        else:
            raise TypeError('Пароль не соответствует требованиям')
    
    @property
    def login(self):
        return self._login
    @login.setter
    def login(self, value):
        if isinstance(value, str) and login_check(value):
            self._login = value
        else:
            raise TypeError('Неверный формат логина')
        
    @property
    def role(self):
        return self._role
    @role.setter
    def role(self, value):
        if not isinstance(value, str):
            raise TypeError('Роль должна быть строкой')
        allowed_roles = ['user', 'admin', 'moderator', 'superadmin']
        value = value.lower()
        if value not in allowed_roles:
            raise TypeError(f'Такой роли не существует она должна быть одной из {allowed_roles}')
        else:
            self._role = value
     
    @classmethod
    def get_total_users(cls):
        return f'ВСего создано пользователей: {cls.total_users}'
    
    #бизнес - методы
    def update_profile(self, bio = None, age = None, city = None):
        if bio is not None:
            if not isinstance(bio, str):
                raise TypeError('bio должно быть строкой')
            self._bio = bio

        if age is not None:
            if not isinstance(age, int):
                raise TypeError('Возраст должен быть числом')
            elif age <= 0:
                raise TypeError('Возраст не может быть нулем или меньше нуля')
            self._age = age 

        if city is not None:
            if not isinstance(city, str):
                raise TypeError('В название города допустимы только буквы')
            self._city = city

        return f'Профиль изменён'
    
    def view_profile(self):
        return{
            'nickname': self._nickname,
            'login': self._login,
            'role': self._role,
            'bio': self._bio,
            'age': self._age,
            'city': self._city
        }
    

    def __str__(self): #вывод для пользователя
        return (f"Пользователь: {self.nickname}\n"
            f"   Логин: {self.login}\n"
            f"   Роль: {self.role.upper()}\n"
            f"   Возраст: {self._age if self._age else 'не указан'}")
    
    def __repr__(self): #вывод лля программиста
        return f"{self._role}, nickname = {self._nickname}, password = [Пароль скрыт], login = {self._login}"
    
    def __eq__(self, other): #eq - сравнение по содержимому
        if not isinstance(other, User):
            return False
        return self._login == other._login

```

## ```demo.py```

```
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


if __name__ == '__main__':
    main()

```



