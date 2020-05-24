import json

fvar=open(r'c:/Temp/servers.json', 'r')
data=fvar.readlines()
fvar.close()
jsonfile=json.dumps(data)
with open(r'c:/temp/data.txt',"w") as f:
    f.write(data)
