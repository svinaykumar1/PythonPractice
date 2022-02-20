import pandas as pd

df=pd.read_csv(r'C:\Users\visiripu\Desktop\Desktop_2020605\PythonCodes\Titanic\test.csv')

#print(df.head(),df.describe(),df.count())
print(df.columns)

print(df)

print(df.describe())

print(df[['Age','Sex']])
print(df[['Age','Sex','Pclass']][df['Pclass']==2].max())



#print(df['Age'][df.Pclass==2].max(),df['Age'][df.Pclass==2].min())
#print(df['Age'][df.Pclass==2][df.Sex=="female"].max(),df['Age'][df.Pclass==2][df.Sex=="female"].min())

#print(df.groupby(['Pclass'])[["PassengerId","Name"]].min(),df.groupby(['Pclass','Sex','Embarked'])[["PassengerId","Age","Fare"]].max())
#print(df[df.Age>40])

#print(df['Pclass'].agg(['sum','mean']))


dict1={ "date":['1/1/2020','2/2/2021','12/31/2021'],
        "location":['Area1','Area2','Area3'],
        "Temp":[30,50,70]
        }

df2=pd.DataFrame(dict1)

#print(df2)
#df2.set_index('location',inplace=True)
#print(df2.loc['Area2'])