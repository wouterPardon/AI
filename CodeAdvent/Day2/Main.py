#!/usr/bin/env python
inputFile = open('./input.txt')
lines = []
counts_per_word = []
global_count_two = 0
global_count_three = 0


def main():

    for line in inputFile.readlines():
        lines.append(line.strip())

    for word in lines:
        count_same_letters_in_word(word)

    print(lines)
    print(global_count_two, ' ', global_count_three)
    print(global_count_two * global_count_three)


def count_same_letters_in_word(word):
    global global_count_two
    global global_count_three
    count_letter = []

    for letter in word:
        count = word.count(letter)
        word = word.replace(letter, '')
        if count == 2 or count == 3:
            count_letter.append(count)

        print(count_letter)

    if 2 in count_letter:
        global_count_two += 1
    if 3 in count_letter:
        global_count_three += 1


if __name__ == '__main__':
    main()




