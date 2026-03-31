import os
from src.parser import extract_text, extract_images
from src.extractor import extract_structured_data
from src.processor import merge_data, handle_conflicts
from src.report import generate_report


def run(inspection_path, thermal_path):
    try:
        # ✅ Step 1: Ensure required folders exist
        os.makedirs("data/images", exist_ok=True)
        os.makedirs("data/output", exist_ok=True)

        # ✅ Step 2: Extract text
        inspection_text = extract_text(inspection_path)
        thermal_text = extract_text(thermal_path)

        # ✅ Step 3: Extract structured data
        data1 = extract_structured_data(inspection_text)
        data2 = extract_structured_data(thermal_text)

        # ✅ Step 4: Merge + handle conflicts
        merged_data = merge_data(data1, data2)
        final_data = handle_conflicts(merged_data)

        # ✅ Step 5: Extract images
        images = extract_images(inspection_path, "data/images")

        # ✅ Step 6: Generate report
        report = generate_report(final_data, images)

        # ✅ Step 7: Save report
        output_path = "data/output/ddr_report.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)

        return report

    except Exception as e:
        return f"Error occurred: {str(e)}"


# Optional: run directly (for testing without Streamlit)
if __name__ == "__main__":
    result = run("data/raw/inspection_report.pdf", "data/raw/thermal_report.pdf")
    print(result)