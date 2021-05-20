import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


st.set_page_config(layout="wide")

menu = ['PORTADA', 'PRESENTACIÓN', 'MOTIVACIÓN', 'CAMINO', 'TECNOLOGÍAS']
choice = st.selectbox('MENU', menu)

if choice == 'PORTADA':
    portada = Image.open('img/Portada.jpg')
    st.image(portada)

if choice == 'PRESENTACIÓN':
    presentacion = Image.open('img/Presentacion.jpg')
    st.image(presentacion)

if choice == 'MOTIVACIÓN':
    motivacion = Image.open('img/Motivacion.jpg')
    st.image(motivacion)

if choice == 'CAMINO':
    camino = Image.open('img/Camino.jpg')
    st.image(camino)

if choice == 'TECNOLOGÍAS':
    tecnologias = Image.open('img/Tecnologias.jpg')
    st.image(tecnologias)