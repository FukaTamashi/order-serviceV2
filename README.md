# Order Service

Этот проект представляет собой Django-приложение для управления заказами, упакованное в Docker и использующее PostgreSQL в качестве базы данных.

## Содержание

1. [Клонирование репозитория](#клонирование-репозитория)
2. [Настройка переменных окружения](#настройка-переменных-окружения)
3. [Установка зависимостей](#установка-зависимостей)
4. [Запуск проекта с Docker](#запуск-проекта-с-docker)
5. [Эндпоинты для работы с API](#эндпоинты-для-работы-с-API)
6. [Завершение работы контейнеров](#завершение-работы-контейнеров)

## Клонирование репозитория

Сначала клонируйте репозиторий на свой локальный компьютер:

```bash
git clone https://github.com/FukaTamashi/order-service.git
cd order-service
```

## Настройка переменных окружения

Создайте виртуальное окружение и активируйте его:

```активация
./venv/Scripts/activate - Для Windows
```

## Установка зависимостей

Для того чтобы установить зависимости пропишите в терминале комманду:

```
pip install -r requirements.txt
```
после установки в .venv должны появиться все необходимые для работы библиотеки 

## Запуск проекта с Docker

Создай в корневой директории каталог logs с файлом внутри sql_queries.log, куда будут записываться все операции с бд.
Далее в каталог order и user добавить каталог migrations с файлами _ _ _init__ _.py,
Прописать в терминале idea
```активация
python manage.py makemigrations
python manage.py migrate
```
или в самом Docker в терминале order-service-web
```активация
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

Следующим прописать в терминале idea
```активация
docker-compose up --build
```

## Эндпоинты для работы с API

Для примера буду использовать приложение Postman. Для id используется формат uuid.

Для получения списка пользователей:

```
Get http://127.0.0.1:8000/api/users/
```

Для получения пользователя по id:

```
Get http://127.0.0.1:8000/api/users/{id}
```

Для создания пользователя:

```
POST http://127.0.0.1:8000/api/users/
Body:
{
    "name": "vlad",
    "email": "test1@gmail.com",
    "age": 19
}
```

Для обновления полей пользователя:

```
PUT http://127.0.0.1:8000/api/users/{id}/
Body
{
    "name": "Vlad",
    "email": "vlad.updated@gmail.com",
    "age": 35
}
```

Для обновления поля пользователя:

```
PATCH http://127.0.0.1:8000/api/users/{id}/
Body
{
    "name": "update"
}
```

Для получения списка заказов:

```
GET http://127.0.0.1:8000/api/orders
```

Для получения заказа по id:

```
GET http://127.0.0.1:8000/api/orders/{id}
```

Для создания заказа:

```
POST http://127.0.0.1:8000/api/orders/
Body
{
    "name": "Boots 42",
    "description": "wool boots",
    "user": "916cd776-0f91-4de4-87f3-6e5d3eac8ac4"
}
```

Для обновления заказа:

```
PUT http://127.0.0.1:8000/api/orders/{order_id}/
Body
{
    "name": "Boots 42",
    "description": "wool boots",
    "user": "user{id}"
}
```

Для обновления некоторых полей заказа:

```
PATCH http://127.0.0.1:8000/api/orders/{order_id}/
Body
{
    "name": "Boots 42",
    "user": "user{id}"
}
```

## Завершение работы контейнеров

Для завершения работы контейнера введите в консоль idea:

```
docker-compose down
```

Для удаления контейнеров, томов и сетей добавьте флаг -v:

```
docker-compose down -v
```



