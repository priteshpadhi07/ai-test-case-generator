
def analyze_coverage(test_cases):

    categories = ["Positive", "Negative", "Boundary"]

    coverage = {}

    for category in categories:
        count = sum(
            1 for tc in test_cases
            if tc.get("type", "").strip().lower() == category.lower()
        )

        coverage[category] = count

    print("\n========== TEST COVERAGE REPORT ==========")

    for category, count in coverage.items():
        status = "Covered" if count > 0 else "Missing"

        print(f"{category} Test Cases: {count} - {status}")

    missing = [
        category for category, count in coverage.items()
        if count == 0
    ]

    if missing:
        print("\nCoverage gaps detected:", missing)
    else:
        print("\nAll test categories are covered!")

    total = len(test_cases)

    print(f"\nTotal Test Cases: {total}")

    return coverage
