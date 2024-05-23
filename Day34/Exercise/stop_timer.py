import threading
import time
def ready():
    for t in range(3,0,-1):
        time.sleep(1)
        print(f'Timer starts in *{t}sec*')
def start_timer():
    t = 0.0
    while True:
        print(f'{t:,.1f}sec')
        t +=0.1
        time.sleep(0.1)
print('Once timer starts press enter to stop time')
notify = threading.Thread(target=ready)
notify.start()
notify.join()
timer = threading.Thread(target=start_timer, daemon=True)
t = timer.start()
input()
