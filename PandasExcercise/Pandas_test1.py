import pandas as pd
import numpy as np

df=pd.read_csv(r'C:\Users\visiripu\Desktop\Desktop_2020605\PythonCodes\Titanic\train.csv')
print(df)

print(df[['PassengerId','Pclass','Cabin']])