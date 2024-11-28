import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

gniPath = 'data/ecoGrowth.csv'
birthPath = 'data/birthSum.csv'


gniDf = pd.read_csv(gniPath,index_col=0)
birthDf = pd.read_csv(birthPath, index_col='year')

plt.subplot(1,2,1)
plt.plot(gniDf.index, gniDf['gniPerCapital'], label='EcoGrowth', marker='o', color='blue')
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

# 인덱스와 컬럼의 형식 통일
gniDf.index = gniDf.index.astype(str)  # 문자열로 변환
birthDf.columns = birthDf.columns.astype(str)  # 문자열로 변환

# 공통 연도 추출
common_years = gniDf.index.intersection(birthDf.columns)
print("Common years:", common_years)

# 데이터 서브셋 생성
gniSubset = gniDf.loc[common_years, 'gniPerCapital'].astype(float)
birthSubset = birthDf.loc['birthSum', common_years].astype(float)

# 데이터 병합
mergedDf = pd.DataFrame({
    'EcoGrowth': gniSubset.values,
    'BirthSum': birthSubset.values
}, index=common_years)

coef = mergedDf.corr(method='pearson')
print(coef)

fit = ols('EcoGrowth ~ BirthSum', data=mergedDf).fit()
print(fit.summary())