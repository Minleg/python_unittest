def is_correct_answer(user_answer, correct_answer):
    """ Check if user's answer is the same as the correct
    answer, ignoring case """

    string_correct_answer = str(correct_answer).lower()
    string_user_answer = str(user_answer).lower()
    return string_user_answer == string_correct_answer


    # If you accidentally used the same variable name
    # twice in the comparison, for example

    # return string_user_answer == string_user_answer

    # the tests will catch the error, you'll see test fails
    # breaking code that works is called a regression


def main():
    question = 'How many senators in the US senate?'
    answer = 100

    print(question)
    user_answer = input('What is your answer? ')
    
    if is_correct_answer(user_answer, answer):
        print('Correct!')
    else:
        print(f'Sorry, the answer is {answer}')


if __name__ == '__main__':
    main()