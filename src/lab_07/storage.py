import json
import os
from pathlib import Path
from exceptions import StorageError

class Storage:
    def __init__(self, filename='users.json'):
        self.data_dir = Path(__file__).parent / 'data'
        self.data_dir.mkdir(exist_ok=True)
        self.filepath = self.data_dir / filename
    
    def save(self, users):
        """Сохраняет список пользователей в файл"""
        try:
            data = []
            for u in users:
                user_dict = {
                    'nickname': u.nickname,     
                    'login': u.login,            
                    'password': u.password,      
                    'role': u.role,             
                }
                
                if hasattr(u, '_bio'):
                    user_dict['bio'] = u._bio
                if hasattr(u, '_age'):
                    user_dict['age'] = u._age
                if hasattr(u, '_city'):
                    user_dict['city'] = u._city
                
                data.append(user_dict)
            
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            raise StorageError(f"Ошибка сохранения: {e}")
    
    def load(self):
        if not self.filepath.exists():
            return []
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise StorageError(f"Ошибка загрузки: {e}")