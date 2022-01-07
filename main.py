from questions_and_answers import *
from random import randint

print('Welcome to Hangman Game!')


def main():

    diff = int(input('1 - Easy; 2 - Medium; 3 - Hard\nSelect difficult: '))

    if diff == 1:
        quest = diff_easy[randint(0, len(diff_easy)-1)]
        answer_scope = '_' * len(quest[1])
        answer_list = list('_' for _ in quest[1])
        print(quest[0], '\n', answer_scope)
        shots = 5

        while shots > 0:
            answer = input(f'You have {shots} shots! Try a letter: ')

            if answer in str.lower(quest[1]):
                print(f'There is "{answer}" in answer!')
                indexes = []

                for x in range(len(str.lower(quest[1]))):
                    if str.lower(quest[1][x]) == answer:
                        indexes.append(x)

                for i in indexes:
                    answer_list[i] = answer

                print(''.join(answer_list))

            else:
                print('Wrong! Try again.')
                shots -= 1

        print("You've been hanged!")

    elif diff == 2:
        pass
    elif diff == 3:
        pass
    else:
        print('Difficult not reconized. Try again.')
        main()

if __name__ == '__main__':
    main()
