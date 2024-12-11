from playsound import playsound

import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    
    print(CLEAR)
    
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        
        print(f"{CLEAR_AND_RETURN}Alarm will sound in : {minutes_left:02d}:{seconds_left:02d}")
        
    playsound("Parrot Tone.mp3")
    
minutes = int(input("Enter How many minutes to wait ? "))
second = int(input("Enter How many seconds to wait ? "))
    
total_time = minutes * 60 + second
    
alarm(total_time)