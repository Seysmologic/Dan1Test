import numpy as np
import pandas


list1 = [[1,2,3, 4], [5, 6, 7, 8]]
arr = np.array([[1,2,3, 4], [5, 6, 7, 8]])
print(list1, list1.__sizeof__(), end = '\n\n')
print(arr, arr.size)


# Vector - one dim array
vector = np.array([1,2,3,4,5])
print('Vector', vector, vector.shape)
print('Vector', vector.reshape(-1,1),vector.reshape(-1,1).shape)


# Matrix - two dim array, n * m - table , rows * columns = mat
arr = np.array([[1,2,3, 4], [5, 6, 7, 8]])
print(f'Array: {arr}\nShape: {arr.shape}', end = '\n\n')

# Квадратая матрица - row = column , 2x2, 3x3, 4x4, etc rows = columns
arr1 = np.array([[1,2], [5, 6]])
print(f'Array: {arr1}\nShape: {arr1.shape}')


# Zeros - create zero array
zero = np.zeros(5)
print(zero)
zero_2d = np.zeros((2, 5)) # arg - tuple, where first arg - row, second - column
print(zero_2d)
zero_3d = np.zeros((2, 5, 2)) # arg - tuple, where first arg - row, second - column
print(zero_3d)

# Ones - create one-value matrix
arr = np.ones((3,4)) # tuple: [0] - row, [1] - columns
print(arr, arr.shape)

# Arange - generate vector
arr = np.arange(1, 13)
print(arr, arr.shape)

arr1 = np.arange(1, 13).reshape(3,4) # 2d - matrix
print(arr1, arr1.shape)


# Linspace - рівномірний розподіл
arr = np.linspace(0, 1, 10) # three arg - start, end, count of values
print(arr)

arr_bool = np.array([True, False, True, False, False])
print(arr_bool) # Bool

arr_float = np.array([True, 3.14, 1, 15, False])
print(arr_float) # float

arr_string = np.array(['String', 3.14, 15, False, True])
print(arr_string) # when cast type, take biggest data type


# to create with dtype, use dtype
arr_uint8 = np.arange(1, 10, dtype= np.uint8) # unsig type
print(arr_uint8, arr_uint8.dtype)

arr_float32 = np.array([1,2,3,4, 5.14, False, True, -17], dtype= np.float32)
print(arr_float32, arr_float32.dtype)


# Astype - convert data type
arr1 = np.array([9, 12, True, 3.13]).astype('<U5')
arr2 = np.array([9, 12, True, 3.13, 'Numpy'])
arr3 = np.array([9, 12, True, 3.13]).astype(np.int16)
arr4 = np.array([9, 12, True, 3.13]).astype(np.int64)
arr5 = np.random.random((3,4))
arr6 = np.array([[1,2,3], [4,5,6.0], [7, 8, 9]])

for i in range(1, 7):
    print(eval(f'arr{i}'))
    print(eval(f'arr{i}.dtype'), end = '\n\n') # <U - unicode with len



# Vector math
x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])
print(f'Add: {x1 + x2} or {np.add(x1, x2)}')
print(f'Subtract: {x1 - x2} or {np.subtract(x1, x2)}')
print(f'Multiply: {x1 * x2} or {np.multiply(x1, x2)}')
print(f'Divide: {x1 / x2} or {np.divide(x1, x2)}')
print(f'Dot: {np.dot(x1, x2)}')


arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12]])

even_number = arr % 2 == 0 # Arr true/false
print(even_number, arr[even_number], end = '\n\n')

big_mean = arr > arr.mean()
print(big_mean, arr[big_mean], end = '\n\n')


two_statemnt = (arr > 2) & (arr < 10)
print(two_statemnt, arr[two_statemnt], end = '\n\n')

two_statemnt = (arr > 2) | (arr == 10)
print(two_statemnt, arr[two_statemnt], end = '\n\n')

print(arr[arr % 2 == 0]) # or you write in []


print(arr)
print(np.where(arr == 4)) # return position(index)
print(np.where(arr % 2 == 0))


print(arr)
print(np.where(arr % 2 == 0,arr, -1)) # three args: condit, array, default value

arr = np.array([[1,2,3, 4], [5, 6, 7, 8]])
print(arr, end = '\n\n')
print(arr.flatten(), end = '\n\n') # to one dimension, сплющує в одномірний массив, але при цьому створює копію
print(arr.ravel()) # to one dimension, не створює копію8