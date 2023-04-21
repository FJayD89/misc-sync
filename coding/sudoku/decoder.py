from math import sqrt


def get_setup():
	f = open('copied.txt')
	lines = f.read().split('\n')
	lines = [int(num) if len(num) == 1 else 0 for num in lines]
	size = int(sqrt(len(lines)))
	lines = [lines[size*i:size*(i+1)] for i in range(size)]
	return lines


def setup():
	f = open('setup.txt')
	lines = f.read().split('\n')
	lines = [[int(num) for num in line] for line in lines]
	return lines