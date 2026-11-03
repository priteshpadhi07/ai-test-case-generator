# AI Test Case Generator

An AI-powered test case generation tool built using **Python, Ollama, and Llama 3.2**. It converts application requirements into structured test cases, validates their quality, analyzes test coverage, and exports the results to Excel.

## Project Overview

This project demonstrates how Large Language Models (LLMs) can be integrated into software test automation to reduce manual test case design effort.

The application uses a locally hosted LLM through Ollama, so it does not require paid API access.

## Key Features

- **AI-Based Test Case Generation:** Generates test cases from natural-language application requirements.
- **Local LLM Integration:** Uses Ollama with Llama 3.2.
- **JSON Validation:** Checks the generated response structure and mandatory fields.
- **Automatic Retry Mechanism:** Retries generation when validation or coverage checks fail.
- **Test Coverage Analysis:** Identifies Positive, Negative, and Boundary test coverage.
- **Semantic Quality Validation:** Detects vague scenarios, weak expected results, and duplicate scenarios.
- **Requirement Traceability:** Links generated test cases to their source requirement.
- **Excel Reporting:** Exports formatted test cases into an Excel workbook.

## Technology Stack

- Python
- Ollama
- Llama 3.2
- PyCharm
- Requests
- OpenPyXL
- JSON

## Project Architecture

```text
User Requirement
       |
       v
    main.py
       |
       v
 Ollama / Llama 3.2
       |
       v
  JSON Response
       |
       v
  JSON Validation
       |
       v
  Coverage Validation
       |
       v
  Automatic Retry (if required)
       |
       v
  Semantic Quality Validation
       |
       v
 Requirement Traceability
       |
       v
  Excel Export
       |
       v
AI_Generated_Test_Cases.xlsx
```

## Project Structure

```text
ai-test-case-generator/
│
├── main.py
├── llm_client.py
├── validator.py
├── coverage_analyzer.py
├── semantic_validator.py
├── traceability.py
├── excel_exporter.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Prerequisites

1. Python installed.
2. Ollama installed and running.
3. Llama 3.2 model downloaded.

Download Ollama: https://ollama.com/

Download the model:

```bash
ollama pull llama3.2
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai-test-case-generator
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Ensure Ollama is running and the model is available:

```bash
ollama run llama3.2
```

Run the application:

```bash
python main.py
```

## Sample Requirement

```text
As a customer, I want to add products to my shopping cart
and update their quantities. The cart should calculate
the total price based on product price and quantity.
```

## Sample Output

The application generates structured test cases containing:

- Test Case ID
- Scenario
- Preconditions
- Test Steps
- Expected Result
- Priority
- Test Type
- Requirement ID
- Requirement Description

The generated Excel report also includes test coverage and traceability information.

## Future Enhancements

- Multiple requirement support.
- Advanced semantic validation using an LLM evaluator.
- Integration with PyTest.
- Jira integration for test case management.
- Requirement-to-test-case coverage metrics.
- CI/CD pipeline integration.

## Author

Pritesh Padhi

Senior QA Automation Engineer | Python | Selenium | TestComplete | PyTest | AI-Based Test Automation