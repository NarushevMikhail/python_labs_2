from models import User

class AdminUser(User):
    
    def __init__(self, nickname, password, login, server_access=True, admin_level=1):
        # super() - функция для вызова конструктора базового класса 
        super().__init__(nickname, password, login, role='admin')
        self._server_access = server_access      # доступ к серверу
        self._admin_level = admin_level          # уровень администрирования (1-5)
        self._managed_users = []                 # список управляемых пользователей
        self._action_log = []                    # лог действий
    
    @property
    def server_access(self):
        return self._server_access
    @server_access.setter
    def server_access(self, value):
        if isinstance(value, bool):
            self._server_access = value
        else:
            raise TypeError('server_access должен быть bool')
    
    @property
    def admin_level(self):
        return self._admin_level
    @admin_level.setter
    def admin_level(self, value):
        if isinstance(value, int) and 1 <= value <= 5:
            self._admin_level = value
        else:
            raise TypeError('admin_level должен быть числом от 1 до 5')
    
    # Новый метод 1: назначить пользователя модератом 
    def assign_moderator(self, user):
        if not isinstance(user, User): #фильтрация по типу
            raise TypeError('Можно назначить только объект User')
        if self._admin_level < 3:
            return f"Ошибка: уровень админа {self._admin_level} слишком низкий для назначения модератора"
        old_role = user.role
        user.role = 'moderator'
        self._managed_users.append(user)
        self._action_log.append(f"Назначил {user.nickname} модератором")
        return f"Админ {self.nickname} повысил {user.nickname} с {old_role} до moderator"
    
    # метод 2:  кол - во управляемых пользователей
    def get_managed_users_count(self):
        return len(self._managed_users)
    
    # метод 3: показать лог действий
    def show_action_log(self):
        if not self._action_log:
            return "Лог действий пуст"
        return "\n".join(self._action_log)
    
    # переопределенный метод - полиморфное поведение
    def get_access_rights(self):
        """У админа больше прав - переопределение базового метода"""
        if self._admin_level >= 4:
            return f"полный доступ + управление сервером (уровень {self._admin_level})"
        elif self._admin_level >= 2:
            return f"расширенный доступ + управление пользователями (уровень {self._admin_level})"
        else:
            return f"базовый административный доступ (уровень {self._admin_level})"
    
    # Переопределенный __str__ 
    def __str__(self):
        parent_str = super().__str__()
        return parent_str + f"\n   Админ-уровень: {self._admin_level}\n   Доступ к серверу: {'Да' if self._server_access else 'Нет'}"


class VIPUser(User):
    
    def __init__(self, nickname, password, login, role='user', vip_level='gold', discount=0):
        super().__init__(nickname, password, login, role)
        self._vip_level = vip_level      # уровень VIP: silver, gold, platinum
        self._discount = discount        # скидка в процентах
        self._bonus_points = 0           # бонусные баллы
        self._purchases = []             # история покупок
    
    @property
    def vip_level(self):
        return self._vip_level
    @vip_level.setter
    def vip_level(self, value):
        allowed = ['silver', 'gold', 'platinum']
        if value in allowed:
            self._vip_level = value
            discounts = {'silver': 5, 'gold': 15, 'platinum': 30}
            self._discount = discounts[value]
        else:
            raise TypeError(f'vip_level должен быть одним из: {allowed}')
    
    @property
    def discount(self):
        return self._discount
    
    # метод 1 
    def add_bonus_points(self, points):
        """Добавить бонусные баллы"""
        if isinstance(points, int) and points > 0:
            self._bonus_points += points
            return f"Начислено {points} бонусов. Всего: {self._bonus_points}"
        else:
            raise TypeError('Бонусы должны быть положительным числом')
    
    # метод 2 
    def get_bonus_points(self):
        """Получить количество бонусных баллов"""
        return self._bonus_points
    
    # метод 3 
    def make_purchase(self, amount):
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
    
    # переопределенный метод- полиморфное поведение
    def get_access_rights(self):
        """У VIP больше прав и скидка"""
        if self._vip_level == 'platinum':
            return f"VIP Platinum: приоритетная поддержка, скидка {self._discount}%, эксклюзивный контент, бонусов: {self._bonus_points}"
        elif self._vip_level == 'gold':
            return f"VIP Gold: приоритетная поддержка, скидка {self._discount}%, бонусов: {self._bonus_points}"
        else:
            return f"VIP Silver: скидка {self._discount}%, ранний доступ к новинкам, бонусов: {self._bonus_points}"
    
    # переопределенный __str__ 
    def __str__(self):
        parent_str = super().__str__()
        return parent_str + f"\n   VIP уровень: {self._vip_level.upper()}\n   Скидка: {self._discount}%\n   Бонусов: {self._bonus_points}"