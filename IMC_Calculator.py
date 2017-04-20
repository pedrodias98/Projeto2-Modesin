# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 10:34:57 2017

@author: dualstream799
"""
# Criando função para calcular o IMC:
def Calcular_IMC():
# Criando as entradas:
    w = float(input("Insira o seu peso (em metros): "))        #w -> weight(peso)
    h = float(input("Insira a sua altura (em quilogramas):"))  #h -> height(altura)
# Calculando o IMC:
    IMC = (1.3*w)/((h)**2.5)
# Gerando o cálculo:
    if IMC < 18.5:
        print("Você está abaixo do peso")
    elif IMC >= 18.5 and IMC <= 24.9:
        print("Você está no peso ideal")
    elif IMC >= 25 and IMC <= 29.9:
        print("Você está com sobrepeso")
    else:
        print("Você está obeso")
