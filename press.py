from gpiozero import Button
from time import sleep

button = Button(27)

while True:
	if Button.is_pressed:
		print("pressed")
	else:
		print("released")
sleep(0.2)
