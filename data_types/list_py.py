# lists
# List is a collection which is ordered and changeable. Allows duplicate members.
print ('------------------ Lists -------------------')
fam = [1,2,3,4,5,6,7]
print ('A list (array) : ' + str(fam))
print ('Type of list : ' + str(type(fam)))
print ( 'Selecting item no. -1 : ' + str(fam[-1]))
print ('Selecting item 1 to 3 exluding 3 : '+ str(fam[1:3])) #excludes 3
print ('Replacing items in the list : fam[0:3]=["cliz", 1.6, "chiz"] : ')
fam[0:3]=['cliz', 1.6, 'chiz']
print (fam)
print ('Concaneting lists  : ' + str(fam + [8,9,10,11]) )
#print (fam + [8,9,10,11])
fam.append('me')
print ('Appending item to list fam.append("me") : ' + str(fam))
print ('Find the max value in a list max(list) : ' + str(max([9,22,1,2,4,77])))
print ('Find the min value in a list min(list) : ' + str(min([9,22,1,2,4,77])))
print ('Find the number of occurence of an item : ' + str([1,2,1,1,3,6,5].count(1)))
print ('Find the index of an element : ' + str([1,2,1,1,3,6,5].index(5)))
print ('Check if item exist in list : ' + str(1 in [2,3,1,4,5]))
print ("Length of the list : " + str(len([1,3,5,2,7])))
print ("Remove item from list list.remove(el) : " + str([1,3,5].remove(1)))
print ('Delete item from list  del list[i]' )
print ('clear the entire list list.clear()')
print ('Copy list without copying reference using list.copy() ')
print ("Pop item from list : " + str([1,3,5].pop()))
print ('list can be created using list constructor list((1,2,3,4))')
print ('reversed list ' + str([1,2,3,4,5].reverse()))
print ('sort the list : '+ str([1,3,4,5,2,0].sort()))


for index in range(len(fam)):
    print ('look' + str(fam[index]))


