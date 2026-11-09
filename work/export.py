import json,csv,os
rows=[f['attributes'] for f in json.load(open('work/rajasthan_esri.json'))['features']]
rows=[r for r in rows if isinstance(r.get('totipcsll23'),(int,float))]
rows.sort(key=lambda r:(-r['totipcsll23'],r['dis']))
os.makedirs('outputs',exist_ok=True)
with open('outputs/rajasthan_district_reported_crimes_2023.csv','w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f); w.writerow(['district','reported_crimes_against_women_2023','share_of_state_reported_total_percent','rape_cases_2023','cruelty_by_husband_or_relatives_2023','assault_intent_to_outrage_modesty_2023','kidnapping_abduction_women_2023','dowry_deaths_2023'])
 for r in rows:
  w.writerow([r['dis'],int(r['totipcsll23']),round(r['totipcsll23']/45450*100,2),int(r.get('totrape23') or 0),int(r.get('crlhus23') or 0),int(r.get('totmod23') or 0),int(r.get('totkidabd23') or 0),int(r.get('dwydeath23') or 0)])
print('top5sum',sum(r['totipcsll23'] for r in rows[:5]), 'share',sum(r['totipcsll23'] for r in rows[:5])/45450*100)
print('pct increase 21to23',(45450/40738-1)*100,'22to23',(45450/45058-1)*100)
print('counts list',[(r['dis'],int(r['totipcsll23'])) for r in rows[:10]])
