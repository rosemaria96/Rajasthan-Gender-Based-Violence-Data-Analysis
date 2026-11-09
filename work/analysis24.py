import json
rows=[f['attributes'] for f in json.load(open('work/rajasthan_esri.json'))['features']]
rows=[r for r in rows if isinstance(r.get('totcrwom24'),(int,float))]
print('count',len(rows),'sum_total',sum(r['totcrwom24'] for r in rows),'sum IPC',sum(r.get('totipcbns24') or 0 for r in rows),'sll',sum(r.get('totsllcr24') or 0 for r in rows))
print('top10',[(r['dis'],int(r['totcrwom24'])) for r in sorted(rows,key=lambda r:-r['totcrwom24'])[:10]])
print('bottom5',[(r['dis'],int(r['totcrwom24'])) for r in sorted(rows,key=lambda r:r['totcrwom24'])[:5]])
for key in ['crlhus24','totrape24','totmod24','totkidabd24','dwydeath24','totcyit24','totpocso24','prtdomvi24','tottrfc24','totsexh24','totsllcr24','totipcbns24']:
 print(key,sum(r.get(key) or 0 for r in rows))
print('rape women/girls',sum(r.get('w18y_24') or 0 for r in rows),sum(r.get('grl18y_24') or 0 for r in rows),sum(r.get('totrape24') or 0 for r in rows))
