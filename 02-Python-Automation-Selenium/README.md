# 02 — Python Automation with Selenium

> Learn to control a web browser with code — find elements, fill forms, click buttons, and write real automated test scripts using Python and Selenium WebDriver.

---

## Course Overview

Selenium is the world's most widely used browser automation tool. This course teaches you to write Python scripts that control Chrome, and then structure those scripts into professional test suites using `pytest` and the Page Object Model (POM).

**Duration:** 4 weeks  
**Effort:** 5–10 hours per week  
**Level:** Beginner (with Python Fundamentals completed)  
**Pre-requisite:** Course 01 — Python Fundamentals

---

## What You Will Learn

- Set up Selenium WebDriver with Python
- Open browsers and navigate to URLs programmatically
- Find web elements using all major locator strategies
- Write XPath and CSS selectors confidently
- Handle timing issues using Selenium waits
- Interact with forms, buttons, dropdowns, and alerts
- Write test functions using the `pytest` framework
- Organise test code using the Page Object Model (POM)
- Generate HTML test reports

---

## 4-Week Roadmap

### Week 1 — Selenium Setup & Basic Navigation

| Topic | Key Concepts |
|-------|-------------|
| Environment setup | `pip install selenium`, `webdriver-manager`, VS Code |
| WebDriver basics | `driver.get()`, `driver.title`, `driver.quit()` |
| Browser control | `maximize_window()`, `back()`, `forward()`, `refresh()` |
| First automation | Open a website, read the title, close the browser |

### Week 2 — Finding Elements (Locators)

| Topic | Key Concepts |
|-------|-------------|
| `By.ID` | Fastest, most reliable — always prefer ID when available |
| `By.NAME` | Good for form input fields |
| `By.CLASS_NAME` | Targets elements by CSS class |
| `By.TAG_NAME` | Selects by HTML tag |
| `By.LINK_TEXT` | Finds anchor (`<a>`) tags by their visible text |
| `By.XPATH` | Powerful — navigate complex DOM structures |
| `By.CSS_SELECTOR` | Fast and flexible — preferred over XPath when possible |

### Week 3 — Waits, Actions & Form Interaction

| Topic | Key Concepts |
|-------|-------------|
| Implicit wait | `driver.implicitly_wait(10)` — global timeout for all `find_element` calls |
| Explicit wait | `WebDriverWait(driver, 10).until(EC.visibility_of_element_located(...))` |
| Fluent wait | Custom polling interval + ignored exceptions |
| Element actions | `.click()`, `.send_keys()`, `.clear()`, `.text`, `.submit()` |
| ActionChains | Hover, drag-and-drop, right-click |
| JavaScript executor | Scroll into view, click hidden elements |

### Week 4 — pytest & Page Object Model

| Topic | Key Concepts |
|-------|-------------|
| pytest basics | `def test_*`, `assert`, `@pytest.fixture`, auto-discovery |
| Fixtures | Setup and teardown — open/close browser |
| `@pytest.mark.parametrize` | Run the same test with different data |
| Page Object Model | One class per page, locators defined once, tests stay clean |
| POM folder structure | `pages/`, `tests/`, `conftest.py` |
| Reports | `pytest-html`, `allure-pytest` |

---

## Setup Instructions

```bash
# 1. Install Selenium and WebDriver Manager
pip install selenium
pip install webdriver-manager

# 2. Install pytest and reporting
pip install pytest
pip install pytest-html

# 3. Verify installation
python -c "import selenium; print(selenium.__version__)"
```

```python
# Minimal working example
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
print(driver.title)   # Google
driver.quit()
```

---

## Project Structure (POM)

```
project/
├── pages/
│   ├── login_page.py       ← LoginPage class (locators + methods)
│   └── home_page.py        ← HomePage class
├── tests/
│   ├── test_login.py       ← Test functions
│   └── test_search.py
├── conftest.py             ← Shared fixtures (driver setup/teardown)
└── requirements.txt
```

---

## Assignments

| Assignment | Topics | Marks |
|------------|--------|-------|
| Assignment 1 | Automate login on a demo site — open browser, find elements, submit form | 100 |
| Assignment 2 | Scrape product names from a page using all locator types | 100 |
| Assignment 3 | Form submission test with explicit waits | 100 |
| Month Project | Full login → search → logout test suite using POM + pytest + HTML report | 100 |

---

## Practice Websites

| Site | What to Practise |
|------|-----------------|
| [the-internet.herokuapp.com](https://the-internet.herokuapp.com) | Login, forms, alerts, frames, drag-and-drop |
| [demoqa.com](https://demoqa.com) | All element types — inputs, checkboxes, dropdowns |
| [automationexercise.com](https://automationexercise.com) | Full e-commerce test flows |
| [testingplayground.com](http://www.testingplayground.com) | XPath practice |
| [seleniumdemo.com](https://www.seleniumdemo.com) | Beginner-friendly demo site |

---

## Key Rules

```python
# ❌ Never use time.sleep() in production tests
import time
time.sleep(3)   # BAD — brittle, slow

# ✅ Use Selenium waits instead
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))
)

# ❌ Never put locators inside test methods
def test_login():
    driver.find_element(By.ID, "username").send_keys("admin")  # BAD

# ✅ Define locators in a Page class
class LoginPage:
    USERNAME = (By.ID, "username")

    def enter_username(self, text):
        self.driver.find_element(*self.USERNAME).send_keys(text)
```

---

## Useful Resources

| Resource | Link |
|----------|------|
| Selenium Python Docs | [selenium-python.readthedocs.io](https://selenium-python.readthedocs.io/) |
| pytest Docs | [docs.pytest.org](https://docs.pytest.org/) |
| XPath Cheat Sheet | [devhints.io/xpath](https://devhints.io/xpath) |
| CSS Selectors Reference | [w3schools.com/cssref/css_selectors](https://www.w3schools.com/cssref/css_selectors.php) |

---

*Course 2 of 4 — Zinza Institute Of Technology*
