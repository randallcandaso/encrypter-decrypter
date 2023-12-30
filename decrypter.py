def main():
    '''
    This function asks the user for the encrypted file,
    along with its index file. It will then send those
    inputs into the insert() function.
    '''
    decrypt = input('Enter the name of an encrypted text file:\n')
    index = input('Enter the name of the encryption index file:\n')
    insert(decrypt, index)

def insert(decrypt, index):
    '''
    This function takes the two files and organizes them
    into new lists.
    :param decrypt: This parameter takes from
    the user's inputted encrypted file.
    :param index: This parameter takes from
    the user's inputted index file.
    '''
    file = open(decrypt, 'r')
    file_2 = open(index, 'r')
    lines = file.readlines()
    lines_2 = file_2.readlines()
    i = 0
    count_2 = []
    while i < len(lines):
        count_2 += lines_2[i]
        i += 1
    list(lines, count_2)

def list(count, count_2):
    '''
    This function takes the new lists and filters them.
    For the second parameter, it will filter out the
    index values that are not deemed numeric.
    :param count: this parameter contains a list
    of the encrypted content
    :param count_2: this parameter contains a list
    of the index file's content
    '''
    new = ''
    new_2 = []
    for i in (count_2):
        new += i
    blank = new.split('\n')
    for i in (blank):
        if i.isnumeric() == False:
            blank.remove(i)
    for i in (blank):
        new_2.append(int(i))
    organize(count, new_2)

def organize(count, new_2):
    '''
    This function takes the index values and the encrypted info
    that matches it, and organizes them into proper order.
    :param count: this parameter contains a list
    of the encrypted content
    :param new_2: this parameter contains the list
    of numeric indexes
    '''
    new_3 = ''
    i = 0
    while i < len(count):
        minimum = min(new_2)
        j = 0
        z = 0
        while z < len(new_2):
            if new_2[z] != minimum:
                j += 1
            elif new_2[z] == minimum:
                z = len(new_2)
            z += 1
        new_3 += count[j]
        new_2[j] = 100
        i += 1
    write(new_3)

def write(list):
    '''
    This function takes the newly created list that
    was put into order and writes it into a new file
    for the user.
    :param list: this parameter pertains to the new
    list created, which was put into order according
    to the index values
    '''
    file = open('decrypted.txt', 'w')
    file.write(str(list))
    file.close()

main()
