from collections import defaultdict

counter = defaultdict(int)


def is_unified(target: list) -> bool:
	total = sum(list(map(sum, target)))
	return total == 0 or total == len(target)**2


def count_colors(color: int):
	counter[color] += 1
	

def cut_qaurter(target: list) -> list:
	n = len(target) // 2
	qaurter = []
	for x, y in [(0, 0), (0, n), (n, 0), (n, n)]:
		new_paper = []
		for i in range(n):
			new_paper.append(target[x+i][y: y+n])
		qaurter.append(new_paper)
	return qaurter
	
	
def two_two(target: list):
	if is_unified(target):
		count_colors(target[0][0])
		return
	for i in target:
		for j in i:
			count_colors(j)


def four_four(target: list):
	if is_unified(target):
		count_colors(target[0][0])
		return
	for i in cut_qaurter(target):
		two_two(i)


def eight_eight(target: list):
	if is_unified(target):
		count_colors(target[0][0])
		return
	for i in cut_qaurter(target):
		four_four(i)


def sixteen_sixteen(target: list):
	if is_unified(target):
		count_colors(target[0][0])
		return
	for i in cut_qaurter(target):
		eight_eight(i)


def thirty_two(target: list):
	if is_unified(target):
		count_colors(target[0][0])
		return
	for i in cut_qaurter(target):
		sixteen_sixteen(i)
		
		
def sixty_four(target: list):
	if is_unified(target):
		count_colors(target[0][0])
		return
	for i in cut_qaurter(target):
		thirty_two(i)
		

def hundred_twenty_eight(target: list):
	if is_unified(target):
		count_colors(target[0][0])
		return
	for i in cut_qaurter(target):
		sixty_four(i)

		
N = int(input())
paper = []
for _ in range(N):
	paper.append(list(map(int, input().split())))
starting_functions = dict()
for number, function in [(2, two_two), (4, four_four), (8, eight_eight), (16, sixteen_sixteen), (32, thirty_two), (64, sixty_four), (128, hundred_twenty_eight)]:
	starting_functions[number] = function
starting_functions[N](paper)
print(counter[0])
print(counter[1])
