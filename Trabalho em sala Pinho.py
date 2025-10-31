# =============================================================
# AULA 3 --- Integração com NumPy e Matplotlib - Versão do Aluno
#
# Você irá simular um estudo de consumo de energia residencial ao longo de 180 dias, criando 
# dados sintéticos com comportamento realista e depois analisando e visualizando padrões desse 
# conjunto. Baseado em um conjunto de dados do Kaggle.
#
# O cenário é um conjunto de dados ambientais e de consumo energético, modelando como a 
# temperatura influencia o uso de energia em um ambiente doméstico:
#
# Temperatura diária (temp): simulada como uma série senoidal (representando ciclos de 
# aquecimento e resfriamento, como as variações sazonais do clima) acrescida de ruído aleatório.
#
# Consumo de energia (energy): criado como uma função da temperatura --- quanto mais distante do
# “conforto térmico” (22 °C), maior o consumo de energia (para aquecimento ou refrigeração).
#
# Anomalias (“spikes”): representam picos de consumo atípicos, simulando eventos reais
# (equipamentos defeituosos, dias de uso intenso, etc.).
#
# HDD/CDD (Heating/Cooling Degree Days): métricas derivadas amplamente usadas em engenharia 
# térmica e modelagem energética, que quantificam quanto a temperatura de um dia se desvia do 
# ideal de conforto.
#
# Média móvel (MA7): suaviza flutuações e ajuda a observar tendências sazonais ou de longo prazo.
# =============================================================

# -----------------------------
# PARTE A --- Setup e Dados
# -----------------------------
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdate

np.random.seed(42)

N = 180
base_temp=22.0
amp=8.0
noise_temp=1.5
noise_energy=10.0


Data = pd.date_range(start= "2025-01-01", periods= N ,freq = "D")
t = np.arange(N)

ruido_normal = np.random.normal(0, noise_temp, N)
temp = base_temp + amp*np.sin(2*np.pi*t/30) + ruido_normal 

ruido_normal1 = np.random.normal(0, noise_energy, N)
energy = 200 +5*np.abs(temp - base_temp) + ruido_normal1

#SPIKES
spike_indices = []
spikes_df = {"temp": [], "energy": []}
for i in np.random.choice(N, 3, replace= False):
    spike_indices.append(i)
    energy[i] += 80 
    spikes_df["temp"].append = temp[i]
    spikes_df["energy"].append = energy[i]

df_spykes = df[df.index.isin(spike_indices)]
spikes_df = pd.DataFrame(spikes_df, index= spike_indices)
print(spikes_df)

df = pd.DataFrame({"temp" : temp, "energy" : energy}, index= Data)
#print(df.head())
#print(df.describe().T)

df["bool_col"] = df["temp"]< base_temp
HDD = df[df["temp"]< base_temp].index
CDD = df[df["temp"]> base_temp].index

df["bool_col"][HDD] = "HDD"
df["bool_col"][CDD] = "CDD"
df["HDD_val"] = (base_temp - df["temp"]).clip(lower=0)
df["CDD_val"] = (df["temp"] - base_temp).clip(lower=0)

kernel = np.ones(7)/7
df["média_temp_7dias"] = np.convolve(df["temp"], kernel, "same")
#rint(df)

# ----------------------------------------------
# PARTE B --- Visualizações Avançadas
# ----------------------------------------------

fig = plt.figure(figsize= (12,8))
gs = fig.add_gridspec(2,2, hspace=0.35, wspace=0.25)

locator = mdate.AutoDateLocator()
fmt = mdate.ConciseDateFormatter(locator)

ax1 = fig.add_subplot(gs[0,0])
df["temp"].plot(ax=ax1, lw=1.0)
df["média_temp_7dias"].plot(ax=ax1, lw=2.0, label="Média móvel (7d)", color="black", alpha=0.30)
ax1.fill_between(Data, y1=base_temp, y2=df["temp"], where=df["CDD_val"], color="green", alpha=0.15)
ax1.fill_between(Data, y1=base_temp, y2=df["temp"], where=df["HDD_val"], color="red", alpha=0.15)
ax1.set_ylabel("ºC", rotation=0)
ax1.set_title("Série Temporal de Temperatura")
ax1.legend(loc="lower left")
ax1.xaxis.set_major_locator(locator)
ax1.xaxis.set_major_formatter(fmt)


ax2 = fig.add_subplot(gs[0,1])
ax2.scatter(df["temp"],df["energy"], alpha=0.7)
ax2.set_ylabel("KW/H", rotation=0)
ax2.set_xlabel("°C")
ax2.set_title("Dispersão Energia x Temperatura")
for i in spike_indices:
    ax2.annotate("spike", (df["temp"].iloc[i], df["energy"].iloc[i]),
                xytext=(8, 8), textcoords="offset points",
                arrowprops=dict(arrowstyle="->", lw=0.8))



plt.show()


# 13) (Ax4) AGREGAÇÃO SEMANAL + TWIN AXES
# Agregamos por semana para reduzir ruído diário e comparamos consumo (barras) com clima (linha) 
# na mesma linha do tempo, sem misturar escalas.
# Pesquise resample
#
# TODO: weekly = df.resample("W").agg({"energy":"sum", "temp":"mean"})
# TODO: ax4 = fig.add_subplot(gs[1, 1])
# TODO: barras de weekly["energy"] (width=5, align="center", label="Energia (semanal)")
# TODO: formatação do eixo x de datas com locator e fmt; ylabel adequado
# TODO: crie ax4_t = ax4.twinx() e plote weekly["temp"] como linha (marker="o", lw=1.8, label="Temp média (semanal)")
# TODO: títulos e legendas para ambos os eixos (ax4.legend, ax4_t.legend)

# 14) SALVAR E EXIBIR
# TODO: utilize tight_layout e salve a figura como "numpy_matplotlib.png" com 150 dpi
# TODO: exibir visualização