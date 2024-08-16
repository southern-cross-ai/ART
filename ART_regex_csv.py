import os
import pandas as pd
import chardet
import re

directory = 'ABC'

csv_data = []

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)
        # with open(filepath, 'r') as file:
        #     content = file.read()
        with open(filepath, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
        with open(filepath, 'r', encoding=encoding) as file:
            content = file.read()  
            
            content = re.sub(r'\[.*?\]|\<.*?\>|\{.*?\}', '', content)
            content = '\n'.join(line for line in content.split('\n') if not re.match(r'^Ends \d{2}:\d{2}', line))
            csv_data.append({"content": content})


df = pd.DataFrame(csv_data)


content_csv = 'content_ABC.csv'
df.to_csv(content_csv, index=False)

print(f"Data from .txt files saved to {content_csv}")


