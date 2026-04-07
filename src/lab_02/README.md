# Лабораторная работа № 2.
## Цель работы
* Научиться работать с **коллекциями объектов**.
* Понять разницу между **моделью сущности и контейнером объектов**.
* Реализовать **собственный контейнерный класс**.
* Освоить **итерацию по объектам**.
* Реализовать базовые операции управления коллекцией.

## Процесс создания коллекции: 
 В рамках данной лаборатной работы мною был создан класс-контейнер UserList, предназначенный для хранения и управления объектами класса User из первой лабораторной работы. Коллекция обеспечивает удобный интерфейс для работы с группой пользователей, включая добавление, удаление, поиск, сортировку и фильтрацию элементов.

## Пример работы файла ```demo.py```
### Сценарий 1.
<img width="2286" height="353" alt="image" src="https://github.com/user-attachments/assets/6f922642-0880-445f-b514-f2723758f21b" />

* вывод всей коллекции  
* отработка, что в коллекцию можно добавлять только User
* добавить пользователя с таким, уже существующим nickname, невозможно
* добавить пользователя с таким, уже существующим login, невозможно

### Сценарий 2. 
<img width="1580" height="314" alt="image" src="https://github.com/user-attachments/assets/218273a8-e673-4b2b-9eee-f9499cd00674" />
* удаление объекта
* удалить несуществующего пользователя, невозможно
* удалить можно только User

### Сценарий 3.
<img width="1985" height="81" alt="image" src="https://github.com/user-attachments/assets/c3ba662f-f635-44ea-ab8a-7bdcec89f59d" />
* работа метода get_all, выведи все объекты из коллекции

### Сценарий 4. 
<img width="1413" height="287" alt="image" src="https://github.com/user-attachments/assets/feeeb93b-363d-4681-98f0-37ed6d95104c" />

* поиск User в коллекции по nickname, login и role
* отработка ошибки, когда мы пытаемся найти User  с неверными введенными данными для поиска

### Сценарий 5. 
<img width="453" height="156" alt="image" src="https://github.com/user-attachments/assets/b429a682-f2e5-449f-89a6-c83fc0327fd1" />

* длина коллекции
* длина пустой коллекции

### Сценарий 6.
<img width="615" height="185" alt="image" src="https://github.com/user-attachments/assets/bb765f25-099e-4ed9-856b-33b82bbda8bf" />

* итерация коллекции с помощь цикла for

### Сценарий 7. 
<img width="838" height="252" alt="image" src="https://github.com/user-attachments/assets/7c63b8ab-3b78-440f-97ce-8bc16e09a63e" />

* индексация коллекции с помощью ```__getitem__```
* отработка ошибки, если индекс находиться вне диапазона

### Сценарий 8. 
<img width="768" height="1043" alt="image" src="https://github.com/user-attachments/assets/45ffd883-c929-49bd-8562-bda5db274ad8" />

* сортировка коллекции по nickname, убывание и возврастание
* сортировка по login
* сортировка по role

### Сценарий 9. 
<img width="1058" height="596" alt="image" src="https://github.com/user-attachments/assets/0a36a94f-071a-495c-b48b-0672f9a15a7a" />

* фильтрация коллекции по ролям, отдельно User c ролью ```user```, ```admin```, ```moderator```
* сортировка пользователей, если у них заполнен профиль

### Сценарий 10. 
<img width="951" height="293" alt="image" src="https://github.com/user-attachments/assets/9a44c980-d907-44a2-adcd-0896c52796a1" />

* поиск пользователя по nickname, также выводит их role
* производим удаление пользователя и выводим отсавшиеся кол - во User в коллекции

### Сценарий 11. 
<img width="738" height="693" alt="image" src="https://github.com/user-attachments/assets/e31d98a6-d931-4c1d-adf7-347baed96cd2" />

* сортировка пользователей

### СЦенарий 12. 
<img width="1098" height="591" alt="image" src="https://github.com/user-attachments/assets/8ee68410-1c3a-4b77-b427-f23289336509" />

* индексация и фильтрация по ролям
* удаление пользователя по индексу, и выводим сколко осталось User  в коллекции
  





