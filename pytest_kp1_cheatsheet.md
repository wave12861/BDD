# 🧪 Шпаргалка по Pytest KP1

---

## 1. Основы тестового фреймворка (Testing framework basics)

**Как реализовать простой тест:**
- Любая функция, имя которой начинается с `test_`, считается тестом.
- Для проверки условий используйте `assert`.

**Пример:**
```python
def test_sum():
    assert 1 + 1 == 2
```

**Как пометить методы как тестовые:**
- Имя функции должно начинаться с `test_`.
- Можно использовать классы, имя которых начинается с `Test`.

**Игнорировать тест:**
- Используйте декоратор `@pytest.mark.skip` или `@pytest.mark.skipif`.

**Пример:**
```python
import pytest

@pytest.mark.skip(reason="Not implemented yet")
def test_feature():
    assert False
```

**Подробнее:**
- [Pytest Getting Started](https://docs.pytest.org/en/7.1.x/getting-started.html)

---

## 2. Data Driven Testing (DDT)

**Когда использовать DDT:**
- Когда нужно проверить одну и ту же функцию с разными наборами данных.
- Для параметризации тестов.

**Синтаксис DDT в pytest (parametrize):**
- Используйте декоратор `@pytest.mark.parametrize`.

**Пример:**
```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (10, 5, 15)
])
def test_add(a, b, expected):
    assert a + b == expected
```

**Подробнее:**
- [Pytest Parametrize](https://docs.pytest.org/en/7.1.x/how-to/parametrize.html)

---

## 3. Preconditions and Postconditions (Фикстуры, pre/postconditions)

**Что такое фикстуры?**
Фикстура — это специальная функция, которая подготавливает (и/или очищает) окружение для теста. Фикстуры позволяют:
- Подготовить данные, окружение, соединения, файлы и т.д. до запуска теста.
- Очистить или закрыть ресурсы после выполнения теста.
- Избежать дублирования кода подготовки/очистки.
- Сделать тесты независимыми друг от друга.

**Как объявить фикстуру:**
```python
import pytest

@pytest.fixture
def sample_data():
    # Подготовка (precondition)
    data = {"user": "test"}
    yield data
    # Очистка (postcondition)
    data.clear()
```

**Как использовать фикстуру в тесте:**
```python
def test_user(sample_data):
    assert sample_data["user"] == "test"
```

**Область действия (scope) фикстур:**
- `function` (по умолчанию) — для каждого теста
- `class` — для всех тестов в классе
- `module` — для всех тестов в файле
- `session` — для всех тестов в запуске pytest

```python
@pytest.fixture(scope="module")
def db_connection():
    conn = connect_to_db()
    yield conn
    conn.close()
```

**Автоматический запуск фикстур (autouse):**
Если указать `autouse=True`, фикстура будет запускаться автоматически для всех тестов в области действия:
```python
@pytest.fixture(autouse=True)
def setup_and_teardown():
    print("Setup")
    yield
    print("Teardown")
```

**Фикстуры могут вызывать другие фикстуры:**
```python
@pytest.fixture
def user():
    return {"name": "Alice"}

@pytest.fixture
def user_with_email(user):
    user["email"] = "alice@example.com"
    return user
```

**Где хранить фикстуры:**
- В тестовых файлах (если используются только там)
- В файле `conftest.py` — для общих фикстур, доступных во всех тестах директории

**Пример сложной фикстуры:**
```python
import pytest

@pytest.fixture(scope="function")
def temp_file(tmp_path):
    file = tmp_path / "data.txt"
    file.write_text("hello")
    yield file
    # postcondition: файл автоматически удалится после теста
```

**Подробнее:**
- [Pytest Fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.html)
- [conftest.py (geeksforgeeks)](https://www.geeksforgeeks.org/conftest-in-pytest/)

---

**Советы:**
- Используйте параметризацию для сокращения количества кода
- Разделяйте подготовку и очистку через фикстуры
- Для сложных pre/postconditions используйте разные области действия фикстур
- Не забывайте про `conftest.py` для общих фикстур 