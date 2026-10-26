from gpiozero import Button
from signal import pause

count = 0

def pressed():
	global count 
	count = count + 1
	print(f"total presses: {count}")

button = Button(27, bounce_time=0.05)
button.when_pressed = pressed
pause()
