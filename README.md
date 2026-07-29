SauceDemo Automation Testing Framework

Автоматизированные тесты для SauceDemo на Python, Playwright, pytest (POM & Page Component & Page Elements).

#### 1. Установка
```Bash
git clone https://github.com/quovadiz/saucedemo_testing
cd saucedemo_testing
python3 -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
playwright install
```

#### 2. Конфигурация (.env)
Создайте файл .env в корне проекта:
```
BASE_URL=https://www.saucedemo.com/
STANDARD_USER=standard_user
LOCKED_OUT_USER=locked_out_user
PERFORMANCE_GLITCH_USER=performance_glitch_user
PASSWORD=secret_sauce
HEADLESS=true
```

#### Запуск тестов

Все тесты:

```Bash
python3 -m pytest
```
По маркерам:

```Bash
python3 -m pytest -m regression
python3 -m pytest -m cart
python3 -m pytest -m checkout
python3 -m pytest -m inventory
```

#### Allure-отчеты
```Bash
python3 -m pytest --alluredir=allure-results
allure serve allure-results
```