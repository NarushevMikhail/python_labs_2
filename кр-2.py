# ----- 1 задание ------

# from typing import List


# # Иерархия исключений
# class ServerError(Exception):
#     pass

# class ServerOfflineError(ServerError):
#     pass

# class ServerAlreadyOnlineError(ServerError):
#     pass

# class SessionLimitError(ServerError):
#     pass

# class SessionNotFoundError(ServerError):
#     pass


# class Server:
#     def __init__(self, hostname: str, ip: str, status: str = "offline", max_connections: int = 10):
#         self._hostname = hostname.strip() if hostname else ""
#         self._ip = ip
#         self._status = status if status in ("online", "offline", "maintenance") else "offline"
#         self._max_connections = max_connections if max_connections > 0 else 1
#         self._active_sessions: List[str] = []

#     #Свойства

#     @property
#     def hostname(self) -> str:
#         return self._hostname

#     @property
#     def ip(self) -> str:
#         return self._ip

#     @property
#     def status(self) -> str:
#         return self._status

#     @status.setter
#     def status(self, value: str) -> None:
#         if value not in ("online", "offline", "maintenance"):
#             raise ValueError(f"Недопустимый статус: {value}")
#         self._status = value

#     @property
#     def max_connections(self) -> int:
#         return self._max_connections

#     @property
#     def active_sessions(self) -> List[str]:
#         return self._active_sessions.copy()  # возвращаем копию для защиты

#     #Методы 

#     def start(self) -> None:
#         if self._status == "online":
#             raise ServerAlreadyOnlineError(f"Сервер {self._hostname} уже запущен")
#         self._status = "online"

#     def stop(self) -> None:
#         self._status = "offline"
#         self._active_sessions.clear()

#     def open_session(self, session_id: str) -> None:
#         if self._status != "online":
#             raise ServerOfflineError(f"Сервер {self._hostname} не в онлайне")

#         if len(self._active_sessions) >= self._max_connections:
#             raise SessionLimitError(
#                 f"Достигнут лимит подключений: {self._max_connections}"
#             )

#         self._active_sessions.append(session_id)

#     def close_session(self, session_id: str) -> None:
#         if session_id not in self._active_sessions:
#             raise SessionNotFoundError(f"Сессия {session_id} не найдена")

#         self._active_sessions.remove(session_id)

#     def __str__(self) -> str:
#         return (
#             f"{self._hostname} [{self._ip}] — {self._status}, "
#             f"сессии: {len(self._active_sessions)}/{self._max_connections}"
#         )


# srv = Server('server-01', '192.168.1.10', 'offline', 10)
# srv.start()
# print(srv.status) # online
# try:
#     srv.start()  # ServerAlreadyOnlineError
# except ServerAlreadyOnlineError as e:
#     print(f"[ошибка]: {e}")

    
# srv.open_session('sess-001')
# srv.open_session('sess-002')
# print(f'Активных сессий: {len(srv.active_sessions)}') # 2
# srv.close_session('sess-001')

# try:
#     srv.close_session('sess-999')
# except SessionNotFoundError as e:
#     print(f"[ошибка]: {e}")

# srv.stop()
# print(f"Статус после stop: {srv.status}")

# try:
#     srv.open_session('x')
# except ServerOfflineError as e:
#     print(f"[ошибка]: {e}")

# print(srv)



