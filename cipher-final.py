# Caesar Cipher Hacker
MAX_KEY_SIZE = 26

# Upgraded to python3
from nltk.corpus import wordnet
import time


def get_mode():
     while True:
         mode = input('Do you wish to encrypt or decrypt a message?')
         if mode in 'encrypt, decrypt, e, d':
             return mode
         else:
             print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def get_cipher():
    while True:
        cipher = input('What cipher would you like to use? Caesar or Vignere? (Enter c for Caesar or v for Vingnere)')
        if cipher in 'caesar, vignere, c, v':
            return cipher
        else:
            print('Invalid cipher, please choose c or v.')

def get_message():
        return input('Enter your message:')

def get_key_caesar():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def get_vignere_key():
    while True:
        print('Enter the key string')
        key = input()
        return key


def get_translated_message_caesar(mode, message, key):
    print("Key = %d" % key)
    if mode[0] == 'd':
        key = -key
        return shift_chars_caesar(message, key)
    else:
        return shift_chars_caesar(message, key)

def shift_chars_caesar(message, key):
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated

def get_translated_message_vignere(mode, message, key):
    return shift_chars_vignere_to_cipher(message, key)

def shift_chars_vignere_to_cipher(message, key):
    key = generate_key_vignere(message, key)
    cipher_text = []
    for i in range(len(message)):
        if message[i] == " ":
            cipher_text.append(" ")
        else:
            x = (ord(message[i]) +
                 ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
    return("" . join(cipher_text))

def shift_chars_vignere_from_cipher(cipher_text, key):
    key = generate_key_vignere(cipher_text, key)
    orig_text = []
    for i in range(len(cipher_text)):
        if cipher_text[i] == " ":
            orig_text.append(" ")
        else:
            x = (ord(cipher_text[i]) -
                 ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
    return("" . join(orig_text))

def decrypt_vignere_cipher(message):
    password = dict_attack(message)
    print("Password found from dict attack was: " + str(password))
    print("Decrypted message was: " + str(shift_chars_vignere_from_cipher(message, password)))

start_dict_time = time.time()
def dict_attack(message):
    password_file = open("rockyou.txt", "r", encoding='utf-8', errors='ignore')
    passwords = password_file.read().split('\n')

    best_password = ""
    best_password_score, password_count = 0, 0

    for password in passwords:
        if password and " " not in password :
            dict_run_time = time.time()

            #Print some metrics to see how execution is going
            if (password_count % 50000 == 0):
                print(str(round(password_count/len(passwords), 2) * 100) + " percent complete.")
                print("Execution time is: " + str(dict_run_time -  start_dict_time))
            password_count += 1
            # print("Trying password: " + str(password))
            extracted_text = shift_chars_vignere_from_cipher(message, password)
            password_score = count_real_words_decrypted(extracted_text, password)
            # Now update our best password
            if password_score > best_password_score:
                best_password = password
                best_password_score = password_score

                if best_password_score > 2:
                    print("Found two words decoded from the password: " + best_password)
                    return best_password
    return best_password


def generate_key_vignere(string, key):
    key = list(key)
    for i in range(len(string) - len(key)):
        if key[i] != " ":
            key.append(key[i])
    return("" . join(key))

def count_real_words_decrypted(plain_text, key):
    english_word_count = 0
    for encrypted_word in plain_text.split():
        if wordnet.synsets(encrypted_word):
            english_word_count += 1
    return english_word_count

def count_real_words(encrypted_message, key):
    key = -key
    english_word_count = 0
    for encrypted_word in shift_chars_caesar_caesar(encrypted_message, key).split():
        if wordnet.synsets(encrypted_word):
            english_word_count += 1
    return english_word_count

test_message = "TWO WORD TEST"
test_password = "password"

vcipher = shift_chars_vignere_to_cipher(test_message, test_password)
print(vcipher)
vplaintext = shift_chars_vignere_from_cipher(vcipher, test_password)
print(vplaintext)


mode = get_mode()
message = get_message()
cipher = get_cipher()

start_time = time.time()

if 'd' == mode or 'decrypt' in mode:
    words_found = 0
    best_key = 0

    if cipher == 'c' or cipher == 'caesar':
        for key in range(0,26,1):
            if count_real_words(message, key) > words_found:
                words_found = count_real_words(message, key)
                best_key = key

        print("Found best key of: " + str(best_key))
        print(get_translated_message_caesar(mode, message, best_key))
    elif cipher == 'v' or cipher == 'vignere':
        decrypt_vignere_cipher(message)

elif 'e' in mode or 'encrypt' in mode:
    if cipher == 'c' or cipher == 'caesar':
        key = get_key_caesar()
        print(get_translated_message_caesar(mode,message,key))
    elif cipher == 'v' or cipher == 'vignere':
        key = get_vignere_key()
        print(get_translated_message_vignere(mode, message, key))

end_time = time.time()
print("Computation time is:" + str(end_time - start_time))
