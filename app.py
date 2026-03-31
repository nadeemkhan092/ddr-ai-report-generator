import streamlit as st
from main import run

st.title("AI DDR Report Generator")

inspection = st.file_uploader("Upload Inspection Report", type=["pdf"])
thermal = st.file_uploader("Upload Thermal Report", type=["pdf"])

if st.button("Generate DDR"):
    if inspection and thermal:
        with open("inspection.pdf", "wb") as f:
            f.write(inspection.read())

        with open("thermal.pdf", "wb") as f:
            f.write(thermal.read())

        report = run("inspection.pdf", "thermal.pdf")

        st.success("Report Generated")
        st.text_area("Output", report, height=500)
    else:
        st.warning("Upload both files")
