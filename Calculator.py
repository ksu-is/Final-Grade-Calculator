#These variables are needed to make local variables in functions global
custom_end=''
homework_end=''
assignment_end=''
test_end=''
quiz_end=''
final_end=''
def quizzes():
    while True:
        quiz_weight=input('How much does your quizzes weigh? or if not applicable type n/a ')
        if quiz_weight=='n/a':
            Menu()
        elif quiz_weight.isdigit()==False:
            print('Please use a integer')
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
#This allows the user to input grades and have the iterrated and added to a list for future reference
                    quiz_weighp=int(quiz_weight)/100
# Quiz_weighp converts the category weight from an integer to a float
                    quiz_total=sum(quiz_value)
# Adds all the inputted quiz grades
                    quiz_final=quiz_total/int(quiz_amount)
# Divides the sum of all the quiz grades by the amount resulting in the final grade for the category excluding its weight
                    global quiz_end
                    quiz_end=int(quiz_final)*float(quiz_weighp)
#  Multiplies the final grade of the cateogry to corresponding weight to output how much this category affects the final grade
                    print('Your quizzes are worth',quiz_end,'%', 'of your grade')
                    Menu()
                
def Test():
    while True:
        test_weight=input('How much does your Test weigh? or if not applicable type n/a ')
        if test_weight=='n/a':
            Menu()
        elif test_weight.isdigit()==False:
            print('Please use a integer')
        else:
            while True:
                test_amount=input('How many test have you taken? ')
                if test_amount.isdigit()==False:
                    print('Please use a integer')
                else:
                    test_value=[]
                    for scores in range(int(test_amount)):
                        test_scores=int(input('Please insert scores one at a time '))
                        test_value.append(test_scores)
                    test_weighp=int(test_weight)/100
                    test_total=sum(test_value)
                    test_final=test_total/int(test_amount)
                    global test_end
                    test_end=int(test_final)*float(test_weighp)
                    print('Your test grades are worth',test_end,'%', 'of your grade')
                    Menu()

def assignments():
    while True:
        assignment_weight=input('How much does your assignments weigh? or if not applicable type n/a ')
        if assignment_weight=='n/a':
            Menu()
        elif assignment_weight.isdigit()==False:
            print('Please use a integer')
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
                    assignment_weighp=int(assignment_weight)/100
                    assignment_total=sum(assignment_value)
                    assignment_final=assignment_total/int(assignment_amount)
                    global assignment_end
                    assignment_end=int(assignment_final)*float(assignment_weighp)
                    print('Your assignment grades are worth',assignment_end,'%', 'of your grade')
                    Menu()
def homework():
    while True:
        homework_weight=input('How much does your homework weigh? or if not applicable type n/a ')
        if homework_weight=='n/a':
            Menu()
        elif homework_weight.isdigit()==False:
            print('Please use a integer')
        else:
            while True:
                homework_amount=input('How much homework have you done? ')
                if homework_amount.isalpha()==True:
                    print('Please use a integer')
                else:
                    homework_value=[]
                    for scores in range(int(homework_amount)):
                        homework_scores=int(input('Please insert scores one at a time '))
                        homework_value.append(homework_scores)
                    homework_weighp=int(homework_weight)/100
                    homework_total=sum(homework_value)
                    homework_final=homework_total/int(homework_amount)
                    global homework_end
                    homework_end=int(homework_final)*float(homework_weighp)
                    print('Your homework grades are worth',homework_end,'%', 'of your grade')
                    Menu()
def custom():
    custom_list=[]
    custom_scores=[]
    global custom_end
    def customs(name,weight,amount):
        print('so the category is', name,'with a', weight, '%', 'and a total of', amount  )
        for numbers in range(int(amount)):
            scores=int(input('please provide your scores for this category'))
            custom_scores.append(scores)
        weigh_percentage=int(weight)/100
        custom_totalgrades=sum(custom_scores)
        custom_final=custom_totalgrades/int(amount)
        custom_endd=int(custom_final)*float(weigh_percentage)
        custom_list.append(custom_endd)
    while True:
        custom_amount=input('How many custom categories would you like to add? or enter n/a to return to menu ')
        if custom_amount=='n/a':
            Menu()
        elif custom_amount.isalpha()==True:
            print('Please use a integer or decimal ')
        else:
            for numbers in range(int(custom_amount)):
                custom_name=input('Please provide a name for the category')
                if custom_name.isdigit()==True:
                    print("Please use letters only")
                else:
                    custom_weight=input('Enter the weight of this category ')
                    if custom_weight.isalpha()==True:
                        print('Please use an integer')
                    else:
                        number_custom_grades=input('Please provide the number assignments completed for this category ')
                        if number_custom_grades.isalpha()==True:
                            print('Please use an integer')
                        else:
                            customs(custom_name,custom_weight,number_custom_grades)
                            print(custom_list)
                            custom_end=sum(custom_list)
                            
                                           
    
               


       
if custom_end=="":
        custom_end=0
elif custom_end>-1:
        custom_end=custom_end
if homework_end=='':
    homework_end=0
elif homework_end>-1:
    homework_end=homework_end
if test_end=='':
    test_end=0
elif test_end=='':
    test_end=test_end
if quiz_end=="":
    quiz_end=0
elif quiz_end>-1:
    quiz_end=quiz_end
if assignment_end=='':
    assignment_end=0
elif assignment_end>-1:
    assignment_end=assignment_end
if final_end=='':
    final_end=0
elif final_end>-1:
    final_end=final_end
# The code above allows the function final grade to determine which categories to use. If the user did not insert any grade in a category, it will default to a 0    
def final():
    global final_end
    final_end=custom_end+homework_end+test_end+assignment_end+quiz_end+homework_end
    print( 'Your final Grade is',final_end,'%')
    Menu()

def Menu():
    print("Hello, welcome to the Will I fail Calculator")
    print('1 Grade Quizzes Current grade is',quiz_end,'%')
    print('2 Grade Test Current grade is',test_end,'%')
    print('3 Grade assignments Current grade is',assignment_end,'%')
    print('4 Grade homework Current grade is',homework_end,'%')
    print('5 Grade custom Current grade is',custom_end,'%')
    print('6 Calculate Final Grade (all other pertaining grades have to be filled before hand) Current final grade is', final_end,'%')
    print('7 Close program')
    Grader=input('Please Choose a category to start with by entering any of the following numbers ')
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
    elif Grader=='7':
        exit
    else:
        print('that is not one of the options')
        Menu()


Menu()