# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 13:10:57 2021

@author: Zakaria
"""

import pandas as pd
import numpy as np

dataset = pd.DataFrame(np.random.randn(6,4), index=['1','3','4','6','7','8'],
                       columns=["taux_de_vente","croissance_vente","ratio_vente","ratio_perte"])
print(dataset)

dataset = dataset.reindex(['1','2','3','4','5','6','7','8'])
print(dataset)

print(dataset.isnull())

dataset = dataset[dataset.isnull().any(axis=1)]
print(dataset)

#Remplacer les NaN par une valeur scalaire
print(dataset.fillna(0))

#Supprimer les valeurs NaN
print(dataset.dropna())