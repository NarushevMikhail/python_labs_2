from model import User

class UserList: #класс коллекции

    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, User):
            raise TypeError(f'Добавлять можно только пользователей, передано: {item}')
        
        if any(anyuser is item for anyuser in self._items):  # ← проверка на дубликат объекта
            raise ValueError(f'Дубликат объекта: {item}')
        
        elif any(anyuser.nickname == item.nickname for anyuser in self._items): 
            raise ValueError(f'Пользователь с таким nickname: {item.nickname}, уже существует')
        
        elif any(anyuser.login == item.login for anyuser in self._items):
            raise ValueError(f'Пользователь с таким login: {item.login}, уже существует')
        
        else:   
            self._items.append(item)

    def remove(self, item):
        if not isinstance(item, User):
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
            raise TypeError(f'Введённый nicname не является строкой!')
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
    
    def sort_by_nickname(self, reverse = False): #сортировка по возврастанию
        self._items.sort(key=lambda user: user.nickname, reverse = reverse) #key = lambda - сортировать не по самим объектам, а по их совйству
        return self._items
    
    def sort_by_login(self, reverse=False):
        self._items.sort(key=lambda user: user.login, reverse=reverse) # reverse = False, сортировка по порядку
        return self._items

    def sort_by_role(self, reverse = False):
        self._items.sort(key=lambda user: user.role, reverse = reverse) # key - по какому признаку сортировать, lambda - возьми ученика и достань из него
        return self._items
    

    #логические операции над коллекцией: 
    
    def get_with_profile(self): #возвращает коллекцию пользователей с заполненым профилем
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
    
    # Магические методы
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self): # iter позволяет нам последовательно перебирать элементы коллекции
        return iter(self._items)
    
    def __getitem__(self, index):
        return self._items[index]     
    
    def __str__(self):
        return f'Всего пользователей: {len(self._items)} \nсписок всех пользователей: {self._items}'
    

    