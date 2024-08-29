import time
from countdown_functions import input_message, check_input, show_countdown
input('''
      Just give me a time and I\'ll count down untill eternety for you.
                       
                       To continue , please press Enter . . . 
      ''')


time_input = input_message()
countdown_sec = check_input(time_input)

show_countdown(countdown_sec)

