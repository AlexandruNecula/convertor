import streamlit as st
from unit_converters import LengthConverter, WeightConverter, TemperatureConverter

hometab, abouttab = st.tabs(["Home", "Informatii"])


def main():
    with hometab:
        st.title("Convertor de Unități")

        col_tip, col_valor, col_blank = st.columns(3)
        with col_valor:
            pass
        with col_tip:
            conversion_type = st.selectbox("Selectați tipul de conversie:", ("Lungime", "Greutate", "Temperatură"))
        with col_blank:
            pass

        if conversion_type == "Lungime":
            col_valoare, col_from_convert, col_to_convert, col_result = st.columns(4)
            with col_valoare:
                value = st.number_input("Valoare:", min_value=0.0, format="%f")
            with col_from_convert:
                unit_from = st.selectbox("Din:", list(LengthConverter.length_units.keys()))
            with col_to_convert:
                unit_to = st.selectbox("În:", list(LengthConverter.length_units.keys()))
            converter = LengthConverter()
            with col_result:
                st.write("Resultat:")
                st.write(converter.convert(value, unit_from, unit_to))
        elif conversion_type == "Greutate":
            col_valoare, col_from_convert, col_to_convert, col_result = st.columns(4)
            with col_valoare:
                value = st.number_input("Valoare:", min_value=0.0, format="%f")        
            with col_from_convert:
                unit_from = st.selectbox("Din:", list(WeightConverter.weight_units.keys()))
            with col_to_convert:
                unit_to = st.selectbox("În:", list(WeightConverter.weight_units.keys()))
            converter = WeightConverter()
            with col_result:
                st.write("Resultat:")
                st.write(converter.convert(value, unit_from, unit_to))
        else: # Temperatură
            col_valoare, col_from_convert, col_to_convert, col_result = st.columns(4)
            with col_valoare:
                value = st.number_input("Valoare:", min_value=0.0, format="%f")
            with col_from_convert:
                unit_from = st.selectbox("Din:", ["celsius", "fahrenheit", "kelvin"])
            with col_to_convert:
                unit_to = st.selectbox("În:", ["celsius", "fahrenheit", "kelvin"])
            converter = TemperatureConverter()
            with col_result:
                st.write("Resultat:")
                st.write(converter.convert(value, unit_from, unit_to))


    with abouttab:        
        st.write("Pagină web pentru conversia a diferitor unități de măsură")

        st.page_link("pages/Presiune.py", label="Presiune")
        st.page_link("pages/Procentaj.py", label="Procentaj")        
        st.page_link("pages/Putere.py", label="Putere")        

if __name__ == "__main__":
    main()
