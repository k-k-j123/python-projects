
import time 
def countdown(t): 
    time.sleep(1)
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer ,end='\r') 
        time.sleep(1) 
        t -= 1
if __name__=="__main__":
    countdown(10*60)
