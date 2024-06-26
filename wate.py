import time
import winsound

print("Water reminder script \n")
interval = int(input("Enter interval in minutes: ")) * 60 

while True:
    countdown = interval  
    while countdown:
        mins, secs = divmod(countdown, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        countdown -= 1

    winsound.Beep(2000,1000)
    print("\nTime to drink water! Interval reset.")
