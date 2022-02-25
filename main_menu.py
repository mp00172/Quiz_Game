class MainMenu():

	def __init__(self):
		self.menu_items = {
			1: "Play again with same settings",
			2: "Choose new settings",
			0: "Quit"
		}

	def main_choice(self):
		print("\nPlay again?")
		for i in self.menu_items:
			print(f"{i}: {self.menu_items[i]}")
		user_choice = input("Make your choice: ")
		while not user_choice.isnumeric() or int(user_choice) not in self.menu_items.keys():
			user_choice = input("Invalid input. Please, input one of the numbers above: ")
		return user_choice

	def quit_program(self):
		print("\nThank you for playing! Goodbye! :)")

	def print_greeting(self):
		print("""
=========================
  Welcome to QUIZ GAME!
powered by Open Trivia DB
=========================
		""")
