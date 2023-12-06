import os
import json
from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px
import yaml


def graficar_mapa(anio, delito):
    vista = delitos_por_100k_hab[(delitos_por_100k_hab['delito_semaforo'] == delito)\
                        & (delitos_por_100k_hab['anio'] == anio)]
    fig = px.choropleth(
    data_frame=vista, 
    geojson=mexico_regions, 
    locations=vista['entidad'], # nombre de la columna del Dataframe
    featureidkey='properties.name',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
    color=vista['incidentes_per_10000_hab'], #El color depende de las cantidades
    color_continuous_scale="reds",
    range_color=(vista["incidentes_per_10000_hab"].min(),
                    vista["incidentes_per_10000_hab"].max()),
    width=1000, height=500
    )

    fig.update_layout(
        dragmode=False, # Hacemos que no se pueda arrastrar el mapa
        # scene_camera_eye=dict(x=0),
        # paper_bgcolor="black",
        margin=dict(l=0, r=0, t=0, b=0)
    )
    fig.update_layout(
        coloraxis_colorbar=dict(
            tickmode='array', 
            title="Incidentes por cada 10k hab.",
        )
    )

    # Template para la carta del hover
    salto = "<br>"
    hovertemp = "<b>Estado: </b>"
    hovertemp += "%{location}" + salto
    hovertemp += "<b>Incidentes por cada 10k hab: </b>"
    hovertemp += vista["incidentes_per_10000_hab"].round(2).astype(str) + salto

    fig.update_traces(
        hovertemplate=hovertemp,
    )

    fig.update_geos(
        showcountries=False, # No mostrar los otros paises
        showcoastlines=False, # Lineas de paises
        showland=False, # Si lo activamos muestra los otros paises muy tenues
        fitbounds="locations",
        visible=False,   # El marco exterior del mapa
        # zoom_level=5,
    )

    # fig.show()
    st.plotly_chart(fig)



with open("pages_config.yaml", "r",encoding="utf8") as f:
    config_paginas = yaml.safe_load(f)

nombre_pagina = "pagina_2"
titulo_compartido = config_paginas['titulo_compartido']
titulo_pagina = config_paginas[nombre_pagina]['titulo']
icono_pagina = config_paginas[nombre_pagina]['icono']

st.set_page_config(
    page_title=f"{titulo_compartido} | {titulo_pagina}",
    page_icon=f"{icono_pagina}",
    layout="wide",
)

st.markdown("# Tasa de delitos por Estado")
st.write(
    """
### Delitos cometidos por cada 10,000 habitantes
"""
)

# ===================================================================
# Cargar datos
# ===================================================================
ruta_actual = Path(os.getcwd())
ruta_data = ruta_actual / "data_dashboard"

delitos_por_100k_hab = pd.read_csv(ruta_data / "delito_por_100k_hab.csv")

with open(ruta_data / "mexico_regions.json") as file:
    mexico_regions = json.load(file)

columns = st.columns(2)

anios = delitos_por_100k_hab["anio"].unique()
delitos = delitos_por_100k_hab["delito_semaforo"].unique()


anio_seleccionado = columns[0].slider("Seleccionar año", 2015, 2023, step=1)
delito_seleccionado = columns[1].selectbox("Tipo de delito", delitos)

graficar_mapa(anio_seleccionado, delito_seleccionado)