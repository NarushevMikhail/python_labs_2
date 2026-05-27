# app.py
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from lab_01.model import User
from lab_02.collection import UserList
from lab_05.collection import UserList
from storage import Storage
from exceptions import ValidationError, NotFoundError, DuplicateError


class Application:
    """Бизнес-логика приложения"""
    
    def __init__(self, storage: Storage):
        self.storage = storage
        self.collection = UserList()
        self._load_data()
    
    def _load_data(self):
        "Загружает данные из хранилища"
        users_data = self.storage.load()
        for data in users_data:
            try:
                user = User(
                    nickname=data['nickname'],
                    login=data['login'],
                    password=data['password'],
                    role=data['role']
                )
                self.collection.add(user)
            except Exception as e:
                print(f"Ошибка загрузки пользователя: {e}")
    
    def _save_data(self):
        """Сохраняет данные в хранилище"""
        self.storage.save(self.collection.get_all())
    
    def add_user(self, nickname, login, password, role):
        
        if not nickname or not nickname.strip():
            raise ValidationError("Никнейм обязателен и не может быть пустым")
        
        if not login or not login.strip():
            raise ValidationError("Логин обязателен и не может быть пустым")
        
        existing_by_nickname = self.collection.find_by_nickname(nickname)
        if existing_by_nickname:
            raise DuplicateError(f"Пользователь с никнеймом '{nickname}' уже существует")
        
        existing_by_login = self.collection.find_by_login(login)
        if existing_by_login:
            raise DuplicateError(f"Пользователь с логином '{login}' уже существует")
        
        if len(password) < 6:
            raise ValidationError("Пароль слишком короткий (минимум 6 символов)")
        
        if len(password) > 64:
            raise ValidationError("Пароль слишком длинный (максимум 64 символа)")
        
        if not any(c.isdigit() for c in password):
            raise ValidationError("Пароль должен содержать хотя бы одну цифру")
        allowed_roles = ['user', 'admin', 'moderator']
        if role.lower() not in allowed_roles:
            raise ValidationError(f"Недопустимая роль. Разрешены: {', '.join(allowed_roles)}")
        
        if login.isdigit():
            raise ValidationError("Логин не может состоять только из цифр")
        
        if login.startswith('@'):
            raise ValidationError("Логин не может начинаться с символа @")
        
        try:
            user = User(
                nickname=nickname,
                login=login,
                password=password,
                role=role.lower()
            )
            self.collection.add(user)
            self._save_data()
            return user
        except (TypeError, ValueError) as e:
            raise ValidationError(str(e))
    
    def get_all_users(self):
        return self.collection.get_all()
    
    def find_user_by_nickname(self, nickname):
        if not nickname or not nickname.strip():
            raise ValidationError("Никнейм не может быть пустым")
        
        users = self.collection.find_by_nickname(nickname)
        if not users:
            raise NotFoundError(f"Пользователь с никнеймом '{nickname}' не найден")
        return users
    
    def find_user_by_login(self, login):
        if not login or not login.strip():
            raise ValidationError("Логин не может быть пустым")
        
        users = self.collection.find_by_login(login)
        if not users:
            raise NotFoundError(f"Пользователь с логином '{login}' не найден")
        return users
    
    def delete_user_by_nickname(self, nickname):
        users = self.find_user_by_nickname(nickname)
        if users:
            user = users[0]
            index = self.collection._items.index(user)
            self.collection.remove_at(index)
            self._save_data()
            return user
        raise NotFoundError(f"Пользователь с никнеймом '{nickname}' не найден")
    
    def get_stats(self):
        users = self.collection.get_all()
        
        # БИЗНЕС-ЛОГИКА: подсчет статистики
        stats = {
            'total': len(users),
            'admins': sum(1 for u in users if u.role == 'admin'),
            'users': sum(1 for u in users if u.role == 'user'),
            'moderators': sum(1 for u in users if u.role == 'moderator')
        }
        return stats
    
    def update_user_role(self, nickname, new_role):
        # БИЗНЕС-ПРОВЕРКИ
        allowed_roles = ['user', 'admin', 'moderator']
        if new_role.lower() not in allowed_roles:
            raise ValidationError(f"Недопустимая роль. Разрешены: {allowed_roles}")
        
        users = self.find_user_by_nickname(nickname)
        if users:
            user = users[0]
            old_role = user.role
            user.role = new_role.lower()
            self._save_data()
            return user, old_role
        raise NotFoundError(f"Пользователь '{nickname}' не найден")
    
    def sort_by_user_by_nickname(self):
        self.collection.sort_by_nickname()
        self._save_data()        
    
    def sort_user_by_login(self):
        self.collection.sort_by_login()
        self._save_data()
    
    def filter_user_by_role(self, role):
        allowed_roles = ['user', 'admin', 'moderator']
        if role.lower() not in allowed_roles:
            raise ValidationError(f'Недопустимая роль: {allowed_roles}')
        users = self.collection.get_all()
        filtered = [u for u in users if u.role == role]
        return filtered