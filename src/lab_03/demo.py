import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab_02'))

from models import User
from base import AdminUser, VIPUser
from collection import UserList

print("\n" + "=" * 65)
print("     ЛАБОРАТОРНАЯ РАБОТА - НАСЛЕДОВАНИЕ И ПОЛИМОРФИЗМ")
print("=" * 65)

collection = UserList()

print("\n" + "=" * 65)
print("  1. СОЗДАНИЕ ОБЪЕКТОВ РАЗНЫХ ТИПОВ")
print("=" * 65)

# 1.1 Обычный пользователь
print("\n-- 1.1 Обычный пользователь")
print("   nickname='UserOne', password='pass123', login='userone', role='user'")
try:
    user1 = User("UserOne", "pass123", "userone", "user")
    collection.add(user1)
    print("    РЕЗУЛЬТАТ: УСПЕШНО ДОБАВЛЕН")
except Exception as e:
    print(f"    РЕЗУЛЬТАТ: ОШИБКА - {e}")

# 1.2 VIP пользователь Gold
print("\n-- 1.2 VIP пользователь (Gold)")
print("   nickname='AliceGold', password='gold2024', login='alicegold', role='user', vip_level='gold'")
try:
    vip1 = VIPUser("AliceGold", "gold2024", "alicegold", "user", "gold")
    collection.add(vip1)
    print("   РЕЗУЛЬТАТ: УСПЕШНО ДОБАВЛЕН")
except Exception as e:
    print(f"    РЕЗУЛЬТАТ: ОШИБКА - {e}")

# 1.3 Администратор
print("\n-- 1.3 Администратор")
print("   nickname='BobAdmin', password='admin999', login='bobadmin', role='admin' (через super), server_access=True, admin_level=4")
try:
    admin1 = AdminUser("BobAdmin", "admin999", "bobadmin", True, 4)
    collection.add(admin1)
    print("    РЕЗУЛЬТАТ: УСПЕШНО ДОБАВЛЕН")
except Exception as e:
    print(f"    РЕЗУЛЬТАТ: ОШИБКА - {e}")

# 1.4 VIP пользователь Platinum
print("\n-- 1.4 VIP пользователь (Platinum)")
print("   nickname='CharliePlat', password='plat7777', login='charlieplat', role='user', vip_level='platinum'")
try:
    vip2 = VIPUser("CharliePlat", "plat7777", "charlieplat", "user", "platinum")
    collection.add(vip2)
    print("    РЕЗУЛЬТАТ: УСПЕШНО ДОБАВЛЕН")
except Exception as e:
    print(f"    РЕЗУЛЬТАТ: ОШИБКА - {e}")

# 1.5 Второй обычный пользователь
print("\n-- 1.5 Второй обычный пользователь")
print("   nickname='EveBrown', password='brown2024', login='evebrown', role='user'")
try:
    user2 = User("EveBrown", "brown2024", "evebrown", "user")
    collection.add(user2)
    print("    РЕЗУЛЬТАТ: УСПЕШНО ДОБАВЛЕН")
except Exception as e:
    print(f"    РЕЗУЛЬТАТ: ОШИБКА - {e}")

# 1.6 Модератор
print("\n-- 1.6 Модератор")
print("   nickname='ModMike', password='mod1234', login='mikemod', role='moderator'")
try:
    mod1 = User("ModMike", "mod1234", "mikemod", "moderator")
    collection.add(mod1)
    print("    РЕЗУЛЬТАТ: УСПЕШНО ДОБАВЛЕН")
except Exception as e:
    print(f"    РЕЗУЛЬТАТ: ОШИБКА - {e}")

print("\n" + "=" * 65)
print(f"  ИТОГ: В коллекции {len(collection)} объектов")
print("=" * 65)

print("\n" + "=" * 65)
print("  2. ВЫВОД КОЛЛЕКЦИИ")
print("=" * 65)

try:
    print(f"\n{collection}")
except Exception as e:
    print(f"   ОШИБКА: {e}")

print("\n" + "=" * 65)
print("  3. НОВЫЕ МЕТОДЫ VIPUser")
print("=" * 65)

vip_gold = None
vip_platinum = None
for user in collection:
    if isinstance(user, VIPUser):
        if hasattr(user, 'vip_level') and user.vip_level == 'gold':
            vip_gold = user
        elif hasattr(user, 'vip_level') and user.vip_level == 'platinum':
            vip_platinum = user

if vip_gold:
    print(f"\n   VIP Gold: {vip_gold.nickname}")
    try:
        print(f"   make_purchase(1500): {vip_gold.make_purchase(1500)}")
    except Exception as e:
        print(f"   make_purchase(1500): ОШИБКА - {e}")
    
    try:
        print(f"   add_bonus_points(100): {vip_gold.add_bonus_points(100)}")
    except Exception as e:
        print(f"   add_bonus_points(100): ОШИБКА - {e}")
    
    try:
        print(f"   get_bonus_points(): {vip_gold.get_bonus_points()}")
    except Exception as e:
        print(f"   get_bonus_points(): ОШИБКА - {e}")
else:
    print("\n    VIP Gold не найден")

print("\n" + "=" * 65)
print("  4. НОВЫЕ МЕТОДЫ AdminUser")
print("=" * 65)

