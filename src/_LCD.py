from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import datetime
import time

class PrintLCD:

    def __init__(self):
        self.curent_date = ""
        self.current_time = ""
        self.lcd = LCD()


    def set_cuernt_date_and_time(self):
        utc_time = datetime.datetime.utcnow()

        self.curent_date = utc_time.strftime("%Y-%m-%d")
        self.current_time = utc_time.strftime("%H:%M:%S")



    def return_curent_date(self):
        return self.curent_date

    def return_curent_time(self):
        return self.current_time

    #
    # LCD section wtf
    #

    def save_exit(self, signum, frame):
        exit(1)

    def print_on_LCD(self,top,bot):
        signal(SIGTERM, self.save_exit)
        signal(SIGHUP, self.save_exit)

        self.lcd.text(top, 1)
        self.lcd.text(bot, 2)
