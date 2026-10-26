from gpiozero import LED, Button
from time import sleep
from signal import pause

led = LED(17)
button = Button(27, bounce_time=0.05)

def acknowledge():
	was_lit = led.is_lit
	for _ in range(2):
		led.on()
		sleep(0.1)
		led.off()
		sleep(0.1)
	if was_lit:
		led.on()

button.when_pressed = acknowledge
pause()
