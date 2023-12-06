# QRKOT | Благотворительный фонд поддержки котиков.

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=043A6B)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)](https://pypi.org/project/SQLAlchemy/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat&logo=Alembic&logoColor=ffffff&color=043A6B)](https://pypi.org/project/alembic/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=Pydantic&logoColor=ffffff&color=043A6B)](https://pypi.org/project/pydantic/)
[![Asyncio](https://img.shields.io/badge/-Asyncio-464646?style=flat&logo=Asyncio&logoColor=ffffff&color=043A6B)](https://docs.python.org/3/library/asyncio.html)

## Описание:
#### Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Отчет:

#### Реализована возможность формирования отчета в гугл-таблице.
#### Таблица содержит все закрытые проекты, отсортированные по скорости сбора средств - от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.

### Автор проекта:

[Артем Куркин](https://github.com/ArtyKurkin)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ArtyKurkin/QRkot_spreadsheets.git
```
```
cd QRkot_spreadsheets
```
Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS:

    ```
    source venv/bin/activate
    ```

* Если у вас windows:

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Создайте в корневой директории файл .env со следующим наполнением:
```
APP_TITLE=Кошачий благотворительный фонд
APP_DESCRIPTION=Сервис для поддержки котиков!
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=<<Ваше секретное слово>>
FIRST_SUPERUSER_EMAIL=<<email суперюзера>>
FIRST_SUPERUSER_PASSWORD=<<Пароль суперюзера>>
DATABASE_URL=<<Данные вашего сервисного аккаунта>>
FIRST_SUPERUSER_EMAIL=<<Данные вашего сервисного аккаунта>>
FIRST_SUPERUSER_PASSWORD=<<Данные вашего сервисного аккаунта>>
TYPE=<<Данные вашего сервисного аккаунта>>
PROJECT_ID=<<Данные вашего сервисного аккаунта>>
PRIVATE_KEY_ID=<<Данные вашего сервисного аккаунта>>
PRIVATE_KEY=<<Данные вашего сервисного аккаунта>>
CLIENT_EMAIL=<<Данные вашего сервисного аккаунта>>
CLIENT_ID=<<Данные вашего сервисного аккаунта>>
AUTH_URI=<<Данные вашего сервисного аккаунта>>
TOKEN_URI=<<Данные вашего сервисного аккаунта>>
AUTH_PROVIDER_X509_CERT_URL=<<Данные вашего сервисного аккаунта>>
CLIENT_X509_CERT_URL=<<Данные вашего сервисного аккаунта>>
EMAIL=<<Данные вашего сервисного аккаунта>>
```
Примените миграции:
```
alembic upgrade head
```
Запустить проект:
```
uvicorn app.main:app --reload
```
### Примеры запросов:

* `/auth/register` - POST запрос для регистрации нового пользователя
* `/users/me` - Получение или изменение данных аутентифицированного пользователя
* `/charity_project` - Получение или создание проектов
* `/donation` - Получение или создание пожертвований
* `/google` - Формирование отчета в гугл-таблице

##### Полный список запросов и ответов доступен в документации или в файле спецификации `openapi.json`
