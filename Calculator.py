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

def assignments():
    while True:
        assignment_weight=input('How much does your assignments weigh? or if not applicable type n/a ')
        if assignment_weight.isdigit():
            print('Please use a decimal')
        elif assignment_weight.isalpha():
            print('Please use a decimal')
        elif assignment_weight=='n/a':
            Menu()
        else:
            while True:
                assignment_amount=input('How many quizzes have you taken? ')
                if assignment_amount.isdigit()==False:
                    print('Please use a integer')
                else:
                    assignment_value=[]
                    for scores in range(int(assignment_amount)):
                        assignment_scores=int(input('Please insert scores one at a time '))
                        assignment_value.append(assignment_scores)
                    assignment_total=sum(assignment_value)
                    assignment_final=assignment_total/int(assignment_amount)
                    print('Your assignment grades are worth',assignment_final,'%', 'of your grade')
                    Menu()

def Menu():
    print("Hello, welcome to the Will I fail Calculator")
    print('Please Choose a category to start with')
    Grader=input('Press \n 1 Grade quizzes \n 2 Grade test \n 3 Grade assignments \n 4 Grade homework \n 5 Grade Custom Category \n 6 for final grade (Must have all pertainig grades calculated before use) \n ')
    if Grader=='1':
        quizzes()
    elif Grader=='2':
        Test()
    elif Grader=='3':
        assignments()
    elif Grader=='4':
        homework()
    elif Grader=='5':
        custom()
    elif Grader=='6':
        final()
    else:
        print('that is not one of the options')
        Menu()


Menu()