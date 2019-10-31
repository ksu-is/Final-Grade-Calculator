# Will-I-Fail-Calculator
 The Will-I-Fail-Calculator calculates a student's final grade by asking the weight of some common grade categories. Some being quzzies, test, and assignments. If a student does not see a category to their liking, they will also be allowed to add one. Once all the categories  weight's have been established, the user will then add their grades to the appropriate category. When all grades have been submitted, the calculator will then average all the values of each category and add them together to output the student's current grade. Along with calculating their current grade, this calculator will also have an option to calculate the value they need to achieve their wanted grade. 
 https://github.com/hbg/FinalGradeCalculator
 https://github.com/costajoshua27/simple-python-grade-calculator


#Starting the Calculator
Upon starting the calculator, the user will be welcomed and prompted with a menu asking which grade they would like to calculate first. The user will decide which category to start with by keying in one of the correct inputs ranging from 1-6.

#Example Below
Hello, welcome to the Will I fail Calculator
Please Choose a category to start with
Press 
 1 Grade quizzes 
 2 Grade test 
 3 Grade assignments 
 4 Grade homework
 5 Grade Custom Category
 6 for final grade (Must have all pertainig grades calculated before use)
 
 #Grading a category
 Once a category has been chosen, the user will be asked questions concerning the category. These questions will include, what is the weight of the category, how many times you completed the category, and the input of all the grades you recieved in that category. By the end of these questions, the calculator will output the user's grade with the weight of the categoy applied.
 
 #How each category is calculated
 category_value= all the grades added together in the category
 category_amount= number of instances taken in category
 category_weight= weight of category
 category_value/category_amount = category_average
 category_average x category_weight= category_final
