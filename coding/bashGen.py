passLen = 4
cmd1 = '7z x "TomasB 3-2023 -Zmeny v pracovnej zmluve_ .pdf.zip" -y -ounzipped -p'
cmd2 = '23 -so'
nums = ['0'*(passLen-len(str(num))) + str(num) for num in range(1000)]
cmds = [cmd1+num+cmd2 for num in nums]
[print(cmd) for cmd in cmds]