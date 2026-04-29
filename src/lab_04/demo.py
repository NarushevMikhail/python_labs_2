from models import User, Guest
from interfaces import Profile, Authentication, Printable, Comparable
from collection import UserList


#  Универсальная функция через интерфейс 
def show_all_profiles(objects: list[Profile]): # использование интрейфса, как типа
    for obj in objects:
        print(obj.view_profile()['nickname'])


# Новая универсальная функция через Printable 
def print_all_printable(objects: list[Printable]):
    for obj in objects:
        print(f"   {obj.print_str()}")


print("\n1. Создаём объекты:")
user = User("Alice", "pass123", "alice@mail", "user")
admin = User("Bob", "admin123", "bob@mail", "admin")
guest = Guest("session_001")
print(f"   Пользователь: {user.nickname}")
print(f"   Администратор: {admin.nickname}")
print(f"   Гость: {guest.nickname}")


print("\n2. Разное поведение update_profile():")
print("   Пользователь:")
result = user.update_profile(bio="Люблю Python", age=25, city="Москва")
print(f"      Результат: {result}")

print("   Гость:")
try:
    guest.update_profile(bio="Хакер")
except PermissionError as e:
    print(f"      Ошибка: {e}")


print("\n3. view_profile():")
print(f"   Пользователь: {user.view_profile()}")
print(f"   Гость: {guest.view_profile()}")


print("\n4. Authentication (только у User):")
print(f"   check_password('pass123'): {user.check_password('pass123')}")
print(f"   check_login('alice@mail'): {user.check_login('alice@mail')}")


print("\n5. Полиморфизм (одна функция для всех):")

def show_info(obj):
    profile = obj.view_profile()
    print(f"   {profile['nickname']} - роль: {profile['role']}")

show_info(user)
show_info(guest)

print("\n" + "=" * 50)
print("Иинтерфейс, как тип")
print("=" * 50)

print('\n6. Проверка через isinstance')
print(f'isinstance(user, Profile) = {isinstance(user, Profile)}')
print(f'isinstance(user, Authentication) = {isinstance(user, Authentication)}')
print(f'isinstance(guest, Profile) = {isinstance(guest, Profile)}')
print(f'isinstance(guest, Authentication) = {isinstance(guest, Authentication)}')

print('\n7. Проверка универсального метода (show_all_profiles)')
show_all_profiles([user, guest, admin])

print("\n" + "=" * 50)
print("Новые интрейсы (Printable, Comparable)")
print("=" * 50)

print("\n8. Проверка новых интерфейсов:")
print(f"   isinstance(user, Printable) = {isinstance(user, Printable)}")
print(f"   isinstance(user, Comparable) = {isinstance(user, Comparable)}")
print(f"   isinstance(guest, Printable) = {isinstance(guest, Printable)}")
print(f"   isinstance(guest, Comparable) = {isinstance(guest, Comparable)}")

print("\n9. Метод print_str() (разное поведение):")
print(f"   user.print_str()  → {user.print_str()}")
print(f"   admin.print_str() → {admin.print_str()}")
print(f"   guest.print_str() → {guest.print_str()}")

print("\n10. Метод compare_to() (прямой вызов):")
print(f"   user.compare_to(admin) = {user.compare_to(admin)}")
print(f"   admin.compare_to(user) = {admin.compare_to(user)}")
print(f"   user.compare_to(user)  = {user.compare_to(user)}")

print("\n" + "=" * 50)
print("Работа с коллекцией (UserList)")
print("=" * 50)


collection = UserList()
collection.add(user)
collection.add(admin)
collection.add(guest)
print("\n11. Создана коллекция с 3 объектами")


print("\n11. Фильтрация по интерфейсу Printable (get_printable):")
printable_objects = collection.get_printable()
print(f"   Найдено объектов: {len(printable_objects)}")
for obj in printable_objects:
    print(f"   - {obj.print_str()}")


print("\n12. Фильтрация по интерфейсу Comparable (get_comparable):")
comparable_objects = collection.get_comparable()
print(f"   Найдено объектов: {len(comparable_objects)}")
for obj in comparable_objects:
    print(f"   - {obj.print_str()}")


print("\n13. Вывод всех объектов через Printable:")
collection.print_all_via_printable()


print("\n14. Сортировка через Comparable:")
print("   До сортировки:", [obj.nickname for obj in collection.get_all()])
collection.sort_by_comparable()
print("   После сортировки:", [obj.nickname for obj in collection.get_all()])


print("\n15. Вывод после сортировки:")
collection.print_all_via_printable()


print("\n16. Сортировка в обратном порядке (reverse=True):")
collection.sort_by_comparable(reverse=True)
collection.print_all_via_printable()


print("\n17. Универсальная функция с Printable:")
print_all_printable(collection.get_printable())

