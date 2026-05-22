"""
PORYECTO FINAL: Sistema Tegumentario

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre de los alumnos y número de control :
Campoy Alegria Marco Antonio, 21212145
Sanchez Perez Keybin Daniel, 23210721
Correos institucionales: 
l21212145@tectijuana.edu.mx
l23210721@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Librerías para cálculo numérico y generación de gráficas
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]
plt.rcParams["mathtext.fontset"] = "cm"

# Datos de la simulación
x0, t0, tend, dt, w, h = 0, 0, 4, 1E-3, 10, 3.5
N = int(tend/dt) + 1
t = np.linspace(t0, tend, N)

# Entrada tipo escalón unitario en t = 1 s
Ve = np.zeros(N)
Ve[round(1/dt):] = 1

# Control: piel sana
R1_ctrl = 10
R2_ctrl = 6.8
C_ctrl = 0.1
L_ctrl = 1

num_ctrl = [L_ctrl, 0]
den_ctrl = [
    R1_ctrl*C_ctrl*L_ctrl,
    L_ctrl + R1_ctrl*R2_ctrl*C_ctrl,
    R1_ctrl + R2_ctrl
]

sys_ctrl = ctrl.tf(num_ctrl, den_ctrl)
print(f"FT Control: {sys_ctrl}\n")

# Caso: quemadura de segundo grado
R1_caso = 3.3
R2_caso = 12
C_caso = 0.068
L_caso = 1.5

num_caso = [L_caso, 0]
den_caso = [
    R1_caso*C_caso*L_caso,
    L_caso + R1_caso*R2_caso*C_caso,
    R1_caso + R2_caso
]

sys_caso = ctrl.tf(num_caso, den_caso)
print(f"FT Caso: {sys_caso}\n")

kP = 272.127525318921
kI = 61085.7640330147
kD = 0.0384687429452763
Nf = 4624.79395670643

P = ctrl.tf([kP], [1])
I = ctrl.tf([kI], [1, 0])
D = ctrl.tf([kD*Nf, 0], [1, Nf])

PID = P + I + D
print(f"FT Controlador PID: {PID}\n")

# Lazo cerrado del caso con PID
sys_caso_LC = ctrl.feedback(ctrl.series(PID, sys_caso), 1, sign=-1)
print(f"FT Caso LC: {sys_caso_LC}\n")


_, Vs_ctrl = ctrl.forced_response(sys_ctrl, t, Ve, x0)       # Control
_, Vs_caso = ctrl.forced_response(sys_caso, t, Ve, x0)       # Caso

_, PID_caso = ctrl.forced_response(sys_caso_LC, t, Vs_ctrl, x0)   # Tratamiento PID


clr1 = [0.95, 0.95, 0.00]   # Amarillo: Control
clr2 = [0.50, 0.00, 0.50]   # Morado: Caso
clr3 = [1.00, 0.00, 0.00]   # Rojo: PID

fig, ax = plt.subplots(figsize=(w, h))
fig.patch.set_facecolor('white')

ax.plot(t, Vs_ctrl, '-', color=clr1, linewidth=1.8,
        label=r'$V_s(t):\ Control$')

ax.plot(t, Vs_caso, '-', color=clr2, linewidth=1.8,
        label=r'$V_s(t):\ Caso\ Quemadura$')

ax.plot(t, PID_caso, ':', color=clr3, linewidth=2.2,
        label=r'$PID(t):\ Tratamiento$')

ax.set_xlim(1, 4)
ax.set_xticks(np.arange(1, 4.5, 0.5))

ax.set_ylim(0, 0.3)
ax.set_yticks(np.arange(0, 0.31, 0.05))

ax.set_xlabel(r'$t\ [s]$', fontsize=11)
ax.set_ylabel(r'$V_s(t)\ [V]$', fontsize=11)

ax.set_title('Respuesta del sistema patológico y efecto del controlador PID',
             fontsize=10, fontweight='bold')

ax.tick_params(direction='in', top=True, right=True)

ax.legend(loc='upper center',
          bbox_to_anchor=(0.5, -0.22),
          ncol=3,
          fontsize=9,
          frameon=False)

plt.tight_layout()

plt.savefig('tegumentariopy.pdf', bbox_inches='tight')
plt.savefig('tegumentariopy.png', dpi=600, bbox_inches='tight')

plt.show()