from app import Application
from storage import Storage
from exceptions import ValidationError, NotFoundError, DuplicateError

class CLI:
    def __init__(self, app: Application):
        self.app = app
    
    def start(self):
        while True:
            print("\n" + "=" * 40)
            print("          ГЛАВНОЕ МЕНЮ")
            print("=" * 40)
            print(" 1. Добавить пользователя")
            print(" 2. Показать всех пользователей")
            print(" 3. Найти пользователя")
            print(" 4. Удалить пользователя")
            print(" 5. Сортировка по атрибутам")
            print(" 6. Фильтрация по роли")
            print("-" * 40)
            print(" 0. Выход")
            print("=" * 40)
            
            try:
                choice = int(input(" Ваш выбор: "))
            except ValueError:
                print(" ! Ошибка: введите число!")
                continue
            
            if choice == 1:
                self.add_user()
            elif choice == 2:
                self.show_all()
            elif choice == 3:
                self.find_user()
            elif choice == 4:
                self.delete_user()
            elif choice == 5:
                self.sort()
            elif choice == 6:
                self.filter_by_role()
            elif choice == 0:
                print("\n Работа завершена. До свидания!")
                break
            else:
                print(" ! Ошибка: выберите пункт от 0 до 6")
    
    def add_user(self):
        try:
            nickname = input("Имя: ")
            login = input("Логин: ")
            password = input("Пароль: ")
            role = input("Роль: ")
            
            user = self.app.add_user(nickname, login, password, role)
            print(f"Добавлен: {user.nickname}")
        except (ValidationError, DuplicateError) as e:
            print(f"{e}")
    
    def show_all(self):
        users = self.app.get_all_users()
        if not users:
            print("Нет пользователей")
        else:
            for u in users:
                print(f"{u}")
    
    def find_user(self):
        print('Выберите способ:')
        print('1. Поиск по nickanme')
        print('2. Поиск по login')
        try:
            choice_find = int(input('Способ:'))
        except ValidationError:
            print(f'Введите число!')
            return
        if choice_find == 1:
            try:
                nickname = input("Никнейм: ")
                users = self.app.find_user_by_nickname(nickname)
                for u in users:
                    print(f"Найден: {u}")
            except NotFoundError as e:
                print(f"{e}")
        else:
            try:
                login = input("login:")
                users = self.app.find_user_by_login(login)
                for u in users:
                    print(f'Найден: {u}')
            except NotFoundError as e:
                print(f'{e}')
     
    def delete_user(self):
        try:
            nickname = input("Никнейм для удаления: ")
            confirm = input(f"Удалить {nickname}? (да/нет): ")
            if confirm.lower() == 'да':
                self.app.delete_user_by_nickname(nickname)
                print(f"Удален: {nickname}")
        except NotFoundError as e:
            print(f"{e}")



    def sort(self):
        print('---Варианты сортировки:---')
        print('1. Сортировать по никнейму')
        print('2. Сортировка по логину')
        try:
            choice_sort = int(input('Способ:'))
        except ValueError: 
            print('Введите число!')
            return 
        if choice_sort == 1:
            self.app.sort_by_user_by_nickname()
            print('Сортировка выполнена успешно!')
        else:
            self.app.sort_user_by_login()
            print('Сортировка успешно завершена!')
                
    def filter_by_role(self):
        print('Доступные роли: user, admin, moderator')
        role = input("Роль:")
        try:
            users = self.app.filter_user_by_role(role)
            if not users:
                print(f'Пользователей с такой ролью нету')
            else:
                for u in users:
                    print(f'{u}')
        except ValidationError as e:
            print(f'{e}')


        
            


