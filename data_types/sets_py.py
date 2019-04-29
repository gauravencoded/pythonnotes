# Set is a collection which is unordered and unindexed. 
# No duplicate members.
# Basic uses include membership testing and eliminating duplicate entries. 
# Support operations like union, intersection, difference, and symmetric difference.
# Curly braces or the set() function can be used to create sets. 
# Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary.
# There are currently two built-in set types, set and frozenset. 
# The set type is mutable — the contents can be changed using methods like add() and remove(). 
# Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set. 
# The frozenset type is immutable and hashable — its contents cannot be altered after it is created; 
# it can therefore be used as a dictionary key or as an element of another set.


# CREATING SETS
new_set={'modi', 'godi', 'lodi', 'bodi'}
subset ={'modi', 'godi'}
not_subset={'gandhi', 'nehru'}

# check if item exist in set
print ('Check for existence : ' + str('modi' in new_set))
# check if item is not in set
print ('Check for non-existence : ' + str('godi' not in new_set))
# FIND THE LENGTH OF SET
print ("Length of set : " +  str(len(new_set)))
# Sets are disjoint if and only if their intersection is the empty set.
print ('CHECK IF TWO SETS ARE DISJOINT : ' + str(new_set.isdisjoint(subset)) )
# SUBSET CHECK
issubset(other)
print ('CHECK IF SET IS SUBSET : ' + str(subset <= new_set)) #subset test
#proper subset check

print (' CHECK IF SET IS PROPER SUBSET : ' + str(subset < new_set)) #proper subset test
# Test whether the set is a proper superset of other
issuperset(other)
print ('CHECK IF SET IS SUPERSET : ' + str(new_set > subset) )#superset
# intersection
print ('Intersection of two sets: ' + str(subset & not_subset) )#intersection
print ('Union of two sets : ' + str(subset | not_subset)) #union
# Return a new set with elements in the set that are not in the others.
print ('Difference of tqo sets : ' + str(new_set - subset)) #set difference




# UPDATING SETS
set ^ other
Return a new set with elements in either the set or other but not both.

update(*others)
set |= other | ...
Update the set, adding elements from all others.

intersection_update(*others)
set &= other & ...
Update the set, keeping only elements found in it and all others.

difference_update(*others)¶
Update the set, removing elements found in others.
set -= other

symmetric_difference_update(other)
# Update the set, keeping only elements found in either set, but not in both.
set ^= other
# add()
# clear()
# discard()
# remove()
#pop()
#copy()¶
#Return a shallow copy of the set.


#why use sets