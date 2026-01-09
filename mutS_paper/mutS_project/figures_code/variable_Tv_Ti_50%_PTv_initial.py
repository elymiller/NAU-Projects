import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

df1_45 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_Tv_Ti_50%_PTv_initial/50%_initial_1Tv_45Ti.csv")
df2_44 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_Tv_Ti_50%_PTv_initial/50%_initial_2Tv_44Ti.csv")
df3_43 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_Tv_Ti_50%_PTv_initial/50%_initial_3Tv_43Ti.csv")
df4_42 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_Tv_Ti_50%_PTv_initial/50%_initial_4Tv_42Ti.csv")
df5_41 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_Tv_Ti_50%_PTv_initial/50%_initial_5Tv_41Ti.csv")
df6_40 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_Tv_Ti_50%_PTv_initial/50%_initial_6Tv_40Ti.csv")
df7_39 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_Tv_Ti_50%_PTv_initial/50%_initial_7Tv_39Ti.csv")
df8_38 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_Tv_Ti_50%_PTv_initial/50%_initial_8Tv_38Ti.csv")
df9_37 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_Tv_Ti_50%_PTv_initial/50%_initial_9Tv_37Ti.csv")
df10_36 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_Tv_Ti_50%_PTv_initial/50%_initial_10Tv_36Ti.csv")
df15_31 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_Tv_Ti_50%_PTv_initial/50%_initial_15Tv_31Ti.csv")
df23_23 = pd.read_csv("/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_Tv_Ti_50%_PTv_initial/50%_initial_23Tv_23Ti.csv")


p1_45 = df1_45["P(Tv)"] + df1_45["P(mutS)"]
p2_44 = df2_44["P(Tv)"] + df2_44["P(mutS)"]
p3_43 = df3_43["P(Tv)"] + df3_43["P(mutS)"]
p4_42 = df4_42["P(Tv)"] + df4_42["P(mutS)"]
p5_41 = df5_41["P(Tv)"] + df5_41["P(mutS)"]
p6_40 = df6_40["P(Tv)"] + df6_40["P(mutS)"]
p7_39 = df7_39["P(Tv)"] + df7_39["P(mutS)"]
p8_38 = df8_38["P(Tv)"] + df8_38["P(mutS)"]
p9_37 = df9_37["P(Tv)"] + df9_37["P(mutS)"]
p10_36 = df10_36["P(Tv)"] + df10_36["P(mutS)"]
p15_31 = df15_31["P(Tv)"] + df15_31["P(mutS)"]
p23_23 = df23_23["P(Tv)"] + df23_23["P(mutS)"]


# Prepare data for plotting
data = [p1_45, p2_44, p3_43, p4_42, p5_41, p6_40, p7_39, p8_38, p9_37, p10_36, p15_31, p23_23]
labels = ["1Tv : 45Ti", "2Tv : 44Ti", "3Tv : 43Ti", "4Tv : 42Ti", "5Tv : 41Ti", "6Tv : 40Ti", "7Tv : 39Ti", "8Tv : 38Ti", "9Tv : 37Ti", "10Tv : 36Ti", "15Tv : 31Ti", "23Tv : 23Ti"]

# Use 'tab20' colormap which has bright, distinct colors (20 colors total)
# We'll use the first 11 colors for our 11 lines
colors = [plt.cm.tab20(i) for i in range(12)]

plt.figure(figsize=(10, 6))
for i, (d, label) in enumerate(zip(data, labels)):
    plt.plot(d, label=label, color=colors[i], linestyle='-', linewidth=2)

legend = plt.legend(title="Number of Ti and Tv SNPs\nPre-mutS: PTv = 0.50\nPost-mutS: PTv = 0.05", ncol=2, framealpha=0.9)
legend.get_title().set_fontweight('bold')
plt.xlabel("Mutational Step (46 total)", fontweight="bold")
plt.ylabel("Cumulative Tv Probability", fontweight="bold")

plt.savefig("variable_Tv_Ti_50%_PTv_initial.png", dpi=500)