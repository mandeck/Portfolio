# Urban Grocers: API Testing with Postman

## Project Overview

This project was completed as part of the TripleTen QA Engineer program. It tests two endpoints of Urban Grocers, a practice grocery-ordering application: adding products to a kit, and the Fast Delivery cost calculation.

The work covered analyzing the requirements, designing test cases, running them in Postman with JSON and XML request bodies, comparing each response with the requirements and the API documentation (apiDoc), and reporting bugs in Jira.

A written summary of the project, with results, the full bug list and screenshots, is in [`Urban_Grocers_API_Testing.pdf`](Urban_Grocers_API_Testing.pdf).

## Results at a Glance

| Area | Test cases | Passed | Failed | Bugs reported |
|---|---:|---:|---:|---:|
| Add products to a kit | 29 | 15 | 14 | 12 |
| Delivery cost and availability | 42 | 20 | 22 | 14 |
| **Total** | **71** | **35** | **36** | **26** |

Several failed test cases can point to the same bug, so the number of bugs is lower than the number of failed cases.

## Testing Scope

### 1. Add Products to a Kit

`POST /api/v1/kits/:id/products` (JSON)

- Tested the 30-distinct-product limit with 29, 30 and 31 products.
- Tested kit IDs and product IDs at and beyond their valid range, plus negative, blank, decimal and text values.
- Tested negative, decimal and text quantities, missing fields and an empty request body.
- Compared status codes (200, 400, 404) with the requirements.

**Results:** 15 passed, 14 failed, 12 bugs.

### 2. Delivery Cost and Availability

`POST /fast-delivery/v3.1.1/calculate-delivery.xml` (XML)

- Tested delivery hours inside and outside the 07:00 to 21:00 window, including the boundaries, and invalid values (decimal, blank, negative, text, 24 or more).
- Tested item counts and weights across each price tier, at the boundaries and beyond the maximums.
- Checked the host cost and client cost returned for each combination.

**Results:** 20 passed, 22 failed, 14 bugs.

## Testing Approach

- Reviewed the requirements and API documentation (apiDoc) to understand each endpoint's expected behavior.
- Designed positive, negative and boundary test cases in a spreadsheet, with expected status codes and responses.
- Ran each case in Postman and compared the actual result with the expected result.
- Reported each bug in Jira and linked it to its test case in the workbook.

## Notable Findings

- Eight requests with decimal or text IDs and quantities, or a missing product ID or quantity, return 500 Internal Server Error instead of a 400 or 404.
- Negative and nonexistent product IDs are accepted, and a negative quantity subtracts from the kit, instead of the request being rejected.
- Orders above the maximum item count or weight return host cost 6 and client cost 6 instead of the documented 7 and 9.
- Blank, text, decimal and out-of-range values for delivery time, item count and weight are accepted with 200 OK.

## Severity

Each bug is rated in the PDF on a Low / Medium / High scale: 2 High, 3 Medium–High, 12 Medium and 9 Low–Medium.

## Tools & Technologies

- **Postman**: sending requests and checking responses
- **apiDoc**: API documentation and requirements analysis
- **Jira**: bug reporting and tracking
- **Google Sheets** (with an Excel copy): test cases, execution records and results
- **JSON and XML**: request and response formats

## Project Deliverables

- [`Urban_Grocers_API_Testing.pdf`](Urban_Grocers_API_Testing.pdf): summary of the project with results, bugs and screenshots.
- [Test case workbook (Google Sheets)](https://docs.google.com/spreadsheets/d/1nli_9__ca63m2QNUNBTMO1zkod3_ACSSJDeliMh9iR0/edit?usp=sharing): the test cases and results, with two worksheets (add-products tests and delivery tests).
- `test-cases/`: the Excel copy of the workbook.

## Notes

- This project was completed in a training environment, on a practice application, as part of the TripleTen QA Engineer program.
- Bug IDs in the form S4P-n are reference numbers from the project's Jira board. The reports may no longer be available there, so the workbook and the PDF are the record of the bugs.
- Cases are labeled K1–K29 (add products) and D1–D42 (delivery) in the PDF. The workbook's own numbering on the first sheet skips two numbers because of blank rows.
- Failed tests are discrepancies between expected and actual behavior and are not counted as passes.