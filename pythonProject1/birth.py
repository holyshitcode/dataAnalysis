import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
totalFareForStuPath = '/Users/junyeong/DataScienceProject/pythonProject1/.venv/data/totalFareForStudent.csv'
birthSumPath = '/Users/junyeong/DataScienceProject/pythonProject1/.venv/data/birthSum.csv'

birthSumDf = pd.read_csv(birthSumPath,index_col='year')
totalFareForStuPathDf = pd.read_csv(totalFareForStuPath,index_col='year')

plt.subplot(3, 1, 1)
plt.plot(totalFareForStuPathDf.index, totalFareForStuPathDf['total'], marker='o', linestyle='-', color='blue')
plt.title("Total Fare for Students Over Years")
plt.xlabel("Year")
plt.ylabel("Total Fare")

plt.subplot(3, 1, 2)
plt.plot(birthSumDf.columns, birthSumDf.iloc[0], marker='o', linestyle='-', color='red')
plt.title("Birth Sum Rate Over Years")
plt.xlabel("Year")
plt.ylabel("Birth Sum Rate")

plt.tight_layout()

plt.show()


print(birthSumDf)
