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
ruta_data = ruta_actual / "../data"
ruta_tidy = ruta_data / "tidy"

df_tidy = pd.read_csv(ruta_tidy / "tidy_final_combinado.csv")
# Quitamos columnas que no son de interés para esta sección
df_tidy.drop(columns=["PIRAMIDE", "CVE_GEO",
                      "HOMBRES", "MUJERES",
                      "POBLACION", "CUM_DIFF",
                      "DELITOS"], inplace=True)

# Quitamos a toda la república para no afectar la escala
df_tidy = df_tidy[df_tidy["ENTIDAD"] != "República Mexicana"]
# st.write(df_tidy.head(3))
# ===================================================================
# Graficar
# ===================================================================
def graficar_boxplots_metrica(metrica):
    fig = px.box(df_tidy, x='ENTIDAD', y=metrica,
             labels={'KPI_IIC': 'Valor KPI_IIC'},
             title=f'Gráfico de cajas para {metrica} desde el 2015',
             color_discrete_sequence=["#ee5733"],
             width=1000, height=700,
             )

    st.plotly_chart(fig)

metricas = ['TOTAL_DELITOS', 'PERCEPCION', 'TASA_DELICTIVA', 'KPI_IIC']
nuevos_nombres = {col: " ".join(col.split("_")).title() for col in metricas}
metricas = list(nuevos_nombres.values())
df_tidy.rename(columns=nuevos_nombres, inplace=True)
# st.write(df_tidy)

columns = st.columns(3)
metrica_seleccionada = columns[1].selectbox("Seleccionar métrica", metricas)

graficar_boxplots_metrica(metrica_seleccionada)