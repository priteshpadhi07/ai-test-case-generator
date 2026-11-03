
import json
from llm_client import generate_response
from excel_exporter import export_to_excel
from validator import validate_test_cases
from coverage_analyzer import analyze_coverage
from traceability import add_traceability
from semantic_validator import validate_semantic_quality


# Step 1: Get requirement from user
requirement = input("\nEnter your application requirement: ")

if not requirement.strip():
    print("Requirement cannot be empty.")
    exit()


# Step 2: Build AI prompt
prompt = f"""
You are an experienced Software QA Engineer.

Analyze the following requirement and generate
at least 5 detailed test cases.

Requirement:
{requirement}

Return valid JSON only in this exact structure:

{{
    "test_cases": [
        {{
            "id": "TC_001",
            "scenario": "Test scenario",
            "preconditions": "Required preconditions",
            "steps": ["Step 1", "Step 2"],
            "expected_result": "Expected result",
            "priority": "High",
            "type": "Positive"
        }}
    ]
}}

IMPORTANT TEST CASE GENERATION RULES:

1. Generate at least 2 Positive test cases.
2. Generate at least 2 Negative test cases.
3. Generate at least 2 Boundary test cases.

4. Boundary test cases should cover relevant edge conditions,
   such as minimum quantity, maximum quantity, and values
   just beyond allowed limits.

5. Do not invent business rules or limits that are not
   specified in the requirement. Clearly identify assumptions.

6. Avoid vague words such as:
   correctly, properly, works, something, and anything.

7. Expected results must describe measurable outcomes.

8. Use only these test types:
   Positive, Negative, Boundary.

9. Use priorities:
   High, Medium, Low.

Return valid JSON only.
"""


# Step 3: Generate and validate with automatic retry
MAX_RETRIES = 3
data = None

for attempt in range(1, MAX_RETRIES + 1):

    try:
        print(f"\nAI generation attempt: {attempt}")

        result = generate_response(prompt)

        # Parse AI response
        data = json.loads(result)

        # Validate JSON structure
        if not isinstance(data, dict):
            raise ValueError("AI response must be a JSON object")

        if not isinstance(data.get("test_cases"), list):
            raise ValueError("Invalid test_cases structure")

        if not data["test_cases"]:
            raise ValueError("No test cases generated")

        # Validate individual test cases
        errors = validate_test_cases(data["test_cases"])

        # Check test type coverage
        test_types = {
            str(tc.get("type", "")).strip().capitalize()
            for tc in data["test_cases"]
            if isinstance(tc, dict)
        }

        required_types = {"Positive", "Negative", "Boundary"}
        missing_types = required_types - test_types

        if missing_types:
            errors.append(
                f"Missing test case categories: {list(missing_types)}"
            )

        if not errors:
            print("\nAll test cases passed validation and coverage checks!")
            break

        print("\nValidation errors:")

        for error in errors:
            print("-", error)

        # Ask AI to correct validation errors
        prompt += f"""

Your previous response had these validation errors:
{errors}

Correct all errors and return the complete JSON.
Return JSON only.
"""

        data = None

    except (json.JSONDecodeError, ValueError) as error:
        print("\nInvalid AI response:", error)
        data = None

        prompt += """

Your previous response was invalid.
Generate valid JSON following the exact requested structure.
Return JSON only.
"""

    except Exception as error:
        print("\nUnexpected error:", error)
        data = None
        break


if data is not None:

    analyze_coverage(data["test_cases"])

    add_traceability(data["test_cases"], requirement)

    # Semantic Quality Validation
    semantic_issues = validate_semantic_quality(data["test_cases"])

    if semantic_issues:
        print("\nSemantic Quality Issues Found:")
        for issue in semantic_issues:
            print("-", issue)
    else:
        print("\nAll test cases passed semantic quality checks!")

    # Export to Excel
    export_to_excel(data["test_cases"])

else:
    print("\nERROR: Unable to generate valid test cases.")
    print("Maximum generation attempts reached.")
    print("Excel report was not generated.")
    exit(1)