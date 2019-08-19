import random
from array_class import Array

# Создаем массив рандом-f_array размерностью f_row x f_col
f_row = random.randint(1, 10)
f_col = random.randint(1, 10)
f_array = [[random.randint(1, 100) for y in range(f_row)] for x in range(f_col)]

# Создаем массив рандом-s_array размерностью s_row x s_col
s_row = random.randint(1, 10)
s_col = random.randint(1, 10)
s_array = [[random.randint(1, 100) for y in range(s_row)] for x in range(s_col)]

# Создаем объекты класса Array
f_obj = Array(f_array)
s_obj = Array(s_array)

print("First obj")
f_obj.__get__()

print("Second obj")
s_obj.__get__()

print("Sum 2 obj")
f_obj.__add__(s_obj).__get__()

print("Sum diag")
f_obj.__sumdig__()

print("Multiply two obj")
f_obj.__mul__(s_obj)

print("Transpose obj")
f_obj.__transpose__().__get__()