
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.utils import get_column_letter


def export_to_excel(test_cases):

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "AI Test Cases"

    headers = [
        "Test Case ID",
        "Scenario",
        "Preconditions",
        "Steps",
        "Expected Result",
        "Priority",
        "Type",
        "Requirement ID",
        "Requirement"
    ]

    sheet.append(headers)

    # Add test cases
    for test_case in test_cases:
        sheet.append([
            test_case["id"],
            test_case["scenario"],
            test_case["preconditions"],
            "\n".join(test_case["steps"]),
            test_case["expected_result"],
            test_case["priority"],
            test_case["type"],
            test_case["requirement_id"],
            test_case["requirement"]
        ])

    # Header formatting
    header_fill = PatternFill(
        start_color="1F4E78",
        end_color="1F4E78",
        fill_type="solid"
    )

    for cell in sheet[1]:
        cell.font = Font(
            bold=True,
            color="FFFFFF",
            size=11
        )
        cell.fill = header_fill
        cell.alignment = Alignment(
            horizontal="center",
            vertical="center",
            wrap_text=True
        )

    # Cell formatting
    thin_border = Border(
        left=Side(style="thin", color="D9E1F2"),
        right=Side(style="thin", color="D9E1F2"),
        top=Side(style="thin", color="D9E1F2"),
        bottom=Side(style="thin", color="D9E1F2")
    )

    for row in sheet.iter_rows(min_row=2):
        for cell in row:
            cell.border = thin_border
            cell.alignment = Alignment(
                vertical="top",
                wrap_text=True
            )

    # Column widths
    column_widths = {
        "A": 15,
        "B": 40,
        "C": 30,
        "D": 45,
        "E": 45,
        "F": 15,
        "G": 15
    }

    for column, width in column_widths.items():
        sheet.column_dimensions[column].width = width

    # Row heights
    sheet.row_dimensions[1].height = 30

    for row in range(2, sheet.max_row + 1):
        sheet.row_dimensions[row].height = 65

    # Enable filters
    sheet.auto_filter.ref = sheet.dimensions

    # Freeze header
    sheet.freeze_panes = "A2"

    # Save Excel file
    try:
        workbook.save("AI_Generated_Test_Cases.xlsx")
        print("Excel file generated successfully!")

    except PermissionError:
        print("Error: Please close the Excel file and try again.")

    except Exception as e:
        print(f"Excel export failed: {e}")
