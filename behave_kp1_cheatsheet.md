# Шпаргалка для экзамена Behave KP1

---

## 1. BDD tools (Behave)

**Что такое Behave:**
- Behave — это инструмент BDD для Python, аналогичный Cucumber.
- Позволяет писать тесты на человеко-понятном языке (Gherkin).

**Установка и структура:**
```bash
pip install behave
```
```
features/
  example.feature
  steps/
    steps.py
```

**Запуск тестов:**
```bash
behave
```

**Полезные ссылки:**
- [Behave README](https://github.com/behave/behave/blob/main/README.rst)
- [Feature Testing Layout](https://behave.readthedocs.io/en/latest/gherkin/#feature-testing-layout)

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

**Пример feature-файла:**
```gherkin
Feature: Showing off behave
  Scenario: run a simple test
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!

  Scenario Outline: Eating cucumbers
    Given there are <start> cucumbers
    When I eat <eat> cucumbers
    Then I should have <left> cucumbers

    Examples:
      | start | eat | left |
      |  12   |  5  |  7   |
      |  20   |  5  |  15  |
```

**Полезные ссылки:**
- [Gherkin Reference (Cucumber)](https://cucumber.io/docs/gherkin/reference/)
- [Behat Gherkin Guide](https://docs.behat.org/en/v2.5/guides/1.gherkin.html)

---

## 3. Step Definitions (реализация шагов)

**Как реализовать шаги:**
- В файле `features/steps/steps.py` используйте декораторы:
  - `@given`, `@when`, `@then`, `@step`

**Примеры:**
```python
from behave import given, when, then

@given('we have behave installed')
def step_impl(context):
    pass  # подготовка

@when('we implement a test')
def step_impl(context):
    pass  # действие

@then('behave will test it for us!')
def step_impl(context):
    pass  # проверка
```

**Параметры и типы:**
```python
@when('I eat {number:d} cucumbers')
def step_impl(context, number):
    # number — это int
    pass
```

**Регулярные выражения:**
```python
import re
from behave import when

@when(re.compile('I eat (\d+) cucumbers'))
def step_impl(context, number):
    pass
```

**Полезные ссылки:**
- [Step Implementations (Behave Docs)](https://behave.readthedocs.io/en/latest/tutorial/#python-step-implementations)

---

## 4. English Examples

**Feature file:**
```gherkin
Feature: Login to the system
  Scenario: Successful login
    Given the user is on the login page
    When they enter a valid username and password
    Then they see the main page
```

**Step Definitions:**
```python
from behave import given, when, then

@given('the user is on the login page')
def step_impl(context):
    pass

@when('they enter a valid username and password')
def step_impl(context):
    pass

@then('they see the main page')
def step_impl(context):
    pass
```

**With parameters:**
```python
@when('they enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    pass
```

---

## 5. Советы для экзамена

- Всегда пишите feature-файлы на понятном языке (можно на русском, если указать `# language: ru`)
- Следите за соответствием шагов в feature-файле и step definition
- Используйте параметры и типы для универсальных шагов
- Проверяйте, что ваши шаги не дублируются
- Для сложных сценариев используйте `Background` и `Scenario Outline`
- Читайте официальную документацию и примеры 