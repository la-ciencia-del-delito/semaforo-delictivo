import streamlit as st
import os
import pandas as pd
import plotly.express as px
from pathlib import Path
import yaml


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


with open("dashboard/pages_config.yaml", "r",encoding="utf8") as f:
    config_paginas = yaml.safe_load(f)

nombre_pagina = "pagina_4"
titulo_compartido = config_paginas['titulo_compartido']
titulo_pagina = config_paginas[nombre_pagina]['titulo']
icono_pagina = config_paginas[nombre_pagina]['icono']

st.set_page_config(
    page_title=f"{titulo_compartido} | {titulo_pagina}",
    page_icon=f"{icono_pagina}",
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
ruta_data = ruta_actual / "dashboard/data_dashboard"

series_delitos_filtrables = pd.read_csv(ruta_data / "serie_tiempo_tidy.csv")
series_delitos_filtrables.set_index("fecha", inplace=True)


columns = st.columns(3)
delitos = series_delitos_filtrables["delito_semaforo"].unique()
delito_seleccionado = columns[0].selectbox("Seleccione un delito", delitos)

graficar(delito_seleccionado)