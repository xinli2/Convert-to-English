###
### Author: Xin Li
### In this short PA, i will be writing a
### program that can convert words from
### non-English to their English form. The
### program will accept two inputs via the console.
### The first input will be the name of a file which
### has English words and words that mean the same
### thing from other language(s).
### The second input is a word in a non-English
### language, which should be converted to English.
###
###
def get_word_conversions(words_file_name):
    file = open(words_file_name, 'r')
    conversions = { }
    lines = file.readlines()
    for line in lines:
        line = line.split(',')
        line[len(line)-1]= line[len(line)-1][:len(line[len(line)-1])-1]
        for i in range(len(line)):
            conversions[line[i]] = line[0]
    return conversions


def print_conversion(word, conversions):
    print()
    if word in conversions:
        print('English version is:',conversions[word])
    else:
        print('Not sure.')

def main():
    file_name = input('Enter name of words file:\n')
    conversions = get_word_conversions(file_name)

    word = input('Enter word to convert to English:\n')
    print_conversion(word, conversions)

main()
