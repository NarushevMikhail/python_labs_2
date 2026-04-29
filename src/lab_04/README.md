# Лабораторная работа №4 
## Цель работы: 
* Познакомиться с абстрактными базовыми классами (ABC).
* Освоить понятие интерфейса (контракта поведения).
* Научиться задавать обязательные методы для классов.
* Закрепить полиморфизм через единый интерфейс.
* Научиться проектировать архитектуру, а не просто классы.

## Что изучалось? 

### В данной лабораторной работе я познакомился с понятиями: 
* ```Интрефейс``` - это контракт, который определяет, какие методы должен иметь класс, но не даёт их реализацию. В Python интерфейсы создаются через абстрактные классы с помощью модуля ```abc```.

* ```Абстрактыне классы``` - это класс, который нельзя превратить в объект, то есть нельзя создать экземпляр. Он служит шаблоном для других классов. 

## Описание интерфейсов
### 1.```Profile```(интерфейс профиля), содержит методы: 
* ```view_profile()``` - просмотр профиля. 
* ```update_profile(bio=None, age=None, city=None)``` - обновление профиля с необязательными параметрами. 

### 2. ```Authentication``` (интерфейс аутентификации), методы: 
* ```check_password()``` - проверка пароля.
* ```check_login()``` - проверка логина.

### 3. ```Comparable``` (интрейс сравнения), методы: 
* ```compare_to(other)``` - сравнение с другим объектом, возвращает число.

### 4. ```Printable``` (интрейс печати), методы: 
* ```print_str()``` - вывод строки. 


## Какие классы реализуют интерфейсы?
### 1.  Класс ```User``` реализует несколько интрейфейсов: 
* Profile  
* Authentication 
* Printable
* Comparable

### 2. Класс ```Guest``` реализует данные интерфейсы: 
* Profile  
* Printable
* Comparable

### Отличия в поведении: 
#### 1. User можно создать только с ником, паролем, логином и ролью. Guest создаётся только с session_id (или без него, тогда значение по умолчанию).

#### 2. User увеличивает счётчик total_users при создании. Guest не влияет на этот счётчик.

#### 3. User может свободно менять профиль (bio, age, city). Guest при попытке изменить профиль выбрасывает ошибку PermissionError.

#### 4. User может менять свой логин, никнейм и роль (с проверкой на допустимые значения). Guest не может менять логин, никнейм и роль — при попытке тоже ошибка.

#### 5. User имеет методы check_password и check_login для аутентификации. Guest не имеет этих методов, потому что не наследует интерфейс Authentication.

#### 6. User при сравнении compare_to сравнивает объекты по полю nickname. Guest сравнивает по session_id, причём если сравнивается с User, то Guest всегда считается больше (возвращает 1).

#### 7.User при просмотре профиля view_profile возвращает только свои данные. Guest возвращает те же данные, но добавляет пометку "Зарегистрируйтесь для полного доступа".

## Демонстрация ```demo.py```:

### 1.Создание объекта
  <img width="411" height="166" alt="image" src="https://github.com/user-attachments/assets/b31add5d-9f54-4074-8802-db51d61dab3e" />

### 2.Разное поведение ```update_profile```
  <img width="840" height="199" alt="image" src="https://github.com/user-attachments/assets/28e42141-0335-4b9f-9e49-caf2464c5a7a" />

### 3.Метод ```view_profile()```
  <img width="2147" height="153" alt="image" src="https://github.com/user-attachments/assets/d8209a3b-da92-4464-bc6e-fd10c19fcd73" />

### 4. Authentication (только у User) 
<img width="550" height="125" alt="image" src="https://github.com/user-attachments/assets/e7e71a86-2b7d-4fff-baef-6a7d08088206" />

### 5. Полиморфизм.
<img width="575" height="122" alt="image" src="https://github.com/user-attachments/assets/53ca4ba7-f29d-4940-bcdf-bd4dfb70694a" />


### 6. Проверка через ```isinstance```
<img width="707" height="195" alt="image" src="https://github.com/user-attachments/assets/626feed1-87c7-474c-b350-129df9e8aee5" />

### 7.  Проверка универсальноого метода.
<img width="848" height="146" alt="image" src="https://github.com/user-attachments/assets/e118e1a0-7ef2-4e0f-8305-57fb92d6e056" />

### 8. Проверка новых интрейсов
<img width="630" height="206" alt="image" src="https://github.com/user-attachments/assets/cb961dce-a035-4f46-ac79-da16fba2333c" />

### 9. Метод ```print_str()``` - разное поведение 
<img width="996" height="175" alt="image" src="https://github.com/user-attachments/assets/678a826a-bd25-4b3b-99b8-ffae7fadaae8" />

### 10. Метод ```compare()``` 
<img width="527" height="157" alt="image" src="https://github.com/user-attachments/assets/256256a7-4055-4ad2-b205-5341b7502118" />

### 11. Фильтрация по интерфейсу ```Printable``` 
<img width="833" height="180" alt="image" src="https://github.com/user-attachments/assets/1ccabd32-2f53-40ae-bb37-94b38461175c" />

### 12. Фильтраци по интрейсу ```Comparable```
<img width="830" height="173" alt="image" src="https://github.com/user-attachments/assets/e3d72eec-ffd0-47b2-82de-daa7d2f6007d" />

### 13. Вывод всех польхователей через ```Printable```
<img width="734" height="187" alt="image" src="https://github.com/user-attachments/assets/a67f458b-b3c3-4699-8322-f0e5e114bb4c" />

### 14. Сортировка через ```Comparable```
<img width="700" height="128" alt="image" src="https://github.com/user-attachments/assets/6245f224-5a84-4516-a88f-5d8f05279650" />

### 15. Вывод после сортировки 
<img width="693" height="167" alt="image" src="https://github.com/user-attachments/assets/1dea2761-c376-4763-afc6-f6f45641cae4" />

### 16. Сортировка в обратном порядке
<img width="794" height="163" alt="image" src="https://github.com/user-attachments/assets/de492ddf-2c1b-4037-b7c5-b5abf9c5e7e9" />

### 17. универсальная функция с ```Printable```
<img width="735" height="149" alt="image" src="https://github.com/user-attachments/assets/239f4904-7ec2-429d-9aa9-af3058a1e26c" />
