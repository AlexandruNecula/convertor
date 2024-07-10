import streamlit as st

with st.expander("Unitati"):
    def headerfunc():
        st.page_link("pages/Presiune.py", label="Presiune")
        st.page_link("pages/Procentaj.py", label="Procentaj")        
        st.page_link("pages/Putere.py", label="Putere") 
    