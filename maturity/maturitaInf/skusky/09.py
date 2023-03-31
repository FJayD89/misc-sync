num = int(input("Poprosím celé kladné číslo:\n"))

char = input("A jeden znak:\n")

[print(char * num) for _ in range(num)]

print('\n')

[print(' ' * (num - 1 - i) + char * (2 * i + 1) + ' ' * (num - 1 - i)) for i in range(num)]

print('\n')

[print(char*(i+1)) for i in range(num)]

print('\n')

[print(char + (char if (i%(num-1) == 0) else ' ')*(num-2) + char) for i in range(num)]