[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=KeybinSanchez/MSFPractica4)

# Práctica 4: Sistema endócrino

## Información de la estudiante

Sanchez Perez Keybin Daniel \[23210721]; l23210721@tectijuana.edu.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1. Calcular la función de transferencia del modelo biomecánico del sistema endócrino representado mediante un circuito RLC de segundo orden.
2. Determinar el modelo de ecuaciones integro-diferenciales.
3. Calcular el error en estado estacionario y la estabilidad del sistema.
4. Emular y simular la respuesta del circuito en Simulink/Simscape.
5. Sintonizar las ganancias de un controlador PID.
6. Obtener la respuesta en lazo abierto y en lazo cerrado con el controlador PID en Spyder/Python.
7. Elaborar el diagrama del sistema.

## Descripción detallada del sistema

El sistema endocrino regula diversas funciones fisiológicas mediante la secreción y transporte de hormonas a través del torrente sanguíneo, las cuales actúan sobre órganos diana para generar respuestas específicas. Esta dinámica puede modelarse de forma simplificada mediante un circuito eléctrico de segundo orden tipo RLC, representando los procesos de secreción, transporte y respuesta hormonal bajo las siguientes consideraciones:

1. La secreción hormonal desde una glándula (como el hipotálamo o la hipófisis) se modela como una fuente de entrada Ve(t), que representa un estímulo inicial al sistema, como una señal homeostática o neural.
2. El proceso de transporte y difusión de las hormonas en el torrente sanguíneo se representa mediante una resistencia R1, asociada a las pérdidas y retardos en la señal hormonal durante su desplazamiento.
3. El almacenamiento temporal o acumulación de hormonas en tejidos o compartimentos intermedios se modela mediante un capacitor C, el cual describe la capacidad del sistema para regular la disponibilidad hormonal en el tiempo.
4. La respuesta del órgano diana (como la tiroides o las glándulas suprarrenales) se representa mediante una segunda rama que incluye una resistencia R2 y una inductancia L, donde R2 modela la resistencia al cambio en la concentración hormonal y L representa la inercia o retardo en la respuesta biológica.
5. Se identifican dos variables principales en el sistema: el flujo de secreción hormonal Fe(t) y la respuesta del sistema en el órgano diana Fs(t), análogas a las variables de entrada y salida del circuito eléctrico.

## Palabras clave
Sistema endócrino; Circuito RLC; Controlador PID; Modelo biomecánico; Simulaciones numéricas, EID, Función de transferencia.

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

