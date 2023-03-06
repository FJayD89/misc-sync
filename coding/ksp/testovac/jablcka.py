# jablcka

inp = input().split(' ')
n = int(inp[0])
p = int(inp[1])

jabs = input().split(' ')
jabs = [int(jab) for jab in jabs]

less = ''
eq = ''
more = ''

def outP(lst):
    if not lst:
        print('')
        return
    out = str(lst[0])
    for num in lst[1:]:
        out += ' ' + str(num)
    print(out)

for jab in jabs:
    if jab > p:
        more += str(jab)+' '
        continue
    if jab < p:
        less += str(jab)+' '
        continue
    eq += str(jab)+' '

print(less[:-1])
print(eq[:-1])
print(more[:-1])
