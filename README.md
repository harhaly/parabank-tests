[README_en](https://github.com/harhaly/parabank-tests/blob/master/documents/README_en.md)

<h1 align="center">
  <a href="https://parabank.parasoft.com/parabank/index.htm" title="Демонстрационный сайт">
    <img alt="Logo" src="https://github.com/harhaly/parabank-tests/blob/master/documents/logo.gif?raw=true" width="200px" height="50px" />
  </a>
</h1>

## Что это?

Набор тестов для демонстрационного сайта [Parabank](https://parabank.parasoft.com/parabank/admin.htm) и [Swagger Parabank REST API](https://parabank.parasoft.com/parabank/api-docs/index.html). Основной упор приходится на тестирование API и немного затрагивается UI. Это личный проект для учебных целей.

Тесты разработаны с использованием фреймворка pytest с использованием Requests для тестирования запросов, Pydantic для схем и Selenium WebDriver для UI тестирования (только для Chrome). Для [генерации отчётов](https://harhaly.github.io/parabank-tests/) использован Allure и GitHub Actions.

## Структура проекта

Основные ссылки, переменные хранятся в `configuration.py`, они используются для инициализации тестовых функций (`@pytest.fixture`). Сначала проходит регистрация аккаунта через UI (регистрация по API не предусмотрена со стороны ParaBank), она возвращает переменные, необходимые в последующих тестах.

Часть тестов связаны, при падении некоторых тестов, могут упасть и другие (как пример fixture `create_account`). Разбивка по тестам на текущий момент разделена на GET и POST запросы.

## Установка

- Установить Python 3.10
- Склонировать этот репозиторий и перейти в него.
- Установить пакет env с помощью команды:
    ```
    sudo apt install python3-venv
    ``` 
- Создать виртуальное окружение для Python:
    ```
    python -m venv venv
    ```
- Далее перейти в созданный каталог и активировать виртуальное окружение:
    ```
    source ./bin/activate
    ```
- Установить зависимости:
    ```
    pip install -r requirements.txt
    ```

## Запуск тестов

Запускать тесты можно группами (заранее определены) и индивидуально. Быстрый доступ к основным командам:
- Запуск всех тестов: 
	```
	pytest tests/users
	```
- Запуск тестов GET-запросов:
	```
	pytest tests/users/test_get_accounts.py
	``` 
- Запуск тестов POST-запросов:
	```
	pytest tests/users/test_post.py
	```
- Запуск конкретного теста:
	```
	pytest tests/users/test_get_accounts.py::TestGet::test_validate_accounts_accounts_id
	```

## Запуск генерации Allure report

### Локальный отчёт

Для генерации отчетов необходимо установить в систему приложение Allure. Составление отчета можно запускать как локально, так и через GitHub Actions.

1. Для локальной генерации отчета необходимо запустить:
	```
	pytest --alluredir=\\allure_result tests
	```
2. Выполнить команду:
	```
	allure serve 
	```
После этого должен сформироваться сам html–отчет, который откроется в браузере по умолчанию автоматически.

### GitHub Actions

1. Склонировать этот репозиторий в ваш GitHub account. Файл отвечающий за GitHub Actions — `.github/workflows/run_test.yml`.
2. В ваш аккаунт необходимо добавить секретный TOKEN (название сохранить), создается он по ссылке:
`https://github.com/{имя_аккаунт}/{название_репозитория}/settings/pagesb.com/settings/tokens.`
3. Во вкладке Actions зайти в Automated test и запустить на выбор тест в Run workflow. 
4. Зайти на сгенерированный тест можно
`https://github.com/{имя_аккаунта}/{название_репозитория}/settings/pages`

## TODO

Несмотря на что, что многие цели были достигнуты, все еще есть дополнительные функции, которые я хотел бы добавлять в будущем, когда будет время.  

- [ ] Добавить различных параметров в API запросы.
- [ ] Убрать импорт time.sleep
- [ ] Интеграция в Jenkins
- [ ] Составить шаблон и пример тест кейса
- [ ] Составить шаблон и пример баг репорта

## Ссылки по теме и документация
* [Тестируемый веб сайт](https://parabank.parasoft.com/parabank/admin.htm)
* [Тестируемое API](https://parabank.parasoft.com/parabank/api-docs/index.html)
* [Allure report](https://harhaly.github.io/parabank-tests/)
* [Тест кейс на английском](https://docs.google.com/spreadsheets/d/1eoF9LRaEGKj63altIam2rnDXi5NagGyF/edit?usp=drive_link&ouid=118116959263751703136&rtpof=true&sd=true)
* [Тест кейс на русском](https://docs.google.com/spreadsheets/d/1wWk-MLANMcW1VtjMtVnqmTfoTZvg3aRK/edit?usp=drive_link&ouid=118116959263751703136&rtpof=true&sd=true)
