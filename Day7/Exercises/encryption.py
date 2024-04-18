import random
import string

encrypt = list(' ' + string.punctuation + string.ascii_letters)
copied_encrypt = encrypt.copy()

random.shuffle(encrypt)

user_text = input("Enter A Text To Encrypt : ")
encrypted_text = ''

for character in user_text:
	index = copied_encrypt.index(character)
	encrypted_text += encrypt[index]
	
print("\nEncrypted Message : "+encrypted_text)
print('DisEncrypted Message : ',end='')
for character in encrypted_text:
	index = encrypt.index(character)
	letter = copied_encrypt[index]
	print(letter,end='')
