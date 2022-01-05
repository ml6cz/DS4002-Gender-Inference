from os import listdir
from os.path import isfile, join
import pandas as pd

mypath = "/Users/megan/Documents/4th Year/DS 4002/Week 1/gender model/crop_images"
files = [f.split("_") for f in listdir(mypath) if isfile(join(mypath, f))]

df = pd.DataFrame(files, columns = ['Age', 'Gender', 'Race', 'Time Taken'])
print(df)

df2 = df.loc[(df['Gender'] == '0') | (df['Gender'] == '1')]
df2.loc[:, 'Age'] = df2['Age'].astype(int)
df2 = df2.loc[(df2['Age'] >= 0) & (df2['Age'] <= 116)]
