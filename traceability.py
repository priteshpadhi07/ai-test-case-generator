
def add_traceability(test_cases, requirement):

    requirement_id = "REQ_001"

    for test_case in test_cases:
        test_case["requirement_id"] = requirement_id
        test_case["requirement"] = requirement

    print("\nRequirement Traceability Added!")

    print("Requirement ID:", requirement_id)
    print("Linked Test Cases:", len(test_cases))

    return test_cases
