# Selenium Python Automation Framework

This project is a scalable test automation framework built using Python, Selenium WebDriver, Pytest, and the Page Object Model (POM) design pattern.

The framework is designed following best practices for maintainability, reusability, and readability, similar to production-level automation frameworks used in real projects.

## Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* WebDriver Manager

## Project Structure

```
selenium-python-framework/
│
├── data/                # Test data
├── pages/               # Page Object classes
├── tests/               # Test cases
├── utils/               # Utilities (driver factory, config, logger)
│
├── conftest.py          # Pytest fixtures
├── pytest.ini           # Pytest configuration
├── requirements.txt     # Dependencies
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd selenium-python-framework
```

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

## How to Run Tests

To execute all tests:

```
pytest
```

To run a specific test file:

```
pytest tests/test_login.py
```

To run a specific test case:

```
pytest tests/test_login.py::test_valid_login
```

## Test Target

The framework uses the following demo application:

https://www.saucedemo.com/

## Features

* Page Object Model (POM) implementation
* Reusable base page with common actions
* Centralized driver management
* Pytest fixtures for setup and teardown
* Clean and scalable project structure

## Best Practices Applied

* Separation of concerns (tests vs pages vs utilities)
* Explicit waits instead of static waits
* Reusable components and methods
* Easy test execution and scalability

## Future Improvements

* Allure reporting integration
* Parallel execution with pytest-xdist
* CI/CD pipeline (GitHub Actions or Jenkins)
* Environment configuration (QA / Prod)
* Screenshot on failure
* Logging improvements