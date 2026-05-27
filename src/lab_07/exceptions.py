
class AppException(Exception):
    """Базовое исключение для всего приложения"""
    pass

class ValidationError(AppException):
    """Ошибка при проверке данных (неправильный формат)"""
    pass

class NotFoundError(AppException):
    """Объект не найден в базе данных"""
    pass

class DuplicateError(AppException):
    """Попытка добавить дубликат"""
    pass

class StorageError(AppException):
    """Ошибка при работе с файлом"""
    pass