import random

class Array:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        max_col = max(len(self.data), len(other.data))
        max_row = max(len(self.data[0]), len(other.data[0]))
        result = [[0 for y in range(max_row)] for x in range(max_col)]
        for x in range(len(self.data)):
            for y in range(len(self.data[0])):
                result[x][y] += self.data[x][y]
        for x in range(len(other.data)):
            for y in range(len(other.data[0])):
                result[x][y] += other.data[x][y]

        return Array(result)

    def __sub__(self, other):
        max_col = max(len(self.data), len(other.data))
        max_row = max(len(self.data[0]), len(other.data[0]))
        result = [[0 for y in range(max_row)] for x in range(max_col)]
        for x in range(len(self.data)):
            for y in range(len(self.data[0])):
                result[x][y] += self.data[x][y]
        for x in range(len(other.data)):
            for y in range(len(other.data[0])):
                result[x][y] -= other.data[x][y]

        return Array(result)

    def __mul__(self, other):
        if len(self.data[0]) == len(other.data):
            result = [[0 for y in range(len(other.data[0]))] for x in range(len(self.data))]
            for x in range(len(self.data)):
                for y in range(len(other.data[0])):
                    for z in range(len(self.data[0])):
                        result[x][y] += self.data[x][z] * other.data[z][y]
            return Array(result)
        else:
            print("Mul is imposible")

    def __transpose__(self):
        result = [[0 for y in range(len(self.data))] for x in range(len(self.data[0]))]
        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                result[x][y] = self.data[y][x]
        return Array(result)

    def __sumdig__(self):
        result = 0
        if len(self.data) == len(self.data[0]):
            for x in range(len(self.data)):
                result += self.data[x][x] * self.data[len(self.data) - x - 1][x]
            print(result)
        else:
            print("No answer")
            pass

    def __get__(self):
        for x in range(len(self.data)):
            for y in range(len(self.data[0])):
                print(self.data[x][y], end=" ")
            print()


# Создаем массив f_array размерностью f_row x f_col
f_row = random.randint(1, 10)
f_col = random.randint(1, 10)
f_array = [[random.randint(1, 100) for y in range(f_row)] for x in range(f_col)]

# Создаем массив s_array размерностью s_row x s_col
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
