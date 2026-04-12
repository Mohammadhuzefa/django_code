import json

python_data={'active1':True,
        'active2':False,
        'active3':None}

print(python_data)
print(type(python_data))

json_data=json.dumps(python_data)
print(json_data)
print(type(json_data))

python_data2=json.loads(json_data)
print(python_data2)
print(type(python_data2))

