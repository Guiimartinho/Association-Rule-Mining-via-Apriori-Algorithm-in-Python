# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 22:07:22 2019

@author: Guilherme
"""

import matplotlib.pyplot as plt
from numpy import genfromtxt

dados = genfromtxt('tempo-decorrido.csv')
histograma = plt.hist(dados, bins="sturges")
#histograma = plt.hist(dados, bins="scott")
#histograma = plt.hist(dados, bins="fd")
histograma = plt.hist(dados, bins=4)
histograma = plt.hist(dados)