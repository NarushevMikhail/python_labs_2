from abc import ABC, abstractmethod

# интерфейс - абстрактный класс с каким - то методом или методами
class Profile(ABC):

    @abstractmethod
    def view_profile(self):
        pass

    @abstractmethod
    def update_profile(self, bio = None, age = None, city = None):
        pass

class Authentication(ABC):

    @abstractmethod
    def check_password(self, password: str):
        pass

    @abstractmethod
    def check_login(self, login: str):
        pass

class Comparable(ABC):

    @abstractmethod
    def compare_to(self, other) -> int:
        pass

class Printable(ABC):

    @abstractmethod
    def print_str(self):
        pass