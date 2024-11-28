import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression

agingPath = 'data/aging.csv'
birthPath = 'data/birthSum.csv'

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
plt.savefig("agingGraph.png", dpi=300)

plt.show()

agingScores = agingDf[(agingDf['Year'] >= 2014) & (agingDf['Year'] <= 2023)]['agingIndex'].tolist()

birthScores = birthDf.loc['birthSum', '2014':].tolist()

corrData = {'aging': agingScores, 'birth': birthScores}
corrDf = pd.DataFrame(corrData)

corrResult = corrDf.corr(method='pearson')
print(corrResult)

# 공통 연도 추출
agingDf['Year'] = agingDf['Year'].astype(str)  # 연도를 문자열로 변환
common_years = birthDf.columns.intersection(agingDf['Year'])
print("Common years:", common_years)

# 데이터 서브셋 생성
birthSubset = birthDf.loc['birthSum', common_years]
agingSubset = agingDf[agingDf['Year'].isin(common_years)].set_index('Year')['agingIndex']

# 데이터 병합
sumDf = pd.concat([birthSubset, agingSubset], axis=1).dropna()
sumDf.columns = ['birthSum', 'agingIndex']

# 병합 결과 확인
print("Merged DataFrame:\n", sumDf)

fit = ols('birthSum ~ agingIndex', data=sumDf).fit()
print(fit.summary())