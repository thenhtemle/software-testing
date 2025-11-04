# Software Testing - Project Case Study

This repository contains all testing artifacts and deliverables for the **CS423-CSC13003 - Software Testing** course project at the University of Sciences (HCMUS). The objective was to apply a comprehensive suite of professional software testing techniques to a real-world web application.

## 📦 Software Under Test (SUT)

* **Application:** The Toolshop
* **Version:** Sprint 5 with bugs

---

## 🚀 Local Test Environment (Docker Setup)

To ensure a consistent testing environment, the "The Toolshop" (Sprint 5) application was run locally using Docker.

The setup involved using the `docker-compose.yml` file provided with the application's source code.

1.  The necessary application source code (target folder: `/sprint5-with-bugs`) was obtained.
2.  From within that directory, the application was built and run in detached mode using Docker Compose:
    ```bash
    docker-compose up -d
    ```
3.  This process launched both the frontend and backend services, making the application accessible for testing at `http://localhost:3000`.

---

## 📁 Repository Structure

This repository is organized by testing type, with each folder containing the relevant test cases, scripts, analysis, and documentation.

* `README.md`: This file.
* **/API Testing**: Contains Postman collections, test cases, and reports for API endpoint testing.
* **/Automation Testing**: Houses automated test scripts (e.g., Selenium, Cypress, etc.) for regression and functional testing.
* **/Domain Testing**: Includes analysis, test data, and test cases designed using the domain/partition testing technique.
* **/GUI Usability Testing**: Focuses on test cases for the Graphical User Interface (GUI) and overall user experience.
* **/Performance Testing**: Contains scripts (e.g., JMeter) and reports for load, stress, and scalability testing.
* **/Scenario Testing & Data Generation**: Details user-centric, scenario-based test cases and strategies for test data generation.

---

## 📝 Key Project Deliverables

This project involved the creation of a complete set of professional testing documentation, culminating in a final report.

* **Test Plan:** Outlined the scope, objectives, resources, and testing strategy.
* **Detailed Test Cases:** Included step-by-step instructions, expected results, and actual outcomes for each testing type.
* **Test Case Summary:** A high-level summary highlighting test execution status (Pass/Fail) and coverage.
* **Bug Reports:** Formal documentation of all identified defects, including severity, priority, and steps to reproduce.
* **Final Test Report:** A comprehensive summary of the entire testing process, key findings, and recommendations for improvement.
