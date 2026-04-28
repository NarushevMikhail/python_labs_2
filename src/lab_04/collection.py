from functools import cmp_to_key

class UserList:
    def __init__(self):
        self._items = []

    def add(self, item):
        # Убираем проверку типа или оставляем без импорта
        # Проверка будет позже через hasattr
        if not hasattr(item, 'nickname') or not hasattr(item, 'login'):
            raise TypeError(f'Добавлять можно только пользователей, передано: {item}')
        
        if any(anyuser is item for anyuser in self._items):
            raise ValueError(f'Дубликат объекта: {item}')
        
        elif any(anyuser.nickname == item.nickname for anyuser in self._items): 
            raise ValueError(f'Пользователь с таким nickname: {item.nickname}, уже существует')
        
        elif any(anyuser.login == item.login for anyuser in self._items):
            raise ValueError(f'Пользователь с таким login: {item.login}, уже существует')
        
        else:   
            self._items.append(item)

    def remove(self, item):
        if not hasattr(item, 'nickname'):
            raise TypeError(f'Можно удалить только пользователя, передано: {item}')
        elif item not in self._items:
            raise TypeError(f'Такого объекта не существует')
        self._items.remove(item)
    
    def remove_at(self, index):
        if not isinstance(index, int):
            raise TypeError(f'Индекс должен быть числом, передан: {index}')
        if index < 0 or index >= len(self._items):
            raise IndexError(f'Индекс {index} вне диапазона (0-{len(self._items)-1})')
        removed = self._items.pop(index)
        return removed
        
    def get_all(self):
        return self._items
    
    def find_by_nickname(self, nickname):
        if not isinstance(nickname, str):
            raise TypeError(f'Введённый nickname не является строкой!')
        result = [user for user in self._items if user.nickname == nickname]
        return result
    
    def find_by_login(self, login):
        if not isinstance(login, str):
            raise TypeError('Введённый login не является строкой!')
        return [user for user in self._items if user.login == login]
    
    def find_by_role(self, role):
        if not isinstance(role, str):
            raise TypeError('Введённая role не является строкой!')
        return [user for user in self._items if user.role == role.lower()]
    
    def sort_by_nickname(self, reverse=False):
        self._items.sort(key=lambda user: user.nickname, reverse=reverse)
        return self._items
    
    def sort_by_login(self, reverse=False):
        self._items.sort(key=lambda user: user.login, reverse=reverse)
        return self._items

    def sort_by_role(self, reverse=False):
        self._items.sort(key=lambda user: user.role, reverse=reverse)
        return self._items
    
    def get_with_profile(self):
        new_collection = UserList()
        for user in self._items:
            if user._bio or user._age > 0 or user._city:
                new_collection.add(user)
        return new_collection
    
    def get_by_role(self, role):
        if not isinstance(role, str):
            raise TypeError('Роль должна быть строкой')
        new_collection = UserList()
        for user in self._items:
            if user.role == role.lower():
                new_collection.add(user)
        return new_collection

    def get_admins(self):
        return self.get_by_role('admin')   

    def get_users(self):
        return self.get_by_role('user')

    def get_moderators(self):
        return self.get_by_role('moderator') 
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        return self._items[index]     
    
    def __str__(self):
        if len(self._items) == 0:
            return 'Всего пользователей: 0 \nсписок всех пользователей: []'
        return f'Всего пользователей: {len(self._items)} \nсписок всех пользователей: {self._items}'
    
    ### Новые методы для интрефйесов
    def get_printable(self): #вовзращает объекты, реализующие тот или иной интрефейс 
        from interfaces import Printable
        return [item for item in self._items if isinstance(item, Printable)]
    
    def get_comparable(self):
        from interfaces import Comparable
        return [item for item in self._items if isinstance(item, Comparable)]
    
    def get_profile(self):
        from interfaces import Profile
        return [item for item in self._items if isinstance(item, Profile)]
    
    def get_authentication(self):
        from interfaces import Authentication
        return [item for item in self._items if isinstance(item, Authentication)]
    

    def sort_by_comparable(self, reverse = False):
        
        from interfaces import Comparable

        comparable = self.get_comparable()
        non_comparable = [item for item in self._items if not isinstance(item, Comparable)]

        comparable.sort(key = cmp_to_key(lambda a, b: a.compare_to(b))) #превращаем функцию сравнения в ключ для сортировки
        
        if reverse:
            comparable.reverse()

        self._items = comparable + non_comparable
        return self._items

    def print_all_via_printable(self):
        from interfaces import Printable

        for item in self._items:
            if isinstance(item, Printable):
                print(f'{item.print_str()}')
            else:
                print(f'{item}, не поддерживает Printable')