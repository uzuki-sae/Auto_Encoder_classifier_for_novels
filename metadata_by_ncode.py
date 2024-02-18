import requests
import json
import time
import pandas as pd
from tqdm import tqdm
from datetime import datetime, timedelta

url = "https://api.syosetu.com/novelapi/api/"
def main(url, ncode):
    payload = {"out":"json", "lim":"500", "order":"favnovelcnt", "ncode":ncode}
    try:
        r=requests.get(url, params=payload)
    except Exception as e:
        print(e)
    time.sleep(1)
    j=r.json()
    df=pd.json_normalize(j[1:])
    story=df[["ncode","title","writer","story", "keyword"]]
    story.to_csv("story.csv", encoding='utf-8', mode='a', header=False, sep=";")
    df=df.drop(columns=["gensaku", "title", "writer", "story", "keyword"])
    print(df)
    df.to_csv("all_metadata.csv", encoding='ascii',mode='a', header=False)



with open("ncode_list",'r') as f:
    ncode=f.read().splitlines()
a=0
start=0
while a < len(ncode[start:]):
    ncodes="-".join(ncode[a+start:a+start+400])
    main(url, ncodes)
    a=a+400
    print(f'to no.{a+start}, progress:{(a+start)*100//len(ncode)}%')


        


    
