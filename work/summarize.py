import json
x=json.load(open('work/rajasthan_esri.json'))
rows=[f['attributes'] for f in x['features']]
for yr,key in [('2022','totipcsll22'),('2023','totipcsll23')]:
 vals=[r for r in rows if isinstance(r.get(key),(int,float))]
 print(yr,'n',len(vals),'sum',sum(r[key] for r in vals))
 print(sorted([(r['dis'],r[key]) for r in vals],key=lambda z:-z[1])[:10])
print('rows',[(r['dis'],r.get('totipcsll22'),r.get('totipcsll23')) for r in rows if r.get('totipcsll22') is None][:20])
