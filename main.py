'''v1 - bedc7c4 - 10/01/22 - problems and upgrades
1 - Create functions to operate system
2 - Win game message and system
3 - Multiple letters in correct_answer'''

from q_and_a import *
from random import randint

attempts = 5
letters_tried = []

def main():

    print('Welcome to Hangman Game!')

    diff_selected = int(input('1 - EASY 2 - MEDIUM 3 - HARD \n SELECT DIFFICULT: '))

    # if diff_selected != 1 or 2 or 3:
    #     print('Difficult not exist. Try again.')
    #     diff_selected = int(input('1 - EASY 2 - MEDIUM 3 - HARD \n SELECT DIFFICULT: '))

    sort_quest = randint(0, len(q_and_a[diff_selected - 1]) -1)
    question_answer = q_and_a[diff_selected - 1][sort_quest]
    question = question_answer[0]
    correct_answer = [x for x in str.lower(question_answer[1])]
    answer_scope = ['_' for _ in range(len(question_answer[1]))]
 

    print(question)
    print(' '.join(answer_scope))

    def attempt():

        global attempts
        letter = input(f'You got {attempts} tries. Try a letter: ').lower()

        if letter in correct_answer:
            count = 0
            indexes = []

            print(f'There is "{letter}" in answer!')

            for x in correct_answer:
                if x == letter:
                    indexes.append(count)
                count += 1

            for idx, _ in enumerate(answer_scope):
                if idx in indexes:
                    answer_scope[idx] = letter
            
            print(' '.join(answer_scope))
            print(' '.join(correct_answer))

            if (' '.join(answer_scope)) == ' '.join(correct_answer):

                print("Congratulations! You've been save!")

                action1 = input('Want play again? s/n ').lower()

                if action1 == 's':
                    main()
                else:
                    exit()

            attempt()
        
        elif letter in letters_tried:

            print('You already tried this letter. One try out.')

            if attempts == 0:

                print("5 of 5 mistakes. You've been hanged.")
                action1 = input('Want play again? s/n ').lower()

                if action1 == 's':
                    main()
                else:
                    exit()

            else:

                attempts -= 1
                print(f'One out. You have {attempts} left.')

        else:

            letters_tried.append(letter)

            if attempts == 0:

                print("5 of 5 mistakes. You've been hanged.")
                action1 = input('Want play again? s/n ').lower()

                if action1 == 's':
                    main()
                else:
                    exit()

            else:

                attempts -= 1
                print(f'One out. You have {attempts} left.')

            attempt()

    print(attempt())


if __name__ == '__main__':
    main()
