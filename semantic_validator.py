import re


VAGUE_WORDS = [
    "something",
    "anything",
    "properly",
    "correctly",
    "works",
    "it should work",
    "test the feature",
    "check the functionality"
]


def validate_semantic_quality(test_cases):
    issues = []
    seen_scenarios = set()

    for index, test_case in enumerate(test_cases, start=1):

        # 1. Check scenario quality
        scenario = str(test_case.get("scenario", "")).strip().lower()

        if len(scenario.split()) < 3:
            issues.append(
                f"Test Case {index}: Scenario is too vague."
            )

        # 2. Check for vague words in scenario
        for word in VAGUE_WORDS:
            if word in scenario:
                issues.append(
                    f"Test Case {index}: Scenario contains vague wording: '{word}'."
                )
                break

        # 3. Check duplicate scenarios
        if scenario in seen_scenarios:
            issues.append(
                f"Test Case {index}: Duplicate scenario found."
            )
        else:
            seen_scenarios.add(scenario)

        # 4. Check steps
        steps = test_case.get("steps", [])

        if not steps or any(
            len(str(step).strip()) < 5 for step in steps
        ):
            issues.append(
                f"Test Case {index}: Steps are empty or too short."
            )

        # 5. Check expected result
        expected_result = str(
            test_case.get("expected_result", "")
        ).strip().lower()

        if len(expected_result.split()) < 4:
            issues.append(
                f"Test Case {index}: Expected result is too vague."
            )

        for word in VAGUE_WORDS:
            if word in expected_result:
                issues.append(
                    f"Test Case {index}: Expected result contains vague wording: '{word}'."
                )
                break

    return issues


if __name__ == "__main__":

    sample_test_cases = [
        {
            "scenario": "Test cart",
            "steps": ["Click something"],
            "expected_result": "It should work"
        },
        {
            "scenario": "Verify cart quantity update",
            "steps": [
                "Open the shopping application",
                "Add a product to the cart",
                "Increase the product quantity"
            ],
            "expected_result": "Cart total updates based on the new quantity"
        }
    ]

    results = validate_semantic_quality(sample_test_cases)

    if results:
        print("\nQuality issues found:")
        for issue in results:
            print("-", issue)
    else:
        print("All test cases passed semantic quality checks!")