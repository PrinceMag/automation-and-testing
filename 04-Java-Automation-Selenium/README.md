# 04 — Java Automation with Selenium

> Build a professional-grade test automation framework using Java, Selenium WebDriver, TestNG, and the Page Object Model — the exact stack used by QA teams at large companies.

---

## Course Overview

This is the final course in the programme and the most industry-relevant. You will combine everything you have learned — Java OOP, Selenium, and structured test design — into a complete automation framework. By the end you will have a portfolio project you can show to employers.

**Duration:** 4 weeks  
**Effort:** 5–10 hours per week  
**Level:** Intermediate (all previous courses completed)  
**Pre-requisites:** Course 02 (Python Automation) + Course 03 (Java Fundamentals)

---

## What You Will Learn

- Set up a Selenium Maven project in IntelliJ IDEA
- Write and run browser automation tests in Java
- Use TestNG as the test framework (annotations, assertions, grouping)
- Implement the Page Object Model (POM) with `PageFactory`
- Write data-driven tests using `@DataProvider`
- Run tests across multiple browsers (Chrome, Firefox, Edge)
- Generate interactive Allure test reports
- Understand the basics of CI/CD for test automation

---

## Python vs Java Selenium — Syntax Comparison

| Action | Python | Java |
|--------|--------|------|
| Import | `from selenium import webdriver` | `import org.openqa.selenium.WebDriver;` |
| Create driver | `driver = webdriver.Chrome()` | `WebDriver driver = new ChromeDriver();` |
| Open URL | `driver.get("https://...")` | `driver.get("https://...");` |
| Find element | `driver.find_element(By.ID, "x")` | `driver.findElement(By.id("x"));` |
| Click | `element.click()` | `element.click();` |
| Type text | `element.send_keys("text")` | `element.sendKeys("text");` |
| Close browser | `driver.quit()` | `driver.quit();` |

> The logic is identical — only the syntax changes. Your Python knowledge transfers directly.

---

## 4-Week Roadmap

### Week 1 — Maven Project Setup & WebDriver in Java

| Topic | Key Concepts |
|-------|-------------|
| Maven project structure | `src/main/java`, `src/test/java`, `pom.xml` |
| Adding dependencies | `selenium-java`, `testng`, `webdriver-manager` in `pom.xml` |
| `WebDriverManager` | Auto-handles ChromeDriver download — no manual setup |
| `BaseTest` class | Reusable `setup()` and `teardown()` methods |
| First Java Selenium test | Open browser, navigate, read title, close |

### Week 2 — TestNG Framework

| Topic | Key Concepts |
|-------|-------------|
| TestNG vs JUnit | TestNG — more features for test automation (preferred in Selenium projects) |
| Core annotations | `@BeforeMethod`, `@AfterMethod`, `@BeforeClass`, `@AfterClass`, `@Test` |
| Running tests | Right-click → Run, or `mvn clean test` |
| `testng.xml` | Define test suites, groups, parallel execution |
| Assertions | `Assert.assertEquals()`, `Assert.assertTrue()`, `SoftAssert` |
| `@DataProvider` | Run the same test with multiple data sets |

### Week 3 — Page Object Model (POM)

| Topic | Key Concepts |
|-------|-------------|
| POM principle | One Java class per page — separate locators from test logic |
| `PageFactory` | `@FindBy` annotation + `PageFactory.initElements()` |
| `@FindBy` locators | `@FindBy(id = "x")`, `@FindBy(css = ".class")`, `@FindBy(xpath = "//...")` |
| Reusable page methods | `loginPage.login("user", "pass")` — clean test code |
| Folder structure | `pages/`, `tests/`, `utils/`, `conftest` via `@BeforeMethod` |
| Base page | Common methods shared across all page classes |

### Week 4 — Reports, Data-Driven & Cross-Browser

| Topic | Key Concepts |
|-------|-------------|
| Allure Reports | `allure-testng` dependency, `@Step`, `@Description`, `@Severity` |
| Screenshot on failure | `driver.getScreenshotAs(OutputType.FILE)` in `@AfterMethod` |
| `@DataProvider` | Read from inline arrays; advanced: read from Excel with Apache POI |
| Cross-browser | `switch(browser)` → `ChromeDriver / FirefoxDriver / EdgeDriver` |
| `testng.xml` params | `<parameter name="browser" value="firefox"/>` |
| Parallel execution | `parallel="methods"` or `parallel="tests"` in `testng.xml` |

---

## Setup Instructions

### 1. Create Maven Project in IntelliJ

