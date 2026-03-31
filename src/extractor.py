import re

def extract_structured_data(text):
    data = {
        "summary": "",
        "observations": [],
        "root_cause": "",
        "severity": "",
        "recommendations": "",
        "notes": "",
        "missing_info": ""
    }

    text = text.lower()

    # Observations extraction (simple rule-based)
    lines = text.split("\n")

    for line in lines:
        if "-" in line:
            data["observations"].append(line.strip("- ").capitalize())

    # Summary
    if "damp" in text or "leak" in text:
        data["summary"] = "Moisture and leakage issues observed in multiple areas"
    else:
        data["summary"] = "No major issues observed"

    # Root cause
    causes = []
    if "leak" in text:
        causes.append("Plumbing leakage")
    if "damp" in text:
        causes.append("Moisture intrusion")
    if "ventilation" in text or "exhaust" in text:
        causes.append("Poor ventilation")

    data["root_cause"] = ", ".join(causes) if causes else "Not Available"

    # Severity
    if "mold" in text or "leak" in text:
        data["severity"] = "Medium to High – due to moisture and leakage"
    else:
        data["severity"] = "Low"

    # Recommendations
    recs = []
    if "leak" in text:
        recs.append("Fix plumbing leakage")
    if "damp" in text:
        recs.append("Repair damp walls and repaint")
    if "exhaust" in text:
        recs.append("Repair or replace exhaust system")

    data["recommendations"] = ", ".join(recs) if recs else "Not Available"

    # Notes
    data["notes"] = "Generated using rule-based system"

    # Missing info
    data["missing_info"] = "Exact measurements not available"

    return data