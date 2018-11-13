import  numpy as np

# list1=[1,3,5,2,4,3]
# n=np.array(list1)
# print("长度：",n.size)
# print("形状：",n.shape)
# print(n.ndim)
# print(n.dtype)

# array_one = np.ones([10,10])
# array_zero = np.zeros([10,10])
# print("浮点1：",array_one)
# print(("浮点0：",array_zero))
#
# n1=np.random.randint(0,10)
# print(n1)
# n2=np.random.normal(1.75, 0.1, (2, 3))
# print(n2)

# 正态生成4行5列的二维数组
arr = np.random.normal(1.75, 0.1, (4, 5))
print(arr)
# 截取第1至2行的第2至3列(从第0行算起)
after_arr = arr[1:3, 2:4]
print(after_arr)