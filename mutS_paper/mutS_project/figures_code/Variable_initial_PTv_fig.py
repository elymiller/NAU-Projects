import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

df5 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_initial_PTv/5%_initial_Tv.csv")
df10 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_initial_PTv/10%_initial_Tv.csv")
df20 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_initial_PTv/20%_initial_Tv.csv")
df30 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_initial_PTv/30%_initial_Tv.csv")
df36 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_initial_PTv/36%_initial_Tv.csv")
df40 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_initial_PTv/40%_initial_Tv.csv")
df50 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_initial_PTv/50%_initial_Tv.csv")
df60 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_initial_PTv/60%_initial_Tv.csv")
df70 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_initial_PTv/70%_initial_Tv.csv")
df80 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_initial_PTv/80%_initial_Tv.csv")
df90 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_initial_PTv/90%_initial_Tv.csv")

p5 = df5["P(Tv)"] + df5["P(mutS)"]
p10 = df10["P(Tv)"] + df10["P(mutS)"]
p20 = df20["P(Tv)"] + df20["P(mutS)"]
p30 = df30["P(Tv)"] + df30["P(mutS)"]
p36 = df36["P(Tv)"] + df36["P(mutS)"]
p40 = df40["P(Tv)"] + df40["P(mutS)"]
p50 = df50["P(Tv)"] + df50["P(mutS)"]
p60 = df60["P(Tv)"] + df60["P(mutS)"]
p70 = df70["P(Tv)"] + df70["P(mutS)"]
p80 = df80["P(Tv)"] + df80["P(mutS)"]
p90 = df90["P(Tv)"] + df90["P(mutS)"]

# Prepare data for plotting
data = [p5, p10, p20, p30, p36, p40, p50, p60, p70, p80, p90]
labels = ["5%", "10%", "20%", "30%", "36%", "40%", "50%", "60%", "70%", "80%", "90%"]

# Use 'tab20' colormap which has bright, distinct colors (20 colors total)
# We'll use the first 11 colors for our 11 lines
colors = [plt.cm.tab20(i) for i in range(11)]

plt.figure(figsize=(10, 6))
for i, (d, label) in enumerate(zip(data, labels)):
    plt.plot(d, label=label, color=colors[i], linestyle='-', linewidth=2)

legend = plt.legend(title="Initial Probability of Transversion (PTv)\nPost-mutS: PTv = 0.05", ncol=2, framealpha=0.9)
legend.get_title().set_fontweight('bold')
plt.xlabel("Mutational Step (46 total)", fontweight="bold")
plt.ylabel("Cumulative Tv Probability", fontweight="bold")

plt.savefig("Variable_Initial_PTv.png", dpi=500)