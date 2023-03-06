# sort1

n = int(input())
nums = input().split(' ')
nums = [int(num) for num in nums]

def outP():
    out = str(nums[0])
    for num in nums[1:]:
        out += ' ' + str(num)
    print(out)

for i in range(n):
    least = i
    for j in range(i,n):
        if nums[j] < nums[least]:
            least = j
    nums[least], nums[i] = nums[i], nums[least]
outP()


