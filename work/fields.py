import json
x=json.load(open('work_layer.json'))
for f in x['fields']:
 if f['name'].endswith('23') and f['name'] not in ['objectid']: print(f['name'],'|',f.get('alias'))
