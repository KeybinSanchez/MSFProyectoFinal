[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=KeybinSanchez/MSFPractica4)
 
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

$$
V_e(t) = R_1 i_1(t) + \frac{1}{C}\int \left(i_1(t)-i_2(t)\right)dt
$$ **Ecuación 1**

$$
\frac{1}{C}\int \left(i_1(t)-i_2(t)\right)dt = R_2 i_2(t) + L\frac{di_2(t)}{dt}
$$ **Ecuación 2**

$$
V_s(t) = L\frac{di_2(t)}{dt}
$$ **Ecuación 3**

| Ecuación | Modelo |
|---|---|
| **Ec. 1** | $$V_e(t) = R_1 i_1(t) + \frac{1}{C}\int \left(i_1(t)-i_2(t)\right)dt$$ |
| **Ec. 2** | $$\frac{1}{C}\int \left(i_1(t)-i_2(t)\right)dt = R_2 i_2(t) + L\frac{di_2(t)}{dt}$$ |
| **Ec. 3** | $$V_s(t) = L\frac{di_2(t)}{dt}$$ |

### Expresión de las corrientes

A partir del análisis en el dominio de Laplace, se obtienen las expresiones de las corrientes de malla del sistema:

$$
I_1(s)=\left[1 + C R_2 s + C L s^2\right]I_2(s)
$$

Relación entre la corriente de la malla izquierda y la corriente de la malla derecha.

$$
I_2(s)=\frac{V_s(s)}{Ls}
$$

Expresión de la corriente de la malla derecha en función del voltaje de salida.

### Función de transferencia

Sustituyendo estas relaciones en el modelo del circuito, se obtiene la función de transferencia del sistema:

$$
G(s)=\frac{V_s(s)}{V_e(s)}=\frac{Ls}{R_1CLs^2+\left(L+R_1R_2C\right)s+\left(R_1+R_2\right)}
$$

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
8. Imagen en el osciloscopio. 

## Referencias

\[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2025. Permalink: https://biomath.xyz/course/

\[2] M. C. Khoo, Physiological Control Systems Analysis Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018, Section 4, Page 93.

\[3] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley \& Sons, 2020.

\[4] M. C. Khoo, Physiological Control Systems Analysis Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018, Section 2, Page 26.

</div>
