#!/usr/bin/env python
inputFile = open('./input.txt')
words = []


def main():
    for word in inputFile.readlines():
        words.append(word.strip())

    check(words)


def check(word_list):
    done = False

    for word in word_list:
        for _word in word_list:
            count = 0
            all_same_chars = []
            if not done:
                for i in range(len(_word)):
                    if _word[i] == word[i]:
                        count += 1
                        all_same_chars.append(_word[i])

                if count == 25:
                    print(word, _word, count, all_same_chars)
                    for char in all_same_chars:
                        print(char, end='')
                    done = True


if __name__ == '__main__':
    main()




