import pandas as pd

df = pd.read_csv('test.csv')
print(df.isnull())  # NaN인 경우 True
print("=" * 50)
# ================================================================================================
print(df.isnull().sum())
print("=" * 50)
# ================================================================================================
df_new = df.loc[:, df.isnull().sum() == 0]
print(df_new)  # Age, Fare, Cabin 열은 제거되어 출력
print("=" * 50)
# ================================================================================================
constant = 0
df_new = df.fillna(constant)  # Nan이 있는 경우, constant로 대체
print(df_new)
