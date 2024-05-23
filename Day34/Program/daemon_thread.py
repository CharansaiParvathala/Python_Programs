import threading as t
import time
def timer():
    c = 0
    while True:
        print(c)
        c += 1
        time.sleep(0.5)
x = t.Thread(target=timer, daemon=True)
x.start()
input("Enter something : ")