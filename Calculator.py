
def quizzes():
    while True:
        quiz_weight=input('How much does your quizzes weigh? or if not applicable type n/a ')
        if quiz_weight.isdigit():
            print('Please use a decimal')
        elif quiz_weight.isalpha():
            print('Please use a decimal')
        elif quiz_weight=='n/a':
            Menu()
        else:
            while True:
                quiz_amount=input('How many quizzes have you taken? ')
                if quiz_amount.isdigit()==False:
                    print('Please use a integer')
                elif quiz_amount.isalpha():
                    print('Please use an integer')
                else:
                    while True:
                        quiz_scores=input('Please insert all your quizz scores, and once finished press "F" ')
                        if quiz_scores=='F':
                            Menu()
                        elif quiz_scores.isdigit==False:
                            print('Please use integer')

def Menu():
    print("Hello, welcome to the Will I fail Calculator")
    print('Please Choose a category to start with')
    Grader=input('Press \n 1 grade quizzes \n 2 grade test \n 3 grade assignments \n 4 grade homework \n 5 for other \n 6 for final grade \n ')
    if Grader=='1':
        quizzes()

Menu()

