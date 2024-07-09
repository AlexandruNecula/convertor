import streamlit as st

st.title("Convertor de presiune")

def pressure_converter(from_unit, to_unit, value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

col_tip, col_valor, col_blank = st.columns(3)
col_valoare, col_from_convert, col_to_convert, col_result = st.columns(4)
with col_valoare:
    value = st.number_input("Valoare:", min_value=0.0, format="%f")  
with col_from_convert:      
    from_unit = st.selectbox("From", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
with col_to_convert:    
    to_unit = st.selectbox("To", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
with col_result:
    st.write("Resultat:")
    st.write(pressure_converter(from_unit, to_unit, value)) 

with st.expander("SI"):
    st.table()