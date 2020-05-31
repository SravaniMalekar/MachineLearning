#importing required libraries
import pandas as pd
import matplotlib.pyplot as plt

url1="https://gist.githubusercontent.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv"

df=pd.read_csv(url1,delimiter=',')#Reads data from the url removing ','
df.to_csv('Movie.csv')#Writing the data into a new csv file

df0=df['Year'][2:100]
df1=df['Profitability'][2:100]
print(df0)
print(df1)
#Drawing bargraph of the data
plt.bar(df1,df0)
#Command to show the graph
plt.show()
