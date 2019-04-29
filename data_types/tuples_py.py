# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking
# You can not add item to tuple later after creation
# You can not remove item from tuple
# Del can delete entire tuple completely

# CREATING TUPLE 
print ('Constructing a tuple using its constructor : ' + str(tuple(('man' , 'animal' , 'insect'))))
thistuple = ("apple", "banana", "cherry")
print('Accessing item from tuple : ' + thistuple[2])
# CHECK IF ITEM EXIST
print ('Check if item exist in tuple : '+ str('apple' in thistuple))
# FIND THE LENGTH OF ITEM
print ('Length of the tuple : '+ str(len(thistuple)))
# COUNT THE NUMBER OF ITEMS IN TUPLE
print ('Counting the number of occurence of an item in the tuple : ' + str(thistuple.count('apple')))
# FIND THE INDEX OF ITEM
print ('Find the index of an item in the tuple : ' + str(thistuple.index('apple')) )

# WHERE TO USE TUPLES?