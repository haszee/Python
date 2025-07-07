quiz_questions = [     ("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2),     ("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3),     ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "H2"], 1), ]

for i in range(len(quiz_questions)):
	question = print(f"{quiz_questions[i][0]}")
	for j in range(4):
		print(f"{j+1}. {quiz_questions[i][1][j]}")
	pick_ans = int(input("What is your answer (1/2/3/4): ").strip())

	if pick_ans == quiz_questions[2]:
		print("Correct!")
	else:
		print(f"Wrong! The correct answer is {quiz_questions[2]}. {quiz_questions[i][quiz_questions[2]]} ")
