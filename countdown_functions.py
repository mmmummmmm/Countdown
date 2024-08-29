import time
import os


def input_message():
    time_input = input ('\nPlease enter the time. It should be in the hh:mm:ss format: ')
    return time_input


def check_input(time_input):

    while True:
        try:
            if len(time_input) != 8:
                raise ValueError ()

            hh, mm, ss=[ int(i) for i in time_input.split(':')]  # https://stackoverflow.com/questions/57348321/how-can-i-convert-many-variable-to-int-in-one-line
            if len(str(hh)) > 2 or len(str(mm))> 2 or len(str(ss)) > 2:
                raise ValueError ('Error in input') 
            
            countdown_seconds = (hh*60*60) + (mm*60) + ss
            return countdown_seconds

        except Exception:
            time_input = input_message()
            continue
        break


def show_countdown(seconds):
    
    os.system('cls')  
    input('''
          Time is set, to start the countdown press Enter...
          To stop the countdown at any point, press ctrl + c
          ''')
    
    while seconds > 0:
        time.sleep(1)
        os.system('cls')  
        print(time.strftime('%H:%M:%S', time.gmtime(seconds))) #convert seconds into hh:mm:ss format
        print ("(To stop the countdown, press ctrl + c)")
        seconds -= 1
