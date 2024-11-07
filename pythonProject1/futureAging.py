from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

agingPath = 'data/aging.csv'
birthPath = 'data/birthSum.csv'

agingDf = pd.read_csv(agingPath)
birthDf = pd.read_csv(birthPath, index_col='year')
agingDf['agingIndex'] = np.log1p(agingDf['agingIndex'])
agingScores = agingDf[(agingDf['Year'] >= 2014) & (agingDf['Year'] <= 2023)]['agingIndex'].tolist()

birthScores = birthDf.loc['birthSum', '2014':].tolist()

aging_arima = ARIMA(agingScores, order=(1, 1, 1))
aging_model_fit = aging_arima.fit()
aging_forecast = aging_model_fit.forecast(steps=20)

birth_arima = ARIMA(birthScores, order=(1, 1, 1))
birth_model_fit = birth_arima.fit()
birth_forecast = birth_model_fit.forecast(steps=20)

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(range(2014, 2024), agingScores, label='Observed Aging Index')
plt.plot(range(2024, 2044), aging_forecast, label='Forecasted Aging Index', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Aging Index')
plt.legend()
plt.title('Aging Index Prediction')

plt.subplot(1, 2, 2)
plt.plot(range(2014, 2024), birthScores, label='Observed Birth Sum')
plt.plot(range(2024, 2044), birth_forecast, label='Forecasted Birth Sum', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Birth Sum')
plt.legend()
plt.title('Birth Sum Prediction')

plt.tight_layout()
plt.savefig("forecastAboutAgingBirth.png", dpi=300)
plt.show()