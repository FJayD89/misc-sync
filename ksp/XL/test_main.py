from AerolinkoveCeny import main

setup1 = '4 3'
raw1 = ['1 2',
        '2 3',
        '0 1'
        ]
res1 = 17


def test_problem2():
	assert main(setup1, raw1) == res1
