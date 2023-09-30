# Propuestas
1. Valorar el uso de nuevos mapas... etc... desarrollar este tema luego...
Desarrollar esto...
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

$IIC = TI_1 * 0.6 + TI_2 * 0.24 + TI_3 * 0.1 + TI_4 * 0.13 + TI_5 * 0.13 + TI_6 * 0.13 + TI_7 * 0.13 + TI_8 * 0.08 + TI_9 * 0.08 + TI_10 * 0.04 + TI_11 * 0.02.$

Finalmente se ajustarán los pesos asignados hasta encontrar valores acordes con datos procedentes de otras fuentes, tales como la "Percepción sobre seguridad pública" según datos de la [INEGI](https://www.inegi.org.mx/temas/percepcion/).

3. Se propone el uso de un icono nuevo ícono para señalizar los delitos que se encuentran fuera de control.

![Fuera_de_control](https://github.com/la-ciencia-del-delito/semaforo-delictivo/blob/main/notebooks/Red_Arrow.jpg)

4. Se propone el uso alternativo de los datos de la CONAPO, además de los datos que de la INEGI que ya usa el Semáforo en su versión actual.
Se identifica como una de las limitaciones del semáforo el hecho de que contempla solo los datos de población censal del año 2020 lo cual pudiera provocar una interpretación menos precisa de la situación delectiva en el país.
Por ejemplo: en el 2020 la población de México era de unos 126 014 024 habitantes y ocurrieron unos 19620 homicidios, para una tasa acumulada del año de 15.6 por cada 100 000 habitantes.

$Tasa = \frac{19 620}{126 014 024} * 100 000 = 15.6$

Todo bien hasta acá, pero luego en los años venideros se vuelven a realizar los cálculos con las mismas cifras de población del 2020.

En el año 2021 ocurrieron 19 197 homicidios. Para una tasa de 15.2.

$Tasa = \frac{19 197}{126 014 024} * 100 000 = 15.2$

En el año 2022 ocurrieron 17 445 homicidios. Para una tasa de 13.8.

$Tasa = \frac{17 445}{126 014 024} * 100 000 = 13.8$

No se entienden dichos cálculos como desasertados, pero quizás utilizando las estimaciones realizadas por la CONAPO, con las cifras de población desde el 1950 hasta 2070, se pueda tener una impresión más precisa de la situación actual de cada delito.

Ahí entonces que una de las propuestas sea quizás ofrecer al usuario la posibilidad de usar estas estimaciones de población, ya que no es posible negar que la pobación mexicana continúa aumentando, al igual que la esperanza de vida.
