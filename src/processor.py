def merge_data(data1, data2):
    return {
        "summary": data1["summary"] or data2["summary"],
        "observations": list(set(data1["observations"] + data2["observations"])),
        "root_cause": data1["root_cause"] + " | " + data2["root_cause"],
        "severity": data1["severity"] + " | " + data2["severity"],
        "recommendations": data1["recommendations"] + " | " + data2["recommendations"],
        "notes": data1["notes"] + " | " + data2["notes"],
        "missing_info": data1["missing_info"] + " | " + data2["missing_info"]
    }

def handle_conflicts(data):
    if "|" in data["severity"]:
        data["notes"] += " | Conflict detected"
    return data
