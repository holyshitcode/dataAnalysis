import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

agingPath = '/Users/junyeong/DataScienceProject/pythonProject1/.venv/data/aging.csv'
birthPath = '/Users/junyeong/DataScienceProject/pythonProject1/.venv/data/birthSum.csv'

agingDf = pd.read_csv(agingPath)
birthDf = pd.read_csv(birthPath, index_col='year')

print(agingDf.head(3))
print(birthDf.head(3))

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(agingDf['Year'], agingDf['agingIndex'], label='Aging Index')
plt.xlabel('Year')
plt.ylabel('Aging Index')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(birthDf.columns, birthDf.iloc[0].values, label='Birth Sum')
plt.xlabel('Year')
plt.ylabel('Birth Sum')
plt.legend()

plt.tight_layout()
plt.subplots_adjust(wspace=0.3)
plt.show()