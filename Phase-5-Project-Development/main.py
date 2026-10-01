import streamlit as st

st.set_page_config(page_title="LegalEase")

st.title("⚖️ LegalEase")
st.write("AI-Powered Legal Document Generator")

document_type = st.selectbox(
    "Document Type",
    ["Rental Agreement", "Employment Agreement", "NDA", "Legal Notice"]
)

parties = st.text_input("Parties")
effective_date = st.date_input("Effective Date")
terms = st.text_area("Terms / Conditions")

if st.button("Generate Legal Document"):
    st.success("Legal document generated successfully!")

    st.subheader("Generated Legal Document")

    st.write(f"""
    **LEGAL DOCUMENT**

    **Document Type:** {document_type}

    **Parties:** {parties}

    **Effective Date:** {effective_date}

    **Terms:**
    {terms}

    ---
    *Generated using LegalEase*
    """)
