import pandas as pd
df=pd.read_csv(r"/Users/amananku/Desktop/lab_04.csv")
# print(df)
#cleaning the empty or void data rows from the data_frame
a=df.dropna()
print(a)
a=df.fillna(5)
print(a)