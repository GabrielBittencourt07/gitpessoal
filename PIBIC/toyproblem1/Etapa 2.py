import pandas as pd 
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

dados = pd.read_csv("df_filt.csv")
teste = pd.read_csv("df_test.csv")

print(dados.info())





