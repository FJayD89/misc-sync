from random import randint
stupnica = [
	[90, 'výborný'],
	[75, 'chválitebný'],
	[60, 'dobrý'],
	[45, 'dostatočný'],
	[0, 'nedostatočný']
]
pocet = 20

naOpravu = []

def vyskusaj():
	a = randint(1,9)
	b = randint(1,9)
	correct = a*b
	print(a, "*", b, "= ?")
	odpoved = int(input())
	if odpoved == correct:
		print("Super! Dostávaš bod.")
		return 1
	print("Ajaj, to nie je dobre. Malo to byť", correct)
	naOpravu.append([a,b])
	return 0


print("Budeš vyskúšaný/á z malej násobilky. Priprav sa.")

skore = 0

for _ in range(pocet):
	skore += vyskusaj()

vysledok = skore/pocet * 100

for stupen in stupnica:
	# toto proste funguje, znamka bude furt
	# vysledok je kladny, ultimaltely checkujeme >= 0
	if vysledok >= stupen[0]:
		znamka = stupen[1]
		break

print('Tvoj výsledok je', znamka)
print('V percentách:', int(vysledok), '%')
