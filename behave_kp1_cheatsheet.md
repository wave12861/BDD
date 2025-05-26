# Шпаргалка для экзамена Behave KP1

------ 

## 1. BDD tools (Behave)

**Что такое BDD:**
- Behavior-Driven Development (BDD) — методология разработки, основанная на описании поведения системы
- Фокусируется на бизнес-ценности и пользовательском опыте
- Использует естественный язык для описания сценариев

**Что такое Behave:**
- Behave — это инструмент BDD для Python, аналогичный Cucumber
- Позволяет писать тесты на человеко-понятном языке (Gherkin)
- Поддерживает как английский, так и русский языки

**Установка и структура:**
```bash
pip install behave pytest-playwright playwright
```
```
features/
  example.feature
  steps/
    steps.py
  environment.py  # настройки и хуки
```

**Запуск тестов:**
```bash
behave  # запуск всех тестов
behave features/example.feature  # запуск конкретного feature-файла
behave --tags @smoke  # запуск тестов с определенным тегом
```

**Полезные ссылки:**
- [Behave README](https://github.com/behave/behave/blob/main/README.rst)
- [Feature Testing Layout](https://behave.readthedocs.io/en/latest/gherkin/#feature-testing-layout)
- [Playwright Python Docs](https://playwright.dev/python/)

---

## 2. Gherkin syntax (язык описания сценариев)

**Ключевые слова:**
- `Feature:` — описание функционала
- `Scenario:` — отдельный сценарий
- `Given` (Дано) — начальное состояние
- `When` (Когда) — действие
- `Then` (Тогда) — ожидаемый результат
- `And`, `But` (И, Но) — дополнительные шаги
- `Background:` — шаги, выполняющиеся перед каждым сценарием
- `Scenario Outline:` — шаблон сценария для разных данных
- `Examples:` — таблица данных для Scenario Outline
- `@tags` — теги для группировки сценариев

**Пример feature-файла:**
```gherkin
# language: ru
Feature: Покупка товара
  Как покупатель
  Я хочу добавить товар в корзину
  Чтобы оформить заказ

  Background:
    Given я нахожусь на главной странице
    And я авторизован как "test@example.com"

  @smoke
  Scenario: Добавление товара в корзину
    Given я нахожусь в каталоге товаров
    When я добавляю товар "Телефон" в корзину
    Then товар "Телефон" должен появиться в корзине
    And общая сумма корзины должна быть "1000" рублей

  Scenario Outline: Проверка скидок
    Given я нахожусь в каталоге товаров
    When я добавляю товар "<товар>" в корзину
    Then скидка должна быть "<скидка>" рублей

    Examples:
      | товар    | скидка |
      | Телефон  | 100    |
      | Ноутбук  | 200    |
```

**Полезные ссылки:**
- [Gherkin Reference (Cucumber)](https://cucumber.io/docs/gherkin/reference/)
- [Behat Gherkin Guide](https://docs.behat.org/en/v2.5/guides/1.gherkin.html)

---

## 3. Step Definitions (реализация шагов)

**Как реализовать шаги:**
- В файле `features/steps/steps.py` используйте декораторы:
  - `@given`, `@when`, `@then`, `@step`
- Каждый шаг должен быть уникальным
- Используйте контекст (`context`) для передачи данных между шагами

**Примеры с Playwright:**
```python
from behave import given, when, then

@given('я нахожусь на главной странице')
def step_impl(context):
    context.page.goto("http://example.com")

@when('я добавляю товар "{товар}" в корзину')
def step_impl(context, товар):
    context.page.click(f'text={товар}')
    context.page.click('button#add-to-cart')

@then('товар "{товар}" должен появиться в корзине')
def step_impl(context, товар):
    context.page.goto("http://example.com/cart")
    assert context.page.locator(f'text={товар}').is_visible()
```

**Параметры и типы:**
```python
@when('я ввожу {number:d} рублей')
def step_impl(context, number):
    context.page.fill('#amount', str(number))

@when('я выбираю дату "{date}"')
def step_impl(context, date):
    context.page.fill('#date', date)
```

**Регулярные выражения:**
```python
import re
from behave import when

@when(re.compile('я вижу (\d+) товаров'))
def step_impl(context, number):
    count = int(context.page.inner_text('#product-count'))
    assert count == int(number)
```

**Полезные ссылки:**
- [Step Implementations (Behave Docs)](https://behave.readthedocs.io/en/latest/tutorial/#python-step-implementations)
- [Playwright Python Docs](https://playwright.dev/python/)

---

## 4. Environment и Hooks (Playwright)

**Что такое environment.py:**
- Файл для настройки тестового окружения
- Содержит хуки (функции, выполняемые в определенные моменты)
- Позволяет настраивать контекст тестов

**Пример environment.py для Playwright:**
```python
from playwright.sync_api import sync_playwright

def before_all(context):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context.browser = browser
    context.page = browser.new_page()
    context._playwright = playwright

def after_all(context):
    context.page.close()
    context.browser.close()
    context._playwright.stop()

def before_scenario(context, scenario):
    # Можно добавить подготовку данных или логирование
    pass

def after_step(context, step):
    if step.status == "failed":
        context.page.screenshot(path=f"failed_{step.name}.png")
```

**Основные хуки:**
- `before_all` — перед всеми тестами
- `after_all` — после всех тестов
- `before_feature` — перед каждым feature-файлом
- `after_feature` — после каждого feature-файла
- `before_scenario` — перед каждым сценарием
- `after_scenario` — после каждого сценария
- `before_step` — перед каждым шагом
- `after_step` — после каждого шага

---

## 5. Советы для экзамена

- Всегда пишите feature-файлы на понятном языке (можно на русском, если указать `# language: ru`)
- Следите за соответствием шагов в feature-файле и step definition
- Используйте параметры и типы для универсальных шагов
- Проверяйте, что ваши шаги не дублируются
- Для сложных сценариев используйте `Background` и `Scenario Outline`
- Используйте теги для группировки и фильтрации тестов
- Читайте официальную документацию и примеры
- Используйте environment.py для настройки тестового окружения
- Добавляйте скриншоты при падении тестов
- Следуйте принципам BDD: описывайте поведение, а не реализацию 