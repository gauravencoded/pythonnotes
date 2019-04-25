import numpy as np

height =[1.78, 1.89, 1.56, 1.98]
weight =[70, 85, 69, 89]

np_height=np.array(height)
np_weight=np.array(weight)
print type(np_height)



bmi=np_weight/np_height ** 2
print bmi

#concats two arrays
print height + weight

#this adds values rather than concatenating arrays
print np_height + np_weight

# compares each value in array with a value
print bmi >23

np_2d=np.array([
    [1,2,3,4,5,6,7,8,2,1],
    [10,12,13,14,15,16,17,18,3,2]
])

print np_2d
print np_2d.shape
print type(np_2d)
print np_2d[0]
print  np_2d[0,2]


print np.mean(np_2d[0])
print np.median(np_2d[0])
print np.std(np_2d[0])
print np.corrcoef(np_2d[0])

print np.sum(np_2d[0])
print np.sort(np_2d[0])