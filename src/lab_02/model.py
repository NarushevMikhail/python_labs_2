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
    if not login: 
        return False
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
        
    @property #получает значение из атрибута
    def password(self):
        return self.__password
    @password.setter #устнавливает значение атрибута
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




