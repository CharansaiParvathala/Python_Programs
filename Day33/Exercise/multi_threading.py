import threading

def count_char(char):
    global w
    c = 0
    for l in w:
        if char == l:
            c +=1
    return c

def count_word(word):
    global s
    c = 0
    for w in s:
        if w == word:
            c += 1
    return c

w = input('Enter word:')
s = input('Enter sentence:').split()

m1 = threading.Thread(target=count_char, args=('a',))
m2 = threading.Thread(target=count_word, args=("bro",))

m1.start()
m2.start()

m1.join()
m2.join()

print('chars =', count_char('a'))
print('words =', count_word('bro'))
