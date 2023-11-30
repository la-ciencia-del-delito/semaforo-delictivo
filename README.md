# Semáforo Delictivo
#### Proyecto final para la materia **Ingeniería de características**. A cargo del Dr. Julio Waissman Vilanova.
#### Autores:
* Guillermo Velázquez Coronado.
* Misael González Soria.
* Viowi Yirmeiah Cabrisas Amuedo.

### La Ciencia del delito
La "Ciencia del Delito" es una organización creada con el objetivo de realizar un ejercicio docente en la MCD de la Universidad de Sonora. En el marco del ejercicio se realizarán propuestas y posiblemente aportes a la forma de visualizar los datos del Semáforo Delictivo, de realizar el análisis de los mismos y lograr una interpretación más precisa de la situación delictiva actual en México.

### Semáforo Delictivo
El semáforo delictivo es un proyecto o metodología estadística creada para conseguir la semaforización de la incidencia delictiva en México. El mismo fue cuidadosamente consebido para implementar varios tipos de análisis y formas de visualizar la información de la estadística criminal.
Se abordan estadísticas sobre "delitos del fuero común" que se encuentran tipificados en el Código Penal del Estado. Los delitos del fuero común son los que afectan directamente a las personas en lo individual, estos se organizan por el tipo de bien jurídico afectado: la vida y la integridad corporal, la libertad personal, la libertad y la seguridad sexual, el patrimonio, la familia, la sociedad y otros. Los que se cometen con mayor frecuencia son Robo a personas y Robo a vehículos automotores, siendo delitos de alto impacto; el de Homicidio doloso y Feminicidio, entre otros.
Los delitos abordados en el semáforo son los siguientes:
- Homicidios.
- Secuestros.
- Extorsión.
- Narcomenudeo.
- Robo a vehículo.
- Robo a casa.
- Robo a negocio.
- Lesiones.
- Violación.
- Violencia familiar.
- Feminicidio.

La significación de los colores en el semáforo delictivo gira básicamente en torno al parámetro de la media para cada delito ya sea a nivel de entidad federativa o país.
Los valores que se encuentran por encima de la media se representan con el <font color='red'>Rojo</font>, los valores entre la meta y la media en <span style="color:yellow">Amarillo</span> y los valores por debajo de la meta se representan en <span style="color:green">Verde</span>.

${\color{red}Rojo}$

* Fuera de control = Media + (Media / 2).

${\color{red}Rojo}$

* Media

${\color{yellow}Amarillo}$

* Meta = Media - (Media / 2).

${\color{green}Verde}$

Notándose lo que pudiera interpretarse como una limitación, a la dificultad de no poder representar gráficamente el concepto propuesto en dicho proyecto para identificar cuando los delitos se encuentran fuera de control. Presuntivamente para no usar otros colores que rompan la armonía del diseño, o quizás no sobre alarmar.


## La Ciencia del Delito y sus propuestas:
La "Ciencia del Delito" es una organización creada con el objetivo de realizar un ejercicio docente en la MCD de la Universidad de Sonora. En el marco del ejercicio se realizarán propuestas y posiblemente aportes a la forma de visualizar los datos, de realizar el análisis de los mismos y lograr una interpretación más precisa de la situación delictiva actual en México.

Propuestas:
1. Valorar el uso del mapa propuesto.
2. Proponer el uso de nuevos KPIs.
Proponer KPI Índice de Inseguridad Ciudadana (IIC): Para el cálculo de este índice inicialmente se ordenaran los delitos abordados de acuerdo a su gravedad y/o el tiempo sanción en años o meses (Mínimo - Máximo), estableciendose un peso de acuerdo al orden de la siguiente forma.

