import Adafruit_BBIO.PWM as PWM
import time

J18 = 'P8_19'
J25 = 'P8_13'

dutyCycle = 0.0

#optionally, you can set the frequency as well as the polarity from their defaults:
PWM.start(J18, 100.0 - dutyCycle, 1000, 1)
PWM.start(J25, dutyCycle, 1000, 1)

while True:
	PWM.set_duty_cycle(J18, dutyCycle)
	PWM.set_duty_cycle(J25, 100.0 - dutyCycle)
	time.sleep(0.1)
	dutyCycle += 5.0
	if dutyCycle > 100.0:
		dutyCycle = 0

PWM.stop(J18)
PWM.stop(J25)
PWM.cleanup()
