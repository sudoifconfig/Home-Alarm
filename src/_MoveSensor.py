import RPi.GPIO as GPIO
import time


class MoveSensorClass:

    def __init__(self,):
        self.sescription = "Classs that will help comunicate and manage with move sensor"
        self.pid_ID = 4
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.IN)
        self.sensor_state = bool


    def __str__(self):
        return f"Move sensor OUT leg is on {self.pid_ID} pin "

    def check_input_state(self):
        input_state = GPIO.input(self.pid_ID)

        if input_state == GPIO.HIGH:
            self.sensor_state = True
            return True

        elif input_state == GPIO.LOW:
            self.sensor_state = False
            return False

    def test_print(self):
        return self.sensor_state00


    def check_status(self):
        self.check_input_state()
        chuj = self.return_sensor_state()
        return chuj


    #
    # 'return' Section
    #

    def return_sensor_state(self):
        return self.sensor_state