def pos_or_neg(num):
	match num:
		case num if num > 0:
			print("Positive")
		case num if num < 0:
			print("Negative")
		case _:
			print("Zero")


pos_or_neg(9)
pos_or_neg(-21)
pos_or_neg(0)

