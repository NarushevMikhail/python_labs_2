# demo.py
from container import DisplayableCollection, ScorableCollection, Displayable, Scorable
from model import User, AdminUser, VIPUser


def demonstrate_typed_collection() -> None:
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ TYPEDCOLLECTION")
    print("=" * 60)
    
    users = DisplayableCollection[Displayable]()
    
    user1 = User("Alice", "pass123", "alice123", "user")
    user1.update_profile(bio="Python developer", age=25, city="Moscow")
    
    user2 = User("Bob", "pass456", "bob456", "user")
    user2.update_profile(bio="Data scientist", age=30, city="Saint Petersburg")
    
    admin = AdminUser("Admin", "admin123", "admin1", server_access=True, admin_level=4)
    vip = VIPUser("VIPGold", "vip123", "vipgold", vip_level="gold")
    
    users.add(user1)
    users.add(user2)
    users.add(admin)
    users.add(vip)
    
    print("Создана коллекция с 4 объектами:")
    print(f"  - User (Alice)")
    print(f"  - User (Bob)")
    print(f"  - AdminUser (Admin)")
    print(f"  - VIPUser (VIP_Gold)")
    print()
    
    print("Демонстрация валидации типов:")
    print("Попытка добавить объект без метода display()")
    try:
        users.add("not a user object")
    except TypeError as e:
        print(f"  Ошибка: {e}")
    print()


def demonstrate_find() -> None:
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ FIND")
    print("=" * 60)
    
    users = DisplayableCollection[Displayable]()
    
    user1 = User("Alice", "pass123", "alice123", "user")
    user2 = User("Bob", "pass456", "bob456", "user")
    admin = AdminUser("Admin", "admin123", "admin1", server_access=True, admin_level=4)
    
    users.add(user1)
    users.add(user2)
    users.add(admin)
    
    found = users.find(lambda u: u.nickname == "Alice")
    print("Случай 1: find(lambda u: u.nickname == 'Alice')")
    if found:
        print(f"  Найден: {found.display()}")
    else:
        print("  Не найден")
    print()
    
    not_found = users.find(lambda u: u.nickname == "Nonexistent")
    print("Случай 2: find(lambda u: u.nickname == 'Nonexistent')")
    if not_found:
        print(f"  Найден: {not_found.display()}")
    else:
        print("  Результат: None (не найден)")
    print()


def demonstrate_filter() -> None:
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ FILTER")
    print("=" * 60)
    
    users = DisplayableCollection[Displayable]()
    
    user1 = User("Alice", "pass123", "alice123", "user")
    user2 = User("Bob", "pass456", "bob456", "user")
    admin1 = AdminUser("Admin1", "admin123", "admin1", server_access=True, admin_level=5)
    admin2 = AdminUser("Admin2", "admin456", "admin2", server_access=False, admin_level=2)
    vip = VIPUser("VIP_Gold", "vip123", "vipgold", vip_level="gold")
    
    users.add(user1)
    users.add(user2)
    users.add(admin1)
    users.add(admin2)
    users.add(vip)
    
    admins = users.filter(lambda u: "Admin" in u.display())
    print("Фильтр: все админы")
    for admin in admins:
        print(f"  {admin.display()}")
    print()
    
    high_level_admins = users.filter(lambda u: hasattr(u, 'admin_level') and u.admin_level >= 4)
    print("Фильтр: админы с уровнем >= 4")
    for admin in high_level_admins:
        print(f"  {admin.display()}")
    print()


