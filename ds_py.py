# dictionary is just like js object
# no duplicate keys

dict_ministers= {'pm': 'Modi', 'hm':'Singh', 'dm':'Sitharaman' }

print dict_ministers['pm']

print dict_ministers['hrd']

del(dict_ministers['pm'] )
print  dict_ministers
print dict_ministers.keys()
print dict_ministers.values()
print sorted(dict_ministers.keys())
for key in dict_ministers:
    print dict_ministers[key]


#sets
#unordered collection , no duplicate values, 

new_set={'modi', 'godi', 'lodi', 'bodi'}
subset ={'modi', 'godi'}
not_subset={'gandhi', 'nehru'}

print modi in new_set
print godi not in new_set
print new_set.isdisjoint(subset) #empty intersetion
print subset <= new_set #subset test
#proper subset is 
print subset < new_set #proper subset test
print new_set > subset #superset
print subset & not_subset #intersection
print subset | not_subset #union
print new_set - subset #set difference


