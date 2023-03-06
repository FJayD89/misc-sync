# vystava

n = int(input())
cervs = input().split(' ')
cervs = [int(cerv) for cerv in cervs]

best = 0

for i in range(n):
    if cervs[i] < cervs[best]:
        best = i

cervs[best], cervs[0] = cervs[0], cervs[best]

out = str(cervs[0])
for cerv in cervs[1:]:
    out += ' ' + str(cerv)
print(out)
