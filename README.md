# Will-I-Fail-Calculator
 The Will-I-Fail-Calculator calculates a student's final grade by asking the weight of some common grade categories. Some being quzzies, test, and assignments. If a student does not see a category to their liking, they will also be allowed to add one. Once all the categories  weight's have been established, the user will then add their grades to the appropriate category. When all grades have been submitted, the calculator will then average all the values of each category and add them together to output the student's current grade. 
 
 https://github.com/hbg/FinalGradeCalculator
 
 https://github.com/costajoshua27/simple-python-grade-calculator


Starting the Calculator
 Upon starting the calculator, the user will be welcomed and prompted with a menu asking which grade they would like to calculate first. The user will decide which category to start with by keying in one of the correct inputs ranging from 1-8. Along with selecting a category from the menu, it also displays the current grade the program calculated after the user inputted all the required variables.

## Example Below
  
Hello, welcome to the Will I fail Calculator
This program will help calculate your final grade by finding the average weight of each pertaining category of your grade
and then adding them together to output the final grade.

1: Grade Quizzes Current grade is 0 %

2: Grade Test Current grade is 0 %

3: Grade assignments Current grade is 0 %

4: Grade homework Current grade is 0 %

5: Grade custom Current grade is 0 %

6: Displays each individual custom course's grade instead of the entire average

7: Calculate Final Grade (all other pertaining grades have to be filled before hand) Current final grade is 0 %

8 Close program
 
 ## Grading a Category
 Once a category has been chosen, the user will be asked questions concerning the category. These questions will include, what is the weight of the category, the number of assignments completed, and the input of all the grades you recieved in that category. By the end of these questions, the calculator will output the user's grade with the weight of the categoy applied.
 The user will repeat this process until they meet all their categories.
 
 
 ### How each category is Calculated 
  category_value= all the grades added together in the category
  
  category_amount= number of instances taken in category
  
  category_weight= weight of category
  
  category_value/category_amount = category_average
  
  category_average x category_weight= category_final
  
  
 ## Customs Category
 The customs category allows the user to add additional categories to their final grade. However, unlike the other categories, the custom category takes a slightly different approach. It first starts off asking the user how many custom categores it would like to add. After, it will ask the name, weight, number of assignments completed, and the scores for each assignment.
 
 This process will continue depending on the amount of categories the user chooses to add. Once the user finishes adding their custom category, ONLY THE AVERAGE OF ALL THE CATEGORIES IN THE CUSTOMS TAB IS DISPLAYED ON THE MENU. If the user wants to view the details of the customs tab, they will have to choose that option on the menu.
 
 
 ### Example of Custom grading
 
How many custom categories would you like to add? or enter n/a to return to menu 1
You will now be asked to insert information for each category one at a time

Please provide a name for category Projects

Enter the weight of category 50

Please provide the number assignments completed for this category 1

so the category is Projects with a 50 % and a total of 1

please provide your scores for this category one at a time 100

### Example of details of custom

Below are all the categories you added along with their grades

('Projetcs', 'final grade is', 50.0)

('Presentaions', 'final grade is', 95.0)

would you like to return to the Menu? y/n? 

  
 ## Calculating for Final Grade
  
  Once the user has filled out all their categories, they will now be able to use function 7. Function 7 will calculate their final grade by adding all their final values from each category together and then outputting it to the user. Once this is finished, the program will end.
