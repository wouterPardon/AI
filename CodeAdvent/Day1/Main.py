#!/usr/bin/env python
inputFile = open('./input.txt')
changes = []
current_frequency = 0
count = 0
all_frequencies = []


def main():
    global current_frequency
    global count

    for line in inputFile.readlines():
        changes.append(int(line.strip()))

    for change in changes:
        current_frequency += change
        all_frequencies.append(current_frequency)

    all_frequencies.remove(current_frequency)
    print(all_frequencies)
    while current_frequency not in all_frequencies:
        for change in changes:
            current_frequency += change
            if current_frequency in all_frequencies:
                break

    print(current_frequency)


if __name__ == '__main__':
    main()




