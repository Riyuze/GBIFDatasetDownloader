import pandas as pd

# Reads multimedia.txt file
df = pd.read_csv('multimedia.txt', delimiter = "\t")

# Gets the urls for the images
df_new = df['identifier'].tolist()

# Outputs a CSV file containing the URLS
with open("Urls.csv", "w", encoding="utf-8") as output:
    for data in df_new:
        output.write(str(data)+',')