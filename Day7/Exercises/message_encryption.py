import random
import string

def encrypt_msg(user_text):
	encrypt = list(' ' + string.punctuation + string.ascii_letters)
	copied_encrypt = encrypt.copy()

	random.shuffle(encrypt)
	encrypted_text = ""
	for character in user_text:
		index = copied_encrypt.index(character)
		encrypted_text += encrypt[index]
	return  encrypted_text, encrypt,copied_encrypt

def decode():

	message = ""
	for character in encrypted_text:
		index = decode_key.index(character)
		message = message + copy[index]
	return message
	
	
encrypted_text, decode_key, copy = encrypt_msg(input("Enter A Text To Encrypt : "))
print("\nEncrypted Message :",encrypted_text)


decode_message = decode()
print('\nDecoded Message Message : ',decode_message)
