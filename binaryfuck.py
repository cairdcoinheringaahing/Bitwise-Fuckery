import sys

first_tape = [0]
second_tape = [0]
code = sys.argv[1]
debug = sys.argv[2] == "-s"
stdin = sys.stdin.read()
tape_head = 0
code_index = 0
loop_depth = 0
input_index = 0

def nth_index(string, substring, N, reverse):
	if string.count(substring) < N:
		return -1
	string = string[::reverse]
	found = 0
	for i in range(len(string)):
		char = string[i]
		if substring == char:
			found += 1
		if found == N:
			if reverse < 0:
				return len(string) - i
			else:
				return i
	return -1

while code_index < len(code):
	char = code[code_index]
	if char == "^":
		first_tape[tape_head] ^= second_tape[tape_head]
	if char == "&":
		first_tape[tape_head] &= second_tape[tape_head]
	if char == "|":
		first_tape[tape_head] |= second_tape[tape_head]
	if char == "+":
		first_tape[tape_head] += 1
	if char == "-":
		first_tape[tape_head] -= 1
	if char == ">":
		tape_head += 1
		try: first_tape[tape_head]
		except:
			first_tape.append(0)
			second_tape.append(0)
	if char == "<":
		tape_head -= 1
		if tape_head < 0:
			tape_head %= len(first_tape)
	if char == ".":
		print(end=chr(abs(int(first_tape[tape_head]))))
	if char == ",":
		first_tape[tape_head] = ord(stdin[input_index]) if input_index < len(stdin) else -1
		input_index += 1
	if char == "@":
		first_tape, second_tape = second_tape, first_tape
	if char == "[":
		loop_depth += 1
		if not first_tape[tape_head]:
			code_index = nth_index(code, "]", loop_depth, -1)
	if char == "]":
		if first_tape[tape_head]:
			code_index = nth_index(code, "[", loop_depth, 1)
		else:
			loop_depth -= 1
	code_index += 1

if debug:
	if '.' in code: print()
	print(first_tape)
	print(second_tape)
