from QRCodeScanner import decode_qr as dqr
import json
import pandas as pd
data=(dqr()).decode("utf-8") #byte to string

data=data.replace("'", '"')
data=json.loads(data)  #string to dictionary

df=pd.read_excel('car details.xlsx',sheet_name=data.get("wheel_number"))

print(data)
print(data['Registration Number'])
for it in df['Registration Number']:
    if it==data['Registration Number']:
        print("Already Exists")
        break
    else:
        df.loc[len(df)] = data
        df.to_excel('car details.xlsx',index=False,sheet_name=data.get("wheel_number"))
        print("Added")
        break

