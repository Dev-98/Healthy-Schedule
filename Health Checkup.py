from datetime import datetime
import time
from tkinter import messagebox

from pygame import mixer

def musicloops(song, stopper):
    mixer.init()
    mixer.music.load(song)
    # mixer.music.set_volume(1)
    mixer.music.play()
    while True:
        A = input('Enter Exit if you completed  =')
        if A.lower() == stopper :
            mixer.music.stop()
            break
        else :
            continue

def log(msg):
    with open ("C:/Users/Dev Gupta/Documents/Python/health checkup.txt" , "a") as lg:
        lg.write(f"{msg} :- {datetime.now()}\n")

if __name__ == "__main__":
    
    init_water = time.time()
    init_eyes = time.time()
    init_exercise = time.time()
    water = 5
    eyes = 100 
    exer = 50
    while True:
        if time.time() - init_water >  water :
            print('Water drinking time  \#')
            messagebox.showinfo('Water drinking time  #', "Please drink some water it's past half hour ")
            musicloops("C:/Users/Dev Gupta/Downloads/Jumping Water.mp3","exit")
            init_water = time.time()
            log("Water drank at")

        elif time.time() - init_eyes > eyes:
            print('Eyes exercise time  #')
            musicloops("C:/Users/Dev Gupta/Downloads/Jumping Water.mp3", "exit")
            messagebox.showinfo('Water drinking time  #', "Please do some eye exercise it's past an hour ")
            init_eyes = time.time()
            log("Eyes moved at")

        elif time.time() - init_exercise >  exer :
            print('Exercise time  #')
            musicloops("C:/Users/Dev Gupta/Downloads/Gym.mp3", "exit")
            messagebox.showinfo('Water drinking time  #', "Please do some workout it's past an hour and half")
            init_exercise = time.time()
            log("Exercise done at")
