import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

totalFareForStuPath = 'data/totalFareForStudent.csv'
birthSumPath = 'data/birthSum.csv'
femaleParticipationPath = 'data/womenEco.csv'

birthSumDf = pd.read_csv(birthSumPath, index_col='year')
totalFareForStuDf = pd.read_csv(totalFareForStuPath, index_col='year')
femaleParticipationDf = pd.read_csv(femaleParticipationPath, index_col='year')

femaleParticipationDf.columns = femaleParticipationDf.columns.str.strip()



plt.subplot(3, 1, 2)
plt.plot(birthSumDf.columns, birthSumDf.iloc[0], marker='o', linestyle='-', color='red', label='Birth')
plt.title("Birth Sum Rate Over Years")
plt.xlabel("Year")
plt.ylabel("Birth Sum Rate")

plt.subplot(3, 1, 3)
plt.plot(femaleParticipationDf.columns, femaleParticipationDf.iloc[2], marker='o', linestyle='-', color='green')
plt.title("Female Economic Participation Rate Over Years")
plt.xlabel("Year")
plt.ylabel("Participation Rate (%)")

plt.tight_layout()
plt.savefig("correlationGraph.png", dpi=300)
plt.show()