import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

score = pd.read_csv('cricket_score.csv')

# wickets fell at these overs
india_wickets = [3, 7, 12, 17] 
australia_wickets = [2, 4, 8, 10, 11, 14, 15, 16, 19]

plt.figure(figsize=(10,5))
plt.plot(score["Over"], score["India"], linestyle='-', color='blue', label="India")
plt.plot(score["Over"], score["Australia"], linestyle='-', color='orange', label="Australia")

# Add wickets as big red and green circles using scatter
plt.scatter(india_wickets, score.loc[score["Over"].isin(india_wickets), "India"],
            color='red', s=100, label='India Wickets')

plt.scatter(australia_wickets, score.loc[score["Over"].isin(australia_wickets), "Australia"],
            color='green', s=100, label='Australia Wickets')

plt.xlabel("Over")
plt.ylabel("Runs")
plt.title("Cricket Score Comparison (India vs Australia)")
plt.xticks(score["Over"])
plt.legend()
plt.show()
