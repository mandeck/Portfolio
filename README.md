# QA Engineer Portfolio — Michael Andeck

QA portfolio showcasing projects completed through the TripleTen Quality Assurance Engineering program. Focus areas include manual testing, Python-based test automation, API testing, SQL, and defect reporting.

With a background in Mechanical Engineering, I bring experience in technical problem-solving, requirements analysis, and systematic verification to software quality assurance.

## Skills & Tools

- **Test Automation:** Python, Selenium WebDriver, Pytest, Page Object Model (POM), assertions, explicit waits
- **Manual Testing:** Test case design, test execution, exploratory testing, equivalence partitioning, boundary value analysis, requirements analysis
- **API Testing:** Postman, HTTP methods, status codes, positive and negative testing, request and response validation
- **Database Testing:** SQL queries, filtering, aggregation, NULL handling
- **Mobile Testing:** Android Studio emulator, UI validation, notification testing, network connectivity testing
- **Defect Management & Tools:** Jira, Chrome DevTools, PyCharm, Git, GitHub

## Projects

### 1. Urban Routes — Selenium Automation Suite

Developed a Python-based automated test suite using Selenium WebDriver and Pytest to validate a ride-booking workflow.

**Key contributions:**
- Implemented the Page Object Model to organize page locators and reusable interaction methods.
- Automated workflow steps including route selection, service selection, phone number entry, payment details, driver comments, and additional order options.
- Used assertions and explicit waits to validate application behavior and synchronize interactions.
- Separated test data from test logic for easier maintenance.
- Integrated a provided helper function for retrieving SMS confirmation codes during testing.

**Results:** All 8 automated tests passed.

**Technologies:** Python, Selenium WebDriver, Pytest

- [View source code](https://github.com/mandeck/Portfolio/tree/main/automation)
- [Watch project demo](https://www.youtube.com/watch?v=pGnAUSi8O0I)

**Environment & Execution Requirements:**

This project was developed and tested against the Urban Routes application hosted in the TripleTen course environment. The application is accessed through a temporary server URL, which must be entered in `Input_data_UrbanRoutes.py` before running the tests.

The hosted application is provided for educational purposes and is not guaranteed to remain available permanently. Consequently, the automation code can be reviewed independently, but executing the test suite requires access to a compatible, running Urban Routes environment.

### 2. Urban Scooter — QA Capstone Project

Completed a multi-platform testing project covering a scooter rental and delivery application across web, mobile, and backend API functionality.

**Web application testing**
- Designed and executed 66 test cases covering customer information fields, positive and negative inputs, equivalence classes, and boundary values.
- Tested in Google Chrome and Opera at a specified screen resolution.
- Documented defects with reproduction steps, expected and actual results, environments, severity, and supporting evidence.

**Mobile application testing**
- Designed and executed 35 test cases using an Android Studio emulator configured as a Pixel 5 running Android 12 (API 31).
- Tested notification behavior, application states, and connectivity-related error handling.
- Validated interface behavior and documented discrepancies against requirements.

**Backend API testing**
- Designed and executed 9 Postman test cases for courier creation and deletion.
- Validated HTTP status codes, response messages, required parameters, and negative scenarios.

**Deliverables:** Structured test cases, execution results, and Jira defect reports across web, mobile, and API testing.

**Technologies:** Jira, Postman, Chrome DevTools, Android Studio, Google Sheets

### 3. Additional QA & Technical Practice

Additional coursework and exercises provided experience with:

**Manual Web Application Testing**
- Requirements analysis and identification of testable conditions.
- Positive and negative test case design.
- Equivalence partitioning and boundary value analysis.
- UI and field validation.
- Defect documentation with reproducible steps and expected versus actual behavior.

**API Testing with Postman**
- Constructing HTTP requests using appropriate methods and request data.
- Testing successful and unsuccessful operations.
- Validating status codes, response bodies, and error handling.
- Identifying discrepancies between expected and actual API behavior.

**SQL & Database Queries**
- Retrieving and filtering records.
- Aggregating data.
- Handling NULL values.
- Writing queries to validate and interpret database information.

## Background

Mechanical Engineering graduate transitioning into software quality assurance. My engineering background provides a foundation in analytical problem-solving, interpreting specifications, and methodical verification.

Through the TripleTen QA Engineering program, I completed projects involving manual web and mobile testing, API validation, SQL, and Python/Selenium automation.

## Contact

- **LinkedIn:** [linkedin.com/in/mandeck](https://www.linkedin.com/in/mandeck/)
- **Email:** mikeandeck@gmail.com
