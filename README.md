# LumaProjectPython_2024_spring

Перед написанием тестов очень рекомендуются к прочтению, просмотру данные материалы.

Что такое POM:

1. <https://martinfowler.com/bliki/PageObject.html>
2. <https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/>

Каким бывает POM:

1. Перевод статьи Black Norrish: <https://testengineer.ru/bolshoj-gajd-po-page-object-model/>
2. Прекрасный репозиторий с примерами для UI тестов создателя Selene (Яков Крамаренко): <https://github.com/yashaka/python-web-test/tree/master>
3. Прекрасный доклад Андрея Солнцева: <https://www.youtube.com/watch?v=pln38fIbYqA&t=363s>
4. Прекрасный доклад Алексея Виноградова: <https://www.youtube.com/watch?v=zccUzJFduzo&t=2s>
5. Еще один пример UI архитектуры: <https://habr.com/ru/articles/708932/>

Как пишем тесты мы?

При написании тестов используем паттерн Page Objects (Так же называют: Page Elements, POM, Page components и так далее)

В папке /pages хранятся компоненты, которые описывают взаимодействие с компонентами на странице.

В тестах мы импортируем необходимый модуль из pages.

## Нюансы реализации

Правила для написания пэйджей (Так же называют: компоненты, виджеты, страницы и еще как нибудь)

1. Не используем классы
2. Не наследуемся от базового класса. При необходимости вспомогательные сущности можно выносить в отдельные модули (Хэлперы)
3. Локаторы храним только в пэйджах. По необходимости их можно выносить в отдельные модули, но использовать можно только в пэйджах
4. Тестовые данные прокидываем только в тестах

```python
from selene import browser
from selene.support.shared.jquery_style import s

url = "https://magento.softwaretestingboard.com/customer/account/login"


def visit():
    browser.open(url)


def login(user, password):
    s("#email").type(user)
    s("#pass").type(password)
    s("#send2").click()
```

Пример реализации можно глянуть в репозитории c кодом 8 занятия:
<https://github.com/victoretc/selenium_automation_course/tree/main/lesson8>
