import pandas as pd


df_commercial = pd.read_csv('contentCommercial.csv')
df_abc = pd.read_csv('contentABC.csv')


df_combined = pd.concat([df_commercial, df_abc], ignore_index=True)

df_combined.dropna(how='all', inplace=True)

combined_csv = 'combined_content.csv'
df_combined.to_csv(combined_csv, index=False)

print(f"Combined data saved to {combined_csv}")