# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


N = int(input('Введите число N: '))
S = 1
if N < 0:
    print('[ ', end='')
    N *= (-1)
    for i in range(1, N):
        S = S * i
        print(S, end=', ')
    print((S * N), end=' ]')
else:
    print('[ ', end='')
    for i in range(1, N):
        S = S * i
        print(S, end=', ')
    print((S * N), end=' ]')