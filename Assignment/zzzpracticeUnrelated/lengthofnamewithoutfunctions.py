

def length_of_character(letters):
    count = 0
    for _ in letters:
        count+=1
    return count

name = input('Enter a word: ')
lengths = length_of_character(name)
print(lengths)
