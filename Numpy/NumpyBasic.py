import numpy as np
#normal python list
py_list = [1,2,3,4,5,6,7,8,9]

#numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(np_array))


py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)  # 3'e 3'lük matris

print(py_multi)
print(np_multi)



