
print ('------------------ Dicts -------------------')
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
dict_ministers= {'pm': 'Modi', 'hm':'Singh', 'dm':'Sitharaman' }
print (dict_ministers['pm'])
print (dict_ministers['hrd'])
del(dict_ministers['pm'] )
print  dict_ministers
print dict_ministers.keys()
print dict_ministers.values()
print sorted(dict_ministers.keys())
for key in dict_ministers:
    print dict_ministers[key]


