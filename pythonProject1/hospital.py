import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob

# CSV 파일 경로 가져오기
file_paths = glob.glob('data/hospitalInfo/*.csv')

# 각 연도별 파일 읽기
hosInfo2021 = pd.read_csv(file_paths[0])
hosInfo2022 = pd.read_csv(file_paths[1])
hosInfo2023 = pd.read_csv(file_paths[2])
hosInfo2024 = pd.read_csv(file_paths[3])


# '소아' 포함 여부 카운트 함수 정의
def count_contains_keyword(df, keyword="소아"):
    contains_count = df['요양기관명'].str.contains(keyword, na=False).sum()
    not_contains_count = len(df) - contains_count
    return contains_count, not_contains_count


# 연도별 '소아' 포함 데이터 개수와 전체 데이터 개수 가져오기
counts_2021 = count_contains_keyword(hosInfo2021)
counts_2022 = count_contains_keyword(hosInfo2022)
counts_2023 = count_contains_keyword(hosInfo2023)
counts_2024 = count_contains_keyword(hosInfo2024)

# 파이 차트 시각화
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
years = [2021, 2022, 2023, 2024]
data_counts = [counts_2021, counts_2022, counts_2023, counts_2024]


def absolute_values(pct, allvals):
    absolute = int(pct / 100. * np.sum(allvals))
    return f"{absolute}"


for ax, year, counts in zip(axes.flatten(), years, data_counts):
    labels = ['Contains Child', 'Does Not Contain Child']
    ax.pie(counts, labels=labels,autopct=lambda pct: absolute_values(pct, counts), startangle=140)
    ax.set_title(f'{year} Child Hospital')

plt.suptitle("percent of child hospital")
plt.tight_layout()
plt.savefig("hospitalGraph.png", dpi=300)

plt.show()

print(data_counts)
