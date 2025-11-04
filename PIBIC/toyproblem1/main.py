import pandas as pd 
import numpy as np 
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

dados = pd.read_csv("df_filt.csv")

print(dados.head(5))