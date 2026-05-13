import sys
import os

# Добавляем папку src в путь поиска модулей
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab_03.base import AdminUser, VIPUser
from lab_02.collection import UserList
from lab_01.model import User
from strategies import *



class ExtendedUserList(UserList): #класс коллекции с новыми методами (расширенный список)
    
    def sort_by(self, key_func, reverse=False):
        self._items.sort(key=key_func, reverse=reverse)
        return self
    
    def filter_by(self, predicate):
        new_collection = ExtendedUserList()
        for item in self._items:
            if predicate(item):
                new_collection.add(item)
        return new_collection
    
    def apply(self, func):
        for i, item in enumerate(self._items):
            result = func(item)
            # Если функция вернула новое значение, обновляем элемент
            if result is not None:
                if isinstance(result, tuple) and len(result) == 2:
                    # Для случаев, когда функция возвращает (индекс, новое_значение)
                    pass
                elif result != item:
                    # Если результат другой, чем исходный элемент
                    pass
        return self
    
    def map_to(self, transform_func):
        return list(map(transform_func, self._items))
    
    def get_all(self):
        """Возвращает список всех элементов"""
        return self._items
    
    def print_all(self, title=None):
        """Выводит все элементы коллекции (для демонстрации)"""
        if title:
            print(f"\n{title}")
            print("-" * 50)
        for i, user in enumerate(self._items, 1):
            vip_info = f" [VIP: {user.vip_level}]" if hasattr(user, 'vip_level') else ""
            admin_info = f" [Admin lvl: {user.admin_level}]" if hasattr(user, 'admin_level') else ""
            print(f"  {i}. {user.nickname} ({user.role}){vip_info}{admin_info} - {user._age} лет")
        return self


def create_demo_collection():
    """Создание коллекции объектов (минимум 5 штук)"""
    collection = ExtendedUserList()

    # Обычные пользователи
    user1 = User("alex_kuz", "pass12345", "alex92", "user")
    user1.update_profile(bio="Люблю программирование", age=25, city="Москва")
    user1.price = 1000

    user2 = User("mary_jj", "mary2000", "maryjj", "user")
    user2.update_profile(age=16, city="СПб")
    user2.price = 500

    user3 = User("bob_builder", "bob12345", "bobthebuilder", "user")
    user3.update_profile(bio="Строю дома", age=30, city="Новосибирск")
    user3.price = 2000

    # Администраторы
    admin1 = AdminUser("super_admin", "admin999", "superadmin", server_access=True, admin_level=5)
    admin1.update_profile(age=35, city="Москва")
    admin1.price = 0

    admin2 = AdminUser("mod_leader", "mod12345", "modleader", server_access=False, admin_level=2)
    admin2.update_profile(age=28, city="Казань")
    admin2.price = 100

    # VIP пользователи
    vip1 = VIPUser("vip_gold", "gold2023", "golduser", role="user", vip_level="gold")
    vip1.update_profile(age=42, bio="VIP клиент с 2019", city="Сочи")
    vip1.add_bonus_points(500)
    vip1.price = 5000

    vip2 = VIPUser("platinum_lord", "plat777", "platinumuser", role="user", vip_level="platinum")
    vip2.update_profile(age=55, bio="Постоянный клиент", city="Москва")
    vip2.add_bonus_points(1500)
    vip2.price = 10000

    collection.add(user1)
    collection.add(user2)
    collection.add(user3)
    collection.add(admin1)
    collection.add(admin2)
    collection.add(vip1)
    collection.add(vip2)

    return collection

