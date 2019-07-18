# Caesar Cipher Hacker
MAX_KEY_SIZE = 26

# Upgraded to python3
from nltk.corpus import wordnet

def get_mode():
     while True:
         mode = input('Do you wish to encrypt or decrypt a message?')
         if mode in 'encrypt, decrypt, e, d':
             return mode
         else:
             print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def get_message():
        return input('Enter your message:')

def get_key():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def get_translated_message(mode, message, key):
    print("Key = %d" % key)
    if mode[0] == 'd':
        key = -key
        return shift_chars(message, key)
    else:
        return shift_chars(message, key)

def shift_chars(message, key):
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

def count_real_words(encrypted_message, key):
    key = -key
    english_word_count = 0
    for encrypted_word in shift_chars(encrypted_message, key).split():
        if wordnet.synsets(encrypted_word):
            english_word_count += 1
    return english_word_count

mode = get_mode()
message = get_message()


if 'd' in mode :
    words_found = 0
    best_key = 0
    for key in range(0,26,1):
        if count_real_words(message, key) > words_found:
            words_found = count_real_words(message, key)
            best_key = key

    print("Found best key of: " + str(best_key))
    print(get_translated_message(mode, message, best_key))

elif 'e' in mode:
    key = get_key()
    print(get_translated_message(mode,message,key))
