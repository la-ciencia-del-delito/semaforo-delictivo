import os
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

import ast
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from matplotlib.gridspec import GridSpec
from matplotlib import patches


# Para Pirámide poblacional... crear escalas...
def crear_escala(max_pob):
    """
    Para crear ticks vals y labels para las escalas según tamaño de la población...
    """
    max_pob = (max_pob // 4) * 5
    step_exacto = max_pob // 4
    pow = len(str(step_exacto)) - 1
    
    step_round = (step_exacto // 10**pow) * 10 ** pow
    
    vals = list(set(list(np.arange(0,max_pob,step_round))) | set(list(np.arange(0,max_pob,step_round)*(-1))))
    vals.sort()
    
    if max(vals) // 1000 > 1000:
        labels = [str(abs(label // 1000000)) + "M" for label in vals]
    else:
        labels = [str(abs(label // 1000)) + "K" for label in vals]
    return vals, labels

def pob_dict_df(celda_diccionario):
    diccionario = ast.literal_eval(celda_diccionario)
    df = pd.DataFrame(diccionario)
    return df

def delitos_dict_df(celda_diccionario):
    diccionario = ast.literal_eval(celda_diccionario)
    # Ordenar las claves pare evitar bugs...
    claves_ordenadas = sorted(diccionario.keys())
    # Convertir el diccionario a DataFrame
    df = pd.DataFrame({"DELITOS": claves_ordenadas, 'INCIDENCIA': [diccionario[clave] for clave in claves_ordenadas]})
    return df

def crear_recuadro(ax, x, y, width, height, texto, texto_grande, color_borde, color_relleno):
    # Crear la caja con bordes redondeados
    caja = patches.FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.03", edgecolor=color_borde, facecolor=color_relleno)

    # Añadir la caja al eje
    ax.add_patch(caja)

    # Añadir texto grande
    ax.text(x + 0.5 * width, y + 0.65 * height, texto_grande, 
            color='black', 
            # palette=palette,
            ha='center', va='center', fontsize=14)

    # Añadir texto pequeño
    ax.text(x + 0.5 * width, y + 0.21 * height, texto, 
            color='black', 
            # palette=palette,
            ha='center', va='center', fontsize=10)

def crear_banner(valor_kpi, valor_percepcion, valor_tasa, valor_poblacion):
    # Crear una figura y ejes
    fig, ax = plt.subplots(figsize=(14, 1))

    # Ajustar el tamaño y la posición de los recuadros
    separacion = 0.008
    crear_recuadro(ax, 0.2, 0.2, 0.1, 0.6, 'KPI - IIC', valor_kpi, "#ee5733", "#F2D2A9")
    crear_recuadro(ax, 0.2 + 0.205 + separacion, 0.2, 0.1, 0.6, 'Encuesta (INEGI)', valor_percepcion, "#ee5733", "#F2D2A9")
    crear_recuadro(ax, 0.2 + 2 * (0.2 + separacion), 0.2, 0.1, 0.6, 'Tasa delictiva', valor_tasa, "#ee5733", "#F2D2A9")
    crear_recuadro(ax, 0.2 + 3 * (0.2 + separacion), 0.2, 0.1, 0.6, 'Población', f"{valor_poblacion:,}", "#ee5733", "#F2D2A9")

    # Eliminar los ejes
    ax.axis('off')
    st.pyplot(fig)


# Creando el DashBoard...
palette = [
    "#ee5733",
    "#fcd2ba",
    "#ef936d",
    "#a10024",
    "#570119",

    # "rgb(252, 210, 186)",
    # "rgb(239, 147, 109)",
    # "rgb(238, 87, 51)",
    # "rgb(161, 0, 36)",
    # "rgb(87, 1, 25)"
]
palette_sns = sns.color_palette(palette)
sns.set_palette(palette_sns)
def dashboard_vis(entidad, anho):
    set_entidad = df_tidy[df_tidy["ENTIDAD"] == entidad]
    set_entidad_anho = df_tidy[(df_tidy["ENTIDAD"] == entidad) & (df_tidy["AÑO"] == anho)]
    
    set_nacional = df_tidy.loc[df_tidy["CVE_GEO"] != 0, ["KPI_IIC", "PERCEPCION", "TASA_DELICTIVA"]]

    mediana_iic = np.median(set_nacional["KPI_IIC"])
    mediana_inegi = np.median(set_nacional["PERCEPCION"])
    mediana_tasa = np.median(set_nacional["TASA_DELICTIVA"])

    v_kpi = set_entidad_anho["KPI_IIC"].iloc[0]
    v_percepcion = set_entidad_anho["PERCEPCION"].iloc[0]
    v_tasa = set_entidad_anho["TASA_DELICTIVA"].iloc[0]
    v_poblacion = set_entidad_anho["POBLACION"].iloc[0]

    # Intentemos crear el Banner...
    crear_banner(v_kpi, v_percepcion, v_tasa, v_poblacion)

    #fig, axes = plt.subplots(nrows = 3, ncols = 3, figsize=(15, 12))

# Crear una figura y ejes usando GridSpec de Matplotlib
    fig = plt.figure(figsize=(15, 14))
    grid = GridSpec(3, 3, figure=fig, hspace=0.5)


    plt.subplots_adjust (hspace= 1)

    # Gráfico No. 1.
    ax1 = fig.add_subplot(grid[0, 0])
    sns.lineplot(data = set_entidad, x= "AÑO", y = "KPI_IIC", ax = ax1)
    ax1.set(title = "KPI - Índide de Inseguridad Ciudadana",
                   ylabel = "KPI - IIC",
                   xlabel = "Años",
                   xticks = anhos,
                   xlim=(2015,2023)
                   )
    ax1.axhline(y=mediana_iic, linestyle=":", color="red", label="Referencia")
    ax1.tick_params(axis='x', rotation=45)
      
    # Gráfico No. 2.
    ax2 = fig.add_subplot(grid[0, 1])
    sns.lineplot(data = set_entidad, x= "AÑO", y = "PERCEPCION", ax = ax2)
    ax2.set(title = "Percepción de inseguridad (INEGI)",
                   ylabel = "Percepción (INEGI)",
                   xlabel = "Años",
                   xticks = anhos,
                   xlim=(2015,2023)                   
                   )
    ax2.axhline(y=mediana_inegi, linestyle=":", color="red", label="Referencia")
    ax2.tick_params(axis='x', rotation=45)

    # Gráfico No. 3.
    ax3 = fig.add_subplot(grid[0, 2])
    sns.lineplot(data = set_entidad, x= "AÑO", y = "TASA_DELICTIVA", ax = ax3)
    ax3.set(title = "Tasa delictiva según semáforo actual",
                   ylabel = "Tasa delictiva",
                   xlabel = "Años",
                   xticks = anhos,
                   xlim=(2015,2023)
                   )
    ax3.axhline(y=mediana_tasa, linestyle=":", color="red", label="Referencia")
    ax3.tick_params(axis='x', rotation=45)

    # Gráfico No. 4.
    # Preparación de los datos para la Pirámide...
    celda_piramide = set_entidad_anho["PIRAMIDE"].reset_index(drop = True).iloc[0]
    df_pob = pob_dict_df(celda_piramide)

    df_pob["POBLACION"] = df_pob[["HOMBRES", "MUJERES"]].sum(axis = 1)
    df_pob = df_pob[["GRUPO", "HOMBRES", "MUJERES", "POBLACION"]]

    grupos_etarios = list(df_pob["GRUPO"].unique())
    grupos_reverse = grupos_etarios.copy()
    grupos_reverse.reverse()

    max_pob = df_pob[["HOMBRES", "MUJERES"]].max().max()

    # df_pob["MUJERES"] *= -1
    df_pob["HOMBRES"] *= -1

    ticks, labels = crear_escala(max_pob)
    # Datos para la Pirámide... Listos...
    
    # Graficando la Pirámide...
    #fig, ax = plt.subplots(figsize=(8, 7))
    ax4 = fig.add_subplot(grid[1, 0])
    bar_plot = sns.barplot(x='HOMBRES', y='GRUPO', data=df_pob, order=grupos_reverse, 
                           orient='h',ax = ax4,
                           label="Hombres",
                        #    palette='PuBu'
                        color="#a10024"
                           )
    bar_plot = sns.barplot(x='MUJERES', y='GRUPO', data=df_pob, order=grupos_reverse, 
                           orient='h', lw=0, ax = ax4,
                           label="Mujeres",
                        #    palette='OrRd'
                        color="#fcd2ba"
                           )
    bar_plot.set(title=f'Pirámide {entidad} - Año {anho}',
                xlabel="Población",
                ylabel="Grupos de edades",
                xticks=ticks,
                xticklabels=labels
                )
    ax4.legend()
    # Gráfico No. 5.
    # Preparando el df de delitos...
    celda_delitos = set_entidad_anho["DELITOS"].reset_index(drop = True).iloc[0]
    delitos = delitos_dict_df(celda_delitos)
    
    ax5 = fig.add_subplot(grid[1, 1:3])
    sns.barplot(data = delitos, x = "DELITOS", y = "INCIDENCIA", ax = ax5, palette=palette_sns)
    ax5.tick_params(axis='x', rotation=45)
    ax5.set(title = f"Distribución de delitos: {entidad} - Año {anho}",
                   ylabel = "",
                   xlabel = "",
                   )
    # Gráfico No. 6.
    ax6 = fig.add_subplot(grid[2, 0])
    ax6 = sns.scatterplot(data = set_entidad, x = "PERCEPCION", y = "KPI_IIC", ax = ax6)
    ax6 = sns.regplot(data = set_entidad, x = "PERCEPCION", y = "KPI_IIC", ax = ax6)
    ax6.set(title = "Regresión lineal del KPI-IIC y percepción",
            xlabel = "Percepción de inseguridad (INEGI)",
            ylabel = "KPI - IIC",
            )

    # Gráfico No. 7.
    ax7 = fig.add_subplot(grid[2, 1])
    ax7 = sns.scatterplot(data = set_entidad, x = "CUM_DIFF", y = "KPI_IIC", ax = ax7)
    ax7 = sns.regplot(data = set_entidad, x = "CUM_DIFF", y = "KPI_IIC", ax = ax7)
    ax7.set(title = "Regresión KPI-IIC y diferencia acumulada",
            xlabel = "Diferencia acumulada según grupos etarios",
            ylabel = "KPI - IIC",
            )
    ax7.tick_params(axis='x', rotation=45)

    # Gráfico No. 8.
    ax8 = fig.add_subplot(grid[2,2])
    ax8 = sns.scatterplot(data = set_entidad, x = "CUM_DIFF", y = "PERCEPCION", ax = ax8)
    ax8 = sns.regplot(data = set_entidad, x = "CUM_DIFF", y = "PERCEPCION", ax = ax8)
    ax8.set(title = "Regresión diferencia y percepción",
       xlabel = "Diferencia acumulada según grupos etarios",
       ylabel = "Percepción (INEGI)"
       )

    st.pyplot(fig)


st.set_page_config(
    page_title="Dashboard",
    page_icon="📈",
    layout="wide",
)

st.markdown("# Semáforo Delictivo")
st.write(
    """Comparación del actual semaforo delictivo con el KPI propuesto (Índice de inseguridad Ciudadana),
    contrastada con la encuesta de Percepción de inseguridad"""
)

# ===================================================================
# Cargar datos
# ===================================================================
ruta_actual = Path(os.getcwd())
ruta_data = ruta_actual / "../data"
ruta_tidy = ruta_data / "tidy"

df_tidy = pd.read_csv(ruta_tidy / "tidy_final_combinado.csv")

claves = df_tidy["CVE_GEO"].unique()
entidades = df_tidy["ENTIDAD"].unique()
anhos = df_tidy["AÑO"].unique()

columns = st.columns(3)

entidad_seleccionada = columns[0].selectbox("Entidad", entidades)
anio_seleccionado = columns[1].selectbox("Año", anhos)

dashboard_vis(entidad_seleccionada, anio_seleccionado)