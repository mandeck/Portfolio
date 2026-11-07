# Urban Scooter: QA Testing Project

## Project Overview

This project was completed as the final project of the TripleTen QA Engineer program. It tests Urban Scooter, a practice scooter-rental application, across three areas: a web order form, a courier Android app, and the back-end API.

The work covered analyzing requirements, designing and executing test cases, recording expected and actual results, and reporting defects in Jira.

A written summary of the project, with screenshots and findings, is in [`Urban_Scooter_Project_Summary.pdf`](Urban_Scooter_Project_Summary.pdf).
## Results at a Glance

| Area | Test cases | Passed | Failed | Skipped | Bugs reported |
|---|---:|---:|---:|---:|---:|
| Web | 65 | 54 | 11 | 0 | 9 |
| Mobile | 35 | 15 | 17 | 3 | 12 |
| API | 9 | 8 | 1 | 0 | 1 |
| **Total** | **109** | **77** | **29** | **3** | **22** |

Several failed test cases can point to the same bug, so the number of bugs is lower than the number of failed cases.

## Testing Scope

### 1. Web Application Testing

- Designed positive and negative test cases for the Customer Details form (First name, Last name, Address, Phone and Subway station) from the written requirements, using equivalence partitioning and boundary value analysis.
- Executed all 65 cases in both Chrome and Opera at 1280×720. Results were identical in both browsers.
- Recorded expected and actual results for each case and reported each defect in Jira.

**Results (per browser):** 54 passed, 11 failed.

### 2. Mobile Application Testing

- Designed and executed test cases on a Pixel 5 emulator running Android 12 (API 31).
- Covered the two-hour order notification, the "No Internet connection" pop-up on each control, and the pop-up's text and design against Figma.
- Tested with the app active, minimized and with the screen off, switching the network off and on and changing the emulator's date and time to reach time-based behavior.
- Three notification cases were skipped because no notification appeared to check.

**Results:** 15 passed, 17 failed, 3 skipped.

### 3. API Testing

- Used Postman to test the add courier and delete courier endpoints.
- Compared status codes and response messages with the requirements and API documentation, including duplicate, missing-field, missing-ID and non-existent-ID cases.

**Results:** 8 passed, 1 failed.

## Notable Findings

- **Web:** the Last name field accepts more than 15 characters, and short or empty Address entries give no error.
- **Mobile:** the two-hour order notification does not appear, and "Order accepted" flashes when the app is offline.
- **API:** deleting a courier without an ID returns 404 instead of the documented 400.

## Tools & Technologies

- **Postman**: API testing
- **Chrome and Opera**: web application testing
- **Android Studio Emulator**: mobile application testing
- **Figma**: design reference for visual checks
- **Jira**: defect tracking
- **[Google Sheets](https://docs.google.com/spreadsheets/d/1wVyFged6BfLGgCZzT05uGpz-AAIJJPeVSsDufTOTyM0/edit?usp=sharing)** (with an Excel copy): test cases and results

## Project Deliverables

- `Urban_Scooter_QA_Portfolio.pdf`: summary of the project with results, defects and screenshots.
- [Google Sheets workbook](https://docs.google.com/spreadsheets/d/1wVyFged6BfLGgCZzT05uGpz-AAIJJPeVSsDufTOTyM0/edit?usp=sharing): test cases and results, with three worksheets: Web Testing, Mobile Testing and API Testing.
- `test-cases/`: the Excel copy of the same workbook.

## Notes

- This project was completed in a training environment, on a practice application, as part of the TripleTen QA Engineer program.
- Bug IDs in the form S9P-n are reference numbers from the project's Jira board. The reports may no longer be available there, so the workbook and the PDF are the record of the defects.
- Results reflect the outcomes recorded during the project. Failed tests are discrepancies between expected and actual behavior and are not counted as passes.
