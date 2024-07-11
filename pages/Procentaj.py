import streamlit as st
import plotly.graph_objects as go
from header import headerfunc

with st.expander("Unități de măsură"): 
    headerfunc()

def procent_converter(procent_number, from_number):
    return procent_number / 100 * from_number

def procent_finder(procent_from, from_other_number):
    return procent_from / from_other_number * 100


st.title("Convertor de procente")

col_valoare, col_from_convert, col_to_convert, col_result = st.columns(4)
with col_valoare:
    procent_number = st.number_input("%:", min_value=0.0, format="%f")  
with col_from_convert:      
    from_number = st.number_input("Din", min_value=0.0)
with col_to_convert:    
    st.write("Este:")
    st.write(procent_converter(procent_number, from_number))
with col_result:
    st.write(" ")

st.write(" ")

col_valoare2, col_from_convert2, col_to_convert2, col_result2 = st.columns(4)
with col_valoare2:
    procent_from = st.number_input("Nr:", min_value=0.0, format="%f")  
with col_from_convert2:      
    from_other_number = st.number_input("Din numarul", min_value=0.1)
with col_to_convert2:    
    st.write("Este in %:")
    st.write(round(procent_finder(procent_from, from_other_number),2))
with col_result2:
    st.write(" ")

st.write("")
st.write("A suta parte dintr-o cantitate dată. Des folosit în calcule matematice.")

