import pandas as pd
import matplotlib.pyplot as plt
gniPath = 'data/ecoGrowth.csv'
birthPath = 'data/birthSum.csv'


gniDf = pd.read_csv(gniPath)
birthDf = pd.read_csv(birthPath, index_col='year')

plt.subplot(1,2,1)
plt.plot(gniDf.columns,gniDf.loc[0],label='EcoGrowth')
plt.xticks(rotation=45, fontsize=8)
plt.xlabel('Year', fontsize=8)
plt.ylabel('EcoGrowth', fontsize=8)
plt.legend()

plt.subplot(1,2,2)
plt.plot(birthDf.columns, birthDf.iloc[0], marker='o', linestyle='-', color='red', label='Birth')
plt.xticks(rotation=45, fontsize=8)
plt.xlabel('Year')
plt.ylabel('Birth Sum')
plt.legend()

plt.tight_layout()
plt.savefig("gniGraph.png", dpi=300)
plt.show()