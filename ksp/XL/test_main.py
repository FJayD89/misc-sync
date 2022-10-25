from AerolinkoveCeny import main

test1 = [
	'4 3',
	[
		'1 2',
		'2 3',
		'0 1'
	],
	17
]

test2 = [
	'3 3',
	[
		'0 1',
		'0 2',
		'1 2'
	],
	12
]

test3 = [
	'1 0',
	[],
	0
]

test4 = [
	'20 5',
	[
		'3 17',
		'5 3',
		'6 16',
		'7 16',
		'8 5'
	]
	
]



def unpack(test):
	return main(test[0], test[1]) - test[2]

def test_problem2():
	assert unpack(test1) == 0
	assert unpack(test2) == 0
	assert unpack(test3) == 0
