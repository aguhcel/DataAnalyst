#%%
# Importar librerias
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

# %%
df = pd.read_csv('data.csv')

# Mostramos las primeras 5 filas
df.head(5)


# Mostramos las ultimas 5 filas
df.tail(5)
