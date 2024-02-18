import pandas as pd
import numpy as np

#with open("ncodes_0929", "r") as l:
#    ncodes=l.read().splitlines()
df=pd.read_csv("toukei/all_metadata.csv")
#df=df[df["ncode"].isin(ncodes)]
#df=df[(df["all_hyoka_cnt"] > 512) & (df["fav_novel_cnt"] >512) & (df['length'] > 144*50)]
df=df[(df["all_point"] > 17)]
df["general_firstup"]=pd.to_datetime(df["general_firstup_date"])
df["general_firstup"]=df["general_firstup"].apply(lambda t: int(t.timestamp()))
df["general_lastup"]=pd.to_datetime(df["general_lastup_date"])
df["general_lastup"]=df["general_lastup"].apply(lambda t: int(t.timestamp()))
df["logH/B"]=np.log((df["all_hyoka_cnt"])/(df["fav_novel_cnt"]))
df["logH/B"]=(df["logH/B"]-df["logH/B"].mean())/df["logH/B"].std()
df["P"]=((df["all_point"])/(df["all_hyoka_cnt"]))**2
df["P"]=(df["P"]-df["P"].mean())/df["P"].std()
df["novel_type"]=df["novel_type"]-1
df["novel_type"]=df["novel_type"].astype(bool)
df["end"]=df["end"].astype(bool)

df=df.sort_values('all_point', ascending=False).head(8192)
print(df['all_point'], len(df))
d=df.loc[:,["ncode", "biggenre", "general_firstup", "general_lastup", "novel_type", "end", "logH/B", "P"]]

d=pd.get_dummies(d, columns=["biggenre"])
d=d.reset_index(drop=True)
describe=df.describe()
describe.to_csv("toukei/describe_HighPoint.csv")
d.to_csv("toukei/HighPoint.csv")
ncodes=np.array(df["ncode"],dtype=str).tolist()
with open("ncodes_HighPoint.txt", "w") as f:
    f.write("\n".join(ncodes))

