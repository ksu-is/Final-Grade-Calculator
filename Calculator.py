#These variables are needed to make local variables in functions global
custom_end=''
homework_end=''
assignment_end=''
test_end=''
quiz_end=''
final_end=''
custom_advance_details=''

def quizzes():
    while True:
        quiz_weight=input('How much does your quizzes weigh? or if not applicable type n/a ')
#category_weight ask for the weight of the current category in this case, it would be quizzes
        if quiz_weight=='n/a':
            Menu()
        elif quiz_weight.isdecimal()==False:
            print('Please use a integer')
        else:
            while True:
                quiz_amount=input('How many quizzes have you taken? ')
#ask for the number of assignments completed in this category
                if quiz_amount.isdigit()==False:
                    print('Please use a integer')
                elif quiz_amount.isalpha():
                    print('Please use an integer')
                else:
                    quiz_value=[]
                    for scores in range(int(quiz_amount)):
                        quiz_scores=float(input('Please insert scores one at a time '))
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
                    print('Your quiz average was',quiz_final,"%. Your quizzes weigh", quiz_end,"% of your final grade.")
                    Menu()
# This function is repeated for the other hardcoded categories like test and assignments
                    
                
def Test():
    while True:
        test_weight=input('How much does your Test weigh? or if not applicable type n/a ')
        if test_weight=='n/a':
            Menu()
        elif test_weight.isdecimal()==False:
            print('Please use a integer')
        else:
            while True:
                test_amount=input('How many test have you taken? ')
                if test_amount.isdigit()==False:
                    print('Please use a integer')
                else:
                    test_value=[]
                    for scores in range(int(test_amount)):
                        test_scores=float(input('Please insert scores one at a time '))
                        test_value.append(test_scores)
                    test_weighp=int(test_weight)/100
                    test_total=sum(test_value)
                    test_final=test_total/int(test_amount)
                    global test_end
                    test_end=int(test_final)*float(test_weighp)
                    print('Your test average was',test_final,"%. Your test weigh", test_end,"% of your final grade.")
                    Menu()

def assignments():
    while True:
        assignment_weight=input('How much does your assignments weigh? or if not applicable type n/a ')
        if assignment_weight=='n/a':
            Menu()
        elif assignment_weight.isdecimal()==False:
            print('Please use a integer')
        else:
            while True:
                assignment_amount=input('How many assignments have you completed? ')
                if assignment_amount.isdigit()==False:
                    print('Please use a integer')
                else:
                    assignment_value=[]
                    for scores in range(int(assignment_amount)):
                        assignment_scores=float(input('Please insert scores one at a time '))
                        assignment_value.append(assignment_scores)
                    assignment_weighp=int(assignment_weight)/100
                    assignment_total=sum(assignment_value)
                    assignment_final=assignment_total/int(assignment_amount)
                    global assignment_end
                    assignment_end=int(assignment_final)*float(assignment_weighp)
                    print('Your assignments average was',assignment_final,"%. Your assignments weigh", assignment_end,"% of your final grade.")
                    Menu()
def homework():
    while True:
        homework_weight=input('How much does your homework weigh? or if not applicable type n/a ')
        if homework_weight=='n/a':
            Menu()
        elif homework_weight.isdecimal()==False:
            print('Please use a integer')
        else:
            while True:
                homework_amount=input('How many homework assignments have you completed? ')
                if homework_amount.isdigit()==False:
                    print('Please use a integer')
                else:
                    homework_value=[]
                    for scores in range(int(homework_amount)):
                        homework_scores=float(input('Please insert scores one at a time '))
                        homework_value.append(homework_scores)
                    homework_weighp=int(homework_weight)/100
                    homework_total=sum(homework_value)
                    homework_final=homework_total/int(homework_amount)
                    global homework_end
                    homework_end=int(homework_final)*float(homework_weighp)
                    print('Your homework average was',homework_final,"%. Your homework weigh", homework_end,"% of your final grade.")
                    Menu()
