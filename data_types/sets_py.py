
#sets
print '------------------ Sets -------------------'
# Set is a collection which is unordered and unindexed. No duplicate members.

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

