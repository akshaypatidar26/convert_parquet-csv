import pandas as pd
import glob
import os 

 path = glob.glob(folder_path+'/*.parquet')  # Enter folder path as string
df = pd.read_parquet(path[0], engine='pyarrow')
for i in range(1,len(path)):
    df1 = pd.read_parquet(path[i], engine='pyarrow')
    df  = pd.concat([df,df1],axis = 0)
    print(len(df))
df.to_csv("fileName.csv") # add fileName
