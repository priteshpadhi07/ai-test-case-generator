
def validate_test_cases(test_cases):

    required_fields = [
        "id",
        "scenario",
        "preconditions",
        "steps",
        "expected_result",
        "priority",
        "type"
    ]

    valid_priorities = ["High", "Medium", "Low"]
    valid_types = ["Positive", "Negative", "Boundary"]

    errors = []
    existing_ids = set()

    for index, test_case in enumerate(test_cases, start=1):

        for field in required_fields:
            if field not in test_case or not test_case[field]:
                errors.append(
                    f"Test case {index}: Missing or empty {field}"
                )

        test_id = test_case.get("id")

        if test_id:
            if test_id in existing_ids:
                errors.append(f"Duplicate test case ID: {test_id}")
            existing_ids.add(test_id)

        if not isinstance(test_case.get("steps"), list) or not test_case.get("steps"):
            errors.append(f"Test case {index}: Steps must be a non-empty list")

        if test_case.get("priority") not in valid_priorities:
            errors.append(f"Test case {index}: Invalid priority")

        if test_case.get("type") not in valid_types:
            errors.append(f"Test case {index}: Invalid test type")

    return errors
