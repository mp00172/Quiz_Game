import requests
import html


class GetQuizData:

	def __init__(self):
		self.DIFFICULTY = {
			1: "Easy",
			2: "Medium",
			3: "Hard",
		}
		self.QUESTION_TYPE = {
			1: ["multiple", "Multiple answers"],
			2: ["boolean", "True/False"]
		}
		self.category_list = {}
		self.question_data = {}

	def get_category_list(self):
		response = requests.get(url="https://opentdb.com/api_category.php")
		if response.status_code != 200:
			print("Communication error. Unable to continue.")
			return False
		else:
			data = response.json()
			category_list_choice = 1
			for i in data["trivia_categories"]:
				self.category_list[category_list_choice] = [i["id"], i["name"]]
				category_list_choice += 1
			print("\nCategory list:")
			for i in self.category_list:
				print(f"{i}: {self.category_list[i][1]}")
			return True

	def get_question_data(self, number_of_questions, category, difficulty, question_type):
		response = requests.get(url="https://opentdb.com/api.php?amount={}&category={}&difficulty={}&type={}".format(int(number_of_questions), self.category_list[int(category)][0], self.DIFFICULTY[int(difficulty)].casefold(), self.QUESTION_TYPE[int(question_type)][0]))
		if response.status_code != 200:
			print("CONNECTION ERROR. CODE 200.")
			return False, self.question_data
		else:
			self.question_data = response.json()
			if self.question_data["response_code"] != 0:
				print("\nNot enough questions in the base. Try different settings!")
				return False, self.question_data
			else:
				return True, self.question_data


class ValidUserInput:

	def __init__(self):
		pass

	def quiz_category(self, cat_list):
		ui_cat = input("\nChoose your quiz category: ")
		while not ui_cat.isnumeric() or int(ui_cat) not in range(1, (len(cat_list.keys())) + 1):
			ui_cat = input(f"Invalid input. Please, type the number between 1 and {len(cat_list.keys())}: ")
		return ui_cat

	def number_of_questions(self):
		ui_quest = input("\nHow many questions do you want to have (maximum 50)? ")
		while not ui_quest.isnumeric() or int(ui_quest) not in range(1, 51):
			ui_quest = input("Invalid input. Please, type a number between 1 and 50: ")
		return ui_quest

	def question_type(self, q_t):
		print("\nQuestion types:")
		for i in q_t:
			print(f"{i}: {q_t[i][1]}")
		ui_qt = input("\nChoose your type of questions: ")
		while not ui_qt.isnumeric() or int(ui_qt) not in q_t.keys():
			ui_qt = input("Invalid input. Please, type 1 or 2: ")
		return ui_qt

	def quiz_difficulty(self, diff):
		print("\nDifficulty:")
		for i in diff:
			print(f"{i}: {diff[i]}")
		ui_diff = input("\nMake your choice: ")
		while not ui_diff.isnumeric() or int(ui_diff) not in diff.keys():
			ui_diff = input(f"Invalid input. Please, choose a number between 1 and {len(diff.keys())}: ")
		return ui_diff
