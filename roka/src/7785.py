ENTER = "enter"
LEAVE = "leave"

people = dict()
for _ in range(int(input())):
	person, status = input().split()
	if status == ENTER:
		people[person] = True
	elif status == LEAVE:
		people.pop(person)
for i in sorted(people, reverse=True):
	print(i)

