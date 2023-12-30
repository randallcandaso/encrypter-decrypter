import random

def main():
    '''
    This function prompts the user to input a file to encrypt.
    '''
    enter = input('Enter a name of a text file to encrypt:\n')
    random.seed(125)
    insert(enter)

def insert(input):
    '''
    This function takes the inputted file and inserts the
    info into a list. Along with that list, a second list is created
    with matching index values.
    :param input: this pertains to the inputted file in need of
    decryption
    '''
    file = open(input, 'r')
    line = file.readlines()
    count = []
    count_2 = []
    i = 0
    while i < len(line):
        count.append(line[i])
        count_2.append(i + 1)
        i += 1
    randomize(count, count_2)

def randomize(list_1, list_2):
    '''
    This function randomizes the list's original order, creating the encrypted
    effect. Along with the encrypted content of the inputted file, the indexes
    of that content are also randomized.
    :param list_1: This parameter contains the info originally
    contained in the user's file
    :param list_2: This parameter contains the matching indexes
    for the first list.
    '''
    i = 0
    limit = len(list_1) * 5
    while i < limit:
        number_1 = random.randint(0, len(list_1) - 1)
        number_2 = random.randint(0, len(list_1) - 1)
        blank = list_1[number_2]
        list_1[number_2] = list_1[number_1]
        list_1[number_1] = blank
        blank_2 = list_2[number_2]
        list_2[number_2] = list_2[number_1]
        list_2[number_1] = blank_2
        i += 1
    encrypt(list_1, list_2)

def encrypt(list_1, list_2):
    '''
    This function writes the two new lists into two new files. The first
    file is the new encrypted file and the second is an index file
    that can be used as a key.
    :param list_1: this refers to the newly randomized list containing
    the original inputted content
    :param list_2: this list contains the randomized indexes of the
    first list
    '''
    i = 0
    file = open('encrypted.txt', 'w')
    file.close()
    file_2 = open('index.txt', 'w')
    file_2.close()
    limit = len(list_2)
    while i < limit:
        new_1 = open('encrypted.txt', 'a')
        new_1.write(str(list_1[i]))
        new_1.close()
        new_2 = open('index.txt', 'a')
        new_2.write(str(list_2[i]) + '\n')
        new_2.close()
        i += 1

main()