def custom():
#The custom function allows the user to add categories they do not see on the menu, however, it only displays the average of all the categories added
#They will only see the custom average weight of the categories together, if they want more details, they must use custom_advance_details
    custom_list=[]
    custom_scores=[]
    global custom_advance_details
    custom_advance_details=[]
# The custom_advanced_details allows the user to view all the categories they added and their pertaining grade instead of just the average of all of them.
    global custom_end
    custom_end=sum(custom_list)
#The counters job is to signal the program to end the loop once they have entered all their categories in
    counter=0
#the customs functions job is to make the program more versatile, when adding new categories. It is nearly the same function except has more parameters.
#the menu's custom grade will the the product of all the categories in this function added together and multiplied by the weight.
    def customs(name,weight,amount):
        print('so the category is', name,'with a', weight, '%', 'and a total of', amount  )
        for numbers in range(int(amount)):
            scores=float(input('please provide your scores for this category one at a time '))
            custom_scores.append(scores)
        weigh_percentage=int(weight)/100
        custom_totalgrades=sum(custom_scores)
        custom_final=custom_totalgrades/int(amount)
        custom_final_weight=int(custom_final)*float(weigh_percentage)
        custom_details=custom_name,'average is', custom_final, '% and is worth', custom_final_weight,'%.'
        custom_advance_details.append(custom_details)
        for listed in custom_advance_details:
            print(listed)
        custom_list.append(custom_final_weight)
    
    

    
    custom_amount=input('How many custom categories would you like to add? or enter n/a to return to menu ')
    if custom_amount=='n/a':
        Menu()
    elif custom_amount.isalpha()==True:
        print('Please use a integer or decimal ')
    else:
        print('You will now be asked to insert information for each category one at a time\n ')
        for numbers in range(int(custom_amount)):
            custom_name=input('Please provide a name for category ')
            if custom_name.isdigit()==True:
                print("Please use letters only")
            else:
                custom_scores=[]
                custom_weight=input('Enter the weight of category ')
                while custom_weight.isdecimal()==False:     
                    print('Please use an integer')
                    custom_weight=input('Enter the weight of category ')
                else:
                    number_custom_grades=input('Please provide the number assignments completed for this category ')
                    while number_custom_grades.isdecimal()==False:
                        print('Please use an integer')
                        number_custom_grades=input('Please provide the number assignments completed for this category ')
                    else:
                        counter+=1
                        customs(custom_name,custom_weight,number_custom_grades)
                        custom_end=sum(custom_list)
                        while counter>=int(custom_amount):
                             Menu()
                                                   
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
# The codes above allows the function final grade to determine which categories to use. If the user did not insert any grade in a category, it will default to a 0    
def final():
    global final_end
    final_end=custom_end+homework_end+test_end+assignment_end+quiz_end+homework_end
    print( 'Your final Grade is',final_end,'%')
    Menu()
# function final is the final function that adds all the final grades together
def Menu():
    print("Hello, welcome to the Will I fail Calculator")
    print('This program will help calculate your final grade by finding the average weight of each pertaining category of your grade\nand then adding them together to output the final grade.')
    print('1: Grade Quizzes Current weight is',quiz_end,'%')
    print('2: Grade Test Current weight is',test_end,'%')
    print('3: Grade Assignments Current weight is',assignment_end,'%')
    print('4: Grade Homework Current weight is',homework_end,'%')
    print('5: Grade Custom Current weight is',custom_end,'%')
    print("6: Display each individual custom course's grade instead of the entire average")
    print('7: Calculate Final Grade (all other pertaining grades have to be filled before hand) Current final grade is', final_end,'%')
    print('8 Close program')
    
    Grader=input('Please Choose a category to start with by entering any of the following numbers above and press return key to confirm ')
    
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
        print('Below are all the categories you added along with their grades')
        print(custom_advance_details)
        menu_return=input('would you like to return to the Menu? y/n? ')
        if menu_return=='y':
            Menu()
        else:
            exit()
    elif Grader=='7':
        final()
    elif Grader=='8':
        exit()
    else:
        print('That is not one of the options')
        Menu()


Menu()