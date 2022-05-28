from collections import deque
def balancedBrackets(string):
	# Write your code here.
	brackets = {
		"(":")",
		"{": "}",
		"[": "]"
	}
	queue = deque()
	left_brackets = ["(","[","{"]
	right_brackets = [")","]","}"]
	for bracket in string: 
		if bracket in left_brackets:
			queue.append(bracket)
		elif bracket in right_brackets: 
			if len(queue) > 0:
				last_left = queue.pop()
				if bracket != brackets[last_left]:
					return False
			else:
				return False
		else:
			continue
	return len(queue) == 0 
			


if __name__ == "__main__":
	input_dict = {
		"string": "([])(){}(())()()"
	}
	print(balancedBrackets(input_dict["string"]))