admin_obj = None
for user in collection:
    if isinstance(user, AdminUser):
        admin_obj = user
        break

normal_user = None
for user in collection:
    if isinstance(user, User) and not isinstance(user, (VIPUser, AdminUser)):
        normal_user = user
        break

if admin_obj:
    print(f"\n   Администратор: {admin_obj.nickname}")
    
    if normal_user:
        try:
            print(f"   assign_moderator({normal_user.nickname}): {admin_obj.assign_moderator(normal_user)}")
        except Exception as e:
            print(f"   assign_moderator(): ОШИБКА - {e}")
    
    try:
        print(f"   get_managed_users_count(): {admin_obj.get_managed_users_count()}")
    except Exception as e:
        print(f"   get_managed_users_count(): ОШИБКА - {e}")
    
    try:
        print(f"   show_action_log(): {admin_obj.show_action_log()}")
    except Exception as e:
        print(f"   show_action_log(): ОШИБКА - {e}")
else:
    print("\n    Администратор не найден")

print("\n" + "=" * 65)
print("  5. ПЕРЕОПРЕДЕЛЕННЫЙ __str__")
print("=" * 65)

for user in collection:
    try:
        print(f"\n--- {user.__class__.__name__}: {user.nickname} ---")
        print(user)
    except Exception as e:
        print(f"   ОШИБКА: {e}")

print("\n" + "=" * 65)
print("  6. ПОЛИМОРФНОЕ ПОВЕДЕНИЕ (get_access_rights)")
print("=" * 65)

print("\n   Результаты вызова get_access_rights():\n")
for user in collection:
    try:
        print(f"    {user.nickname} ({user.__class__.__name__})")
        print(f"      → {user.get_access_rights()}")
        print()
    except Exception as e:
        print(f"   ОШИБКА у {user.nickname}: {e}")

print("\n" + "=" * 65)
print("  7. ПРОВЕРКА ТИПОВ ЧЕРЕЗ isinstance()")
print("=" * 65)

for user in collection:
    try:
        print(f"\n   {user.nickname}:")
        print(f"      isinstance(User): {isinstance(user, User)}")
        print(f"      isinstance(VIPUser): {isinstance(user, VIPUser)}")
        print(f"      isinstance(AdminUser): {isinstance(user, AdminUser)}")
    except Exception as e:
        print(f"   ОШИБКА: {e}")

print("\n" + "=" * 65)
print("  8. ФИЛЬТРАЦИЯ КОЛЛЕКЦИИ ПО ТИПУ")
print("=" * 65)

try:
    admins = collection.get_admins()
    print("\n    АДМИНИСТРАТОРЫ:")
    for user in admins:
        print(f"      - {user.nickname}")
except Exception as e:
    print(f"\n   ОШИБКА: {e}")

try:
    users_only = collection.get_users()
    print("\n    ОБЫЧНЫЕ ПОЛЬЗОВАТЕЛИ:")
    for user in users_only:
        print(f"      - {user.nickname}")
except Exception as e:
    print(f"\n   ОШИБКА: {e}")

vip_users = [user for user in collection if isinstance(user, VIPUser)]
print("\n   VIP ПОЛЬЗОВАТЕЛИ:")
for user in vip_users:
    try:
        print(f"      - {user.nickname} (уровень: {user.vip_level})")
    except:
        print(f"      - {user.nickname}")


print("\n" + "=" * 65)
print("  9. СЦЕНАРИЙ: РАБОТА С VIP И БОНУСАМИ")
print("=" * 65)

if vip_platinum:
    print(f"\n   Platinum VIP: {vip_platinum.nickname}")
    try:
        print(f"   Покупка на 5000 руб: {vip_platinum.make_purchase(5000)}")
    except Exception as e:
        print(f"   ОШИБКА: {e}")
    
    try:
        print(f"   Покупка на 3200 руб: {vip_platinum.make_purchase(3200)}")
    except Exception as e:
        print(f"   ОШИБКА: {e}")
    
    try:
        print(f"   Статус: {vip_platinum.get_access_rights()}")
    except Exception as e:
        print(f"   ОШИБКА: {e}")
else:
    print("\n   Platinum VIP не найден")


print("\n" + "=" * 65)
print("  10. СЦЕНАРИЙ: АДМИНИСТРИРОВАНИЕ")
print("=" * 65)

if admin_obj:
    print(f"\n   Администратор: {admin_obj.nickname}")
    
    # Находим пользователя для назначения
    target_user = None
    for user in collection:
        if user.role == 'user' and not isinstance(user, VIPUser) and user != normal_user:
            target_user = user
            break
    
    if target_user:
        try:
            print(f"   Назначение модератором {target_user.nickname}: {admin_obj.assign_moderator(target_user)}")
        except Exception as e:
            print(f"   ОШИБКА: {e}")
    
    try:
        print(f"   Управляемых пользователей: {admin_obj.get_managed_users_count()}")
    except Exception as e:
        print(f"   ОШИБКА: {e}")
    
    try:
        print(f"   Лог действий: {admin_obj.show_action_log()}")
    except Exception as e:
        print(f"   ОШИБКА: {e}")
else:
    print("\n   Администратор не найден")

