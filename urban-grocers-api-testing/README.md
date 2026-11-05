# Urban Grocers — API Testing Project

## Project Overview

This project was completed as part of the TripleTen QA Engineering program. It focused on testing the Urban Grocers application through its API endpoints using Postman.

The work involved analyzing API documentation, designing test cases, executing positive and negative tests, validating responses, and documenting defects.

## Testing Scope

### 1. Kit Product Endpoint

**Endpoint:** `POST /api/v1/kits/:id/products`

Tested the functionality for adding products to an existing kit.

Testing included:

- Valid and invalid kit and product identifiers.
- Positive and negative test scenarios.
- Missing, blank, and malformed input values.
- Invalid data types, including text, symbols, negative numbers, and decimal values.
- Non-Latin characters.
- Validation of the maximum limit of 30 distinct products in a kit.
- Verification of HTTP status codes and response messages.

### 2. Fast Delivery Endpoint

**Endpoint:** `/fast-delivery/v3.1.1/calculate-delivery.xml`

Tested the fast delivery calculation functionality using XML requests in Postman.

Testing included:

- Delivery availability.
- Delivery service name.
- Delivery cost.
- Estimated fulfillment time.
- Boundary testing involving product quantities, weights, and delivery-time intervals.

## Testing Approach

- Reviewed API documentation (apiDoc) to understand endpoint behavior, parameters, and expected responses.
- Designed test cases based on documented requirements.
- Executed API requests in Postman.
- Tested positive, negative, and boundary scenarios.
- Validated HTTP status codes, response messages, and returned data.
- Compared actual results against expected results.
- Documented defects in Jira.

## Tools & Technologies

- **Postman** — API request execution and response validation
- **apiDoc** — API documentation and requirements analysis
- **Jira** — Defect reporting and tracking
- **Microsoft Excel** — Test case design, execution records, and results
- **JSON and XML** — API request and response formats

## Project Deliverables

The project includes:

- API test cases and execution results.
- Postman request and response evidence.
- Jira defect documentation.
- Test execution report.

## Notes

This project was completed in a training environment as part of the TripleTen QA Engineering program. The documented test cases and results reflect the work performed during the project.