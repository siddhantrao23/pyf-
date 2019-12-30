import sys

def execute(filename):
	f = open(filename, "r")
	eval(f.read())

def eval(code):
	code 		= cleanup(list(code))
	bracemap 	= buildmap(code)

	cells, codeptr, cellptr = [0], 0, 0
	'''
		cells	array of cells of 0 or 1
		codeptr	index of current command
		cellptr index of pointer
	'''
	while(codeptr < len(code)):
		command = code[codeptr];
		if command == '>':
			cellptr += 1;
			if cellptr >= len(cells): cells.append(0)
		elif command == '<':
			cellptr -= 1;
		elif command == '+':
			cells[cellptr] += 1 if cells[cellptr] < 255 else 0
		elif command == '-':
			cells[cellptr] -= 1 if cells[cellptr] > 0 else 255
		elif command == '.':
			sys.stdout.write(str(cells[cellptr])+'\n')
		elif command == ',':
			cells[cellptr] = int(sys.stdin.read(1))
		elif command == '[':
			if cells[cellptr] == 0:
				codeptr = bracemap[codeptr]
		elif command == ']':
			if cells[cellptr] != 0:
				codeptr = bracemap[codeptr]
		codeptr += 1

def cleanup(code):
	'''
		>	increment the data pointer (to point to the next cell to the right).
		<	decrement the data pointer (to point to the next cell to the left).
		+	increment (increase by one) the byte at the data pointer.
		-	decrement (decrease by one) the byte at the data pointer.
		.	output the byte at the data pointer.
		,	accept one byte of input, storing its value in the byte at the data pointer.
		[]	for looping
	'''
	return ''.join(filter(lambda x: x in ['>', '<', '+', '-', '.', ',', '[', ']'], code))

def buildmap(code):
	stack = []
	bracemap = {}

	for position, command in enumerate(code):
		if command == '[': stack.append(position)
		if command == ']':
			start = stack.pop()	
			bracemap[start] = position
			bracemap[position] = start

	return bracemap

def main():
	if len(sys.argv)== 2:
		execute(sys.argv[1])

if __name__ == '__main__':
	main()