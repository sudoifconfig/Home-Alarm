from src._MoveSensor import *
import time


test_move = MoveSensorClass()

while True:
    time.sleep(1)

    test_move.check_input_state()

    


