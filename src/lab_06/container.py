# container.py
from typing import TypeVar, Generic, List, Iterator, Optional, Callable, Protocol, runtime_checkable

@runtime_checkable
class Displayable(Protocol):
    def display(self) -> str:
        ...

@runtime_checkable
class Scorable(Protocol):
    def score(self) -> float:
        ...


T = TypeVar('T')
R = TypeVar('R') #нужен, т к map - меняет тип данных 
D = TypeVar('D', bound = Displayable)
S = TypeVar('S', bound = Scorable)

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def add(self, item: T) -> None:
        # Проверка на дубликат объекта (универсальная для любого типа)
        if any(stored_item is item for stored_item in self._items):
            raise ValueError(f'Дубликат объекта: {item}')
        self._items.append(item)

    def remove(self, item: T) -> None:
        if item not in self._items:
            raise ValueError(f'Элемент {item} не найден в коллекции')
        self._items.remove(item)
    
    def remove_at(self, index: int) -> T:
        if not isinstance(index, int):
            raise TypeError(f'Индекс должен быть числом, передан: {index}')
        if index < 0 or index >= len(self._items):
            raise IndexError(f'Индекс {index} вне диапазона (0-{len(self._items)-1})')
        removed = self._items.pop(index)
        return removed
        
    def get_all(self) -> List[T]:
        return list(self._items)
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]: #Callable - то, что можно вызвать (function)
        for item in self._items: # функция, которая принимает один парамтер T и возвращает bool
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> list[T]: 
        return [item for item in self._items if predicate(item)] #возвращает список подходящих эллементов
    
    def map(self, transforms: Callable[[T], R]) -> list[R]:
        return [transforms(item) for item in self._items]

    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self) -> Iterator[T]:
        return iter(self._items)
    
    def __getitem__(self, index: int) -> T:
        return self._items[index]
    
    def __contains__(self, item: T) -> bool:
        return item in self._items
    
    def __str__(self) -> str:
        if len(self._items) == 0:
            return f'Всего элементов: 0\nсписок всех элементов: []'
        return f'Всего элементов: {len(self._items)}\nсписок всех элементов: {self._items}'
    
    def __repr__(self) -> str:
        return f"TypedCollection({self._items})"
    

class DisplayableCollection(Generic[D]): #коллекция для displayable object
    def __init__(self) -> None:
        self._items: List[D] = []

    def add(self, item: D) -> None:
        self._items.append(item)

    def find(self, predicate: Callable[[D], bool]) -> Optional[D]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[D], bool]) -> List[D]:
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[D], R]) -> List[R]:
        return [transform(item) for item in self._items]


    def display_all(self) -> List[str]:
        return [item.display() for item in self._items]
    
    def get_all(self) -> List[D]:
        return list(self._items)
    
    def __len__(self) -> int:
        return len(self._items)
    

class ScorableCollection(Generic[S]): #коллекция для scorable object
    def __init__(self) -> None:
        self._items: List[S] = []
    
    def add(self, item: S) -> None:
        self._items.append(item)
    
    def get_scores(self) -> List[float]:
        return [item.score() for item in self._items]
    
    def get_average_score(self) -> float:
        if not self._items:
            return 0.0
        return sum(item.score() for item in self._items) / len(self._items)
    
    def get_all(self) -> List[S]:
        return list(self._items)
    
    def __len__(self) -> int:
        return len(self._items)