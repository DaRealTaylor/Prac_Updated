from string import ascii_lowercase
string = input("enter a word")


def count_letters(string):
    count = 0
    for character in string.lower():
        if character in ascii_lowercase:
            count += 1
        print (count)