def demonstrate_map() -> None:
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ MAP")
    print("=" * 60)
    
    users = DisplayableCollection[Displayable]()
    
    user = User("Alice", "pass123", "alice123", "user")
    user.update_profile(bio="Python developer", age=25, city="Moscow")
    
    admin = AdminUser("Admin", "admin123", "admin1", server_access=True, admin_level=4)
    vip = VIPUser("VIP_Platinum", "vip123", "vipplatinum", vip_level="platinum")
    
    users.add(user)
    users.add(admin)
    users.add(vip)
    
    print("Исходная коллекция (3 объекта):")
    for u in users.get_all():
        print(f"  {u.display()}")
    print()
    
    print("MAP 1: получение никнеймов (User -> str)")
    nicknames = users.map(lambda u: u.nickname)
    print(f"  Тип результата: list[str]")
    print(f"  Результат: {nicknames}")
    print(f"  Тип первого элемента: {type(nicknames[0]).__name__}")
    print()
    
    print("MAP 2: получение оценок (User -> float)")
    scores = users.map(lambda u: u.score())
    print(f"  Тип результата: list[float]")
    print(f"  Результат: {scores}")
    print(f"  Тип первого элемента: {type(scores[0]).__name__}")
    print()
    
    print("MAP 3: преобразование в строки приветствия (User -> str)")
    greetings = users.map(lambda u: f"Hello, {u.nickname}!")
    print(f"  Тип результата: list[str]")
    print(f"  Результат: {greetings}")
    print()


def demonstrate_protocol_without_inheritance() -> None:
    print("=" * 60)
    print("СЦЕНАРИЙ 1: DISPLAYABLE PROTOCOL")
    print("=" * 60)
    
    print("Доказательство: классы НЕ наследуются от Displayable")
    print(f"  User наследует Displayable? {issubclass(User, Displayable)}") #наследуется ли класс от другого 
    print(f"  AdminUser наследует Displayable? {issubclass(AdminUser, Displayable)}")
    print(f"  VIPUser наследует Displayable? {issubclass(VIPUser, Displayable)}")
    print()
    
    display_collection = DisplayableCollection[Displayable]()
    
    user = User("Alice", "pass123", "alice123", "user")
    admin = AdminUser("Admin", "admin123", "admin1", server_access=True, admin_level=4)
    vip = VIPUser("VIP_Gold", "vip123", "vipgold", vip_level="gold")
    
    display_collection.add(user)
    display_collection.add(admin)
    display_collection.add(vip)
    
    print("Коллекция DisplayableCollection содержит объекты разных типов:")
    print(f"  Количество элементов: {len(display_collection)}")
    print("  Вызов метода display() для каждого:")
    for item in display_collection.get_all():
        print(f"    {item.display()}")
    print()
    
    print("=" * 60)
    print("СЦЕНАРИЙ 2: SCORABLE PROTOCOL")
    print("=" * 60)
    
    print("Доказательство: классы НЕ наследуются от Scorable")
    print(f"  User наследует Scorable? {issubclass(User, Scorable)}")
    print(f"  AdminUser наследует Scorable? {issubclass(AdminUser, Scorable)}")
    print(f"  VIPUser наследует Scorable? {issubclass(VIPUser, Scorable)}")
    print()
    
    score_collection = ScorableCollection[Scorable]()
    
    user1 = User("Alice", "pass123", "alice123", "user")
    user1.update_profile(bio="Developer", age=25, city="Moscow")
    
    user2 = User("Bob", "pass456", "bob456", "user")
    
    admin = AdminUser("Admin", "admin123", "admin1", server_access=True, admin_level=5)
    vip = VIPUser("VIP_Platinum", "vip123", "vipplatinum", vip_level="platinum")
    
    score_collection.add(user1)
    score_collection.add(user2)
    score_collection.add(admin)
    score_collection.add(vip)
    
    print("Коллекция ScorableCollection содержит объекты разных типов:")
    print(f"  Количество элементов: {len(score_collection)}")
    print("  Вызов метода score() для каждого:")
    for item in score_collection.get_all():
        print(f"    {item.display()} -> оценка: {item.score()}")
    print()
    
    print(f"Средняя оценка по коллекции: {score_collection.get_average_score():.2f}")
    print(f"Все оценки: {score_collection.get_scores()}")
    print()


demonstrate_typed_collection()
demonstrate_find()
demonstrate_filter()
demonstrate_map()
demonstrate_protocol_without_inheritance()
