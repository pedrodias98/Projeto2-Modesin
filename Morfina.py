# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 10:34:57 2017

@author: dualstream799 'n bolinho_dengoso_29
"""
"""
Ms: Quantidade de morfina absorvida no sangue
m:  Quantidade de Morfina
c:  Capacidade a capacidade máxima do corpo de excretar morfina
Mt: Método terapêutico utilizado
f:  Função da quantidade de morfina na injeção/via oral: Relaciona massa(w)/altura(h) -(IMC)- a quantidade de morfina
g:  Função de excreção de morfina: Relaciona a capacidade máxima do corpo de excretar morfina e a a quantidade de morfina no sangue (fator limitante)

meia-vida da morfina = 120min (2h)

ESTOQUES E FLUXOS (EQUÇÕES À DIFRENÇAS):
 Ms(t+1) = Ms(t) + f(w,m) - g(c,Ms)
 f(w,m)  = Mt*w
 g(c,Ms) = Ms*(2**(-t/2))
 EQUAÇÃO DIFERENCIAL:
 dMs/dt = (f - g)/dt = (Mt*w -Ms*(2**(-t/2)))/dt
"""
"""
Injetável:

- Recem-Nascido:

    # 0,05 a 0,2 (0,1250) mg/kg/dose, a cada 2 a 4 horas
    # administração contínua: 0,01 a 0,04(0,0250) mg/kg/hora

- Criança:

    # dose inicial: 0,05 mg/kg
    # manutenção: 0,1 a 0,2  (0,1500) mg/kg/dose, a cada 2 e 4 horas
    # dose máxima: 15 mg/dose 
    # infusão contínua: 0,025 a 0,1 (0,0625) mg/kg/hora
    
"""
# Importando bibliotecas:
import matplotlib.pyplot as plt
# Parâmetros:
Ic = 0.0625
Ms = []
# Criando as entradas:
w = float(input("Insira a sua peso (em quilogramas):"))  # w -> weight(peso)
def Calcula_f2():
    f = Ic*w
    return f
def Calcula_g2():
    g =





# Plotando Gráfico:

plt.show()