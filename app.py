import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Create a histogram with Streamlit and Plotly') # título de la aplicación
st.subheader('Using a button to build the histogram') # subtítulo de la aplicación

car_data = pd.read_csv('https://raw.githubusercontent.com/EdwardDominguez/vehicles_TT_Project/refs/heads/main/vehicles_us.csv') # leer los datos
build_histogram = st.checkbox('Construir un histograma')
build_disp = st.checkbox('Construir Dispersion') # crear un botón
hist_button = st.button('Construir Graficos') # crear un botón

if hist_button: # al hacer clic en el botón
    if build_histogram: # si la casilla de verificación está seleccionada
        # escribir un mensaje
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches') # crear un histograma
        fig_histogram = px.histogram(car_data, x="odometer") # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig_histogram, use_container_width=True)
    if build_disp:
        # escribir un mensaje
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')# crear un histograma
        fig_scatter = px.scatter(car_data, x="odometer")# mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig_scatter, use_container_width=True)


