import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

ruta = "data\mascotas_limpio.csv"
df = pd.read_csv(ruta)

#---Backround
st.image("https://github.com/alejandrorueda95252/micro-proyecto-2/blob/main/guaro.png?raw=true",use_container_width=True)

#---Titulo de la aplicacion 
st.title("🐶Analisis de datos de mascotas")

#--------- Bloque 1
seleccion_multiple1= st.sidebar.multiselect(
    "Selecciona el tipo de especie de mascotas:",
    df["especie"].unique()
)

##--- Filtrado de datos
if seleccion_multiple1:
    df_friltrado1 = df [df["especie"].isin(seleccion_multiple1)]
else:
    df_friltrado1 = df

if st.checkbox("Mostrar tabla de datos especies selecionadas"):
    st.write(df_friltrado1)

##----------- grafica de barras
if not df_friltrado1.empty:
    conteo= df_friltrado1["especie"].value_counts()
    fig, ax = plt.subplots()
    ax.bar(conteo.index, conteo.values, color = "#306D29")
    ax.set_xlabel("Especie")
    ax.set_ylabel("cantidad")
    ax.set_title("Cantidad de mascotas por especie")
    st.pyplot(fig)
else:
    st.warning("No hay datos para las especies selecionadas")

st.divider()
#------- bloque 2 
seleccion_unica1= st.sidebar.radio(
    "Selecciona el tipo de especie de mascota:",
    df["especie"].unique()
)
#----Bloque 3
seleccion_unica2 = st.sidebar.selectbox(
    "Selecciona el tipo de especie de mascota:",
    df["especie"].unique()
)