#Отработка сценариев
def chain_operations():
    print("\n" + "-"*80)
    print("     Сцнеарий 1: цепочка операций filter_by → sort_by → apply")
    print("-"*80)
    
    # Исходная коллекция
    collection = create_demo_collection()
    collection.print_all("Все пользователи:")
    
    # ШАГ 1: Фильтрация - оставляем только совершеннолетних
    print("\n" + "─"*60)
    print("ШАГ 1: Фильтрация (filter_by) - оставляем только взрослых (is_adult)")
    print("─"*60)
    
    filtered = collection.filter_by(is_adult)
    filtered.print_all("После фильтрации (только взрослые):")
    
    # ШАГ 2: Сортировка по возрасту
    print("\n" + "─"*60)
    print("ШАГ 2: Сортировка (sort_by) - по возрасту (by_age)")
    print("─"*60)
    
    sorted_collection = filtered.sort_by(by_age)
    sorted_collection.print_all("После сортировки по возрасту:")
    
    print("\n" + "─"*60)
    print("ШАГ 3: Применение скидки (apply) - callable-объект DiscountStrategy(15%)")
    print("─"*60)
    
    discount_strategy = DiscountStrategy(15)
    
    print("\nЦены до применения скидки:")
    for user in sorted_collection.get_all():
        if hasattr(user, 'price'):
            print(f"  {user.nickname}: {user.price} руб.")
    
    sorted_collection.apply(discount_strategy)
    
    print("\nЦены после скидки 15%:")
    for user in sorted_collection.get_all():
        if hasattr(user, 'price'):
            print(f"  {user.nickname}: {user.price - (user.price * 0.15):.2f} руб.")
    
    print(f"\nОбщая сумма скидки: {discount_strategy.get_total_discount():.2f} руб.")
    
    # Очищаем и показываем всю цепочку через chaining
    print("\n" + "─"*60)
    print("Это же цепочка, но сделанная проще (method chaiging):") #chaiging - когда мы пишем сразу несколько метолов через точку   
    print("─"*60)
    
    collection2 = create_demo_collection()
    result = (collection2
              .filter_by(is_adult)
              .sort_by(by_age)
              .apply(DiscountStrategy(15)))
    
    result.print_all("Результат цепочки:")


# второй сценарий

def strategy_replacement():
    print("\n" + "-"*80)
    print("     Сценарий 2: замена стратегии без изменения кода коллекции")
    print("-"*80)
    
    collection = create_demo_collection()
    
    print("\n Исходная коллекция (администраторы):")
    admins = collection.filter_by(is_admin)
    admins.print_all("Администраторы:")
    
    # Стратегия 1: сортировка по имени
    print("\n" + "─"*60)
    print(" Стратегия 1: Сортировка по имени (by_nickname)")
    print("─"*60)
    sorted_by_name = sorted(admins.get_all(), key=by_nickname)
    for user in sorted_by_name:
        print(f"  {user.nickname} (admin_level: {user.admin_level if hasattr(user, 'admin_level') else 'N/A'})")
    
    # Стратегия 2: сортировка по уровню админа (другая стратегия!)
    print("\n" + "─"*60)
    print("Стратегия 2: Сортировка по уровню админа (by_admin_level)")
    print("─"*60)
    sorted_by_level = sorted(admins.get_all(), key=by_admin_level, reverse=True)
    for user in sorted_by_level:
        level = user.admin_level if hasattr(user, 'admin_level') else 0
        print(f"  {user.nickname} (admin_level: {level})")
        
    # Демонстрация со скидками
    print("\n" + "─"*60)
    print("Демонстрация замены стратегии скидки:")
    print("─"*60)
    
    vip_users = collection.filter_by(is_vip_instance)
    
    print("\nИсходные цены VIP-пользователей:")
    for user in vip_users.get_all():
        print(f"  {user.nickname}: {user.price} руб.")
    
    # Стратегия скидки 10%
    print("\n стратегия скидки: 10%:")
    discount_10 = DiscountStrategy(10)
    for user in vip_users.get_all():
        new_price = discount_10(user)
        print(f"  {user.nickname}: {user.price} → {new_price:.2f} руб.")
    
    # Создаём новую коллекцию для скидки 30%
    vip_users2 = create_demo_collection().filter_by(is_vip_instance)
    print("\nстратегия скидки 30%:")
    discount_30 = DiscountStrategy(30)
    for user in vip_users2.get_all():
        new_price = discount_30(user)
        print(f"  {user.nickname}: {user.price} → {new_price:.2f} руб.")
    
