
### Оглавление
[Обзор и инструменты](#обзор-и-инструменты) <br>
[Структура проекта](#структура-проекта) <br>
[Установка](#установка) <br>
[Запуск тестов](#запуск-тестов) <br>
[Запуск генерации Allure report](#запуск-генерации-allure-report) <br>
[Ссылки по теме и документация](#ссылки-по-теме-и-документация) <br>
<a name="link"></a>
## Обзор и инструменты
Тестовый фреймворк для демонстрационного сайта [Parabank](https://parabank.parasoft.com/parabank/admin.htm) и [Swagger Paranak REST API](https://parabank.parasoft.com/parabank/api-docs/index.html). Основной упор приходится тестировании API и немного затрагивается UI. Это личный проект для учебных целей, никакого другого отношения к реальной тестируемой систему я не имею.

Текущая среда тестирования разработана с использованием среды тестирования Python Pytest с использованием Request для тестирования запросов. Pydantic для схем и Selenium WebDriver для UI тестирования (Только для Chrome). А также генерации Allure отчетов, как локально, так и через githun actions [Allure report](https://harhaly.github.io/parabank-tests/)
<a name="link"></a>
## Структура проекта
Основные ссылки, переменные хранятся в configuration.py, они используются для инициализации тестовых функций (@pytest.fixture). Сначала проходит регистрация аккаунта через UI (регистрация по API не предусмотрена), она возвращает переменные, необходимые в последующих тестах. Часть тестов связаны, при падении некоторых тестов, могут упасть и другие (как пример fixture create_account). Разбивка по тестам на текущий момент разделена на get и post запросы. 
<a name="link"></a>
## Установка
- Установка Python 3.10
- Копирование этого репозитория и перехода в него.
- Установка пакета env с помощью команды:
`sudo apt install python3-venv` 
- Создать виртуальное окружение для Python:
`python -m venv venv`
- Далее перейти в созданный каталог и активировать виртуальное окружение:
	- для linux source `/bin/activate`
- Установка зависимостей:
`pip install -r requirements.txt`
<a name="link"></a>
## Запуск тестов
Эта среда спроектирована так, чтобы не содержать неясной информации о параметрах при запуске тестов, поэтому их можно запускать с помощью обычных команд Python. Быстрый доступ к основным командам:
- Запуск всех тестов: 
	```
	pytest tests/users
	```
- Запуск тестов get запросов:
	```
	pytest tests/users/test_get_accounts.py
	``` 
- Запуск тестов post запросов:
	```
	pytest tests/users/test_post.py
	```
- Запуск конкретного теста:
	```	
	test tests/users/test_get_accounts.py::TestGet::test_validate_accounts_accounts_id
	```
<a name="link"></a>
## Запуск генерации Allure report
Для генерации отчетов необходимо установить в систему приложение Allure. Составление отчета можно запускать как локально, так и через github actions.

1. Для локальной генерации отчета необходимы запустить отчеты:
	```
	pytest --alluredir=\\allure_result tests
	```
2. Выполнить команду:
	```
	allure serve 
	```
После этого должен сформироваться сам html–отчет, который откроется в браузере по умолчанию автоматически.

1. Для генерации allure отчета в github actions необходимо клонировать этот репозиторий в ваш gitgub account. Файл отвечающий за  github actions находится `.github/workflows/run_test.yml`.
2. В ваш аккаунт необходимо добавить секретный TOKEN (название сохранить), создается он по ссылке:
`https://githuhttps://github.com/{имя_аккаунт}/{название_репозитория}/settings/pagesb.com/settings/tokens.`
3. Во вкладке Actions зайти в Automated test и запустить на выбор тест в Run workflow. 
4. Зайти на сгенерированный тест можно
`https://github.com/{имя_аккаунта}/{название_репозитория}/settings/pages`

Несмотря на что, что многие цели были достигнуты, все еще есть дополнительные функции, которые я хотел бы добавлять в будущем, когда будет время.  
- [ ] Добавить различных параметров в API запросы.
- [ ] Убрать импорт time.sleep
- [ ] Интеграция в Jenkins
- [ ] Создание типового тест кейса
- [ ] Создание типовых баг репортов
<a name="link"></a>
## Ссылки по теме и документация
* [Тестируемый веб сайт](https://parabank.parasoft.com/parabank/admin.htm)
* [Тестируемое API](https://parabank.parasoft.com/parabank/api-docs/index.html)
* [Allure report](https://harhaly.github.io/parabank-tests/)

