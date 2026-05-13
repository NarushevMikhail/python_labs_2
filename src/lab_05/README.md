# ЛР-5 — Функции как аргументы. Стратегии и делегаты.

## 1. Цель работы

* Освоить передачу функций как аргументов в другие функции и методы.
* Научиться применять встроенные функции высшего порядка: `map`, `filter`, `sorted`.
* Понять концепцию паттерна «Стратегия» и реализовать его на Python.
* Освоить `lambda`-выражения и их практическое применение.
* Интегрировать функциональный стиль с объектно-ориентированным кодом из предыдущих ЛР.


## 2. Реализованные функции и стратегии

### Функции-стратегии для сортировки

* ```by_nickname(user)``` - Сортировка по имени

* ```by_age(user)``` - Сортировка по возрасту

* ```by_role_and_nickname(user)``` - Сортировка сначала по роли, потом по имени

* ```by_login(user)``` - Сортировка по логину

* ```by_role(user)``` - Сортировка по роли

* ```by_admin_level(user)``` - Сортировка по уровню админа

* ```by_vip_level(user)``` - Сортировка по VIP-статусу

### Функции-фильтры

* ```is_adult(user)``` - Отбирает взрослых 
* ```is_teenager(user)``` - Отбирает подростков
* ```is_vip_instance(user)``` - Отбирает только VIP-объекты
* ```is_admin(user)``` - Отбирает админов по роли
* ```is_admin_instance(user)```	- Отбирает объекты AdminUser
* ```has_profile_filled(user)``` - Отбирает заполнивших профиль

### Фабрики функций
```1. make_age_filter(min_age, max_age=None)``` - Создаёт фильтр по возрасту с гибкими параметрами.

```2. make_role_filter(allowed_roles)``` - Создаёт фильтр по роли (одной или нескольким).

```3.make_discount_applier(discount_percent)``` - Создаёт функцию для применения скидки к цене.


### Паттерн Стратегия и callable-объекты

* ```class DiscountStrategy``` - применяет скидку к товарам и запоминает историю.

* ```class UpgradeStrategy``` - Повышает роль пользователя и запоминает историю повышений.

* ```class BonusStrategy``` - Начисляет бонусы VIP-пользователям (разный множитель для разных уровней).

* ```class PrintStrategy``` - Форматирует вывод информации о пользователе (с возможностью детального или краткого режима).

### Функции для ```map```

* ```user_to_dict(user)``` - Словарь с данными
* ```user_to_short_str(user)``` - вывод: "alex (user)"
* ```extract_nickname(user)``` - Только имя
* ```extract_role(user)``` - Только роль


**Паттерн Стратегия** определяет семейство алгоритмов, помещает каждый в отдельный класс и делает их взаимозаменяемыми. Это позволяет выбирать алгоритм во время выполнения без изменения кода коллекции.

**Callable-объекты** — классы с методом `__call__`, которые можно вызывать как функции. Они могут хранить внутреннее состояние.

## Демонстрация ```demo.py```
### ```Сценарий 1```
* #### Шаг 1. Выполняем цепочку операций filter_by → sort_by → apply. Шаг 1 сначала фильтрация filter_by, фильтруем всех взрослых. 
<img width="1852" height="917" alt="image" src="https://github.com/user-attachments/assets/34291ff4-7f1f-4c7b-8d56-9930f87d72ec" />

* #### Шаг 2. Sort_by - сортировка по возврасту
<img width="1125" height="433" alt="image" src="https://github.com/user-attachments/assets/c5327717-b052-4024-973e-e3f576ba7fe1" />

* #### Шаг 3. Apply - применение скидки, callable - объект DiscountStrategy(15%) 
<img width="1351" height="714" alt="image" src="https://github.com/user-attachments/assets/2638776e-359f-4f76-819d-c696ede7f259" />

* ####  Такая же цепочка, но сделанная проще и короче. 
<img width="1133" height="316" alt="image" src="https://github.com/user-attachments/assets/d5032c5e-ee90-49f8-852d-da8dd3efe2db" />

### ```Сценарий 2.```
* #### Замена стратегии без изменения кода. Исходная коллекция: 
<img width="812" height="185" alt="image" src="https://github.com/user-attachments/assets/506dc728-a5de-4aba-a7d0-04603fdb2de4" />

* #### Шаг 1. Стратегия первая, сортировка по имени ```(by_nickname)```
<img width="907" height="132" alt="image" src="https://github.com/user-attachments/assets/1c8cea98-9a80-4c1c-870c-62faf3a360a0" />

* #### Шаг 2. Стратегия вторая, сортировка оп уровня адмиистратора ```(by_admin_level)```
<img width="592" height="126" alt="image" src="https://github.com/user-attachments/assets/b9e3eafb-85d2-450e-9174-887a88427964" />

* #### Шаг 3. Замена стратегии скидки. 
<img width="863" height="433" alt="image" src="https://github.com/user-attachments/assets/1b3762eb-e77f-46f6-bb18-da24e76a7305" />

### ```Сценарий 3. callable - объекты, как стартегии```
* #### 1. Исходные данные.
<img width="851" height="292" alt="image" src="https://github.com/user-attachments/assets/232561dd-1880-43b5-bfe3-d7cb563bcc73" />

* #### 2. callable - объекты 1: ```DiscountStrategy (скидка)```
<img width="1149" height="523" alt="image" src="https://github.com/user-attachments/assets/2be65af8-ffd7-4a7d-93d7-4a781c5cee4e" />

* #### 3. callable - объект 2: ```BonusStrategy (начисление бонусов)```
<img width="1172" height="397" alt="image" src="https://github.com/user-attachments/assets/d80f336d-e693-427e-ab28-aa2a0fcc8a6e" />

* #### 4. callable - объект 3: ```UpgradeStrategy (повышение роли)```
<img width="1181" height="864" alt="image" src="https://github.com/user-attachments/assets/11d88fe5-3fae-462d-ac55-704e0ce19f68" />

* #### 5. Демоснтарция метода ```apply()```, а также отработка ```PrintStrategy```. 
<img width="1258" height="710" alt="image" src="https://github.com/user-attachments/assets/960857a3-7a05-4f13-9eec-639d1fa7612a" />
