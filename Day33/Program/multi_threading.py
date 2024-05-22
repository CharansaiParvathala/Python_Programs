import threading
import time


def numbers():
    for i in range(5):
        time.sleep(1)
        print(i + 1)


def letter():
    l = ["a", "b", "c", "d", "e"]
    for i in l:
        print(i)
        time.sleep(1)


x = threading.Thread(target=numbers)

y = threading.Thread(target=letter)

x.start()
y.start()