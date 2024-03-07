import time                                                                                   
from datetime import datetime                                                                 
import os 


class CameraClass:

    def __init__(self):
        self.name = "siemanko tu kamera"
        self.data_time = str

    def set_data_time(self,set):
        self.data_time = set

    def return_data_time(self):
        return self.data_time

    def make_photo_and_save(self):
        datatime_now = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')                           
        self.set_data_time(datatime_now)
        cmd = f"libcamera-jpeg -o {datatime_now}.jpg"                                         
        os.system(cmd)
