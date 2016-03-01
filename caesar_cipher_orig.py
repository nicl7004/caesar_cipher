# Nicholas Clement
# 2/29/16
# Breaking a caesar cipher with brute force


cipher = open('cipher.txt', 'r')  # open the text containing the message to decrypt
solved = open('answer.txt', 'w')  # open the file to write the answer to.
alphabet = 'abcdefghijklmnopqrstuvwxyz'

print cipher.read()  # Print cipher

# Since we know it is a caesar cipher we can just loop through 26 different possible shifts
# this is the brute force method

for key in range(len(alphabet)):
    #print('in the first for loop')
    translation = ''

    for letter in cipher:
        print('in the second for loop')
        if letter in alphabet:
            number = alphabet.find(letter)
            number = number - key

        # for the case if number is 26 or larger or less than 0

            if number < 0:
                print('in the second if statement')
                number = number + len(alphabet)

            translation = translation + alphabet[number]

        else:
            translation = translation + symbol
print('Key #%s: %s' % (key, translation))
solved.write('Key #%s: %s' % (key, translation))
