# -*- coding: utf-8 -*-
"""Carregar dados para análise

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aDg-wN54DMITvOqiMgVzv6dhlasokQb7
"""

import pandas as pd
import matplotlib.pyplot as plt
excel_file_patch = 'estimativa_dou_2021.xlsx'
df = pd.read_excel(excel_file_patch)
print(df)