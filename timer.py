import time
seconds = input("Enter the time in the number of seconds")
def countDown_timer(seconds):
    while seconds >0 :
        
        mins = int(seconds/60)
        secs = int(seconds%60)
        timer = f'{mins}:{secs}'
        print(timer)
        time.sleep(1)
        seconds-=1
    print("Time Up!")
    
countDown_timer(int(seconds))