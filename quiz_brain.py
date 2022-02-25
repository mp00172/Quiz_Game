import random
import html

class QuizBrain:

	def __init__(self):
		self.user_score = 0
		self.question_number = 0
		self.question_dict = {}
		self.possible_answers_list = []
		self.possible_answers_dict = {}

	def prepare_questions(self, fetched_data):
		ind = 0
		for i in fetched_data["results"]:
			self.question_dict[ind] = i
			ind += 1

	def prepare_possible_answers(self, question_types):
		self.possible_answers_list = []
		if self.question_dict[self.question_number]["type"] == question_types[1][0]:
			self.possible_answers_list.append(self.question_dict[self.question_number]["correct_answer"])
			self.possible_answers_list.extend(self.question_dict[self.question_number]["incorrect_answers"])
			random.shuffle(self.possible_answers_list)
			ind = 1
			for i in self.possible_answers_list:
				self.possible_answers_dict[ind] = i
				ind += 1
		else:
			self.possible_answers_dict[0] = "False"
			self.possible_answers_dict[1] = "True"

	def next_question(self, question_types):
		self.prepare_possible_answers(question_types)
		print("\nQuestion no. {}: {}".format(self.question_number + 1, html.unescape(self.question_dict[self.question_number]["question"])))
		for i in self.possible_answers_dict:
			print("{}: {}".format(i, html.unescape(self.possible_answers_dict[i])))
		user_answer = input("What's your answer? ")
		while not user_answer.isnumeric() or int(user_answer) not in self.possible_answers_dict.keys():
			user_answer = input("Invalid answer. Please, input one of the numbers above: ")
		self.check_answer(self.possible_answers_dict[int(user_answer)], self.question_dict[self.question_number]["correct_answer"])
		self.question_number += 1

	def still_has_questions(self):
		return self.question_number in range(len(self.question_dict))

	def check_answer(self, user_answer, correct_answer):
		if user_answer == correct_answer:
			print("\nYou got it right! ", end="")
			self.user_score += 1
		else:
			print("\nYou got it wrong. ", end="")
		print(f"The correct answer was: {html.unescape(correct_answer)}.")
		print(f"Your score: {self.user_score}/{self.question_number + 1}")

	def quiz_completed(self):
		print("\nCongratulations! You got to the end of quiz!")
		print(f"Your final score is: {self.user_score}/{self.question_number}")
		self.clean_userscore_qnumber_possibleanswersdict()

	def clean_userscore_qnumber_possibleanswersdict(self):
		self.user_score = 0
		self.question_number = 0
		self.possible_answers_dict = {}

	def clean_all(self):
		self.user_score = 0
		self.question_number = 0
		self.question_dict = {}
		self.possible_answers_list = []
		self.possible_answers_dict = {}


