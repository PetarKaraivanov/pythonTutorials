import random
TEXT = "If your favorite Python library or framework didn’t make this list of the top ten must-have Python packages, don’t take offense. The Python ecosystem has generated so many valuable packages that it would be impossible to include all of the important ones even on a top 100 list, let alone a top 10 list. Still, for general-purpose Python programming, the packages described above often come in handy."

def check_letter(letter_guess, searched_word, lst_spaces, attempts_left):

	if letter_guess in searched_word:
		""" we found a letter!
			BUT they may be a multiple occurrences
			of the letter
		"""
		for idx, letter in enumerate(searched_word):

			if letter == letter_guess:
				lst_spaces[idx] = letter


		print("THERE IS A '%s' IN THE WORD " %(letter_guess))
	else:
		print("THERE IS NO '%s' IN THE WORD " %(letter_guess))
		attempts_left -= 1

	return lst_spaces, attempts_left


def start_game():
	""" get each word as lowercase in Text if the words length is bigger then 5
	"""
	lst_words = [word.lower() for word in TEXT.split(" ") if len(word) > 5]
	# choose the searched word
	searched_word = random.choice(lst_words)

	lst_spaces = ["_" for _ in range(len(searched_word))]
	attempts_left = 5

	print("CAN YOU GUESS THE WORD?\n")

	while True:
		print(" ".join(lst_spaces), "\n")
		print("Enter a letter:\n")
		letter_guess = str(input()).lower()

		#case you quit
		if letter_guess == "quit":
			print("YOU PUSSY, YOU LOST!")
			break

		lst_spaces, attempts_left = check_letter(letter_guess, searched_word, lst_spaces, attempts_left)

		if attempts_left <= 0:
			print("You lost noob, The word was: %s" % searched_word)
			break

		if "_" not in lst_spaces:
			print("YOU CANNOT BELEAVE A PUSSY LIKE YOU CAN WIN, BUT HEY")