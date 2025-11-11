import pandas as pd 
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import Tentativa_de_fazer_com_OO as mod

dados = mod.DadosIMU(pd.read_csv("df_filt.csv"))
teste = mod.DadosIMU(pd.read_csv("df_test.csv"))

dados["Timestamp"] = pd.to_datetime(dados["Timestamp"])
dados["segundo"] = dados["Timestamp"].dt.floor("S")

dados = dados.drop(columns=["Type", "Position", "Breed", "Subject", "Timestamp"])

grouped = dados.groupby("segundo")

features = pd.DataFrame()

for col in dados.columns[:-1]:
    _ = grouped[col].describe()
    features[f"{col}_mean"] = _["mean"]
    features[f"{col}_std"] = _["std"]









