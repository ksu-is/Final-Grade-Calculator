custom_end=''
homework_end=''
assignment_end=''
test_end=''
quiz_end=''
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
                    global quiz_end
                    quiz_end= int(quiz_final)*float(quiz_weight)
                    print('Your quizzes are worth',quiz_end,'%', 'of your grade')
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
                test_amount=input('How many test have you taken? ')
                if test_amount.isdigit()==False:
                    print('Please use a integer')
                else:
                    test_value=[]
                    for scores in range(int(test_amount)):
                        test_scores=int(input('Please insert scores one at a time '))
                        test_value.append(test_scores)
                    test_total=sum(test_value)
                    test_final=test_total/int(test_amount)
                    global test_end
                    test_end=int(test_final)*float(test_weight)
                    print('Your test grades are worth',test_end,'%', 'of your grade')
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
                assignment_amount=input('How many assignments have you done? ')
                if assignment_amount.isdigit()==False:
                    print('Please use a integer')
                else:
                    assignment_value=[]
                    for scores in range(int(assignment_amount)):
                        assignment_scores=int(input('Please insert scores one at a time '))
                        assignment_value.append(assignment_scores)
                    assignment_total=sum(assignment_value)
                    assignment_final=assignment_total/int(assignment_amount)
                    global assignment_end
                    assignment_end=int(assignment_final*float(assignment_weight))
                    print('Your assignment grades are worth',assignment_end,'%', 'of your grade')
                    Menu()
def homework():
    while True:
        homework_weight=input('How much does your homework weigh? or if not applicable type n/a ')
        if homework_weight.isdigit():
            print('Please use a decimal')
        elif homework_weight.isalpha():
            print('Please use a decimal')
        elif homework_weight=='n/a':
            Menu()
        else:
            while True:
                homework_amount=input('How much homework have you done? ')
                if homework_amount.isdigit()==False:
                    print('Please use a integer')
                else:
                    homework_value=[]
                    for scores in range(int(homework_amount)):
                        homework_scores=int(input('Please insert scores one at a time '))
                        homework_value.append(homework_scores)
                    homework_total=sum(homework_value)
                    homework_final=homework_total/int(homework_amount)
                    global homework_end
                    homework_end=int(homework_final)*homework_weight
                    print('Your homework grades are worth',homework_end,'%', 'of your grade')
                    homework_end=int(homework_final)*float(homework_weight)
                    print('Your homework grades are worth',homework_end,'%', 'of your grade')
                    return homework_end
                    Menu()
def custom():
    questc=input('What is this category called')
    while True:
        custom_weight=input('How much does' 'weigh? or if not applicable type n/a ')
        if custom_weight.isdigit():
            print('Please use a decimal')
        elif custom_weight.isalpha():
            print('Please use a decimal')
        elif custom_weight=='n/a':
            Menu()
        else:
            while True:
                custom_amount=input('How many' 'are there? ')
                if custom_amount.isdigit()==False:
                    print('Please use a integer')
                else:
                    custom_value=[]
                    for scores in range(int(custom_amount)):
                        custom_scores=int(input('Please insert scores one at a time '))
                        custom_value.append(custom_scores)
                    custom_total=sum(custom_value)
                    custom_final=custom_total/int(custom_amount)
                    global custom_end
                    custom_end=int(custom_final)*float(custom_weight)
                    print('Your' 'grades are worth',custom_end,'%', 'of your grade')
                    Menu()

if custom_end=="":
        custom_end=0
elif custom_end>1:
        custom_end=custom_end
if homework_end=='':
    homework_end=0
elif homework_end>1:
    homework_end=homework_end
    
def final():
    print(custom_end+homework_end)

        
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