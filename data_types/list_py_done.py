# List is a collection which is ordered and changeable. Allows duplicate members.
# Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list
from collections import deque #to use list as queue

# CREATING LIST
print ('list can be created using list constructor list((1,2,3,4))')
fam = [1,2,3,4,5,6,7]
print ('A list (array) : ' + str(fam))
#GETTING TYPE OF OBJECT
print ('Type of list : ' + str(type(fam)))
#FETCHING ITEM
print ( 'Selecting item no. -1 : ' + str(fam[-1]))
#SELECTING A RANGE OF ITEM
print ('Selecting item 1 to 3 exluding 3 : '+ str(fam[1:3])) #excludes 3
#REPLACING A RANGE OF ITEMS
print ('Replacing items in the list : fam[0:3]=["cliz", 1.6, "chiz"] : ')
fam[0:3]=['cliz', 1.6, 'chiz']
print (fam)
#CONCATENATING LIST
print ('Concaneting lists  : ' + str(fam + [8,9,10,11]) )
#print (fam + [8,9,10,11])
fam.append('me')
print ('Appending item to list fam.append("me") : ' + str(fam))
#FIND THE LARGEST ITEM IN LIST
print ('Find the max value in a list max(list) : ' + str(max([9,22,1,2,4,77])))
#FIND THE SMALLEST ITEM IN LIST
print ('Find the min value in a list min(list) : ' + str(min([9,22,1,2,4,77])))
#COUNT THE NUMBER OF EXISTENCE OF AN ITEM IN LIST
print ('Find the number of occurence of an item : ' + str([1,2,1,1,3,6,5].count(1)))
#FINDING INDEX OF ITEM IN LIST
print ('Find the index of an element : ' + str([1,2,1,1,3,6,5].index(5)))
#CHECKING EXISTENCE OF ITEM IN LIST
print ('Check if item exist in list : ' + str(1 in [2,3,1,4,5]))
# FIND LENGHT OF LIST
print ("Length of the list : " + str(len([1,3,5,2,7])))
# REMOVE ITEM FROM LIST
print ("Remove item from list list.remove(el) : " + str([1,3,5].remove(1)))
# DELETE ITEM FROM 
print ('Delete item from list  del list[i]' )
# Empty the enitre list
print ('clear the entire list list.clear()')
# Creating a copy without reference
print ('Copy list without copying reference using list.copy() ')
# POP ITEMS
print ("Pop item from list : " + str([1,3,5].pop()))
# REVERSING LIST
print ('reversed list ' + str([1,2,3,4,5].reverse()))
# SORTING LIST
print ('sort the list : '+ str([1,3,4,5,2,0].sort()))
#LOOPING THROUGH LIST
for index in range(len(fam)):
    print ('look' + str(fam[index]))


#fam.extend
#fam.insert


#USING LIST AS QUEUE
#FIFO
queue = deque(["Eric", "John", "Michael"])
print (queue.append("Terry"))           # Terry arrives
print (queue.append("Graham"))          # Graham arrives
print (queue)
print (queue.popleft())                 # The first to arrive now leaves
print (queue.popleft())                 # The second to arrive now leaves
print (queue)                           # Remaining queue in order of arrival




# NESTED LISTS

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

#TRANSPOSE ROWS AND COLUMNS
print [[row[i] for row in matrix] for i in range(4)]    
#transposing using zip function 
print list(zip(matrix))