# Сценарий 3
def callable_strategies():
    print("\n" + "-"*80)
    print("     Сценарий 3: callable - объекты как стратегии")
    print("-"*80)
    
    collection = create_demo_collection()
    
    print("\nИсходные данные:")
    collection.print_all("Все пользователи:")
    
    # Callable-объект 1: DiscountStrategy (скидка)
    print("\n" + "─"*60)
    print("callable - объекты 1: DiscountStrategy (скидка)")
    print("─"*60)
    
    discount = DiscountStrategy(20)
    print(f"\nСоздан объект discount с параметром 20%")
    print(f"Тип объекта: {type(discount)}")
    print(f"Является callable: {callable(discount)}")
    
    print("\nПрименяем скидку к VIP-пользователям:")
    vip_users = collection.filter_by(is_vip_instance)
    for user in vip_users.get_all():
        result = discount(user)
        print(f"  {user.nickname}: {user.price} → {result:.2f} руб.")
    
    print(f"\nСостояние объекта discount (хранит историю):")
    print(f"  Всего скидок применено: {len(discount.applied_items)}")
    print(f"  Общая сумма скидки: {discount.get_total_discount():.2f} руб.")
    
    # Callable-объект 2: BonusStrategy (бонусы)
    print("\n" + "─"*60)
    print("callable - объект 2: BonusStrategy (начисление бонусов)")
    print("─"*60)
    
    bonus_strategy = BonusStrategy(base_bonus=100)
    print(f"\nСоздан объект bonus_strategy с базовым бонусом 100")
    print(f"Тип объекта: {type(bonus_strategy)}")
    print(f"Является callable: {callable(bonus_strategy)}")
    
    print("\nНачисляем бонусы VIP-пользователям:")
    for user in vip_users.get_all():
        result = bonus_strategy(user)
        print(result)
    
    print(f"\n Состояние объекта bonus_strategy (хранит историю):")
    print(f"  Всего начислено бонусов: {bonus_strategy.get_total_bonus()}")
    
    # Callable-объект 3: UpgradeStrategy (повышение роли)
    print("\n" + "─"*60)
    print("callable - объект 3: UpgradeStrategy (повышение роли)")
    print("─"*60)
    
    # Создаём коллекцию обычных пользователей
    regular_users = create_demo_collection().filter_by(lambda u: u.role == 'user' and not isinstance(u, VIPUser))
    
    print("\nДо повышения:")
    regular_users.print_all("Обычные пользователи:")
    
    upgrade = UpgradeStrategy('premium')
    print(f"\nСоздан объект upgrade для повышения до роли 'premium'")
    print(f"Является callable: {callable(upgrade)}")
    
    print("\nПовышаем пользователей:")
    collection.apply(upgrade)
    for user in regular_users.get_all():
        print(f"  {user.nickname}: {user.role}")
    
    print(f"\nСостояние объекта upgrade (хранит историю):")
    for u in upgrade.get_upgraded_users():
        print(f"  {u['user']}: {u['old_role']} → {u['new_role']}")
    
  
#Демонстрация apply()
def apply_method():
    print("\n" + "-"*80)
    print("Демонстрация метода apply()")
    print("-"*80)
    
    collection = create_demo_collection()
    
    print("\nИсходная коллекция:")
    collection.print_all("Все пользователи:")
    
    def activate_user(user):
        user.is_active = True
        return user
    
    collection.apply(activate_user)
    collection.apply(lambda u: setattr(u, 'status', 'active'))
    

    print('-'*50)
    print('Отрабтка: PrintStrategy')
    printer = PrintStrategy(verbose=True)
    for user in collection.get_all():
        print(printer(user))


# Сценарий 1: полная цепочка filter -> sort -> apply
chain_operations()

# Сценарий 2: замена стратегии без изменения кода коллекции
strategy_replacement()

# Сценарий 3: callable-объекты как стратегии
callable_strategies()

#демонстрация apply()
apply_method()
