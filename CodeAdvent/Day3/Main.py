#!/usr/bin/env python
count_same = 0


def main():
    inputFile = open('./input.txt')
    claims_word = []
    matrix = [['.' for i in range(1000)] for j in range(1000)]

    for claim in inputFile.readlines():
        claims_word.append(claim.strip())

    for claim_word in claims_word:
        claim_word = claim_word.replace('#', '').replace('@', '').replace(',', ' ').replace(':', '').replace('x', ' ').replace('  ', ' ')
        claim_digits = claim_word.split(' ')

        execute_claim(claim_digits, matrix)
        print(claim_digits)
    print_matrix(matrix)
    print(count_same)


def print_matrix(_matrix):
    for x in range(len(_matrix)):
        for y in range(len(_matrix[x])):
            print(_matrix[x][y], end='')
        print()


def execute_claim(claim, _matrix):
    global count_same
    char = str(claim[0])
    margin_left = int(claim[1])
    margin_top = int(claim[2])
    wide = int(claim[3])
    tall = int(claim[4])
    count_tall = 0
    for y in range(margin_top, len(_matrix)):
        count_wide = 0
        for x in range(margin_left, len(_matrix[y])):
            if count_wide < wide and count_tall < tall:
                if _matrix[y][x].isdigit():
                    _matrix[y][x] = 'X'
                    count_same += 1
                else:
                    _matrix[y][x] = char
                count_wide += 1
        count_tall += 1


if __name__ == '__main__':
    main()
