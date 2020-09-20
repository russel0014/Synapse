import json

with open('data2.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}

p=data['data']
with open('fulldata.json', 'w') as json_file:

    json.dump(p, json_file)
    
d={}
l=[]

   
for item in p:  # my_list if the list that you have in your question
    del item['session_id']
    del item['device']
    del item['location']['latitude']
    del item['location']['longitude']

    del item['location']['zip_code'] 
    del item['location']['city']

for x in p:
   y=x['location']
   l=l+[y]
  
print(l)  



with open('state.json', 'w') as json_file:

    json.dump(l, json_file)