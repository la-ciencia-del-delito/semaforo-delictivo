import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import os

st.set_page_config(page_title="Semáforo Delictivo | TOP delitos",
                    page_icon="📊",
                    layout="wide")

st.markdown("# Top delitos más cometidos por estado")

# ===================================================================
# Cargar datos
# ===================================================================
ruta_actual = Path(os.getcwd())
ruta_tidy = ruta_actual / "../data/tidy/"
ruta_parquet = ruta_tidy / "delitos_semaforo.parquet"

semaforo = pd.read_parquet(ruta_parquet)


# ===================================================================
# Graficar
# ===================================================================
def graficar_topn_delitos(anio: int=2022, n: int=1):
    palette = [
        "rgb(252, 210, 186)",
        "rgb(239, 147, 109)",
        "rgb(238, 87, 51)",
        "rgb(161, 0, 36)",
        "rgb(87, 1, 25)"

        # "rgb(246, 246, 246)",
        # "rgb(179, 19, 18)",
        # "rgb(234, 144, 108)",
        # "rgb(238, 226, 222)",
    ]
    vista1 = semaforo[semaforo['anio'] == anio]
    # print(vista1.shape)
    vista1 = vista1.groupby(['entidad', 'delito_semaforo'])['total'].sum().reset_index()
    # Obtener top n delitos con más ocurrencia por entidad
    vista1 = vista1.groupby('entidad').apply(lambda x: x.nlargest(n, 'total')).reset_index(drop=True)
    vista1.sort_values(by='total', ascending=False, inplace=True)
    fig = px.bar(
        vista1, 
        x='total', 
        y='entidad', 
        color='delito_semaforo', 
        barmode='stack', 
        color_continuous_scale=palette,
        color_discrete_sequence=palette,
        width=1000, height=500,
    )
    fig.update_layout(yaxis_categoryorder = 'total ascending')

    # Mostrar el gráfico
    # fig.show()
    st.plotly_chart(fig)

anios = semaforo["anio"].unique()
ns = [1,2,3,4]

columns = st.columns(3)
anio_seleccionado = columns[0].selectbox("Seleccionar año", anios)
top_n_seleccionado = columns[1].selectbox("Seleccionar cantidad de delitos", ns)

graficar_topn_delitos(anio_seleccionado, top_n_seleccionado)