# Urban Routes — Selenium Automation

## Demo Video

[Watch the Urban Routes Selenium Automation Demo](https://www.youtube.com/watch?v=pGnAUSi8O0I&vq=hd720)

The video demonstrates the Urban Routes application, the Selenium automation code, test execution, and the final results.

*For best viewing quality, select 720p in YouTube's playback settings if it is not selected automatically.*

## Project Overview

This project involved developing automated end-to-end tests for the Urban Routes web application using Python and Selenium WebDriver.

The test suite covers key steps in the ride-ordering workflow, including entering pickup and destination addresses, selecting a service, providing contact and payment information, and configuring additional ride options.

## Tools & Technologies

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)

## Testing Approach

- Structured automation code using the Page Object Model
- Created reusable methods for interacting with application elements
- Implemented element locators and explicit waits
- Used assertions to verify expected application behavior
- Separated test data from test logic

## Environment & Execution Requirements

This project was developed and tested against the Urban Routes application hosted in the TripleTen course environment.

The application is accessed through a temporary server URL, which must be entered in `Input_data_UrbanRoutes.py` before running the tests.

The hosted application is provided for educational purposes and is not guaranteed to remain available permanently. Consequently, the automation code can be reviewed independently, but executing the test suite requires access to a compatible, running Urban Routes environment.

## Running the Tests

To run the test suite, a compatible Urban Routes application environment must first be available.

1. Clone or download this repository.
2. Create and activate a Python virtual environment.
3. Install the project dependencies:

   ```bash
   pip install -r automation/requirements.txt
   ```

4. Open `automation/Input_data_UrbanRoutes.py` and enter the active Urban Routes server URL.
5. Run the test suite from the repository root:

   ```bash
   python -m pytest automation/Test_Suite_UrbanRoutes.py -v
   ```

**Note:** The test execution steps depend on the availability of the hosted application and its compatibility with the automation code.

## Implementation Notes

A brief fixed delay was used in the recorded demonstration to make application interactions easier to follow. The test automation also uses explicit waits to handle element availability and synchronization.

## Test Results

**8 automated tests passed.**

*This project was completed as part of the TripleTen QA Engineering program.*
