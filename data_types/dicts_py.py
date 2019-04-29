# Dictionary is a collection which is unordered.
# INDEXED
# MUTABLE
# NO DUPLICATES
# A mapping object maps hashable values to arbitrary objects. Mappings are mutable objects. There is currently only one standard mapping type, the dictionary





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


