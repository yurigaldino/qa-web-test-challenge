# qa-web-test-challenge

This README includes explanations of the project, instructions on how to run the tests, and information about commit and branch patterns.

# Selenium Web Automation Project

This project is a Selenium-based web automation framework for testing the saucedemo.com website. It includes test cases written in Python using the unittest framework, and the Page Object Pattern for better test maintenance.

## Setup

### Prerequisites

- Python (version 3.7 or higher)
- ChromeDriver (or WebDriver for your preferred browser)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yurigaldino/qa-web-test-challenge.git
```
   
2. Navigate to the project directory:
  ```bash
  cd qa-web-test-challenge
  ```
3. Install the required dependencies:

  ```bash
  pip install selenium
  ```

4. Download and place the WebDriver executable (e.g., ChromeDriver) in the project directory or update the webdriver.Chrome() line in the code with the correct path.

## Running Tests
Run the following command to execute the tests:

```bash
python test_script.py
```
This will run the tests and generate an XML report in the 'test-reports' directory.

## Commit and Branch Patterns
#### Branch Naming
- feature/{two_chars_of_your_name}/{feature-name}: For adding a new feature.
- bugfix/{two_chars_of_your_name}/{bug-description}: For fixing a bug.
- enhancement/{two_chars_of_your_name}/{enhancement-description}: For improvements and enhancements.

#### Commit Messages
English commits pattern:

For example:

```bash
git commit -m "add login test"
```

Contributor
Your Name yurifgdesouza@gmail.com





