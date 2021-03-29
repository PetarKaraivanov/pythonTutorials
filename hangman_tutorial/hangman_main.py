
""" hangman is a simple game, where the player should guess
	a chosen word. The word is hidden and the player is guessing
	the letter. For each correct guess, all occurrences of that 
	letter are being revealed. If the guess is incorrect, then
	the player looses a life. After all lives are lost, the player
	looses the game. If the player guesses the word before that,
	than he won.

	In this tutorial you will learn:

	- importing modules dynamically
	- list comprehensions
	- filtering a list
	- string and list manipulation 
	- working with command line inputs
	- working with command line arguments
	- creating and calling definitions(functions)
	- working with variables
	- using a basic TDD
	- using source control(git)
	- applying basic DRY principles

	The tutorial will be devided in multiple sessions. For easier
	management and understanding the different tutorials will be 
	defined as different files and later imported here. You can choose
	a different tutorial by entering a command line argument.
"""

HELP = """
	Hello and welcome to the hangman tutorial!
	|---
	|  |
	|  O
	| /|\\
	|  |
	| / \\
	|

	Here is how you start:
	python hangman_main.py {argument}

	and here a list with the possible arguments:

        tutorial_1 - start the first turorial from 22.03.2021

        tutorial_2 - start the second tutorial from 29.03.2021

"""




if __name__ == '__main__':
	""" If you call python hangman_main.py
		this is where you will land. No mattter
		if you have addition arguments or not. This
		is your main script here you can import other
		script and run functions. If you import
		this file somewhere else and then try to run
		the script where you imported hangman_main
		then this part bellowe wont be executed
	"""

	""" In python you can pass additional arguments over the
		command line. The arguments are seperated by a space(' ')
		So be carefull, 'my argument' will be then counted as
		2 arguments 'my' and 'argument'. To retreave the arguments
		you need to import a build-in library called 'sys'.
		Then 'sys.argv' is giving you a list of all arguments,
		where the first argument is the file name(in this case
		it will be 'hangman_main.py')
	"""
	import sys

	lst_args = sys.argv
	""" if the len is less then 2, then lst_args just has the
		file name as first argument. In this case we will print
		a user-friendly message, to display the options available
	"""
	if len(lst_args) < 2:
		print(HELP)
		exit()

	""" get the selected tutorial and then import it.
		Here we will use the build-in library importlib.
		With getattr we are specifying which function from the
		module we want to import. In this case 'start_game'.

		- Write a test which is checking if the imported tutorials
		have the start_game definition.
	"""

	tutorial = lst_args[1]

	import importlib

	start_game = getattr(importlib.import_module(tutorial), "start_game")

	start_game()
