def generate_report(data, images):
    report = f"""
==============================
DETAILED DIAGNOSTIC REPORT
==============================

1. PROPERTY ISSUE SUMMARY
{data['summary']}

--------------------------------
2. AREA-WISE OBSERVATIONS
--------------------------------
"""

    for obs in data["observations"]:
        report += f"• {obs}\n"

    report += f"""
--------------------------------
3. PROBABLE ROOT CAUSE
--------------------------------
{data['root_cause']}

--------------------------------
4. SEVERITY ASSESSMENT
--------------------------------
{data['severity']}

--------------------------------
5. RECOMMENDED ACTIONS
--------------------------------
{data['recommendations']}

--------------------------------
6. ADDITIONAL NOTES
--------------------------------
{data['notes']}

--------------------------------
7. MISSING INFORMATION
--------------------------------
{data['missing_info']}
"""

    return report