from quiz_brain import QuizBrain
from data import GetQuizData, ValidUserInput
from main_menu import MainMenu

get_quiz_data = GetQuizData()
valid_user_input = ValidUserInput()
quiz_brain = QuizBrain()
main_menu = MainMenu()


def prepare_quiz():
	if get_quiz_data.get_category_list():
		quiz_category = valid_user_input.quiz_category(get_quiz_data.category_list)
		number_of_questions = valid_user_input.number_of_questions()
		question_type = valid_user_input.question_type(get_quiz_data.QUESTION_TYPE)
		quiz_difficulty = valid_user_input.quiz_difficulty(get_quiz_data.DIFFICULTY)
		if get_quiz_data.get_question_data(number_of_questions, quiz_category, quiz_difficulty, question_type)[0]:
			fetched_data = get_quiz_data.get_question_data(number_of_questions, quiz_category, quiz_difficulty, question_type)[1]
			quiz_brain.prepare_questions(fetched_data)
			return True
		else:
			quiz_brain.clean_all()
			return False


def play_quiz():
	while quiz_brain.still_has_questions():
		quiz_brain.next_question(get_quiz_data.QUESTION_TYPE)
	quiz_brain.quiz_completed()


program_running = True
settings_chosen = False

main_menu.print_greeting()

while program_running:
	if not settings_chosen:
		if prepare_quiz():
			settings_chosen = True
			play_quiz()
		else:
			settings_chosen = False
			quiz_brain.clean_userscore_qnumber_possibleanswersdict()
	main_choice = int(main_menu.main_choice())
	if main_choice == 2:
		quiz_brain.clean_all()
		settings_chosen = False
	elif main_choice == 0:
		main_menu.quit_program()
		program_running = False

