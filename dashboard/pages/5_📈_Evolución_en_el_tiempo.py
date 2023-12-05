import streamlit as st
import os
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Plotting Demo", 
    page_icon="📈",
    layout="wide",
)

st.markdown("# Evolución de los delitos en el tiempo")
st.write(
"""
Evolución de los delitos desde el 2015 a la fecha
"""
)

# ===================================================================
# Cargar datos
# ===================================================================
ruta_actual = Path(os.getcwd())
ruta_tidy = ruta_actual / "../data/tidy/"

series_delitos_filtrables = pd.read_csv(ruta_tidy / "serie_tiempo_tidy.csv")
series_delitos_filtrables.set_index("fecha", inplace=True)

# ===================================================================
# Graficar
# ===================================================================
def graficar(delito):
    vista = series_delitos_filtrables[series_delitos_filtrables['delito_semaforo'] == delito]
    fig = px.line(
        vista, 
        x=vista.index, 
        y='incidentes', 
        color = 'entidad',
        width=1000, height=500
    )
    fig.update_traces(visible='legendonly')
    # fig.show()
    st.plotly_chart(fig)


columns = st.columns(3)
delitos = series_delitos_filtrables["delito_semaforo"].unique()
delito_seleccionado = columns[0].selectbox("Seleccione un delito", delitos)

graficar(delito_seleccionado)