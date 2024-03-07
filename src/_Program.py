import os 
import RPi.GPIO as GPIO
import time

from src._Camera import CameraClass
from src._LCD import PrintLCD
from src._MoveSensor import MoveSensorClass
from src._EmailHeandler import SendEmailClass

pin_number = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_number, GPIO.IN)

EMAIL_SENDER = 'example@gmail.com'
EMAIL_RECIVER = 'example@zwp.pl'
EMAIL_PASS = '2137 ACAB HWDP 1312'


#
# So here is class that heandle and run my simple program.
# In __init__ function a create thous object like Camer, MoveSensor, LCD
# to make it easer to heandle and operate them (you know, easier to print some thiong on LCD, or send email with .jpg)
# 


class ProgramClass:
    def __init__(self):
        self.camera = CameraClass()
        self.move_sensor = MoveSensorClass()
        self.lcd = PrintLCD()
        self.email = SendEmailClass(EMAIL_SENDER,EMAIL_RECIVER,EMAIL_PASS)

        self.alarm_bool = bool
        self.time_out = 60
        self.pin_state = bool

    def return_pin_state(self):
        self.pin_state = GPIO.input(17)
    

    def count_x_sec(self,x_sec):
        x = x_sec
        while x != 0:
            self.lcd.print_on_LCD("ACTIVE IN:",f"{x}")
            time.sleep(1)
            x = x - 1

    def if_alarm_ON(self):
        program_status = True
        self.count_x_sec(10)

        while program_status:
            time.sleep(0.1)
            self.return_pin_state()

            if self.pin_state:
                self.lcd.print_on_LCD("alarm ON","")
                if self.move_sensor.check_status():
                    self.lcd.print_on_LCD("SENSOR ACTIV","PHOTO TAKEN")
                    self.camera.make_photo_and_save()
                    try:
                        self.email.send_jpg(self.camera.return_data_time()+".jpg")
                        self.lcd.print_on_LCD("SENT","SUCCESS")
                    except:
                        self.lcd.print_on_LCD("SENT","FAILED")    
            else:       
                break



    def if_alarm_OFF(self):
        while True:
            time.sleep(0.1)
            self.return_pin_state()
            if self.pin_state == False: 
                self.lcd.print_on_LCD("alarm OFF","Zzz Zzz")
            else:
                break


    def check_PID_value(self):
        if self.pin_state == GPIO.HIGH:
            self.alarm_bool = True
        
        else:
            self.alarm_bool = False

#
# Here is the main loop that is callen from main.py file. I know it looks dump but 
# its work ... next one will be better. 
#


    def run_program(self):
        program_status = True
        while program_status:
            time.sleep(0.1)
            self.check_PID_value()
            self.return_pin_state()

            if self.pin_state:
                self.if_alarm_ON()

            else:
                self.if_alarm_OFF()


    def clear_screen(self):
        os.system("clear")