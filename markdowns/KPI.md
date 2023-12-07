# Definicion de KPIs.

# Indice de inseguridad ciudadana

## Definicion

Se consideran los siguientes delitos, en el siguiente orden: feminicidio, homicidios, secuestros, robo a casa, robo a negocio, robo a vehiculo, violacion, narcomenudeo, extorsión, violencia familiar y lesiones.

La fórmula para el Índice de Incidencia Delictiva (IIC) es la siguiente:

$IIC(\text{entidad}, \text{periodo}) = 0.6 \cdot TI_1  + 0.24 \cdot TI_2 + 0.1 \cdot TI_3  +  0.13\cdot TI_4  + 0.13\cdot TI_5$
$+ 0.13\cdot TI_6  + 0.13\cdot TI_7 + 0.08\cdot TI_8  + 0.08\cdot TI_9 + 0.04\cdot TI_{10}  + 0.02\cdot TI_{11}.$

donde  $TI_i = \frac{\text{numero de indicidencias del delito i}}{\text{poblacion entidad}}\cdot 100000$, es decir, la tasa de incidencia correspondiente al delito $i$ por cada 100,000 habitantes durante el mes evaluado.

El coeficiente que acompañan a cada $TI_i$ son los pesos asignados en función de la gravedad de cada delito, los cuales se detallan a fondo en el documento principal del proyecto.

## Umbrales de Desempeño

Para determinar la clasificación de una entidad como positiva, neutral, negativa o crítica, se considera el historial del país, en especial desde el año 2015 hasta el 2022. El IIC se calculó durante esos años y, a partir de los resultados obtenidos, se establecen los límites de referencia.

$\text{bueno o postivo}<q_2$

$q_2<= \text{normal o neutral}< q_3$

$q_3<= \text{mal o negativo}< q3 + 1.5\text{IQR}$

$q3 + 1.5\text{IQR}<= \text{critico}$

donde  $q_2$, $q_3$ y $IQR$ corresponen a al segundo cuartil, tercer cuartil y rango intercuartil del ICC calculado en cada uno de los meses y entidades de los años mencionados.

Los límites variarán anualmente debido a la naturaleza de su cálculo,sin embargo, están protegidos contra valores extremos al estar fundamentados en percentiles.

## Audiencia

La audiencia principal abarca a la Subsecretaría de Gobierno Digital del Estado de Sonora, la Procuraduría General de Justicia del Distrito Federal y la Dirección de Estadística Criminal, así como al público en general. 

## Pregunta clave de desempeño

Dada la definición de este KPI, nos permite responder la pregunta sobre el estado actual de la entidad/país en relación con los tipos de delitos considerados. Un valor alto indica la presencia de una cantidad significativa de delitos, sugiere la posibilidad de diferentes escenarios: ya sea una concentración de delitos no tan graves pero numerosos, una presencia más limitada pero impactante de delitos graves, o una combinación de ambos casos. Sirve como un indicador numérico que, aunque no proporciona detalles específicos sobre la composición, sugiere posibles patrones en la incidencia delictiva.

## Como debe usarse

Este indicador está diseñado para facilitar una comparación rápida entre los estados del país, ofreciendo ademas una visión clara de si una entidad está experimentando mejoras o agravamientos en la incidencia de delitos considerados a lo largo del tiempo. Se recomienda su aplicación específica en el análisis de estados que se sitúen en extremos tanto positivos como negativos, con el propósito de identificar medidas efectivas para reducir la incidencia de los delitos que más impactan en el indicador.

## Datos

La información se actualiza mensualmente, lo que se traduce en una actualización mensual del índice de inseguridad ciudadana de igual manera.

# Tasas en general

Se implementó un KPI básico pero esencial para el análisis: las tasas de incidencia por delito, expresadas por cada 10,000 habitantes. En otras palabras, utilizamos 11 indicadores (uno por delito), considerando las incidencias en ventanas de tiempo correspondientes a los años.

## Definicion

Seleccionado un delito $i$, la tasa de delitos $T_i$ se define como

$T_i(\text{estado}, \text{ año}) = \frac{\text{numero de delitos en el año del i-esimo delito}}{\text{poblacion de la entidad}} \cdot 10000.$



## Umbrales de Desempeño

Los umbrales para las tasas son en base al conjunto de estados, para la evaluacion del año actual se calculan los cuartiles $q_2$ y $q_3$ de la misma tasa del año inmediato anterior y luego se separa de la siguiente manera:

$\text{bueno} < q_2$

$q_2=<\text{normal }< q_3$

$q_3=<\text{malo }$

## Audiencia

La audiencia principal abarca a la Subsecretaría de Gobierno Digital del Estado de Sonora, la Procuraduría General de Justicia del Distrito Federal y la Dirección de Estadística Criminal, así como al público en general. 

## Pregunta clave de desempeño

Si solo se tiene el numero de delitos totales por entidad, es muy facil perderse en el hecho que las entidades tienen poblaciones muy variadas y por lo mismo creer que una entidad se encuentra en un peor estado al superar a otra en un delito $x$.  Para esta situacion se seleccionó estas tasa, ya que escalan los datos una manera natural e interpretable para ahora sí poder compararse las entidades sin preocuparse por la poblacion.

## Como debe usarse

Estas tasas tiene una aplicacion muy directa dada la simplicidad de su definicion, estas indican que tan mal se encuentra la entidad con respecto al resto de las entidades. Ademas, al calificarse como malo cuando la entidad se encuentra por encima del tercer cuartil del año anterior se tiene que estos estadas estan en una situacion bastante mas criticas que los demas. 
La aplicacion directa es que si una entidad se encuentra en estado malo, se debe atacar todas las fuentes del delito en cuestion.

## Datos

Dado que la información se actualiza mensualmente pero el KPI debe ser actualizado anualmente por definicion.


