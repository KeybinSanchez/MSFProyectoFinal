[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=KeybinSanchez/MSFProyectoFinal)
 
# Proyecto Final: Sistema tegumentario

<img width="1448" height="1086" alt="Image" src="https://github.com/user-attachments/assets/6785a0fd-fc1c-4a83-8aa5-d17ff1af16de" />

<div align="justify">

## Información de los estudiantes

Sanchez Perez Keybin Daniel \[23210721]; l23210721@tectijuana.edu.mx, Campoy Alegria Marco Antonio \[21212145]; L21212145@tectijuana.edu.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1. Calcular la función de transferencia del modelo biomecánico del sistema tegumentario representado mediante un circuito RLC de segundo orden.
2. Determinar el modelo de ecuaciones integro-diferenciales.
3. Calcular el error en estado estacionario y la estabilidad del sistema.
4. Emular y simular la respuesta del circuito en Simulink/Simscape.
5. Sintonizar las ganancias de un controlador PID.
6. Obtener la respuesta en lazo abierto y en lazo cerrado con el controlador PID en Spyder/Python.
7. Elaborar el diagrama del sistema.

## Sistema Tegumentario: Modelo RLC

Este proyecto modela el sistema tegumentario mediante una analogía con un circuito RLC, enfocándose en la regulación térmica de la piel ante un estímulo externo. El sistema tegumentario está formado por la piel, anexos cutáneos, vasos sanguíneos superficiales, glándulas sudoríparas y tejido subcutáneo.

La piel participa en el intercambio de calor a través de la epidermis, dermis, microcirculación cutánea y tejido subcutáneo. En condiciones normales, regula la pérdida o ganancia de calor mediante su función de barrera y sus mecanismos vasculares. Sin embargo, en una lesión como una quemadura de segundo grado, parte de la epidermis y la dermis se dañan, alterando la resistencia superficial, la capacidad de almacenamiento térmico y la respuesta vascular local.

## Justificación del sistema

### Tabla 1. Parámetros del modelo RLC térmico para piel sana y piel con quemadura de segundo grado

| Componente | Control: piel sana | Caso: quemadura de segundo grado | Interpretación fisiológica |
|---|---:|---:|---|
| **R1** | **10 Ω** | **3.3 Ω** | Disminuye porque la epidermis dañada ofrece menor barrera al paso del calor. |
| **R2** | **6.8 Ω** | **12 Ω** | Aumenta porque la inflamación y el edema dificultan el intercambio térmico profundo. |
| **C** | **0.1 F** | **0.068 F** | Disminuye porque el tejido lesionado pierde capacidad de almacenar y liberar calor. |
| **L** | **1 H** | **1.5 H** | Aumenta porque la respuesta vascular se vuelve más lenta o irregular. |

## Descripción del modelo
El circuito RLC del sistema tegumentario se modela con una rama principal y dos ramas secundarias, con el propósito de representar el intercambio térmico y la respuesta fisiológica de la piel ante un estímulo externo. El circuito inicia con una fuente de voltaje de entrada [Ve (t)], la cual proporciona la señal de excitación y representa un estímulo térmico externo, como un cambio brusco de temperatura en el ambiente o el contacto de la piel con una superficie caliente. En la rama principal se conecta el resistor [R1], el cual representa la resistencia superficial de la piel, asociada principalmente al estrato córneo y la epidermis, actuando como barrera al paso del calor hacia las capas internas. 

Después de este primer elemento se encuentra un nodo intermedio, del cual parte la primera rama secundaria formada por el capacitor [C], conectado hacia tierra. Este elemento representa la capacidad de almacenamiento térmico de la dermis y del tejido cutáneo, es decir, la capacidad de la piel para absorber y liberar energía térmica de forma gradual. Posteriormente, en la misma rama principal se conecta el resistor [R2], que representa la resistencia al flujo de calor hacia capas más profundas, incluyendo el tejido subcutáneo y el intercambio térmico con la microcirculación sanguínea. Finalmente, en el nodo de salida se conecta la segunda rama secundaria, formada por el inductor [L], también conectado hacia tierra, el cual representa la inercia o retardo fisiológico de la respuesta vascular cutánea. La salida del sistema [Vs (t)] se toma en el nodo asociado al inductor [L], por lo que representa principalmente la respuesta transitoria relacionada con el retardo de la microcirculación ante un estímulo térmico externo. 

