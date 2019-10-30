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
                    quiz_value=[]
                    for scores in range(int(quiz_amount)):
                        quiz_scores=int(input('Please insert scores one at a time '))
                        quiz_value.append(quiz_scores)
                    quiz_total=sum(quiz_value)
                    quiz_final=quiz_total/int(quiz_amount)
                    print('Your quizzes are worth',quiz_final,'%', 'of your grade')
                    Menu()
                
def Test():
    while True:
        test_weight=input('How much does your Test weigh? or if not applicable type n/a ')
        if test_weight.isdigit():
            print('Please use a decimal')
        elif test_weight.isalpha():
            print('Please use a decimal')
        elif test_weight=='n/a':
            Menu()
        else:
            while True:
                test_amount=input('How many quizzes have you taken? ')
                if test_amount.isdigit()==False:
                    print('Please use a integer')
                else:
                    test_value=[]
                    for scores in range(int(test_amount)):
                        test_scores=int(input('Please insert scores one at a time '))
                        test_value.append(test_scores)
                    test_total=sum(test_value)
                    test_final=test_total/int(test_amount)
                    print('Your test grades are worth',test_final,'%', 'of your grade')
                    Menu()



def Menu():
    print("Hello, welcome to the Will I fail Calculator")
    print('Please Choose a category to start with')
    Grader=input('Press \n 1 grade quizzes \n 2 grade test \n 3 grade assignments \n 4 grade homework \n 5 for other \n 6 for final grade \n ')
    if Grader=='1':
        quizzes()
    elif Grader=='2':
        Test()


Menu()