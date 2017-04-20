from IMC_Calculator import Calcular_IMC()
"""
Ms: Quantidade de morfina absorvida no sangue
m:  Quantidade de Morfina
c:  Capacidade a capacidade máxima do corpo de excretar morfina
f:  Função da quantidade de morfina na injeção/via oral: Relaciona massa(w)/altura(h) -(IMC)- a quantidade de morfina
g:  Função de excreção de morfina: Relaciona a capacidade máxima do corpo de excretar morfina e a a quantidade de morfina no sangue (fator limitante)

ESTOQUES E FLUXOS (EQUÇÕES À DIFRENÇAS):
 Ms(t+1) = Ms(t) + f(h,w,m) - g(c,Ms)
"""


"""
Via oral: 0,2 a 0,5 (0,3500) mg/kg, a cada 4 a 24 horas.

Injetável:

- Recem-Nascido:

    #0,05 a 0,2 (0,1250) mg/kg/dose, a cada 2 a 4 horas

    #em administração contínua de 0,01 a 0,04(0,0250) mg/kg/hora.

-Dose Criança:

    #inicial: 0,05 mg/kg;

    #manutenção: 0,1 a 0,2  (0,1500) mg/kg/dose, a cada 2 e 4 horas;
 
    #dose máxima: 15 mg/dose; infusão contínua: 0,025 a 0,1 (0,0625 ) mg/kg/hora.
"""

