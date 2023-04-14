from math import floor
inp = input()
try: num = float(inp)
except:
	print("Blbý vstup")
	exit()

if num != floor(num) or num <= 0:
	print("Nie je to prirodzené číslo")
else:
	print(int(2*num))