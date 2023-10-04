#!/usr/bin/env python3

if __name__ == '__main__':
    number_of_students = int(input('Enter number of students: '))
    number_of_labs = (number_of_students / 24)
    remainder = number_of_students % 24

    print((int(number_of_labs), 'full labs, and ', remainder, 'students in left over group'))
