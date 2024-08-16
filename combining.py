import pandas as pd


df_commercial = pd.read_csv('content_Commercial.csv')
df_abc = pd.read_csv('content_ABC.csv')


df_combined = pd.concat([df_commercial, df_abc], ignore_index=True)

df_combined.dropna(how='all', inplace=True)

combined_csv = 'content_combined.csv'
df_combined.to_csv(combined_csv, index=False)

print(f"Combined data saved to {combined_csv}")