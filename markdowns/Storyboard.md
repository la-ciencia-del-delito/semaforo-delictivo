# Storyboard

Hacia el año 2015, surgió el actual semáforo delictivo como un proyecto de metodología estadística con el objetivo de conseguir la semaforización de la incidencia delictiva en México.
Como se sabe, los conteos de población en México se realizan cada 5 años (censo y conteo), lo cual provoca que el cálculo de las tasas no se actualicen junto con el cambio de población. Además, el utilizar la media hace susceptible a cambios bruscos al tener valores extremos en los años, lo que puede provocar que un cambio no se refleje adecuadamente. 
Por ejemplo, un Estado con pocos delitos en el pasado puede continuar con el indicador positivo (verde) a pesar de que exista una gran cantidad de delitos en el presente. O un Estado con muchos delitos en el pasado puede continuar con un indicador negativo (rojo) a pesar de haber disminuido la incidencia delictiva en la actualidad.

En este trabajo, se propone un Indicador Clave de Desempeño (KPI) que utiliza proyecciones de población de CONAPO y una fórmula diferente. Este KPI realiza una suma ponderada de tasas delictivas, dando mayor peso a delitos más graves como feminicidio, homicidio y secuestro, en contraste con otros menos graves como extorsión, violencia familiar y lesiones. La ponderación se establece según la gravedad de cada delito, ordenándolos según la cifra máxima de años de sanción del delito base.

Además, hemos incorporado diversas visualizaciones diseñadas de manera intuitiva, de tal forma que la interpretación de la información en ellas no requiere más que observar los elementos presentes. Estas herramientas visuales proporcionan a la audiencia una comprensión clara y accesible de los datos de delitos definidos por el gobierno, contribuyendo así a una interpretación más informada del estado actual de seguridad y delincuencia en nuestro país.

## Descubrimientos
1. No todos los delitos presentan un comportamiento uniforme a lo largo del tiempo; en términos generales, podemos distinguir dos categorías. Por un lado, están los delitos estacionarios, aquellos que permanecen estáticos alrededor de una media, lo que dificulta prever su evolución, ya que no se ven afectados por acciones o cambios sociales a lo largo de los años. Un ejemplo representativo de delitos estacionarios son los secuestros en Jalisco, que mantienen una media constante de 1.5 incidentes a lo largo del periodo estudiado.

2. Por otro lado, se encuentran los delitos no estacionarios, los cuales muestran tendencias temporales marcadas, indicando la influencia de factores que alteran su comportamiento. Estos cambios pueden deberse a acciones gubernamentales que generan una tendencia a la baja del delito o a modificaciones en el comportamiento de la población. Un ejemplo ilustrativo de esta categoría es el robo a casas en Aguascalientes, que mantuvo una media de 200 incidentes hasta mediados de 2016, experimentó una marcada tendencia al alza hasta finales de 2019, con una media de 275, y luego mostró una disminución constante hasta estabilizarse en 200.


3. Al analizar los delitos más frecuentes por estado, se nota una alta presencia de violencia familiar, seguida de lesiones en todos ellos. Este patrón sugiere que la violencia doméstica puede ser un factor significativo en los niveles delictivos a nivel nacional, destacando la importancia de abordar esta problemática para reducir la incidencia delictiva en el país.



4. Al explorar la modalidad de delitos, se destaca que en el caso de homicidios, la gran mayoría se llevan a cabo utilizando armas de fuego, sugiriendo la existencia de una población con un acceso significativo a este tipo de armamento. Al realizar una comparación entre distintas categorías de delitos, como homicidios, feminicidios y lesiones, se revela que la modalidad más recurrente es "Con otro elemento". Este hallazgo señala una cierta ambigüedad en la ejecución de los delitos y destaca la necesidad de abordar de manera específica esta categoría para comprender mejor las circunstancias que rodean los actos delictivos y, en consecuencia, desarrollar estrategias más efectivas de prevención y control.

5. El análisis reveló que las gráficas del KPI y la percepción de inseguridad muestran un comportamiento similar a lo largo de los años, tanto en términos de pendiente como de cambios. Este hallazgo sugiere una correlación entre la medida objetiva de incidencia delictiva proporcionada por el KPI y los datos de percepción seguridad, respaldando la validez del indicador como una herramienta eficaz para reflejar y seguir las tendencias delictivas a nivel nacional. La consistencia en la dinámica de ambas gráficas refuerza la utilidad del KPI como una métrica que no solo cuantifica, sino que también se alinea con la percepción general de seguridad en la población.

## Datos
La recopilación y clasificación de los datos sobre incidencia delictiva se obtuvo de la página oficial del Gobierno de México: https://www.gob.mx. Por otro lado, las cifras poblacionales utilizadas se basaron en datos oficiales descargados directamente del sitio de la Comisión Nacional de Población (CONAPO) disponible en https://conapo.segob.gob.mx. 

Para abordar la percepción ciudadana y complementar la perspectiva del estudio, los datos relativos a la seguridad percibida fueron adquiridos directamente del Instituto Nacional de Estadística y Geografía (INEGI). De igual manera, las geometrías utilizadas en la representación cartográfica fueron obtenidas de las fuentes oficiales del INEGI.

## Conclusión
Este estudio introduce un enfoque para evaluar la incidencia delictiva en México mediante un KPI que aprovecha proyecciones poblacionales y ponderaciones basadas en la gravedad del delito. 

La distinción entre delitos estacionarios y no estacionarios arroja luz sobre tendencias a lo largo del tiempo, señalando posibles factores influyentes. 

Adicionalmente, el análisis de modalidades delictivas, especialmente en homicidios, subraya desafíos relacionados con el uso de armas de fuego.



