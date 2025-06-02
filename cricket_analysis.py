import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

score = pd.read_csv('cricket_score.csv')

plt.figure(figsize=(10,5))
plt.plot(score["Over"], score["India"], marker='o', linestyle='-', color='blue', label="India")
plt.plot(score["Over"], score["Australia"], marker='s', linestyle='-', color='orange', label="Australia")
plt.xlabel("Over")
plt.ylabel("Runs")
plt.title("Cricket Score Comparison (India vs Australia)")
plt.xticks(score["Over"])
plt.legend()
plt.show()