`File → New → Project → Maven → Fill in GroupId and ArtifactId`

### 2. Add Dependencies to `pom.xml`

```xml
<dependencies>
    <!-- Selenium -->
    <dependency>
        <groupId>org.seleniumhq.selenium</groupId>
        <artifactId>selenium-java</artifactId>
        <version>4.18.1</version>
    </dependency>

    <!-- WebDriver Manager -->
    <dependency>
        <groupId>io.github.bonigarcia</groupId>
        <artifactId>webdrivermanager</artifactId>
        <version>5.7.0</version>
    </dependency>

    <!-- TestNG -->
    <dependency>
        <groupId>org.testng</groupId>
        <artifactId>testng</artifactId>
        <version>7.9.0</version>
        <scope>test</scope>
    </dependency>

    <!-- Allure TestNG -->
    <dependency>
        <groupId>io.qameta.allure</groupId>
        <artifactId>allure-testng</artifactId>
        <version>2.25.0</version>
    </dependency>
</dependencies>
```

---

## Code Examples

### Base Test Class

```java
// src/test/java/base/BaseTest.java
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;

public class BaseTest {
    protected WebDriver driver;

    @BeforeMethod
    public void setup() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        driver.manage().window().maximize();
    }

    @AfterMethod
    public void teardown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
```

### Page Class (POM + PageFactory)

```java
// src/test/java/pages/LoginPage.java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class LoginPage {

    @FindBy(id = "username")
    private WebElement usernameField;

    @FindBy(id = "password")
    private WebElement passwordField;

    @FindBy(id = "loginBtn")
    private WebElement loginButton;

    public LoginPage(WebDriver driver) {
        PageFactory.initElements(driver, this);
    }

    public void login(String username, String password) {
        usernameField.sendKeys(username);
        passwordField.sendKeys(password);
        loginButton.click();
    }
}
```

### Test Class

```java
// src/test/java/tests/LoginTest.java
import base.BaseTest;
import org.testng.Assert;
import org.testng.annotations.Test;
import pages.LoginPage;

public class LoginTest extends BaseTest {

    @Test
    public void testValidLogin() {
        driver.get("https://the-internet.herokuapp.com/login");

        LoginPage loginPage = new LoginPage(driver);
        loginPage.login("tomsmith", "SuperSecretPassword!");

        Assert.assertTrue(
            driver.getCurrentUrl().contains("secure"),
            "Login failed — URL does not contain 'secure'"
        );
    }
}
```

---

## Project Structure

```
automation-framework/
├── pom.xml
├── testng.xml
└── src/
    └── test/
        └── java/
            ├── base/
            │   └── BaseTest.java       ← WebDriver setup/teardown
            ├── pages/
            │   ├── LoginPage.java      ← Page class with locators + methods
            │   └── HomePage.java
            ├── tests/
            │   ├── LoginTest.java      ← Test methods
            │   └── SearchTest.java
            └── utils/
                └── ScreenshotUtil.java ← Helper: take screenshot on failure
```

---

## Assignments

| Assignment | Topics | Marks |
|------------|--------|-------|
| Assignment 1 | Automate login on The Internet — BaseTest + TestNG annotations | 100 |
| Assignment 2 | Build `LoginPage` and `HomePage` using POM + PageFactory | 100 |
| Assignment 3 | Data-driven login tests — valid + invalid credentials via `@DataProvider` | 100 |
| Month Project | Full e-commerce suite — login, search, add to cart, checkout — POM + TestNG + Allure report | 100 |

---

## Career Outcomes

After completing this course you can apply for:

| Role | Typical Salary (ZAR) | Requirements |
|------|----------------------|-------------|
| Junior QA Automation Engineer | R20,000 – R35,000/month | This programme + portfolio project |
| Mid-level SDET | R35,000 – R60,000/month | 1–2 years experience + CI/CD knowledge |
| QA Lead / Automation Architect | R60,000 – R90,000/month | 3+ years + framework design experience |

---

## Useful Resources

| Resource | Link |
|----------|------|
| Selenium Java Docs | [selenium.dev/documentation](https://www.selenium.dev/documentation/) |
| TestNG Documentation | [testng.org](https://testng.org/doc/) |
| Allure Framework | [allurereport.org](https://allurereport.org/) |
| The Internet (practice site) | [the-internet.herokuapp.com](https://the-internet.herokuapp.com) |
| WebDriverManager Docs | [github.com/bonigarcia/webdrivermanager](https://github.com/bonigarcia/webdrivermanager) |

---

*Course 4 of 4 — Zinza Institute Of Technology*
