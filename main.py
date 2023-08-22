N = int(input("Введите количество арбузов: "))

max = int(input("Введите массу арбуза: "))

min = max

for i in range(N-1):

    a = int(input("Введите массу арбуза: "))

    if a > max:

        max = a

    else :

        if a < min:

            min = a

print(min, max)