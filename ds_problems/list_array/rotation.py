# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
# in -> 1, 2, 3, 4, 5, 6, 7
# rotated by 2 elements
# out -> 3, 4, 5, 6, 7, 1, 2
import time

# MY RECURSIVE
test_list_rec=[1,2,3,4,5,6,7]
def recur_rotate(in_list, rotate_by, list_size):
    start = time.time()
    print ('Input Array : ' + str(in_list) )

recur_rotate(test_list_rec,2,len(test_list_rec))




# MY ITERATIVE
test_list= [1 , 2, 3, 4, 5, 6, 7]
def iter_rotate( in_list , rotate_by, list_size):
    start = time.time()
    print ('Input Array : ' + str(in_list) )
    for i in range(rotate_by):
        in_list.append(in_list[i])
    while len(in_list) >list_size:
        del in_list[0]
    print('Output Array : ' + str(in_list))
    end = time.time()
    print('Time taken : ' + str(end - start))

iter_rotate(test_list, 2 ,len(test_list))
