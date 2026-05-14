from lab_03.base import AdminUser, VIPUser


#strategies - алгоритм, который можно передать, как параметр 
def by_nickname(user):
    return user.nickname

def by_age(user):
    return user._age

def by_role_and_nickname(user):
    return (user.role, user.nickname)

def by_login(user):
    return user.login

def by_role(user):
    return user.role

def by_admin_level(user):
    if isinstance(user, AdminUser):
        return user.admin_level
    return 0

def by_vip_level(user):
    try:
        levels = {'platinum': 4, 'gold': 3, 'silver': 2}
        return levels.get(user.vip_level, 1)
    except AttributeError:
        return 1

#функции - фильтры
def is_adult(user):
    return user._age >= 18 #True, if age >= 18

def is_teenager(user):
    return 13 <= user._age <= 17 #True

def is_vip_instance(user):
    return isinstance(user, VIPUser)

def is_admin(user):
    return user.role == 'admin'

def is_admin_instance(user):
    return isinstance(user, AdminUser)

def has_profile_filled(user):
    return bool(user._bio) or user._age > 0 or bool(user._city)

#фабрики функций
def make_age_filter(min_age, max_age=None):
    def filter_fn(user):
        age = user._age
        if max_age is None:
            return age >= min_age
        else:
            return min_age <= age <= max_age
    return filter_fn


def make_role_filter(allowed_roles):
    if isinstance(allowed_roles, str):
        allowed_roles = [allowed_roles]
    
    def filter_fn(user):
        return user.role in allowed_roles
    return filter_fn


def make_discount_applier(discount_percent):
    def apply_discount(price):
        return price * (100 - discount_percent) / 100
    return apply_discount


#callable - объекты для паттерана стратегия
class DiscountStrategy: #класс - статегия с состоянием
    def __init__(self, percent):

        self.percent = percent #% of discount
        self.total_discount = 0
        self.applied_items = []
    
    def __call__(self, item): #метод, который делает объект вызываемым
        if hasattr(item, 'price'): #check that object has a atribut 
            discount = item.price * self.percent / 100
            self.total_discount += discount
            self.applied_items.append({
                'item': item.nickname if hasattr(item, 'nickname') else str(item),
                'original_price': item.price,
                'discount': discount,
                'new_price': item.price - discount
            })
            return item.price - discount
        return item
    
    def get_total_discount(self):
        return self.total_discount #общая скидка
    
    def get_report(self):
        return self.applied_items


class UpgradeStrategy:
    def __init__(self, new_role):
        self.new_role = new_role
        self.upgraded_users = []
    
    def __call__(self, user):
        old_role = user.role
        user.role = self.new_role
        self.upgraded_users.append({
            'user': user.nickname,
            'old_role': old_role,
            'new_role': self.new_role
        })
        return f"  → {user.nickname}: {old_role} → {self.new_role}"
    
    def get_upgraded_users(self):
        return self.upgraded_users


class BonusStrategy:
    def __init__(self, base_bonus=100):
        self.base_bonus = base_bonus
        self.bonus_multiplier = {
            'silver': 1,
            'gold': 2,
            'platinum': 3
        }
        self.total_bonus_given = 0
        self.bonus_log = []
    
    def __call__(self, user): #method that make a callable object ()
        if hasattr(user, 'vip_level') and user.vip_level in self.bonus_multiplier:
            multiplier = self.bonus_multiplier[user.vip_level]
            bonus = self.base_bonus * multiplier
            if hasattr(user, 'add_bonus_points'):
                user.add_bonus_points(bonus)
                self.total_bonus_given += bonus
                self.bonus_log.append({
                    'user': user.nickname,
                    'vip_level': user.vip_level,
                    'bonus': bonus
                })
                return f"  → {user.nickname} ({user.vip_level}): +{bonus} бонусов"
        return f"  → {user.nickname}: не VIP, бонусов нет"
    
    def get_total_bonus(self):
        return self.total_bonus_given #общее количество начисленных бонусов


class PrintStrategy:
    def __init__(self, verbose=False):
        self.verbose = verbose
    
    def __call__(self, user):
        if self.verbose:
            return f"  • {user.nickname} | {user.role} | {user._age} лет"
        return f"  • {user.nickname}"


#functions fot map 
def user_to_dict(user):
    return {
        'nickname': user.nickname,
        'role': user.role,
        'age': user._age,
        'login': user.login
    }


def user_to_short_str(user):
    return f"{user.nickname} ({user.role})"

def extract_nickname(user):
    return user.nickname

def extract_role(user):
    return user.role

#доп функции для цепочек
def apply_discount_10(item):
    if hasattr(item, 'price'):
        return item.price * 0.9
    return item


def apply_discount_20(item):
    if hasattr(item, 'price'):
        return item.price * 0.8
    return item


def activate_user(user):
    user.is_active = True
    return user


def print_user_info(user):
    print(f"  {user.nickname} - {user.role}")
    return user