# slava-tube
Rest API for acting with database with videos


## Запуск проекта

### Требования:
Установить программу Docker на свой компьютер.

### Запуск:
Перейти в корневую папку проекта, где находятся файлы `Dockerfile` и `docker-compose.yaml`.
Выполнить команды:
```bash
docker-compose build --no-cache
```

и 

```bash
docker-compose up
```

## Доступ:
После успешного старта проекта, будут доступны следующие urls для подключения:
- http://0.0.0.0:8000/docs - сваггер документация для ручек нашего API
- http://localhost:5432 - подключение к СУБД PostgreSQL. Данные для подключения можно посмотреть в `docker-compose.yaml` файле.


## Если запуск через архив:

1) Установить на компьютер Python, версии 3.10+

2) Создать и активировать виртуальное окружение.
Находясь в корневой директории, выполнить
```bash
python -m venv venv
```

```bash
source venv\Scripts\activate
```

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

3) Установить на компьютер программу Docker.
4) Выполнить следующие команды, находясь в корневой директории проекта:
```bash
docker-compose built --no-cache
```

```bash
docker-compose up
```

### Готово, теперь вам будут доступны те же URL-адреса для взаимодействия с проектом, что и в предыдущем описанном способе развертывания проекта.