# У нас есть массив:
# my @unsorted = ( qw/ 7 1 3 4 2 4 6 5 5 / );
# Напиши алгоритм, который отсортирует этот массив. Пользоваться встроенной функцией sort нельзя. Для простоты можно написать алгоритм bubble sort.
# Напиши алгоритм двоичного поиска. Если поиск элемента удачный, должно выводиться MATCH, если неудачный - NOT_MATCH.

unsorted = [7, 1, 3, 4, 2, 4, 6, 5, 5]

print(unsorted)

for i in range(len(unsorted)-1):
    for j in range(len(unsorted)-i-1):
        if unsorted[j] > unsorted[j + 1]:
            unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]

print(unsorted)


key = 5
start = 0
end = len(unsorted)

while start <= end:

    midpoint = (start + end) // 2

    if key == unsorted[midpoint]:
        print("MATCH")
        break

    elif (end - start) // 2 == 0:
        print("NOT_MATCH")
        break

    elif key < unsorted[midpoint]:
        end = midpoint - 1

    elif key > unsorted[midpoint]:
        start = midpoint + 1



