text = 'Muumi (ruots. mumin) on suomenruotsalaisen kirjailijan ja taiteilijan Tove \
Janssonin luoma satuhahmolaji. Yksi tunnetuimmista muumihahmoista on \
Muumipeikko, joka asuu huolettoman ja seikkailunhaluisen perheensä kanssa \
Muumitalossa Muumilaaksossa. Jansson kirjoitti ruotsiksi lukuisia \
Muumi-kirjoja, jotka ovat suosituinta ja käännetyintä suomalaista \
lastenkirjallisuutta. Muumikirjoja on käännetty yli 50 eri kielelle, ja \
niistä on tehty kirjojen ja sarjakuvien lisäksi muun muassa \
animaatiosarjoja, interaktiivisia kirjasovelluksia, lukuisia näytelmiä ja \
ooppera. Muumien nousu maailmanmaineeseen perustui merkittävästi myös Tove \
ja Lars Janssonin Muumi-sarjakuviin, joita julkaistiin 1954 alkaen ensin The \
Evening News -lehdessä Lontoossa ja myöhemmin 40 maassa 20 miljoonalle \
lukijalle. Erityisen suosittuja muumit ovat olleet Pohjoismaissa ja \
Japanissa. '

counts = {}

for char in text:
	if char in counts.keys():
		counts[char] += 1
		continue
	counts[char] = 1

for key in counts.keys():
	print(key, counts[key])