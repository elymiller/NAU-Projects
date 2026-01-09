import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

df1 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_project/mutS_model_output/36%_initial_PTv_variable_post_mutS/36%_initial_1%_post_Tv.csv")
df2_5 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_project/mutS_model_output/36%_initial_PTv_variable_post_mutS/36%_initial_2.5%_post_Tv.csv")
df5 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_project/mutS_model_output/36%_initial_PTv_variable_post_mutS/36%_initial_5%_post_Tv.csv")
df10 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_project/mutS_model_output/36%_initial_PTv_variable_post_mutS/36%_initial_10%_post_Tv.csv")
df20 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_project/mutS_model_output/36%_initial_PTv_variable_post_mutS/36%_initial_20%_post_Tv.csv")
df30 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_project/mutS_model_output/36%_initial_PTv_variable_post_mutS/36%_initial_30%_post_Tv.csv")
df36 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_project/mutS_model_output/36%_initial_PTv_variable_post_mutS/36%_initial_36%_post_Tv.csv")
df50 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_project/mutS_model_output/36%_initial_PTv_variable_post_mutS/36%_initial_50%_post_Tv.csv")


p1 = df1["P(Tv)"] + df1["P(mutS)"]
p2_5 = df2_5["P(Tv)"] + df2_5["P(mutS)"]
p5 = df5["P(Tv)"] + df5["P(mutS)"]
p10 = df10["P(Tv)"] + df10["P(mutS)"]
p20 = df20["P(Tv)"] + df20["P(mutS)"]
p30 = df30["P(Tv)"] + df30["P(mutS)"]
p36 = df36["P(Tv)"] + df36["P(mutS)"]
p50 = df50["P(Tv)"] + df50["P(mutS)"]


# Prepare data for plotting
data = [p1, p2_5, p5, p10, p20, p30, p36, p50]
labels = ["1%", "2.5%", "5%", "10%", "20%", "30%", "36%", "50%"]

# Use 'tab20' colormap which has bright, distinct colors (20 colors total)
# We'll use the first 11 colors for our 11 lines
colors = [plt.cm.tab20(i) for i in range(8)]

plt.figure(figsize=(10, 6))
for i, (d, label) in enumerate(zip(data, labels)):
    plt.plot(d, label=label, color=colors[i], linestyle='-', linewidth=2)

legend = plt.legend(
    title='Post-mutS Probability of Transversion $\\boldsymbol{P}(\\mathbf{Tv})$\nPre-mutS: $\\boldsymbol{P}(\\mathbf{Tv})$ = 0.36',
    ncol=2,
    framealpha=0.9
)
legend.get_title().set_fontweight('bold')
plt.xlabel("Mutational Step (46 total)", fontweight="bold")
plt.ylabel("Tv Probability $\\boldsymbol{P}(\\mathbf{Tv})$", fontweight="bold")

plt.savefig("/Users/elymiller/Desktop/Research/mutS_paper/mutS_project/figures_v2/36%_inital_PTv_variable_post_mutS.png", dpi=500)