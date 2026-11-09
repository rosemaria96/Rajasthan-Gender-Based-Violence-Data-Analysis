import urllib.parse, urllib.request, json
base='https://livingatlas.esri.in/server1/rest/services/NCRB/District_Wise_Crime_Against_Women_2022/MapServer/0/query'
params={'where':"state='Rajasthan'",'outFields':'*','returnGeometry':'false','f':'json'}
u=base+'?'+urllib.parse.urlencode(params)
data=json.load(urllib.request.urlopen(u))
print('features',len(data.get('features',[])), 'error',data.get('error'))
for f in data.get('features',[])[:3]:
 a=f['attributes']; print(a.get('dis'),a.get('state'),a.get('totipcsll22'),a.get('totipcsll24'))
open('work/rajasthan_esri.json','w').write(json.dumps(data))
