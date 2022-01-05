from os import listdir
from os.path import isfile, join
import pandas as pd

mypath = "/Users/megan/Documents/4th Year/DS 4002/Week 1/gender model/crop_images"
files = [f.split("_") for f in listdir(mypath) if isfile(join(mypath, f))]

df = pd.DataFrame(files, columns = ['Age', 'Gender', 'Race', 'Time Taken'])
df2 = df.drop(["Time Taken"], axis = 1) #drop the last column as it is unneeded

<<<<<<< HEAD
#remove any rows with null values
df2 = df2.dropna()

#remove any rows with non-numeric values
df2 = df2[df2.Age.apply(lambda x: x.isnumeric())]
df2 = df2[df2.Gender.apply(lambda x: x.isnumeric())]
df2 = df2[df2.Race.apply(lambda x: x.isnumeric())]

df2["Age"] = pd.to_numeric(df2["Age"])
df2["Gender"] = pd.to_numeric(df2["Gender"])
df2["Race"] = pd.to_numeric(df2["Race"])

gendermap = {0: "Male", 1: "Female"}
racemap = {0: "White", 1: "Black", 2: "Asian", 3: "Indian", 4: "Other"}
df2 = df2.replace({"Gender": gendermap, "Race": racemap})
print(df2)

print(len(df.index)-len(df2.index), "pictures were removed from the dataset")
=======
df2 = df.loc[(df['Gender'] == '0') | (df['Gender'] == '1')]
df2.loc[:, 'Age'] = df2['Age'].astype(int)
df2 = df2.loc[(df2['Age'] >= 0) & (df2['Age'] <= 116)]

df3 = df2
bins= [0]+list(range(4,85,5))+[116]
df3['Age Range'] = pd.cut(df3['Age'], bins=bins, right=False)
>>>>>>> ece81038cde2883b6d4d1b1f2049f2156353d9ec
