'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# inputs: word
# outputs: count of th
# constraints: no loops


# base case, if length of word is less than one letter return
# iteration, grab  the first letters and check if they are equal to "th" if it is add it to count
def count_th(word):

	count = 0

	def iteratethrough(word=word):
		nonlocal count
		if len(word) < 1:
			return count
		# generator function will make the time complexity increase
		front_two_letters = word[:2]
		if front_two_letters == "th":
			count += 1
		return iteratethrough(word[1:])
	
	return iteratethrough()