Si la entrada [Ve (t)] se define como una señal de escalón, ésta representa una alteración térmica repentina sobre la superficie cutánea. En el caso control, correspondiente a una piel sana, la barrera superficial presenta mayor resistencia, la capacidad de almacenamiento térmico es adecuada y la respuesta vascular ocurre de manera más regulada. En el caso patológico, como una quemadura de segundo grado, la resistencia superficial disminuye debido al daño en la epidermis, la capacidad térmica del tejido se altera y la respuesta vascular presenta un mayor retardo, ocasionando una respuesta distinta en la salida [Vs (t)]. De esta manera, el circuito RLC permite describir el comportamiento dinámico del sistema tegumentario de forma análoga a un sistema eléctrico. 

<div align="center">
<img width="1672" height="941" alt="Modelo RLC para el Sistema Tegumentario" src="https://github.com/user-attachments/assets/b8f6efcf-d8bb-48e1-8879-2708728ea25a" />
<br>
<b>Figura 1.</b> Modelo RLC para el sistema tegumentario.
</div>

## Modelo matemático del sistema

Se calculó de forma analítica la función de transferencia, el error en estado estacionario y el modelo de ecuaciones integro-diferenciales. Además, se determinó la estabilidad en lazo abierto para el caso control y el caso patológico.

### Ecuaciones integro-diferenciales del circuito

Las ecuaciones integro-diferenciales que describen el comportamiento del circuito RLC análogo al sistema tegumentario son:

<div align="center">

| Ecuación | Modelo |
|---|---|
| **Ec. 1** | $$V_e(t) = R_1 i_1(t) + \frac{1}{C}\int \left(i_1(t)-i_2(t)\right)dt$$ |
| **Ec. 2** | $$\frac{1}{C}\int \left(i_1(t)-i_2(t)\right)dt = R_2 i_2(t) + L\frac{di_2(t)}{dt}$$ |
| **Ec. 3** | $$V_s(t) = L\frac{di_2(t)}{dt}$$ |

</div>

### Modelo de ecuaciones integro-diferenciales

A partir del análisis del circuito RLC, las corrientes de malla se pueden expresar de la siguiente manera:

$$
i_1(t)=\frac{V_e(t)-\frac{1}{C}\int\left(i_1(t)-i_2(t)\right)dt}{R_1}
$$

$$
i_2(t)=\frac{\frac{1}{C}\int\left(i_1(t)-i_2(t)\right)dt-L\frac{di_2(t)}{dt}}{R_2}
$$

$$
V_s(t)=L\frac{di_2(t)}{dt}
$$

Donde $i_1(t)$ representa la corriente de la malla izquierda asociada a la transferencia térmica superficial, mientras que $i_2(t)$ representa la corriente de la malla derecha relacionada con la transferencia térmica profunda y la respuesta vascular.

### Función de transferencia

Sustituyendo estas relaciones en el modelo del circuito, se obtiene la función de transferencia del sistema:

$$
G(s)=\frac{V_s(s)}{V_e(s)}=\frac{Ls}{R_1CLs^2+\left(L+R_1R_2C\right)s+\left(R_1+R_2\right)}
$$

### Error en estado estacionario

El error en estado estacionario se define como la diferencia entre la entrada y la salida de un sistema cuando el límite en el tiempo tiende a infinito. Este análisis solo es útil para sistemas estables, por lo que primero se debe determinar la estabilidad del sistema. Para sistemas en lazo abierto, el error en estado estacionario está dado por:

$$
e_{ss}=\lim_{s \to 0}\left[1-G(s)\right]
$$

### Error en estado estacionario para el sistema de control

**Valores del sistema de control**

<div align="center">

| Condición | R1 | R2 | C | L |
|---|---:|---:|---:|---:|
| **Control: piel sana** | 10 Ω | 6.8 Ω | 0.1 F | 1 H |

</div>

Sustituyendo los valores en la función de transferencia:

