a = [1,2,3,4,5]
b = [1,2,3,6,7]

c = [i for i in a if i not in b]
d = [i for i in b if i not in a]
print(len(c + d)) # Кол-во различных чисел содержится одновременно в 1 и во 2 списках - это [4, 5, 6, 7] = 4 шт.



