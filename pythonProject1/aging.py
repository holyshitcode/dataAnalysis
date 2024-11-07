import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

# agingDf와 birthDf의 공통 연도에 맞는 데이터 선택
agingScores = agingDf[(agingDf['Year'] >= 2014) & (agingDf['Year'] <= 2023)]['agingIndex'].tolist()

# birthDf에서 2014년 이후 데이터만 선택하여 리스트로 변환
birthScores = birthDf.loc['birthSum', '2014':].tolist()

# 상관관계 분석 데이터프레임 생성
corrData = {'aging': agingScores, 'birth': birthScores}
corrDf = pd.DataFrame(corrData)

# 피어슨 상관계수 계산
corrResult = corrDf.corr(method='pearson')
print(corrResult)