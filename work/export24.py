import json,csv,os
rows=[f['attributes'] for f in json.load(open('work/rajasthan_esri.json'))['features']]
rows=[r for r in rows if isinstance(r.get('totcrwom24'),(int,float))]
rows.sort(key=lambda r:(-r['totcrwom24'],r['dis']))
total=36563
os.makedirs('outputs',exist_ok=True)
with open('outputs/rajasthan_district_reported_crimes_2024.csv','w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f); w.writerow(['district','reported_crimes_against_women_2024','share_of_state_reported_total_percent','rape_cases_2024','cruelty_by_husband_or_relatives_2024','assault_intent_to_outrage_modesty_2024','kidnapping_abduction_women_2024','dowry_deaths_2024','sexual_harassment_2024','cyber_crimes_women_centric_2024','POCSO_girl_child_victim_cases_2024'])
 for r in rows:
  w.writerow([r['dis'],int(r['totcrwom24']),round(r['totcrwom24']/total*100,2),int(r.get('totrape24') or 0),int(r.get('crlhus24') or 0),int(r.get('totmod24') or 0),int(r.get('totkidabd24') or 0),int(r.get('dwydeath24') or 0),int(r.get('totsexh24') or 0),int(r.get('totcyit24') or 0),int(r.get('totpocso24') or 0)])
print('sum',sum(r['totcrwom24'] for r in rows))
print('top5sum share',sum(r['totcrwom24'] for r in rows[:5]),sum(r['totcrwom24'] for r in rows[:5])/total*100)
print('top10',[(r['dis'],int(r['totcrwom24']),round(r['totcrwom24']/total*100,1)) for r in rows[:10]])
print('changes',[(a,b,round((b/a-1)*100,1)) for a,b in [(40738,45058),(45058,45450),(45450,36563),(40738,36563)]])
for k in ['crlhus24','totrape24','totmod24','totkidabd24','dwydeath24','totcyit24','totpocso24','totsexh24']:
 v=sum(r.get(k) or 0 for r in rows); print(k,v,round(v/total*100,1))
