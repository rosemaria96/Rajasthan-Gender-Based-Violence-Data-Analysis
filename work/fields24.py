import json
x=json.load(open('work_layer.json'))
for f in x['fields']:
 if f['name'].endswith('24') and f['name']!='objectid': print(f['name'],'|',f.get('alias'))
