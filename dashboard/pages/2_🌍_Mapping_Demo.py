import os
from pathlib import Path

import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


st.set_page_config(page_title="Semáforo Delictivo | Mapa",
                    page_icon="🌍")

st.markdown("# Mapa del semáforo delictivo")
st.sidebar.header("Mapas")
st.write(
    """
## Indicador del semáforo delictivo por estado
"""
)

# ===================================================================
# Cargar datos
# ===================================================================
ruta_actual = Path(os.getcwd())
ruta_data = ruta_actual / "../data"
ruta_tidy = ruta_data / "tidy"

ruta_semaforo = ruta_tidy / "delitos_semaforo.parquet"
ruta_poblacion = ruta_tidy / "poblacion.parquet"

gdf = gpd.read_file(ruta_data / 'conjunto_de_datos/areas_geoestadisticas_estatales.shp', 
                    columns = ["clave_entidad", 'nombre_entidad', 'geometry'])

poblacion = pd.read_parquet(ruta_poblacion)
semaforo = pd.read_parquet(ruta_poblacion)

st.write(semaforo.sample(5))
st.write(poblacion.sample(5))



poblacion_2 = poblacion.groupby(['AÑO','ENTIDAD'])['POBLACION'].sum().reset_index()
poblacion_2 = poblacion_2[(poblacion_2['AÑO'] <= 2023) & (poblacion_2['AÑO'] >= 2015)]
poblacion_2 = poblacion_2[~(poblacion_2['ENTIDAD'] == 'República Mexicana' )]
meses = semaforo.columns[10:22]

semaforo2 = semaforo.replace(to_replace = 'Veracruz de Ignacio de la Llave', value = 'Veracruz')\
    .groupby(['anio', 'entidad','delito_semaforo'])[meses].sum()\
    .sum(axis = 1)\
    .to_frame()\
    .reset_index()
    

semaforo2.rename(columns = {0:'incidentes'}, inplace = True)
gdf.replace({'Veracruz de Ignacio de la Llave':'Veracruz'}, inplace = True)
set(gdf['NOM_ENT']) == set(semaforo2['entidad'])
poblacion_2.ENTIDAD.replace({'Michoacán':'Michoacán de Ocampo','Coahuila':'Coahuila de Zaragoza'}, inplace = True)
set(semaforo2['entidad']) == set(poblacion_2.ENTIDAD)

geometrias = pd.merge(poblacion_2, gdf, left_on = 'ENTIDAD', right_on = 'NOM_ENT', how = 'outer')\
    .drop(columns = ['CVE_ENT', 'NOM_ENT'])

geometrias = geometrias.merge(semaforo2, left_on = 'ENTIDAD', right_on = 'entidad', how = 'left')\
    .drop(columns  = ['AÑO', 'ENTIDAD'])\
    .rename(columns = {'POBLACION':'poblacion'})\
    [['anio', 'entidad', 'geometry', 'poblacion', 'delito_semaforo', 'incidentes']] #ordenar de una vez
geometrias['incidentes_per_10000_hab'] = 100000 * geometrias['incidentes'] / geometrias['poblacion']

#lo pasamos a geopandas porque se perdio
geometrias = gpd.GeoDataFrame(geometrias)


# =======================================================================
# Graficar
# =======================================================================
def graficar_mapa(delito, año = 2022):
    fig, ax = plt.subplots(1,1, figsize = (10,10), dpi = 200)
    
    vista = geometrias[(geometrias['delito_semaforo'] == delito) & (geometrias['anio'] == año)]
    
    vista.plot(column = 'incidentes_per_10000_hab', 
               scheme = 'quantiles', 
               k = 3, 
               legend=True, 
               cmap='Reds', 
               ax = ax,
               edgecolor='black', 
               linewidth=0.3) 

    leg = ax.get_legend()
    leg.set_title("Incidentes cada 10,000 habitantes")
    ax.set_title(delito)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_facecolor('grey')
    

widgets.interact(graficar_mapa, delito = geometrias.delito_semaforo.unique(), año = range(2015, 2023));