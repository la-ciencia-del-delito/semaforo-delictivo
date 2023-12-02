import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path
from urllib.error import URLError

import matplotlib as plt
import ipywidgets as widgets
from statsmodels.tsa.stattools import kpss
from statsmodels.tsa.stattools import adfuller
import warnings 
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

import os


st.set_page_config(page_title="Semáforo Delictivo | Exploración de los datos",
                    page_icon="📊",
                    layout="wide")

st.markdown("# Exploración de los datos")
st.sidebar.header("Exploración de los datos")
st.write(
    """Gráfico"""
)

import pandas as pd
import plotly.express as px

# Supongamos que tienes un DataFrame llamado series_delitos_filtrables
# Debes cargar tus datos o modificar el ejemplo para que se ajuste a tus necesidades.

def graficar(delito):
    # ff.create_streamline
    vista = series_delitos_filtrables[series_delitos_filtrables['delito_semaforo'] == delito]
    # print(vista)
    st.write("Vista")
    st.write(vista.head())
    fig = px.bar(vista, x="entidad", y='incidentes')
    # fig.update_traces(visible='legendonly')
    st.plotly_chart(fig)

    # df = px.data.gapminder().query("country=='Canada'")
    # fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
    # # fig.show()
    # st.plotly_chart(fig)

# Cargar datos de ejemplo
# (Reemplaza esto con tu propia carga de datos)
series_delitos_filtrables = pd.DataFrame({
    'delito_semaforo': ['A', 'A', 'B', 'B', 'C', 'C'],
    'entidad': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'incidentes': [10, 15, 8, 12, 20, 25]
})

# Interfaz de usuario de Streamlit
st.title('Visualización de Delitos')

# Widget interactivo
delitos_unicos = series_delitos_filtrables['delito_semaforo'].unique()
delito_seleccionado = st.selectbox('Selecciona un delito:', delitos_unicos)

st.write(delito_seleccionado)
# Llamar a la función para graficar
graficar(delito_seleccionado)


def graficar_topn_delitos(anio: int=2022, n: int=1):
    vista1 = semaforo[semaforo['anio'] == anio]
    print(vista1.shape)
    vista1 = vista1.groupby(['entidad', 'delito_semaforo'])['total'].sum().reset_index()
    # Obtener top n delitos con más ocurrencia por entidad
    vista1 = vista1.groupby('entidad').apply(lambda x: x.nlargest(n, 'total')).reset_index(drop=True)
    vista1.sort_values(by='total', ascending=False, inplace=True)
    fig = px.bar(vista1, x='total', y='entidad', color='delito_semaforo', barmode='stack', width=1200, height=700)
    fig.update_layout(yaxis_categoryorder = 'total ascending')

    # Mostrar el gráfico
    # fig.show()
    st.plotly_chart(fig)

anios = semaforo["anio"].unique()
ns = [1,2,3,4]

anio_seleccionado = st.selectbox("Seleccionar año", anios)
top_n_seleccionado = st.selectbox("Seleccionar cantidad de delitos", ns)

graficar_topn_delitos(anio_seleccionado, top_n_seleccionado)