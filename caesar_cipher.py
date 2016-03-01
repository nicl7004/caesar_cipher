#Nicholas Clement
#2/29/16

key_size = 26

def decrypt_or_encrypt():
    while True:
        print('Do you want to decrypt or encrypt? (d for decrypt e for encrypt')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Please type "d" or "e".')
def recieveMessage():
    print('Please enter your message:')
    return input()
def recieveKey():
    key = 0
    while True:
        print('Enter the key number (1-%i)' (key_size))
        key = int(input())
        if (key >= 1 and key <= key_size):
            return key
def breakCipher(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():




