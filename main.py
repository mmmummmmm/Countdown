"""Your Task
Create a program which will take a time from the user as a timer and start to countdown in the terminal. You can use any library and function you want for this mini project. Make sure your program - is written only using Python - each new countdown line appears after one second, not immediately
"""

import time
import traceback



input('''
      Just give me a time and I\'ll count down untill eternety for you.
                       
                       To continue , please press Enter . . . 
      ''')


def input_message():
    time_input = input ('\nPlease enter The time. It should be in the hh:mm:ss format: ')
    return time_input


def check_input(time_input):
    if len(time_input) != 8:
        raise ValueError ()

    while True:
        try:
            if len(time_input) != 8:
                raise ValueError ()

            print ('begin split')
            hh, mm, ss=[ int(i) for i in time_input.split(':')]  # https://stackoverflow.com/questions/57348321/how-can-i-convert-many-variable-to-int-in-one-line
            if len(str(hh)) > 2 or len(str(mm))> 2 or len(str(ss)) > 2:
                print("!2")
                raise ValueError ('Error in input') 
            countdown_seconds = (hh*60*60)+(mm*60)+ ss
            return countdown_seconds

        except Exception:
            #traceback.print_exc()
            print('l')
            input_message()
            continue
        break


def show_countdown(seconds):
    print('''
          Time is set, to start the countdown press Enter...
          To stop the countdown at any point, press ctrl + c
          ''')
    
    while seconds > 0:
        time.sleep(1)
        print(time.strftime('%H:%M:%S', time.gmtime(seconds))) #convert seconds into hh:mm:ss format
        seconds -= 1


time_input = input_message()
countdown_sec = check_input(time_input)

show_countdown(countdown_sec)

