import streamlit as st
from unit_converters import LengthConverter, WeightConverter, TemperatureConverter

def main():
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
        unit_from = st.selectbox("Din:", list(WeightConverter.weight_units.keys()))
        unit_to = st.selectbox("În:", list(WeightConverter.weight_units.keys()))
        converter = WeightConverter()
    else: # Temperatură
        unit_from = st.selectbox("Din:", ["celsius", "fahrenheit", "kelvin"])
        unit_to = st.selectbox("În:", ["celsius", "fahrenheit", "kelvin"])
        converter = TemperatureConverter()


        
    if st.button("Converteste"):
        try:
            result = converter.convert(value, unit_from, unit_to)
            st.success(f"Rezultat: {result:.2f} {unit_to}")
        except ValueError as e:
            st.error(str(e))

if __name__ == "__main__":
    main()
