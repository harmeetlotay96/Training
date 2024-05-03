# Added this comment to show changes in git hub
with open('DrSeus.txt', 'r', encoding='latin-1') as my_file: # closes the file 
    my_poem = my_file.read()
    print(my_poem)


with open('DrSeus.txt', 'r', encoding='latin-1') as my_file2:
    for line in my_file2:
        print(line.rstrip('\n')) 
        my_new_line = line.lower().replace('you ', 'me ')
        if 'you' not in line.lower():
            print(line, end="") # both works
