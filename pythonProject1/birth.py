import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
totalFareForStuPath = 'data/totalFareForStudent.csv'
birthSumPath = 'data/birthSum.csv'

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
plt.savefig("birthGraph.png", dpi=300)

plt.show()


print(birthSumDf)


# totalFareForStuDf의 인덱스를 문자열로 변환
totalFareForStuPathDf.index = totalFareForStuPathDf.index.astype(str)

# 공통 연도 추출
common_years = birthSumDf.columns.intersection(totalFareForStuPathDf.index)
print("Common years:", common_years)

# 데이터 서브셋 생성
birthSumSubset = birthSumDf.loc['birthSum', common_years].astype(float)
totalFareSubset = totalFareForStuPathDf.loc[common_years, 'total'].astype(float)

# 데이터 병합
mergedDf = pd.DataFrame({
    'birthSum': birthSumSubset.values,
    'totalFare': totalFareSubset.values
}, index=common_years)

print(mergedDf)

coef = mergedDf.corr(method='pearson')
print(coef)

fit = ols('birthSum ~ totalFare', data=mergedDf).fit()
print(fit.summary())


