import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import os
import yaml


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


with open("dashboard/pages_config.yaml", "r",encoding="utf8") as f:
    config_paginas = yaml.safe_load(f)

nombre_pagina = "pagina_3"
titulo_compartido = config_paginas['titulo_compartido']
titulo_pagina = config_paginas[nombre_pagina]['titulo']
icono_pagina = config_paginas[nombre_pagina]['icono']

st.set_page_config(
    page_title=f"{titulo_compartido} | {titulo_pagina}",
    page_icon=f"{icono_pagina}",
    layout="wide",
)
st.markdown("# Indicadores Estado")

# ===================================================================
# Cargar datos
# ===================================================================
ruta_actual = Path(os.getcwd())
ruta_data = ruta_actual / "dashboard/data_dashboard"

df_tidy = pd.read_csv(ruta_data / "tidy_final_combinado.csv")
# Quitamos columnas que no son de interés para esta sección
df_tidy.drop(columns=["PIRAMIDE", "CVE_GEO",
                      "HOMBRES", "MUJERES",
                      "POBLACION", "CUM_DIFF",
                      "DELITOS"], inplace=True)

# Quitamos a toda la república para no afectar la escala
df_tidy = df_tidy[df_tidy["ENTIDAD"] != "República Mexicana"]


metricas = ['TOTAL_DELITOS', 'PERCEPCION', 'TASA_DELICTIVA', 'KPI_IIC']
nuevos_nombres = {col: " ".join(col.split("_")).title() for col in metricas}
metricas = list(nuevos_nombres.values())
df_tidy.rename(columns=nuevos_nombres, inplace=True)
# st.write(df_tidy)

columns = st.columns(2)
metrica_seleccionada = columns[0].selectbox("Seleccionar indicador", metricas)

graficar_boxplots_metrica(metrica_seleccionada)