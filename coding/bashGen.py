passLen = 3
cmd1 = '7z x data.zip -y -ounzipped -p'
cmd2 = ' -so'
nums = ['0'*(passLen-len(str(num))) + str(num) for num in range(10**passLen)]
cmds = [cmd1+num+cmd2 for num in nums]
[print(cmd) for cmd in cmds]