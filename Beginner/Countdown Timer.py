import time

def countdown(seconds):
	while seconds:
		mins, secs = divmod(seconds, 60)
		timer = f"{mins:02d}:{secs:02d}"
		print(timer, end="\r")
		time.sleep(1)
		seconds -= 1
	print("Time's Up!")

seconds = int(input("Enter the countdown time in seconds: "))


countdown(seconds)