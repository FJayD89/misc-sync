text = 'QlpoOTFBWSZTWcQFLwQAAQpYAEAAQABgADAA0AZpoJPVIGaadvTRSRIobEAZNASddwRpaxhCjTNKWzIsmyGoVSDKlaRCNUaNMnddCpIiKJMlmlalNrQQUyGtnqybbXNsrN8XckU4UJDEBS8E'

collected = {}

for char in text:
	if char in collected.keys():
		collected[char] += 1
		continue
	collected[char] = 1

ordered = dict(sorted(collected.items(), key=lambda item: item[1]))

print(ordered)

