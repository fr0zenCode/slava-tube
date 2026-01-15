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