#!/usr/bin/env python3

import random
import sys


def print_stats(correct_answers, incorrect_answers):
    if correct_answers == 0 and incorrect_answers == 0:
        print('No answers yet')
        return
    print(f'-- Correct: {correct_answers}.')
    percent_incorrect = (incorrect_answers /
        (correct_answers + incorrect_answers) * 100)
    print(f'-- Incorrect: {incorrect_answers} ({percent_incorrect:.0f}%)')


def main():
    print('Multiplication trainer (x to exit, p to print statistics).')
    correct_answers = 0
    incorrect_answers = 0
    random.seed()
    while True:
        m1 = random.randint(2,9)
        m2 = random.randint(2,9)
        if m1 > m2:
            tmp = m1
            m1 = m2
            m2 = tmp
        answer = None
        while not answer:
            str_answer = 'p'
            while str_answer == 'p':
                str_answer = input(f'{m1} * {m2} = ')
                if str_answer == 'p':
                    print_stats(correct_answers, incorrect_answers)
            if str_answer == 'x':
                print_stats(correct_answers, incorrect_answers)
                return 0
            try:
                answer = int(str_answer)
            except ValueError:
                print('Enter an integer or \'x\' to exit ' +
                      '(\'p\' to print statistics)')
                answer = None
        if answer == m1 * m2:
            print('Correct!')
            correct_answers += 1
        else:
            print('No, the correct answer is {}.'.format(m1 * m2))
            incorrect_answers += 1


if __name__ == '__main__':
    sys.exit(main())
