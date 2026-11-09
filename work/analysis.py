import json
rows=[f['attributes'] for f in json.load(open('work/rajasthan_esri.json'))['features']]
rows=[r for r in rows if isinstance(r.get('totipcsll23'),(int,float))]
print('n',len(rows),'total',sum(r['totipcsll23'] for r in rows))
for key in ['crlhus23','totrape23','totkidabd23','dwydeath23','totmod23','totpocso23','totcyit23','prtdomvi23','abtsui23','dwyph23']:
 vals=[r.get(key) or 0 for r in rows]; print(key,sum(vals))
print('jaipur',[(r['dis'],r['totipcsll23']) for r in rows if r['dis']=='Jaipur'])
print('top10',[(r['dis'],r['totipcsll23']) for r in sorted(rows,key=lambda r:-r['totipcsll23'])[:10]])
print('bottom5',[(r['dis'],r['totipcsll23']) for r in sorted(rows,key=lambda r:r['totipcsll23'])[:5]])
print('rape women/girls',sum(r.get('w18y_23') or 0 for r in rows),sum(r.get('grl18y_23') or 0 for r in rows),sum(r.get('totrape23') or 0 for r in rows))