$$
\frac{V_s(s)}{V_e(s)}=
\frac{1s}{(0.1)(1)(10)s^2+\left(1+(0.1)(10)(6.8)\right)s+(10+6.8)}
$$

Por lo tanto, el error en estado estacionario para el sistema de control es:

$$
e_{ss}=\lim_{s \to 0}\left(1-\frac{s}{s^2+7.8s+16.8}\right)
$$

$$
e_{ss}=1
$$

### Error en estado estacionario para el sistema del caso

**Valores del sistema del caso**

<div align="center">
 
| Condición | R1 | R2 | C | L |
|---|---:|---:|---:|---:|
| **Caso: quemadura de segundo grado** | 3.3 Ω | 12 Ω | 0.068 F | 1.5 H |
</div>

Sustituyendo los valores en la función de transferencia:

$$
G(s)=\frac{1.5s}{(0.068)(1.5)(3.3)s^2+\left(1.5+(0.068)(3.3)(12)\right)s+(3.3+12)}
$$

Por lo tanto, el error en estado estacionario para el sistema del caso es:

$$
e_{ss}=\lim_{s \to 0}\left(1-\frac{1.5}{0.3366s^2+4.1928s+15.3}\right)
$$

$$
e_{ss}=1
$$

### Estabilidad del sistema en lazo abierto

Para analizar la estabilidad en lazo abierto se utiliza el denominador de la función de transferencia:

$$
G(s)=\frac{Ls}{R_1CLs^2+\left(L+R_1R_2C\right)s+\left(R_1+R_2\right)}
$$

Para determinar la estabilidad se calculan las raíces del denominador usando la fórmula general:

$$
s=\frac{-b \pm \sqrt{b^2-4ac}}{2a}
$$

Donde:

$$
a=R_1CL
$$

$$
b=L+R_1R_2C
$$

$$
c=R_1+R_2
$$

### Estabilidad del sistema en lazo abierto para control

Control:

$$
s^2+7.8s+16.8=0
$$

Resultados:

$$
s_1=-3.9+1.2609j
$$

$$
s_2=-3.9-1.2609j
$$

Por lo tanto, como las raíces $\lambda_i$ del denominador de la función de transferencia son complejas conjugadas $(\sigma \pm j\omega)$ con parte real negativa $(Re\lambda_i < 0)$, entonces el sistema control es **estable en lazo abierto con una respuesta subamortiguada**.

### Estabilidad del sistema en lazo abierto para caso

Caso:

$$
0.3366s^2+4.1928s+15.3=0
$$

Resultados:

$$
s_1=-6.2281+2.5815j
$$

$$
s_2=-6.2281-2.5815j
$$

Por lo tanto, como las raíces $\lambda_i$ del denominador de la función de transferencia son complejas conjugadas $(\sigma \pm j\omega)$ con parte real negativa $(Re\lambda_i < 0)$, entonces el sistema del caso es **estable en lazo abierto con una respuesta subamortiguada**.

## Palabras clave
Sistema tegumentario; Circuito RLC; Controlador PID; Modelo biomecánico; Simulaciones numéricas; EID; Función de transferencia; Regulación térmica; Quemadura de segundo grado; Respuesta vascular cutánea; Transferencia de calor.

## Lista de archivos incluidos en el repositorio

1. Cuaderno computacional de MATLAB \[.mlx].
2. Modelo de Simulink \[.slx].
3. Archivos de Spyder \[.py].
4. Imagen con los parámetros del controlador.
5. Imágenes de las simulaciones \[.pdf].
6. Evidencia del análisis matemático: función de transferencia, modelo de ecuaciones integro-diferenciales, error en estado estacionario y estabilidad en lazo abierto.
7. Modelo fisiológico en Biorender o BioArt.
8. Ensayo gráfico. 

## Referencias

\[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2025. Permalink: https://biomath.xyz/course/

\[2] M. C. Khoo, Physiological Control Systems Analysis Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018, Section 4, Page 93.

\[3] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley \& Sons, 2020.

\[4] M. C. Khoo, Physiological Control Systems Analysis Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018, Section 2, Page 26.

\[5] Alzola, R. (2002). Sistema tegumentario.

</div>
