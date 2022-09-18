import subprocess
import pigpio
import time
import RPi.GPIO as GPIO
#subprocess.run('tmux new-session -d -s "displayscript1" /home/pillbot/Desktop/facedisplay.sh'.split())
small = int(input("How many small pills?: "))
large = int(input("How many large pills?: "))
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
start = time.time()
#numpills = 2
pi = pigpio.pi()
subprocess.run('tmux new-session -d -s displayscript2 /home/pillbot/Desktop/facedisplay2.sh'.split())
time.sleep(4)
pi.set_servo_pulsewidth(18, 1430)
#pi.set_servo_pulsewidth(12, 1430)
for x in range(0, small):
	while GPIO.input(21) == 0:
		if time.time() - start > 5 and time.time() - start < 5.3:
			pi.set_servo_pulsewidth(18, 2000)
			#pi.set_servo_pulsewidth(12, 2000)
		if time.time() - start > 5.3:
			pi.set_servo_pulsewidth(18, 1430)
			#pi.set_servo_pulsewidth(12, 1430)
			start = time.time()
	while GPIO.input(21) == 1:
		pi.set_servo_pulsewidth(18, 0)
		#pi.set_servo_pulsewidth(12, 0)
	time.sleep(0.2)
pi.set_servo_pulsewidth(18, 0)
start = time.time()

pi.set_servo_pulsewidth(12, 1420)
for x in range(0, large):
        while GPIO.input(21) == 0:
                if time.time() - start > 5 and time.time() - start < 5.3:
                        #pi.set_servo_pulsewidth(18, 2000)
                        pi.set_servo_pulsewidth(12, 2000)
                if time.time() - start > 5.3:
                        #pi.set_servo_pulsewidth(18, 1430)
                        pi.set_servo_pulsewidth(12, 1420)
                        start = time.time()
        while GPIO.input(21) == 1:
                #pi.set_servo_pulsewidth(18, 0)
                pi.set_servo_pulsewidth(12, 0)
        time.sleep(0.2)
pi.set_servo_pulsewidth(18, 0)
pi.set_servo_pulsewidth(12, 0)
subprocess.run('tmux kill-session -t displayscript2'.split())
pi.stop()
