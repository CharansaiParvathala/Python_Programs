import  pandas as pd
#Importing DataFrame
ds = pd.read_csv("C:\\Users\\Charansai\\Downloads\\Anime.csv")
#Return first 5 rows
print(ds.head(5))
#Return last 5 rows
print(ds.tail(5))