No.   |  Orden                 |  Mínimo |  Máximo
------|------------------------|---------|-------------------
1     |  [Feminicidio](https://mexico.justia.com/federales/codigos/codigo-penal-federal/libro-segundo/titulo-decimonoveno/capitulo-v/)           |  40	 |  60
2     |  [Homicidios](https://mexico.justia.com/federales/codigos/codigo-penal-federal/libro-segundo/titulo-decimonoveno/capitulo-ii/)            |  12	 |  24
3     |  [Secuestros](https://mexico.justia.com/federales/codigos/codigo-penal-federal/libro-segundo/titulo-vigesimoprimero/capitulo-unico/)            |  3	     |  10
4     |  [Robo a casa](https://mexico.justia.com/federales/codigos/codigo-penal-federal/libro-segundo/titulo-vigesimosegundo/capitulo-i/)           |  6	     |  13
5     |  [Robo a negocio](https://mexico.justia.com/federales/codigos/codigo-penal-federal/libro-segundo/titulo-vigesimosegundo/capitulo-i/)        |  6	     |  13
6     |  [Robo a vehículo](https://mexico.justia.com/federales/codigos/codigo-penal-federal/libro-segundo/titulo-vigesimosegundo/capitulo-i/)       |  6	     |  13
7     |  [Violación](https://mexico.justia.com/federales/codigos/codigo-penal-federal/libro-segundo/titulo-decimoquinto/capitulo-i/)             |  6	     |  13
8     |  [Narcomenudeo](https://mexico.justia.com/federales/leyes/ley-general-de-salud/titulo-decimo-octavo/capitulo-vii/)          |  4	     |  8
9     |  [Extorsión](https://mexico.justia.com/federales/codigos/codigo-penal-federal/libro-segundo/titulo-vigesimosegundo/capitulo-iii-bis/)             |  2	     |  8
10    |  [Violencia familiar](https://mexico.justia.com/federales/codigos/codigo-penal-federal/libro-segundo/titulo-decimonoveno/capitulo-octavo/)    |  6m	 |  4
11    |  [Lesiones](https://mexico.justia.com/federales/codigos/codigo-penal-federal/libro-segundo/titulo-decimonoveno/capitulo-i/)              |  4m	 |  2

Luego se realizará la suma del producto de la tasa de incidencia del delito con el peso asignado al mismo según el límite máximo de la sanción, quedando de la siguiente forma:

$IIC = TI_1 * 0.6 + TI_2 * 0.24 + TI_3 * 0.1 + TI_4 * 0.13 + TI_5 * 0.13 + TI_6 * 0.13 + TI_7 * 0.13 + TI_8 * 0.08 + TI_9 * 0.08 + TI_{10} * 0.04 + TI_{11} * 0.02.$

Unidad de medida del IIC: años de sanción máxima por cada 1000 habitantes.

Para explicar la unidad de medida basta recordar que los pesos o índices asignados a cada delito se basa en la cifra máxima en años de sanción al delito base, sin incluir los agravantes, y luego esta cifra se divide por 100.
Ejemplo: en el Feminicidio, la sanción máxima resulta ser de 60 años, entonces el índice de este delito en el KPI sería de 0.6.
Luego, las tasas específicas de cada delito se encuentran calculadas según población por cada 100 000 habitantes, así que viendo de cercca el primer componente del IIC que analizaría el Feminicidio y se calcularía a partir de la multiplicación de la tasa de incidencia de Feminicidio ($TI_1$) por el índice establecido, y sería así según la fórmula:

$TI_1 * 0.6$

Desglosando:

$(\frac{cantidad \hspace{2pt} de \hspace{2pt} Feminicidios}{población \hspace{2pt} total} * 100 \hspace{2pt} 000 habitantes) * (\frac{años \hspace{2pt} de \hspace{2pt} sanción \hspace{2pt} máxima \hspace{2pt} del \hspace{2pt} Feminicidio \hspace{2pt} según \hspace{2pt} código \hspace{2pt} penal}{100})$

Luego:

$\frac{100 \hspace{2pt} 000 \hspace{2pt} habitantes}{100}= 1000 \hspace{2pt} habitantes$

Quedando entonces la unidad de medida fijada en: años de sanción  máxima por cada 1000 habitantes.

Luego se definirán los rangos o categorías de sus valores en conversaciones posteriores con el usuario al frente del proyecto.

Finalmente se verificarán resultados con datos procedentes de otras fuentes, tales como la "Percepción sobre seguridad pública" según datos de la [INEGI](https://www.inegi.org.mx/temas/percepcion/). Para de esta forma chequear el comportamiento del KPI durante el período de 2015 a 2023. Y más adelante incluir además el Índice de marginalidad para establecer comparaciones.  

<div><div/> <!-- Sin esto, el texto también se centra -->
3. Se propone el uso de un icono nuevo ícono para señalizar los delitos que se encuentran fuera de control.
<!-- Cetrar imagen -->
<img src="./assets/Red_Arrow.jpg" 
        alt="Picture" 
        width="" 
        height="" 
        style="display: block; margin: 20 auto" />
4. Se propone el uso alternativo de los datos de la CONAPO, además de los datos que de la INEGI que ya usa el Semáforo en su versión actual.
Se identifica como una de las limitaciones del semáforo el hecho de que contempla solo los datos de población censal del año 2020 lo cual pudiera provocar una interpretación menos precisa de la situación delectiva en el país.
Por ejemplo: en el 2020 la población de México era de unos 126 014 024 habitantes y ocurrieron unos 19620 homicidios, para una tasa acumulada del año de 15.6 por cada 100 000 habitantes.

$$
Tasa = \frac{19 620}{126 014 024} * 100 000 = 15.6
$$

Todo bien hasta acá, pero luego en los años venideros se vuelven a realizar los cálculos con las mismas cifras de población del 2020.

En el año 2021 ocurrieron 19 197 homicidios. Para una tasa de 15.2.

$$
Tasa = \frac{19 197}{126 014 024} * 100 000 = 15.2
$$

En el año 2022 ocurrieron 17 445 homicidios. Para una tasa de 13.8.

$$
Tasa = \frac{17 445}{126 014 024} * 100 000 = 13.8
$$

No se entienden dichos cálculos como desasertados, pero quizás utilizando las estimaciones realizadas por la CONAPO, con las cifras de población desde el 1950 hasta 2070, se pueda tener una impresión más precisa de la situación actual de cada delito.

Ahí entonces que una de las propuestas sea quizás ofrecer al usuario la posibilidad de usar estas estimaciones de población, ya que no es posible negar que la pobación mexicana continúa aumentando, al igual que la esperanza de vida.

### Fuentes de datos consultadas
- Bases de datos de la Conciliación Demográfica 1950 a 2019 y Proyecciones de la población de México 2020 a 2070. (CONAPO).
https://www.gob.mx/conapo/documentos/bases-de-datos-de-la-conciliacion-demografica-1950-a-2019-y-proyecciones-de-la-poblacion-de-mexico-2020-a-2070?idiom=es
https://conapo.segob.gob.mx/work/models/CONAPO/pry23/DB/ConDem50a19_ProyPob20a70.zip

- Datos abiertos de incidencia delictiva (Gobierno de México).
https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva
https://drive.google.com/file/d/13TjyJ9RkR49o0eWTFvhNqazeL4maORYp/view

- Resultados de la Encuesta de Percepción sobre seguridad pública. (INEGI).
https://www.inegi.org.mx/temas/percepcion/

### Libretas de Jupyter
- [ETL](https://github.com/la-ciencia-del-delito/semaforo-delictivo/tree/main/ETL)
- [EDA](https://github.com/la-ciencia-del-delito/semaforo-delictivo/tree/main/EDA)
- [Dashboard](https://github.com/la-ciencia-del-delito/semaforo-delictivo/tree/main/dashboard)