#--------------2 задание---------------



    from abc import ABC, abstractmethod
    from typing import Dict, List, Optional, Any, Union
    from collections import defaultdict


    # Иерархия исключений
    class ServerError(Exception):
        pass

    class ServerOfflineError(ServerError):
        pass

    class ServerAlreadyOnlineError(ServerError):
        pass

    class SessionLimitError(ServerError):
        pass

    class SessionNotFoundError(ServerError):
        pass

    class ValidationError(ServerError):
        pass

    class RateLimitExceededError(ValidationError):
        pass

    class IPNotAllowedError(ValidationError):
        pass

    class PayloadTooLargeError(ValidationError):
        pass


    # Абстрактный валидатор

    class RequestValidator(ABC): #Абстрактный класс для валидатора запросов
        def __init__(self) -> None:
            self._next_validator: Optional[RequestValidator] = None
        
        def set_next(self, validator: 'RequestValidator') -> 'RequestValidator':
            self._next_validator = validator
            return validator
        
        def validate(self, request: Dict[str, Any]) -> None:
            self._check(request)
            
            if self._next_validator is not None:
                self._next_validator.validate(request)
        
        @abstractmethod
        def _check(self, request: Dict[str, Any]) -> None:
            pass

    #Конкретные валидаторы
    class AuthValidator(RequestValidator): #Проверяет наличие и валидность токена
        def _check(self, request: Dict[str, Any]) -> None:
            token = request.get("token")
            if not token or not isinstance(token, str) or token.strip() == "":
                raise ValidationError("пустой токен")


    class IPWhitelistValidator(RequestValidator):
        def __init__(self, allowed_ips: List[str]) -> None:
            super().__init__()
            self._allowed_ips = set(allowed_ips)
        
        def _check(self, request: Dict[str, Any]) -> None:
            source_ip = request.get("source_ip")
            if source_ip not in self._allowed_ips:
                raise IPNotAllowedError(f"IP {source_ip} не в белом списке")


    class RateLimitValidator(RequestValidator):
        
        def __init__(self, max_per_user: int) -> None:
            super().__init__()
            self._max_per_user = max_per_user
            self._counts: Dict[str, int] = defaultdict(int)
        
        def _check(self, request: Dict[str, Any]) -> None:
            user_id = request.get("user_id")
            if user_id is None:
                raise ValidationError("Отсутствует user_id")
            
            self._counts[user_id] += 1
            
            if self._counts[user_id] > self._max_per_user:
                raise RateLimitExceededError(
                    f"Превышен лимит запросов для {user_id}: {self._max_per_user}"
                )


    class PayloadSizeValidator(RequestValidator):
        def __init__(self, max_size: int) -> None:
            super().__init__()
            self._max_size = max_size
        
        def _check(self, request: Dict[str, Any]) -> None:
            payload = request.get("payload", "")
            payload_str = str(payload)
            if len(payload_str) > self._max_size:
                raise PayloadTooLargeError(
                    f"Payload слишком большой: {len(payload_str)} > {self._max_size}"
                )

    # Функция сборки цепочки
    def build_validation_chain(*validators: RequestValidator) -> Optional[RequestValidator]:
        if not validators:
            return None
        
        first = validators[0]
        current = first
        
        for validator in validators[1:]:
            current.set_next(validator)
            current = validator
        
        return first



    # Класс Server (расширенный)
    class Server:
        def __init__(self, hostname: str, ip: str, status: str = "offline", max_connections: int = 10):
            self._hostname = hostname.strip() if hostname else ""
            self._ip = ip
            self._status = status if status in ("online", "offline", "maintenance") else "offline"
            self._max_connections = max_connections if max_connections > 0 else 1
            self._active_sessions: List[str] = []
            self._validator: Optional[RequestValidator] = None

        @property
        def hostname(self) -> str:
            return self._hostname

        @property
        def ip(self) -> str:
            return self._ip

        @property
        def status(self) -> str:
            return self._status

        @status.setter
        def status(self, value: str) -> None:
            if value not in ("online", "offline", "maintenance"):
                raise ValueError(f"Недопустимый статус: {value}")
            self._status = value

        @property
        def max_connections(self) -> int:
            return self._max_connections

        @property
        def active_sessions(self) -> List[str]:
            return self._active_sessions.copy()

        def set_validator(self, validator: Optional[RequestValidator]) -> None:
            """Устанавливает цепочку валидаторов"""
            self._validator = validator

        def start(self) -> None:
            if self._status == "online":
                raise ServerAlreadyOnlineError(f"Сервер {self._hostname} уже запущен")
            self._status = "online"

        def stop(self) -> None:
            self._status = "offline"
            self._active_sessions.clear()

        def open_session(self, request: Dict[str, Any]) -> None:
            # Проверяем статус сервера
            if self._status != "online":
                raise ServerOfflineError(f"Сервер {self._hostname} не в онлайне")
            
            # Валидация запроса
            if self._validator is not None:
                self._validator.validate(request)
            
            # Получаем session_id из запроса
            session_id = request.get("session_id")
            if not session_id:
                raise ValidationError("Отсутствует session_id в запросе")
            
            # Проверяем лимит сессий
            if len(self._active_sessions) >= self._max_connections:
                raise SessionLimitError(f"Достигнут лимит подключений: {self._max_connections}")
            
            self._active_sessions.append(session_id)

        def close_session(self, session_id: str) -> None:
            if session_id not in self._active_sessions:
                raise SessionNotFoundError(f"Сессия {session_id} не найдена")
            self._active_sessions.remove(session_id)

        def __str__(self) -> str:
            return f"{self._hostname} [{self._ip}] — {self._status}, сессии: {len(self._active_sessions)}/{self._max_connections}"


    print("=" * 60)
    print("ЗАПУСК ПРИМЕРА")
    print("=" * 60)

    srv = Server('server-01', '192.168.1.10', 'offline', 10)
    srv.start()
    print(f"Сервер запущен: {srv.status}\n")

    chain = build_validation_chain(
        AuthValidator(),
        IPWhitelistValidator(['192.168.1.5', '192.168.1.6']),
        RateLimitValidator(max_per_user=3),
        PayloadSizeValidator(max_size=1024),
    )

    srv.set_validator(chain)
    print("Цепочка валидаторов настроена\n")

    req = {
        'token': 'abc123',
        'user_id': 'u1',
        'source_ip': '192.168.1.5',
        'session_id': 's1',
        'payload': 'hello',
    }

    print("1. Корректный запрос:")
    try:
        srv.open_session(req)
        print(f"   Сессия открыта: {srv.active_sessions}")
    except Exception as e:
        print(f"   {type(e).__name__}: {e}")

    print("\n2. Пустой токен:")
    req2 = {**req, 'token': '', 'session_id': 's2'}
    try:
        srv.open_session(req2)
        print(f"   Сессия открыта: {srv.active_sessions}")
    except ValidationError as e:
        print(f"   {type(e).__name__}: {e}")

    print("\n3. ip не в белом списке:")
    req3 = {**req, 'source_ip': '10.0.0.1', 'session_id': 's3'}
    try:
        srv.open_session(req3)
        print(f"   Сессия открыта: {srv.active_sessions}")
    except IPNotAllowedError as e:
        print(f"   {type(e).__name__}: {e}")

    print("\n4. ПРЕВЫШЕНИЕ ЛИМИТА ЗАПРОСОВ (4 запроса от u1):")
    for i in range(4):
        try:
            srv.open_session({**req, 'session_id': f's_{i}'})
            print(f"   Запрос {i+1}: сессия s_{i} открыта")
        except RateLimitExceededError as e:
            print(f"   Запрос {i+1}: {type(e).__name__}: {e}")

    print("\n5. Слишком большой payloa:")
    big_payload = "x" * 2000
    req5 = {**req, 'session_id': 's_big', 'payload': big_payload}
    try:
        srv.open_session(req5)
        print(f"   Сессия открыта: {srv.active_sessions}")
    except PayloadTooLargeError as e:
        print(f"   {type(e).__name__}: {e}")

    print("\n6. Отсутсвует session_id:")
    req6 = {**req, 'session_id': None}
    try:
        srv.open_session(req6)
        print(f"   Сессия открыта")
    except ValidationError as e:
        print(f"   ValidationError: {e}")

    print("\n7. Сервер остановлен:")
    srv.stop()
    try:
        srv.open_session({**req, 'session_id': 's_stop'})
        print(f"   Сессия открыта")
    except ServerOfflineError as e:
        print(f"   {type(e).__name__}: {e}")

    print("\n" + "=" * 60)
    print(f"Итоговое состояние сервера:")
    print(f"   {srv}")
    print(f"   Активные сессии: {srv.active_sessions}")
