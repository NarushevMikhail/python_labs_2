import re 
from typing import Optional, Any, Dict, Protocol

def password_check(password: str) -> bool: 
    if len(password) > 0 and len(password) < 64:
        if any(x in '0123456789' for x in password): 
            return True
        else: 
            return False
    else:
        return False
    
def login_check(login: str) -> bool:
    if not login: 
        return False
    if login.isdigit() or login[0] == '@': #проверка что логин состоит только из цифр
        return False 
    else: 
        pattern = r'^[A-Za-z0-9@]+$'
        return bool(re.match(pattern, login))
    

class User:
    total_users: int = 0
    def __init__(self, nickname: str, password: str, login: str, role: str) -> None:
        User.total_users += 1
        self.nickname = nickname
        self.password = password
        self.login = login
        self.role = role
        self._bio: str = ''
        self._age: int = 0
        self._city: str = ''
        

    @property #из метода в свойство 
    def nickname(self) -> str:
        return self._nickname
    @nickname.setter
    def nickname(self, value: str) -> None:
        if isinstance(value, str) and value != '':
            self._nickname = value
        else:
            raise TypeError('Неверный формат имени')
        
    @property #получает значение из атрибута
    def password(self) -> str:
        return self.__password
    @password.setter #устнавливает значение атрибута
    def password(self, value: str) -> None:
        if isinstance(value, str) and password_check(value): 
            self.__password = value
        elif any(x not in '0987654321' for x in value):
            raise TypeError('В пароле должны быть цифры')
        else:
            raise TypeError('Пароль не соответствует требованиям')
    
    @property
    def login(self) -> str:
        return self._login
    @login.setter
    def login(self, value: str) -> None:
        if isinstance(value, str) and login_check(value):
            self._login = value
        else:
            raise TypeError('Неверный формат логина')
        
    @property
    def role(self) -> str:
        return self._role
    @role.setter
    def role(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError('Роль должна быть строкой')
        allowed_roles: list[str] = ['user', 'admin', 'moderator', 'superadmin', 'premium']
        value = value.lower()
        if value not in allowed_roles:
            raise TypeError(f'Такой роли не существует она должна быть одной из {allowed_roles}')
        else:
            self._role = value
     
    @classmethod
    def get_total_users(cls) -> str:
        return f'ВСего создано пользователей: {cls.total_users}'
    
    #бизнес - методы
    def update_profile(self, bio: Optional[str] = None, age: Optional[int] = None, city: Optional[str] = None) -> str:
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
    
    def view_profile(self) -> Dict[str, Any]:
        return{
            'nickname': self._nickname,
            'login': self._login,
            'role': self._role,
            'bio': self._bio,
            'age': self._age,
            'city': self._city
        }
    
    # МЕТОДЫ ДЛЯ PROTOCOLS
    def display(self) -> str:
        return f"User: {self.nickname} (login: {self.login}, role: {self.role})"
    
    def score(self) -> float:
        # Базовая оценка за роль
        role_scores = {'user': 5, 'premium': 7, 'moderator': 8, 'admin': 9, 'superadmin': 10}
        base_score = role_scores.get(self.role, 5)
        if self._bio: # Бонус за заполненный профиль
            base_score += 1
        if self._age > 0:
            base_score += 1
        if self._city:
            base_score += 1
        return min(base_score, 10.0) 

    def __str__(self) -> str: #вывод для пользователя
        return (f"Пользователь: {self.nickname}\n"
            f"   Логин: {self.login}\n" 
            f"   Роль: {self.role.upper()}\n"
            f"   Возраст: {self._age if self._age else 'не указан'}")
    
    def __repr__(self) -> str: #вывод лля программиста
        return f"{self._role}, nickname = {self._nickname}, password = [Пароль скрыт], login = {self._login}"
    
    def __eq__(self, other: object) -> bool: #eq - сравнение по содержимому
        if not isinstance(other, User):
            return False
        return self._login == other._login


class VIPUser(User):
    """VIP-пользователь с расширенными привилегиями"""
    
    def __init__(self, nickname: str, password: str, login: str, role: str = 'user', 
                 vip_level: str = 'gold', discount: int = 0) -> None:
        super().__init__(nickname, password, login, role)
        self._vip_level: str = vip_level      # уровень VIP: silver, gold, platinum
        self._discount: int = discount        # скидка в процентах
        self._bonus_points: int = 0           # бонусные баллы
        self._purchases: list[Dict[str, float]] = []  # история покупок
        
        # Устанавливаем скидку в зависимости от уровня
        discounts = {'silver': 5, 'gold': 15, 'platinum': 30}
        self._discount = discounts.get(vip_level, 0)
    
    #МЕТОДЫ ДЛЯ PROTOCOL 
    
    def display(self) -> str:
        """Метод для Protocol Displayable"""
        return f"VIP {self._vip_level.upper()}: {self.nickname} (discount: {self._discount}%, bonus: {self._bonus_points})"
    
    def score(self) -> float:
        """Метод для Protocol Scorable - выше оценка за VIP статус"""
        base_score = super().score()
        vip_bonus = {'silver': 1, 'gold': 2, 'platinum': 3}
        bonus = vip_bonus.get(self._vip_level, 0)
        return min(base_score + bonus, 10.0)
        
    @property
    def vip_level(self) -> str:
        return self._vip_level
    
    @vip_level.setter
    def vip_level(self, value: str) -> None:
        allowed = ['silver', 'gold', 'platinum']
        if value in allowed:
            self._vip_level = value
            discounts = {'silver': 5, 'gold': 15, 'platinum': 30}
            self._discount = discounts[value]
        else:
            raise TypeError(f'vip_level должен быть одним из: {allowed}')
    
    @property
    def discount(self) -> int:
        return self._discount
    
    @property
    def bonus_points(self) -> int:
        return self._bonus_points
    
    # ========== БИЗНЕС-МЕТОДЫ ==========
    
    def add_bonus_points(self, points: int) -> str:
        """Добавить бонусные баллы"""
        if isinstance(points, int) and points > 0:
            self._bonus_points += points
            return f"Начислено {points} бонусов. Всего: {self._bonus_points}"
        else:
            raise TypeError('Бонусы должны быть положительным числом')
    
    def get_bonus_points(self) -> int:
        """Получить количество бонусных баллов"""
        return self._bonus_points
    
    def make_purchase(self, amount: float) -> str:
        """Совершить покупку со скидкой"""
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise TypeError('Сумма покупки должна быть положительным числом')
        
        discounted_amount = amount * (100 - self._discount) / 100
        self._purchases.append({
            'amount': amount,
            'discounted': discounted_amount,
            'saved': amount - discounted_amount
        })
        
        # Начисляем бонусы (1 бонус за каждые 100 рублей)
        bonus = int(discounted_amount // 100)
        if bonus > 0:
            self.add_bonus_points(bonus)
        
        return f"Покупка на {amount} руб. Со скидкой {self._discount}%: {discounted_amount:.2f} руб. Сэкономлено: {amount - discounted_amount:.2f} руб."
    
    def get_purchase_history(self) -> list[Dict[str, float]]:
        """Получить историю покупок"""
        return self._purchases.copy()
    
    def get_access_rights(self) -> str:
        """У VIP больше прав и скидка"""
        if self._vip_level == 'platinum':
            return f"VIP Platinum: приоритетная поддержка, скидка {self._discount}%, эксклюзивный контент, бонусов: {self._bonus_points}"
        elif self._vip_level == 'gold':
            return f"VIP Gold: приоритетная поддержка, скидка {self._discount}%, бонусов: {self._bonus_points}"
        else:
            return f"VIP Silver: скидка {self._discount}%, ранний доступ к новинкам, бонусов: {self._bonus_points}"
    
    def __str__(self) -> str:
        parent_str = super().__str__()
        return parent_str + f"\n   VIP уровень: {self._vip_level.upper()}\n   Скидка: {self._discount}%\n   Бонусов: {self._bonus_points}"
    
    def __repr__(self) -> str:
        return f"VIPUser({self._nickname}, {self._login}, {self._vip_level})"


class AdminUser(User):
    def __init__(self, nickname: str, password: str, login: str, 
                 server_access: bool = True, admin_level: int = 1) -> None:
        super().__init__(nickname, password, login, role='admin')
        self._server_access: bool = server_access      # доступ к серверу
        self._admin_level: int = admin_level          # уровень администрирования (1-5)
        self._managed_users: list[User] = []          # список управляемых пользователей
        self._action_log: list[str] = []              # лог действий
    
    # МЕТОДЫ ДЛЯ PROTOCOL    
    def display(self) -> str:
        return f"Admin: {self.nickname} (level: {self._admin_level}, server_access: {self._server_access})"
    
    def score(self) -> float:
        base_score = super().score()
        admin_bonus = self._admin_level * 0.5
        server_bonus = 2 if self._server_access else 0
        return min(base_score + admin_bonus + server_bonus, 10.0)


    @property
    def server_access(self) -> bool:
        return self._server_access
    
    @server_access.setter
    def server_access(self, value: bool) -> None:
        if isinstance(value, bool):
            self._server_access = value
        else:
            raise TypeError('server_access должен быть bool')
    
    @property
    def admin_level(self) -> int:
        return self._admin_level
    
    @admin_level.setter
    def admin_level(self, value: int) -> None:
        if isinstance(value, int) and 1 <= value <= 5:
            self._admin_level = value
        else:
            raise TypeError('admin_level должен быть числом от 1 до 5')
    
    @property
    def managed_users(self) -> list[User]:
        return self._managed_users.copy()
    
    @property
    def action_log(self) -> list[str]:
        return self._action_log.copy()
    
    #БИЗНЕС-МЕТОДЫ 
    
    def assign_moderator(self, user: User) -> str:
        """Назначить пользователя модератором"""
        if not isinstance(user, User):
            raise TypeError('Можно назначить только объект User')
        if self._admin_level < 3:
            return f"Ошибка: уровень админа {self._admin_level} слишком низкий для назначения модератора"
        old_role = user.role
        user.role = 'moderator'
        self._managed_users.append(user)
        self._action_log.append(f"Назначил {user.nickname} модератором")
        return f"Админ {self.nickname} повысил {user.nickname} с {old_role} до moderator"
    
    def get_managed_users_count(self) -> int:
        """Количество управляемых пользователей"""
        return len(self._managed_users)
    
    def show_action_log(self) -> str:
        """Показать лог действий"""
        if not self._action_log:
            return "Лог действий пуст"
        return "\n".join(self._action_log)
    
    def add_action_to_log(self, action: str) -> None:
        self._action_log.append(action)
    
    def get_access_rights(self) -> str:
        if self._admin_level >= 4:
            return f"полный доступ + управление сервером (уровень {self._admin_level})"
        elif self._admin_level >= 2:
            return f"расширенный доступ + управление пользователями (уровень {self._admin_level})"
        else:
            return f"базовый административный доступ (уровень {self._admin_level})"
    
    def __str__(self) -> str:
        parent_str = super().__str__()
        return parent_str + f"\n   Админ-уровень: {self._admin_level}\n   Доступ к серверу: {'Да' if self._server_access else 'Нет'}\n   Управляемых пользователей: {len(self._managed_users)}"
    
    def __repr__(self) -> str:
        return f"AdminUser({self._nickname}, {self._login}, level={self._admin_level})"