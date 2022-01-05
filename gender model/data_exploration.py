from os import listdir
from os.path import isfile, join
import pandas as pd
import matplotlib.pyplot as plt

mypath = "/Users/megan/Documents/4th Year/DS 4002/Week 1/gender model/crop_images"
files = [f.split("_") for f in listdir(mypath) if isfile(join(mypath, f))]

df = pd.DataFrame(files, columns = ['Age', 'Gender', 'Race', 'Time Taken'])
df2 = df.drop(["Time Taken"], axis = 1) #drop the last column as it is unneeded

#remove any rows with null values
df2 = df2.dropna()

#remove any rows with non-numeric values
df2 = df2[df2.Age.apply(lambda x: x.isnumeric())]
df2 = df2[df2.Gender.apply(lambda x: x.isnumeric())]
df2 = df2[df2.Race.apply(lambda x: x.isnumeric())]

#convert all columns to numeric values
df2["Age"] = pd.to_numeric(df2["Age"])
df2["Gender"] = pd.to_numeric(df2["Gender"])
df2["Race"] = pd.to_numeric(df2["Race"])

print(len(df.index)-len(df2.index), "pictures were removed from the dataset")

#map numeric values to their UTK counterpart
gendermap = {0: "Male", 1: "Female"}
racemap = {0: "White", 1: "Black", 2: "Asian", 3: "Indian", 4: "Other"}
df2 = df2.replace({"Gender": gendermap, "Race": racemap})

#print a numeric summary of the age column as it is the only numeric column
print(df2.describe())

#Manual Check the Distributions
print(df2.groupby(by='Gender').agg('count'))
print(df2.groupby(by='Race').agg('count'))


#Plotting all three distributions
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.hist(df2["Age"])
ax1.set_title("Age Distribution")
ax1.set_xlabel('Ages')

ax2.bar(["Female", "Male"], df2["Gender"].value_counts())
ax2.set_title("Gender Distribution")
ax2.set_xlabel('Gender')

df2['Race'].value_counts().plot(kind='bar')
ax3.set_title("Race Distribution")
plt.show()
