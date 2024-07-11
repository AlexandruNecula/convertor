import streamlit as st
import plotly.graph_objects as go
from header import headerfunc

with st.expander("Unități de măsură"): 
    headerfunc()

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

st.write("")
st.write("Presiunea în fizică și tehnică este o mărime fizică scalară derivată, definită prin raportul dintre forță și unitatea de suprafață, forța fiind aplicată în direcție perpendiculară pe suprafața considerată. De regulă, este reprezentat prin simbolul p, mai rar, prin H sau h. Presiunea relativă este diferența de presiune față de presiunea atmosferică.")

with st.expander("SI"):
    fig = go.Figure(data=[go.Table(
        header=dict(values=['Unitate de convertit', 'Echivalent'],
                    align='left'),
        cells=dict(values=[["Pascali","Hectopascali","Kilopascali","Bari"], 
                        [1, 100, 1000, 100000]], 
                align='left'))
    ])

    #fig.update_layout(width=500, height=300)
    st.write(fig)
