import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the score data
score = pd.read_csv('cricket_score.csv')

# Wickets fell at these overs
india_wickets = [3, 7, 12, 17] 
australia_wickets = [2, 4, 8, 10, 11, 14, 15, 16, 19]

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(score["Over"], score["India"], linestyle='-', color='blue', linewidth=2, label="India")
plt.plot(score["Over"], score["Australia"], linestyle='-', color='orange', linewidth=2, label="Australia")

# Add wickets as large circles
plt.scatter(india_wickets, score.loc[score["Over"].isin(india_wickets), "India"],
            color='red', s=120, edgecolor='black', label='India Wickets', zorder=5)

plt.scatter(australia_wickets, score.loc[score["Over"].isin(australia_wickets), "Australia"],
            color='green', s=120, edgecolor='black', label='Australia Wickets', zorder=5)

# Add grid and labels
plt.xlabel("Over", fontsize=12)
plt.ylabel("Runs", fontsize=12)
plt.title("Cricket Score Comparison: India vs Australia", fontsize=14, fontweight='bold')
plt.xticks(score["Over"])
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
