'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены
только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте
выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля
и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
'''


def parse_file(file):
    with open(file) as data:
        input_file = data.read()
    input_file = input_file.split()
    input_file.pop(1)
    return input_file


def find_best_pos(source_arr, n):
    arr = []
    for num in source_arr:
        arr.append(int(num))
    print(arr)
    prev = arr[n - 1]
    nex = arr[1]
    index = 0
    if n == 1:
        return arr[0]
    if n <= 3:
        max = sum(arr)
        return max
    max = arr[0] + nex + prev
    for i in range(n - 1):
        if i == n-2:
            nex = arr[0]
        else:
            nex = arr[i+2]
        prev = arr[i]
        if max < arr[i + 1] + nex + prev:
            max = arr[i + 1] + nex + prev
            index = i + 2

    return max, index


if __name__ == "__main__":
    file = "input_for_tak24.txt"
    source = parse_file(file)
    n = int(source[0])
    source.pop(0)
    max_berries, bush_number = find_best_pos(source, n)
    print(f"Max {max_berries} berries can be collected from {bush_number} bush")
