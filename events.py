from gpiozero import Button
from signal import pause

def hello():
	print("pressed!")

button = Button(27, bounce_time=0.05)
button.when_pressed = hello

pause()
