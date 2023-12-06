import os
import json
from pathlib import Path

import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Semáforo Delictivo | Índice de Inseguridad Ciudadana",
    page_icon="🌍",
    layout="wide",
)

st.markdown("# Índice de Inseguridad Ciudadana")
st.write(
    """
### Índice de Inseguridad Ciudadana
"""
)

# ===================================================================
# Cargar datos
# ===================================================================
ruta_actual = Path(os.getcwd())
ruta_data = ruta_actual / "../data"
ruta_tidy = ruta_data / "tidy"

kpi = pd.read_csv(ruta_tidy / "tidy_final_combinado.csv")

# st.write(kpi.sample(3))


with open(ruta_data / "mexico_regions.json") as file:
    mexico_regions = json.load(file)


colors = {
        1: "rgb(252, 210, 186)",
        2: "rgb(238, 87, 51)",
        3: "rgb(237, 0, 53)",
        4: "rgb(161, 0, 36)",
    }

colors = {
        1: "Bajo",
        2: "Moderado",
        3: "Alto",
        4: "Muy alto",
    }

color_map= {
    "Bajo":"rgb(252, 210, 186)",
        "Moderado": "rgb(238, 87, 51)",
        "Alto": "rgb(237, 0, 53)",
        "Muy alto": "rgb(161, 0, 36)",
    }

kpi["rgb"] = kpi.apply(lambda x: colors[x["KPI_IIC_Color"]], axis=1)

palette = [
    "#fcd2ba",
    "#ef936d",
    "#ee5733",
    "#a10024",
    "#570119",
]
def graficar_mapa(anio):
    vista = kpi[kpi['AÑO'] == anio]
    fig = px.choropleth(
    data_frame=vista, 
    geojson=mexico_regions, 
    locations=vista['ENTIDAD'], # nombre de la columna del Dataframe
    featureidkey='properties.name',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
    color=vista['KPI_IIC_Color'], #El color depende de las cantidades
    color_continuous_scale=[
        (0.0, palette[0]), (0.25, palette[0]),
        (0.25, palette[1]), (0.50, palette[1]),
        (0.5, palette[2]), (0.75, palette[2]),
        (0.75, palette[3]), (1.00, palette[3]),
    ],
    color_continuous_midpoint=None,
    range_color=[1,4],
    width=1000, height=500
    )
    fig.update_layout(
        coloraxis_colorbar=dict(
            tickmode='array', 
            tickvals=[1, 2, 3, 4],
            title="Nivel de IIC",
        )
    )


    fig.update_layout(
        dragmode=False, # Hacemos que no se pueda arrastrar el mapa
        # scene_camera_eye=dict(x=0),
        # paper_bgcolor="black",
        margin=dict(l=0, r=0, t=0, b=0)
    )

    # Template para la carta del hover
    salto = "<br>"
    hovertemp = "<b>Estado: </b>"
    hovertemp += "%{location}" + salto
    hovertemp += "<b>IIC: </b>"
    hovertemp += kpi["KPI_IIC"].astype(str) + salto

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

columns = st.columns(2)

anios = kpi["AÑO"].unique()
# delitos = kpi["delito_semaforo"].unique()


anio_seleccionado = columns[0].slider("Seleccionar año", 2015, 2023, step=1)
# delito_seleccionado = columns[1].selectbox("Tipo de delito", delitos)

graficar_mapa(anio_seleccionado)